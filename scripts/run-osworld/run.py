"""
Run OSWorld evaluation with Claude CLI + osworld-controller MCP.

Architecture (Docker isolation):
  1. This script creates one or more DesktopEnv (OSWorld VM containers).
  2. Each worker creates an isolated Docker network.
  3. The VM container is attached to the network with alias "osworld-vm".
  4. For each task, a Claude CLI container is launched on the same network.
     Inside the container: bridge.py proxies MCP→VM, Claude CLI runs with
     --mcp-config pointing to the osworld-controller MCP server.
  5. Claude cannot escape to the host — no docker socket, no host network.
  6. After Claude exits, env.evaluate() scores the result (host-side via
     published ports).

Memory isolation:
  - CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 prevents auto-memory writes/reads
  - -p (print mode) runs non-interactively with no session persistence
  - Each task gets a fresh Claude container with no shared state

Parallel execution:
  - Use --parallel N for multiple workers
  - Each worker gets its own VM + isolated network, tasks distributed round-robin

Usage:
    # Single task (Docker provider)
    python scripts/run-osworld/run.py \\
        --provider_name docker \\
        --specific_task_id <task_id>

    # All Chrome tasks, parallel on 4 containers
    python scripts/run-osworld/run.py \\
        --provider_name docker \\
        --domain chrome --parallel 4

    # Ablation: text vs multimodal vs none
    python scripts/run-osworld/run.py ... --skill_mode text
    python scripts/run-osworld/run.py ... --skill_mode multimodal
    python scripts/run-osworld/run.py ... --skill_mode none
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import logging
import os
import subprocess
import sys
from pathlib import Path

import docker

MMSKILLS_ROOT = Path(__file__).resolve().parents[2]
MCP_SERVER_PATH = "/opt/mmskills/tools/osworld-controller/server.py"
PLUGIN_DIRS = {
    "text": "/opt/mmskills/plugins/osworld-text",
    "multimodal": "/opt/mmskills/plugins/osworld-multimodal",
}
CLAUDE_CLI_IMAGE = os.environ.get("CLAUDE_CLI_IMAGE", "osworld-claude-cli")


SYSTEM_PROMPT = """\
You are controlling an Ubuntu desktop inside a virtual machine to complete a task autonomously.

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
- type_text(text): type text (newlines become Enter key presses)
- key_press(key): press a single key (e.g. "enter", "tab", "escape")
- hotkey(keys): press a shortcut (e.g. ["ctrl", "c"], ["alt", "f4"])

Every action tool automatically returns a screenshot after execution.

When you believe the task is complete, simply stop — do not call any signal tool.

Start by taking a screenshot to see the current state, then proceed step by step.\
"""


# ── VM port helper ────────────────────────────────────────────────────────────

def _get_vm_host_port(env) -> int:
    """Get the host-mapped port for the VM's API server (port 5000).

    The OSWorld Docker provider runs QEMU inside a container. Port 5000 is
    inside the QEMU guest, accessible from the host via Docker port mapping
    but NOT from other containers on the same Docker network. So the bridge
    must connect via the host.
    """
    return env.provider.server_port


# ── MCP config for inside the Claude container ────────────────────────────────

def _write_mcp_config(output_dir: Path, skill_mode: str) -> None:
    """Write MCP config JSON to the output dir (mounted as /workspace)."""
    config = {
        "mcpServers": {
            "osworld-controller": {
                "command": "python3",
                "args": [MCP_SERVER_PATH],
                "env": {"OSWORLD_BRIDGE_URL": "http://127.0.0.1:8765"},
            }
        }
    }
    (output_dir / "mcp_config.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8"
    )


# ── Run Claude in Docker ─────────────────────────────────────────────────────

def _run_claude_in_docker(
    docker_client: docker.DockerClient,
    vm_host_port: int,
    output_dir: Path,
    args: argparse.Namespace,
    logger: logging.Logger,
) -> tuple[str, str]:
    """Run Claude CLI in a Docker container.

    The bridge inside the container connects to the VM via the host's
    mapped port (host.docker.internal:<port>), since the QEMU guest's
    port 5000 is only reachable through Docker's port mapping.

    Returns (stdout, stderr) from the container.
    """
    # Build CLI args for entrypoint.sh (passed as CMD)
    cli_args = [
        "--mcp-config", "/workspace/mcp_config.json",
        "--output-format", "text",
        "--model", args.model,
        "--no-session-persistence",
        "--dangerously-skip-permissions",
    ]
    if args.skill_mode in PLUGIN_DIRS:
        cli_args.extend(["--plugin-dir", PLUGIN_DIRS[args.skill_mode]])

    env_vars = {
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "OSWORLD_VM_URL": f"http://host.docker.internal:{vm_host_port}",
    }

    container_name = f"osworld-claude-{output_dir.name[:12]}"
    # Remove stale container if exists
    try:
        old = docker_client.containers.get(container_name)
        old.remove(force=True)
    except docker.errors.NotFound:
        pass

    logger.info("Starting Claude container: %s (VM port %d)", container_name, vm_host_port)

    container = docker_client.containers.run(
        CLAUDE_CLI_IMAGE,
        command=cli_args,
        name=container_name,
        environment=env_vars,
        extra_hosts={"host.docker.internal": "host-gateway"},
        volumes={
            str(output_dir): {"bind": "/workspace", "mode": "rw"},
            str(MMSKILLS_ROOT): {"bind": "/opt/mmskills", "mode": "ro"},
            # Mount Claude credentials file for API authentication
            os.path.expanduser("~/.claude/.credentials.json"): {
                "bind": "/home/node/.claude/.credentials.json", "mode": "ro",
            },
        },
        detach=True,
        # No docker socket mounted — Claude can't escape
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


# ── argument parsing ──────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run OSWorld evaluation with Claude CLI + computer-use MCP"
    )
    parser.add_argument(
        "--osworld_root",
        default=os.environ.get("OSWORLD_ROOT", str(MMSKILLS_ROOT / "vendor" / "OSWorld")),
        help="Path to the OSWorld repository root (default: vendor/OSWorld submodule or $OSWORLD_ROOT)",
    )
    parser.add_argument("--path_to_vm", default=None, help="Path to the VM file (.vmx / .vbox). Not required for Docker provider.")
    parser.add_argument(
        "--provider_name", default="vmware", choices=["vmware", "virtualbox", "docker"]
    )
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--screen_width", type=int, default=1920)
    parser.add_argument("--screen_height", type=int, default=1080)
    parser.add_argument(
        "--model",
        default="claude-opus-4-6",
        help="Claude model to use (default: claude-opus-4-6)",
    )
    parser.add_argument(
        "--task_timeout",
        type=int,
        default=600,
        help="Max seconds for Claude to complete a single task (default: 600)",
    )
    parser.add_argument("--test_config_base_dir", default="evaluation_examples")
    parser.add_argument("--test_all_meta_path", default="evaluation_examples/test_all.json")
    parser.add_argument("--domain", default="all", help="Domain to run, or 'all'")
    parser.add_argument("--specific_task_id", help="Run a single task by ID")
    parser.add_argument("--result_dir", default=str(MMSKILLS_ROOT / "scripts" / "run-osworld" / "workspaces"))
    parser.add_argument(
        "--skill_mode",
        default="none",
        choices=["none", "text", "multimodal"],
        help="Which OS World skill variant to inject: none (baseline), text, or multimodal",
    )
    parser.add_argument(
        "--max_tasks",
        type=int,
        default=0,
        help="Maximum number of tasks to run (0 = all)",
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=1,
        help="Number of parallel workers (each gets its own VM + isolated network)",
    )
    parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"]
    )
    parser.add_argument(
        "--rerun", action="store_true",
        help="Re-run tasks even if results already exist (default: skip existing)",
    )
    return parser.parse_args()


# ── task helpers ──────────────────────────────────────────────────────────────

def select_tasks(args: argparse.Namespace) -> list[tuple[str, str]]:
    osworld = Path(args.osworld_root)
    meta = json.loads((osworld / args.test_all_meta_path).read_text(encoding="utf-8"))
    if args.specific_task_id:
        for domain, task_ids in meta.items():
            if args.specific_task_id in task_ids:
                return [(domain, args.specific_task_id)]
        raise ValueError(f"Task ID {args.specific_task_id!r} not found")
    if args.domain != "all":
        if args.domain not in meta:
            raise ValueError(f"Domain {args.domain!r} not found")
        return [(args.domain, tid) for tid in meta[args.domain]]
    return [(d, tid) for d, tids in meta.items() for tid in tids]


def load_example(args: argparse.Namespace, domain: str, task_id: str) -> dict:
    osworld = Path(args.osworld_root)
    path = osworld / args.test_config_base_dir / "examples" / domain / f"{task_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def task_result_dir(args: argparse.Namespace, domain: str, task_id: str) -> Path:
    import shutil
    path = Path(args.result_dir) / args.model / f"skill-{args.skill_mode}" / domain / task_id
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    return path


def task_logger(task_id: str, output_dir: Path) -> logging.Logger:
    lg = logging.getLogger(f"desktopenv.example.{task_id}.claude_mcp")
    lg.handlers.clear()
    lg.setLevel(logging.DEBUG)
    lg.propagate = False
    lg.addHandler(logging.FileHandler(output_dir / "runtime.log"))
    return lg


# ── task runner ───────────────────────────────────────────────────────────────

def run_task(
    docker_client: docker.DockerClient,
    env,
    example: dict,
    args: argparse.Namespace,
    output_dir: Path,
) -> float:
    task_id: str = example["id"]
    instruction: str = example["instruction"]
    lg = task_logger(task_id, output_dir)

    # Reset the VM to a clean state for this task
    lg.info("Resetting environment for task: %s", task_id)
    env.reset(task_config=example)

    # Start screen recording
    try:
        env.controller.start_recording()
    except Exception:
        lg.warning("Could not start recording")

    # Build prompt and write to workspace
    prompt = f"{SYSTEM_PROMPT}\n\nTask: {instruction}"
    (output_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

    # Write MCP config for the container
    _write_mcp_config(output_dir, args.skill_mode)

    start_time = datetime.datetime.now()

    # Run Claude in isolated Docker container
    vm_host_port = _get_vm_host_port(env)
    max_retries = 3
    stdout, stderr = "", ""
    for attempt in range(1, max_retries + 1):
        stdout, stderr = _run_claude_in_docker(
            docker_client, vm_host_port, output_dir, args, lg,
        )
        if "API Error: 500" in stdout or "API Error: 500" in stderr:
            lg.warning("API 500 error on attempt %d/%d, retrying...", attempt, max_retries)
            continue
        break
    else:
        lg.error("All %d attempts failed with API 500 errors", max_retries)

    elapsed = (datetime.datetime.now() - start_time).total_seconds()

    # Read signal from workspace (written by bridge.py)
    signal_file = output_dir / "signal.txt"
    signal = signal_file.read_text(encoding="utf-8").strip() if signal_file.exists() else "DONE"
    lg.info("Claude exited (%.1fs), signal=%s", elapsed, signal)

    # Save Claude output (also saved inside container, but capture logs too)
    claude_output_file = output_dir / "claude_output.txt"
    if not claude_output_file.exists():
        claude_output_file.write_text(stdout, encoding="utf-8")
    if stderr:
        lg.debug("Claude stderr: %s", stderr[:2000])

    # Take a final screenshot of the desktop state
    try:
        final_png = env.controller.get_screenshot()
        if final_png:
            (output_dir / "final_screenshot.png").write_bytes(final_png)
    except Exception:
        lg.warning("Could not capture final screenshot")

    # Record the final action so env.evaluate() handles infeasible tasks correctly
    env.step(signal)

    # Score the task
    result: float = env.evaluate()
    lg.info("Task score: %.4f", result)

    (output_dir / "result.txt").write_text(f"{result}\n", encoding="utf-8")
    (output_dir / "meta.json").write_text(
        json.dumps(
            {
                "task_id": task_id,
                "instruction": instruction,
                "signal": signal,
                "result": result,
                "elapsed_seconds": round(elapsed, 1),
                "model": args.model,
                "skill_mode": args.skill_mode,
                "timestamp": start_time.isoformat(),
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    # Stop VLC recording (unreliable, may miss early steps)
    try:
        env.controller.end_recording(str(output_dir / "recording_vlc.mp4"))
    except Exception:
        pass

    # Generate reliable replay video from step screenshots
    screenshots_dir = output_dir / "screenshots"
    replay_path = output_dir / "recording.mp4"
    if screenshots_dir.exists() and any(screenshots_dir.iterdir()):
        try:
            subprocess.run(
                [
                    "ffmpeg", "-y", "-framerate", "1",
                    "-i", str(screenshots_dir / "step_%03d.png"),
                    "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-vf", "scale=1920:1080",
                    str(replay_path),
                ],
                capture_output=True,
                timeout=60,
            )
            lg.info("Generated replay video from %d screenshots", len(list(screenshots_dir.iterdir())))
        except Exception:
            lg.warning("Could not generate replay video")

    return result


# ── parallel worker ───────────────────────────────────────────────────────────

def _resolve_vm_paths(path_to_vm: str | None, num_workers: int, provider: str) -> list[str | None]:
    """Resolve VM paths for each worker."""
    if provider == "docker":
        # Docker creates containers on the fly, no VM path needed
        return [None] * num_workers
    if path_to_vm is None:
        raise ValueError("--path_to_vm is required for VMware/VirtualBox providers")
    p = Path(path_to_vm)
    if p.is_dir():
        vmx_files = sorted(p.glob("*.vmx"))
        if not vmx_files:
            raise ValueError(f"No .vmx files found in {p}")
        return [str(f) for f in vmx_files[:num_workers]]
    # Single file — replicate for all workers (they'll share the VM sequentially)
    return [str(p)] * num_workers


def _make_desktop_env(args: argparse.Namespace, vm_path: str | None):
    """Create a DesktopEnv with the right arguments for the provider."""
    from desktop_env.desktop_env import DesktopEnv  # noqa: PLC0415

    kwargs = dict(
        provider_name=args.provider_name,
        action_space="pyautogui",
        screen_size=(args.screen_width, args.screen_height),
        headless=args.headless,
        os_type="Ubuntu",
        require_a11y_tree=True,
        require_terminal=False,
    )
    if vm_path is not None:
        kwargs["path_to_vm"] = vm_path
    return DesktopEnv(**kwargs)


def _run_worker(
    worker_id: int,
    vm_path: str | None,
    task_queue: list[tuple[str, dict]],
    args: argparse.Namespace,
) -> list[tuple[str, str, float]]:
    """Run tasks sequentially on a single VM/container. Returns list of (domain, task_id, score)."""
    logger = logging.getLogger(f"desktopenv.worker.{worker_id}")

    osworld_root = Path(args.osworld_root)
    sys.path.insert(0, str(osworld_root))

    docker_client = docker.from_env()
    logger.info("Worker %d: vm=%s, %d tasks", worker_id, vm_path, len(task_queue))

    results = []
    env = None

    try:
        env = _make_desktop_env(args, vm_path)

        for idx, (domain, example) in enumerate(task_queue, start=1):
            task_id = example["id"]
            logger.info("Worker %d [%d/%d] %s / %s", worker_id, idx, len(task_queue), domain, task_id)
            output_dir = task_result_dir(args, domain, task_id)
            result_file = output_dir / "result.txt"
            if not args.rerun and result_file.exists():
                prev = result_file.read_text().strip()
                logger.info("Worker %d [%d/%d] skipping (existing score=%s)", worker_id, idx, len(task_queue), prev)
                try:
                    results.append((domain, task_id, float(prev)))
                except ValueError:
                    results.append((domain, task_id, 0.0))
                continue
            try:
                score = run_task(docker_client, env, example, args, output_dir)
                results.append((domain, task_id, score))
                logger.info("Worker %d [%d/%d] score=%.4f", worker_id, idx, len(task_queue), score)
            except Exception:
                logger.exception("Worker %d: task failed: %s / %s", worker_id, domain, task_id)
                results.append((domain, task_id, 0.0))
    finally:
        if env is not None:
            try:
                env.close()
            except Exception:
                logger.exception("Worker %d: failed to close environment", worker_id)

    return results


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )
    logger = logging.getLogger("desktopenv.experiment.claude_mcp")

    osworld_root = Path(args.osworld_root)
    if not osworld_root.exists():
        logger.error("OSWorld root not found: %s", osworld_root)
        return 1
    sys.path.insert(0, str(osworld_root))

    # OSWorld's Docker provider uses relative paths (./docker_vm_data/),
    # so we must run from the OSWorld root directory.
    os.chdir(osworld_root)

    # Validate args
    if args.provider_name != "docker" and args.path_to_vm is None:
        logger.error("--path_to_vm is required for %s provider", args.provider_name)
        return 1

    # Discover tasks
    task_ids = select_tasks(args)
    if args.max_tasks > 0:
        task_ids = task_ids[:args.max_tasks]
    tasks = [(domain, load_example(args, domain, tid)) for domain, tid in task_ids]
    logger.info("Running %d task(s), model=%s, skill_mode=%s, parallel=%d",
                len(tasks), args.model, args.skill_mode, args.parallel)

    num_workers = min(args.parallel, len(tasks))

    if num_workers <= 1:
        # ── Sequential mode (single worker) ──
        docker_client = docker.from_env()

        scores: list[float] = []
        env = None
        try:
            env = _make_desktop_env(args, args.path_to_vm)

            for idx, (domain, example) in enumerate(tasks, start=1):
                task_id = example["id"]
                logger.info("[%d/%d] %s / %s", idx, len(tasks), domain, task_id)
                output_dir = task_result_dir(args, domain, task_id)
                try:
                    score = run_task(docker_client, env, example, args, output_dir)
                    scores.append(score)
                    logger.info("[%d/%d] score=%.4f", idx, len(tasks), score)
                except Exception:
                    logger.exception("Task failed: %s / %s", domain, task_id)
                    scores.append(0.0)

            avg = sum(scores) / len(scores) if scores else 0.0
            logger.info("Done. %d tasks, avg score %.4f", len(scores), avg)
            print(f"Average score: {avg:.4f}")
        except KeyboardInterrupt:
            logger.warning("Interrupted")
            return 130
        finally:
            if env is not None:
                try:
                    env.close()
                except Exception:
                    logger.exception("Failed to close environment")
    else:
        # ── Parallel mode (multiple workers) ──
        vm_paths = _resolve_vm_paths(args.path_to_vm, num_workers, args.provider_name)
        if len(vm_paths) < num_workers:
            logger.warning("Only %d VM(s) found, reducing workers to %d", len(vm_paths), len(vm_paths))
            num_workers = len(vm_paths)

        # Distribute tasks round-robin across workers
        task_queues: list[list[tuple[str, dict]]] = [[] for _ in range(num_workers)]
        for i, task in enumerate(tasks):
            task_queues[i % num_workers].append(task)

        logger.info("Distributing %d tasks across %d workers", len(tasks), num_workers)
        all_results: list[tuple[str, str, float]] = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [
                executor.submit(_run_worker, i, vm_paths[i], task_queues[i], args)
                for i in range(num_workers)
            ]
            try:
                for future in concurrent.futures.as_completed(futures):
                    all_results.extend(future.result())
            except KeyboardInterrupt:
                logger.warning("Interrupted")
                return 130

        scores = [r[2] for r in all_results]
        avg = sum(scores) / len(scores) if scores else 0.0
        logger.info("Done. %d tasks, avg score %.4f", len(scores), avg)
        print(f"Average score: {avg:.4f}")

    # Write summary
    summary_path = Path(args.result_dir) / args.model / f"skill-{args.skill_mode}" / "summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps({
        "model": args.model,
        "skill_mode": args.skill_mode,
        "domain": args.domain,
        "num_tasks": len(tasks),
        "avg_score": round(avg, 4),
        "timestamp": datetime.datetime.now().isoformat(),
    }, indent=2), encoding="utf-8")
    logger.info("Summary written to %s", summary_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
