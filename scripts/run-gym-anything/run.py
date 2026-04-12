"""
Run gym-anything evaluation with Claude CLI + MCP (two-Docker design).

Architecture (Docker isolation):
  1. This script uses gym-anything's from_config() to spin up Docker 1
     (the desktop environment, e.g. Ubuntu + VSCode).
  2. A bridge (bridge.py) runs host-side, holding the live env object and
     exposing screenshot/action over HTTP on localhost.
  3. For each task, a Claude CLI Docker container (Docker 2) is launched.
     Inside: the MCP server connects to the bridge via host.docker.internal.
     Claude has NO bash, NO file edit — only GUI tools (screenshot, click, etc).
  4. After Claude exits, env.close() runs the task's verifier automatically.

Memory isolation:
  - CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 prevents auto-memory writes/reads
  - -p (print mode) runs non-interactively with no session persistence
  - Each task gets a fresh Claude container with no shared state

Parallel execution:
  - Use --parallel N for multiple workers
  - Each worker gets its own env + bridge on a unique port
  - Tasks are distributed round-robin across workers

Usage:
    # Single task (baseline, no skill)
    python scripts/run-gym-anything/run.py \
        --env_dir vendor/gym-anything/benchmarks/cua_world/environments/vscode_env \
        --task fix_broken_test_suite

    # With skill
    python scripts/run-gym-anything/run.py \
        --env_dir vendor/gym-anything/benchmarks/cua_world/environments/vscode_env \
        --task fix_broken_test_suite --skill_mode text

    # All test split tasks, 4 parallel workers
    python scripts/run-gym-anything/run.py \
        --env_dir vendor/gym-anything/benchmarks/cua_world/environments/vscode_env \
        --split test --skill_mode multimodal --parallel 4
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import logging
import os
import shutil
import sys
from pathlib import Path

import docker

MMSKILLS_ROOT = Path(__file__).resolve().parents[2]
MCP_SERVER_PATH = "/opt/mmskills/tools/gym-anything-controller/server.py"
BRIDGE_PORT_BASE = 8766  # worker 0 gets 8766, worker 1 gets 8767, etc.

PLUGIN_DIRS = {
    "text": "/opt/mmskills/plugins/gym-anything-text",
    "multimodal": "/opt/mmskills/plugins/gym-anything-multimodal",
}

CLAUDE_CLI_IMAGE = os.environ.get("CLAUDE_CLI_IMAGE", "ga-claude-cli")

SYSTEM_PROMPT = """\
You are controlling an Ubuntu desktop inside a container to complete a task autonomously.

IMPORTANT RULES:
- Never ask the user for clarification or confirmation. Make a decision and act on it.
- Never present multiple options or ask which approach to use. Pick the most direct approach and execute it.
- Complete the task fully by yourself without any interaction.
- You MUST interact with applications through their graphical user interface (GUI) only. Do NOT open a terminal, run shell commands, edit config files, or use any programmatic workaround.

You have the following tools to interact with the desktop:
- screenshot(): take a screenshot to see the current desktop state
- click(x, y, button): click at pixel coordinates ("left"/"right"/"middle")
- double_click(x, y): double-click at coordinates
- move_to(x, y): move the mouse without clicking
- drag_to(start_x, start_y, end_x, end_y): click and drag
- scroll(x, y, clicks): scroll up (positive) or down (negative)
- type_text(text): type text
- key_press(key): press a single key (e.g. "Return", "Tab", "Escape")
- hotkey(keys): press a shortcut (e.g. ["ctrl", "c"], ["alt", "F4"])

Every action tool automatically returns a screenshot after execution.

GUI INTERACTION TIPS:
- The screen resolution is 1280x720. Menu bars are at y≈25.
- After each action, CAREFULLY examine the returned screenshot before proceeding.
- If a click doesn't work, try clicking more precisely — zoom in mentally on the target area.
- If you get stuck in a loop (trying the same thing 3+ times), STOP and try a completely different approach.
- Use keyboard shortcuts when menu clicks are unreliable.
- Close any unexpected dialogs with Escape before retrying.
- If the window disappears, press Alt+Tab to bring it back.

When you believe the task is complete, simply stop — do not call any signal tool.\
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run gym-anything evaluation with Claude CLI + MCP (two-Docker)"
    )
    parser.add_argument(
        "--env_dir", required=True,
        help="Path to a gym-anything environment directory (contains env.json)",
    )
    parser.add_argument(
        "--task", default=None,
        help="Specific task ID to run. If omitted, runs all tasks (or --split).",
    )
    parser.add_argument(
        "--split", default=None, choices=["train", "test", "all", "verified"],
        help="Run all tasks in a split. Ignored if --task is set.",
    )
    parser.add_argument(
        "--model", default="claude-opus-4-6",
        help="Claude model to use (default: claude-opus-4-6)",
    )
    parser.add_argument(
        "--skill_mode", default="none",
        choices=["none", "text", "multimodal"],
        help="Which skill variant to inject (default: none = baseline)",
    )
    parser.add_argument(
        "--task_timeout", type=int, default=1800,
        help="Max seconds for Claude to complete a single task (default: 1800)",
    )
    parser.add_argument(
        "--result_dir",
        default=str(MMSKILLS_ROOT / "scripts" / "run-gym-anything" / "workspaces"),
        help="Directory for result artifacts",
    )
    parser.add_argument(
        "--max_tasks", type=int, default=0,
        help="Maximum number of tasks to run (0 = all)",
    )
    parser.add_argument(
        "--rerun", action="store_true",
        help="Re-run tasks even if results already exist",
    )
    parser.add_argument(
        "--use_cache", action="store_true",
        help="Use Docker checkpoint cache for faster env init",
    )
    parser.add_argument(
        "--parallel", type=int, default=1,
        help="Number of parallel workers (each gets its own env + bridge port)",
    )
    parser.add_argument(
        "--log_level", default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
    )
    return parser.parse_args()


# ── task discovery ────────────────────────────────────────────────────────────

def discover_tasks(env_dir: str, task: str | None, split: str | None) -> list[str]:
    """Return list of task IDs to run."""
    if task:
        return [task]

    env_path = Path(env_dir)
    tasks_dir = env_path / "tasks"

    if split:
        env_name = env_path.name
        splits_dir = env_path.parent.parent / "splits"
        # Try multiple naming conventions: qgis_env_split.json, qgis_split.json
        candidates = [
            splits_dir / f"{env_name}_split.json",
            splits_dir / f"{env_name.removesuffix('_env')}_split.json",
        ]
        for split_file in candidates:
            if split_file.exists():
                split_data = json.loads(split_file.read_text(encoding="utf-8"))
                key = f"{split}_tasks" if split != "all" else "all_tasks"
                if key in split_data:
                    # Only return tasks that actually exist locally
                    task_ids = split_data[key]
                    existing = [t for t in task_ids if (tasks_dir / t).is_dir()]
                    if existing:
                        return existing
                break

    # Fallback: list all task directories
    if tasks_dir.is_dir():
        return sorted(d.name for d in tasks_dir.iterdir() if d.is_dir())

    return []


# ── MCP config (for inside the Claude container) ─────────────────────────────

def _write_mcp_config(output_dir: Path, bridge_port: int) -> None:
    """Write MCP config JSON to the output dir (mounted as /workspace).

    The MCP server runs inside the Claude container and connects to the bridge
    on the host via host.docker.internal.
    """
    config = {
        "mcpServers": {
            "gym-anything-controller": {
                "command": "python3",
                "args": [MCP_SERVER_PATH],
                "env": {"GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}"},
            }
        }
    }
    (output_dir / "mcp_config.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8"
    )


# ── Run Claude in Docker ─────────────────────────────────────────────────────

def _run_claude_in_docker(
    docker_client: docker.DockerClient,
    output_dir: Path,
    bridge_port: int,
    args: argparse.Namespace,
    logger: logging.Logger,
) -> tuple[str, str]:
    """Run Claude CLI in an isolated Docker container (Docker 2).

    Claude can ONLY use MCP GUI tools — no Bash, no file editing.
    The MCP server inside the container connects to the bridge on the host
    via host.docker.internal:bridge_port.

    Returns (stdout, stderr) from the container.
    """
    cli_args = [
        "--mcp-config", "/workspace/mcp_config.json",
        "--output-format", "stream-json",
        "--verbose",
        "--model", args.model,
        "--no-session-persistence",
        "--dangerously-skip-permissions",
        # Block all tools except our MCP GUI tools + Skill + Read (for viewing skill images)
        "--disallowed-tools", "Bash,Edit,Write,Glob,Grep,Agent,AskUserQuestion,NotebookEdit",
    ]
    if args.skill_mode in PLUGIN_DIRS:
        cli_args.extend(["--plugin-dir", PLUGIN_DIRS[args.skill_mode]])

    env_vars = {
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}",
    }

    container_name = f"ga-claude-{output_dir.name[:12]}-p{bridge_port}"
    # Remove stale container if exists
    try:
        old = docker_client.containers.get(container_name)
        old.remove(force=True)
    except docker.errors.NotFound:
        pass

    logger.info("Starting Claude container: %s (bridge port %d)", container_name, bridge_port)

    container = docker_client.containers.run(
        CLAUDE_CLI_IMAGE,
        command=cli_args,
        name=container_name,
        environment=env_vars,
        extra_hosts={"host.docker.internal": "host-gateway"},
        volumes={
            str(output_dir): {"bind": "/workspace", "mode": "rw"},
            str(MMSKILLS_ROOT): {"bind": "/opt/mmskills", "mode": "ro"},
            os.path.expanduser("~/.claude/.credentials.json"): {
                "bind": "/home/node/.claude/.credentials.json", "mode": "ro",
            },
        },
        detach=True,
    )

    try:
        result = container.wait(timeout=args.task_timeout)
        stdout = container.logs(stdout=True, stderr=False).decode(errors="replace")
        stderr = container.logs(stdout=False, stderr=True).decode(errors="replace")
        exit_code = result.get("StatusCode", -1)
        logger.info("Claude container exited with code %d", exit_code)
    except Exception as exc:
        logger.warning("Claude container timed out or errored: %s", exc)
        try:
            container.kill()
        except Exception:
            pass
        stdout = container.logs(stdout=True, stderr=False).decode(errors="replace")
        stderr = container.logs(stdout=False, stderr=True).decode(errors="replace")
    finally:
        try:
            container.remove(force=True)
        except Exception:
            pass

    return stdout, stderr


# ── task runner ───────────────────────────────────────────────────────────────

def run_task(
    docker_client: docker.DockerClient,
    env_dir: str,
    task_id: str,
    bridge_port: int,
    args: argparse.Namespace,
    output_dir: Path,
    logger: logging.Logger,
) -> dict:
    """Run a single task end-to-end. Returns result dict."""

    # Import gym-anything
    ga_root = MMSKILLS_ROOT / "vendor" / "gym-anything"
    if str(ga_root / "src") not in sys.path:
        sys.path.insert(0, str(ga_root / "src"))
    from gym_anything.api import from_config

    # gym-anything's Docker runner resolves paths relative to CWD:
    # - Preset Dockerfiles: "gym_anything/presets/.../Dockerfile"
    # - Env mounts: "benchmarks/cua_world/environments/.../scripts"
    # Both resolve correctly when CWD = vendor/gym-anything/src/ IF we also
    # symlink benchmarks there. Simpler: chdir to repo root and add a symlink.
    original_cwd = os.getcwd()
    os.chdir(str(ga_root))
    # Ensure gym_anything package is findable from this CWD
    gapkg_link = ga_root / "gym_anything"
    if not gapkg_link.exists():
        os.symlink("src/gym_anything", str(gapkg_link))

    # Create and reset environment (Docker 1: desktop env)
    logger.info("Creating env for task: %s", task_id)
    env = from_config(env_dir, task_id=task_id)

    try:
        logger.info("Resetting environment...")
        env.reset(use_cache=args.use_cache)

        env.set_episode_limits(timeout_sec=args.task_timeout)
        logger.info("Environment ready (timeout=%ds)", args.task_timeout)
    except Exception as exc:
        logger.error("Failed to set up environment: %s", exc)
        env.close()
        return {"task_id": task_id, "error": str(exc), "score": 0.0}

    # Start bridge on host (holds the env object, serves HTTP on unique port)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from bridge import start_bridge_server
    bridge_server = start_bridge_server(env, port=bridge_port, workspace=str(output_dir))

    try:
        # Load task description
        task_json_path = Path(env_dir) / "tasks" / task_id / "task.json"
        task_desc = ""
        if task_json_path.exists():
            task_data = json.loads(task_json_path.read_text(encoding="utf-8"))
            task_desc = task_data.get("description", "")

        # Build prompt with optional skill content
        skill_section = ""
        if args.skill_mode != "none":
            env_name = Path(env_dir).name.removesuffix("_env")
            skill_dir = MMSKILLS_ROOT / "skills" / f"{env_name}-workflow-{args.skill_mode}"
            if not skill_dir.exists():
                # Fallback to knowledge skill
                skill_dir = MMSKILLS_ROOT / "skills" / f"{env_name}-knowledge-{args.skill_mode}"

            guide_file = skill_dir / "guide.md" if skill_dir.exists() else None

            if guide_file and guide_file.exists():
                guide_text = guide_file.read_text(encoding="utf-8")

                # Copy skill images into workspace so Claude can Read them
                skill_images_dir = output_dir / "skill_images"
                skill_images_dir.mkdir(exist_ok=True)
                image_paths = []
                for img in sorted(skill_dir.glob("*.png")):
                    dest = skill_images_dir / img.name
                    shutil.copy2(img, dest)
                    # Path inside the Claude container (output_dir is mounted at /workspace)
                    image_paths.append(f"/workspace/skill_images/{img.name}")

                # Build skill section with guide text + image reading instructions
                skill_section = "\n\n" + "=" * 60 + "\n"
                skill_section += "SKILL GUIDE — Read this carefully before starting!\n"
                skill_section += "=" * 60 + "\n\n"
                skill_section += guide_text
                if image_paths:
                    skill_section += "\n\n" + "-" * 60 + "\n"
                    skill_section += "IMPORTANT: The guide references screenshots. You MUST view them "
                    skill_section += "using the Read tool to understand the UI layout. View ALL of these "
                    skill_section += "images BEFORE taking any GUI action:\n\n"
                    for p in image_paths:
                        skill_section += f"  Read(\"{p}\")\n"
                    skill_section += "\nStudy these screenshots carefully — they show you exactly what "
                    skill_section += "each UI element looks like so you can find it on the actual screen.\n"
            else:
                logger.warning("Skill guide not found at %s", skill_dir)

        prompt = f"{SYSTEM_PROMPT}{skill_section}\n\nTask: {task_desc}"
        (output_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

        # Write MCP config for inside the Claude container
        _write_mcp_config(output_dir, bridge_port)

        start_time = datetime.datetime.now()

        # Run Claude in isolated Docker container (Docker 2)
        max_retries = 3
        stdout, stderr = "", ""
        for attempt in range(1, max_retries + 1):
            stdout, stderr = _run_claude_in_docker(
                docker_client, output_dir, bridge_port, args, logger,
            )
            if "API Error: 500" in stdout or "API Error: 500" in stderr:
                logger.warning("API 500 error on attempt %d/%d, retrying...", attempt, max_retries)
                continue
            break
        else:
            logger.error("All %d attempts failed with API 500 errors", max_retries)

        elapsed = (datetime.datetime.now() - start_time).total_seconds()

        # Save container logs (entrypoint echo messages) separately.
        # Claude's actual output is written by the entrypoint to
        # /workspace/claude_output.txt and /workspace/claude_stderr.txt
        # which map to output_dir — do NOT overwrite them.
        (output_dir / "container_stdout.txt").write_text(stdout, encoding="utf-8")
        if stderr:
            (output_dir / "container_stderr.txt").write_text(stderr, encoding="utf-8")
        logger.debug("Container stdout: %s", stdout[:2000])
        logger.debug("Container stderr: %s", stderr[:2000])

    finally:
        bridge_server.shutdown()

    # Save episode_dir BEFORE close() — close() clears it.
    # Resolve to absolute path while CWD is still vendor/gym-anything/
    episode_dir = getattr(env, "episode_dir", None)
    if episode_dir:
        episode_dir = Path(episode_dir).resolve()

    # Close env — this triggers the verifier
    logger.info("Closing env (running verifier)...")
    env.close()

    # Restore CWD
    os.chdir(original_cwd)

    # Read verification results from gym-anything's episode dir
    score = 0.0
    verifier_result = {}
    if episode_dir:
        summary_path = Path(episode_dir) / "summary.json"
        if summary_path.exists():
            try:
                summary = json.loads(summary_path.read_text(encoding="utf-8"))
                verifier_result = summary.get("verifier", {})
                passed = verifier_result.get("passed", False)
                score = verifier_result.get("score", 100.0 if passed else 0.0)
                # Normalize: gym-anything scores are 0-100, we store 0-1
                if score > 1:
                    score = score / 100.0
                logger.info("Verifier: passed=%s score=%.4f feedback=%s",
                            passed, score, verifier_result.get("feedback", "")[:200])
            except Exception as exc:
                logger.warning("Failed to read summary.json: %s", exc)

    result = {
        "task_id": task_id,
        "score": score,
        "elapsed_seconds": round(elapsed, 1),
        "model": args.model,
        "skill_mode": args.skill_mode,
        "timestamp": start_time.isoformat(),
        "verifier_result": verifier_result,
        "episode_dir": str(episode_dir) if episode_dir else None,
    }
    (output_dir / "result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (output_dir / "score.txt").write_text(f"{score}\n", encoding="utf-8")

    return result


# ── parallel worker ───────────────────────────────────────────────────────────

def _run_worker(
    worker_id: int,
    task_queue: list[str],
    env_dir: str,
    bridge_port: int,
    args: argparse.Namespace,
) -> list[tuple[str, float]]:
    """Run tasks sequentially on a single worker. Returns list of (task_id, score)."""
    logger = logging.getLogger(f"gym-anything.worker.{worker_id}")
    docker_client = docker.from_env()
    env_name = Path(env_dir).name

    logger.info("Worker %d: bridge_port=%d, %d tasks", worker_id, bridge_port, len(task_queue))

    results = []
    for idx, task_id in enumerate(task_queue, start=1):
        logger.info("Worker %d [%d/%d] %s", worker_id, idx, len(task_queue), task_id)

        # Check existing result
        output_dir = Path(args.result_dir) / args.model / f"skill-{args.skill_mode}" / env_name / task_id
        score_file = output_dir / "score.txt"
        if not args.rerun and score_file.exists():
            prev = score_file.read_text().strip()
            logger.info("Worker %d [%d/%d] skipping (existing score=%s)",
                        worker_id, idx, len(task_queue), prev)
            try:
                results.append((task_id, float(prev)))
            except ValueError:
                results.append((task_id, 0.0))
            continue

        # Create fresh output dir
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)

        try:
            result = run_task(
                docker_client, env_dir, task_id, bridge_port, args, output_dir, logger,
            )
            score = result.get("score", 0.0)
            results.append((task_id, score))
            logger.info("Worker %d [%d/%d] score=%.4f", worker_id, idx, len(task_queue), score)
        except Exception:
            logger.exception("Worker %d: task failed: %s", worker_id, task_id)
            results.append((task_id, 0.0))

    return results


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )
    logger = logging.getLogger("gym-anything.runner")

    # Resolve paths
    args.result_dir = str(Path(args.result_dir).resolve())
    env_dir = str(Path(args.env_dir).resolve())

    # Discover tasks
    task_ids = discover_tasks(env_dir, args.task, args.split)
    if not task_ids:
        logger.error("No tasks found")
        return 1
    if args.max_tasks > 0:
        task_ids = task_ids[:args.max_tasks]

    env_name = Path(env_dir).name
    num_workers = min(args.parallel, len(task_ids))
    logger.info("Running %d task(s) from %s, model=%s, skill=%s, parallel=%d",
                len(task_ids), env_name, args.model, args.skill_mode, num_workers)

    if num_workers <= 1:
        # ── Sequential mode ──
        docker_client = docker.from_env()
        bridge_port = BRIDGE_PORT_BASE
        scores: list[float] = []

        for idx, task_id in enumerate(task_ids, start=1):
            logger.info("[%d/%d] %s / %s", idx, len(task_ids), env_name, task_id)

            output_dir = Path(args.result_dir) / args.model / f"skill-{args.skill_mode}" / env_name / task_id
            score_file = output_dir / "score.txt"
            if not args.rerun and score_file.exists():
                prev = score_file.read_text().strip()
                logger.info("[%d/%d] skipping (existing score=%s)", idx, len(task_ids), prev)
                try:
                    scores.append(float(prev))
                except ValueError:
                    scores.append(0.0)
                continue

            if output_dir.exists():
                shutil.rmtree(output_dir)
            output_dir.mkdir(parents=True)

            try:
                result = run_task(
                    docker_client, env_dir, task_id, bridge_port, args, output_dir, logger,
                )
                scores.append(result.get("score", 0.0))
                logger.info("[%d/%d] score=%.4f", idx, len(task_ids), scores[-1])
            except Exception:
                logger.exception("Task failed: %s", task_id)
                scores.append(0.0)

    else:
        # ── Parallel mode ──
        # Distribute tasks round-robin across workers
        task_queues: list[list[str]] = [[] for _ in range(num_workers)]
        for i, task_id in enumerate(task_ids):
            task_queues[i % num_workers].append(task_id)

        logger.info("Distributing %d tasks across %d workers", len(task_ids), num_workers)
        all_results: list[tuple[str, float]] = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [
                executor.submit(
                    _run_worker,
                    i,
                    task_queues[i],
                    env_dir,
                    BRIDGE_PORT_BASE + i,  # unique port per worker
                    args,
                )
                for i in range(num_workers)
            ]
            try:
                for future in concurrent.futures.as_completed(futures):
                    all_results.extend(future.result())
            except KeyboardInterrupt:
                logger.warning("Interrupted")
                return 130

        scores = [r[1] for r in all_results]

    avg = sum(scores) / len(scores) if scores else 0.0
    logger.info("Done. %d tasks, avg score %.4f", len(scores), avg)
    print(f"\nResults: {len(scores)} tasks, avg score: {avg:.4f}")

    # Write summary
    summary_dir = Path(args.result_dir) / args.model / f"skill-{args.skill_mode}"
    summary_dir.mkdir(parents=True, exist_ok=True)
    (summary_dir / f"summary_{env_name}.json").write_text(json.dumps({
        "model": args.model,
        "skill_mode": args.skill_mode,
        "env": env_name,
        "num_tasks": len(scores),
        "num_workers": num_workers,
        "avg_score": round(avg, 4),
        "per_task": dict(zip(task_ids, scores)) if num_workers <= 1
                    else {r[0]: r[1] for r in all_results},
        "timestamp": datetime.datetime.now().isoformat(),
    }, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
