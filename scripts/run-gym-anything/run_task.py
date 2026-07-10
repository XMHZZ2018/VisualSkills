"""
Run a single gym-anything task end-to-end, or perform utility operations.

This is the atomic unit of execution. Each invocation handles exactly one task
with its own bridge port, Docker containers, and result directory.

Usage:
    # Run a single task
    python3 run_task.py --config config.yaml --task fix_broken_test --bridge_port 8766

    # List tasks from config
    python3 run_task.py --config config.yaml --discover-tasks

    # Write summary of all results
    python3 run_task.py --config config.yaml --summarize
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import shutil
import sys
import threading
import time
from pathlib import Path

import docker
import yaml

MMSKILLS_ROOT = Path(__file__).resolve().parents[2]
MCP_SERVER_PATH = "/opt/mmskills/tools/gym-anything-controller/server.py"

# Where MMSKILLS_ROOT is mounted inside the Claude CLI container.
CONTAINER_MMSKILLS_ROOT = "/opt/mmskills"
# Where the per-task output_dir is mounted inside the Claude CLI container.
CONTAINER_WORKSPACE = "/workspace"


def _resolve_skill_dir(env_name: str, skill_mode: str) -> Path | None:
    """Find the on-disk skill directory for this env + mode.

    Tries, in order:
      skills/<env>-<mode>-v1     (current v1 layout)
      skills/<env>-<mode>        (legacy layout)
      skills/<env>-workflow-<mode>         (workflow-style skills, e.g. qgis)
    """
    candidates = [
        MMSKILLS_ROOT / "skills" / f"{env_name}-{skill_mode}-stage1",
        MMSKILLS_ROOT / "skills" / f"{env_name}-{skill_mode}-loader-v1",
        MMSKILLS_ROOT / "skills" / f"{env_name}-{skill_mode}-v1",
        MMSKILLS_ROOT / "skills" / f"{env_name}-{skill_mode}",
        MMSKILLS_ROOT / "skills" / f"{env_name}-workflow-{skill_mode}",
    ]
    for p in candidates:
        if p.is_dir():
            return p
    return None


def _build_plugin_dir(
    env_name: str,
    skill_mode: str,
    output_dir: Path,
    logger: logging.Logger,
) -> str | None:
    """Build a per-task plugin dir that exposes exactly one skill.

    Layout created under `output_dir/plugin/`:
        .claude-plugin/marketplace.json   # lists only this domain's skill
        skills/<skill_name>               # symlink → /opt/mmskills/skills/<skill_name>

    The symlink target is the container-mount path (CONTAINER_MMSKILLS_ROOT),
    which the Claude CLI resolves inside its container. Returns the path Claude
    should see via --plugin-dir, or None if no matching skill is on disk.
    """
    skill_dir = _resolve_skill_dir(env_name, skill_mode)
    if skill_dir is None:
        logger.warning(
            "No skill directory found for env=%s mode=%s — running without plugin",
            env_name, skill_mode,
        )
        return None

    skill_name = skill_dir.name
    plugin_root = output_dir / "plugin"
    (plugin_root / ".claude-plugin").mkdir(parents=True, exist_ok=True)
    (plugin_root / "skills").mkdir(parents=True, exist_ok=True)

    link_path = plugin_root / "skills" / skill_name
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()
    link_path.symlink_to(f"{CONTAINER_MMSKILLS_ROOT}/skills/{skill_name}")

    manifest = {
        "name": f"gym-anything-{skill_mode}",
        "owner": {"name": "MMSkills"},
        "metadata": {
            "description": f"{skill_mode.capitalize()} skill for {env_name}",
            "version": "1.0.0",
        },
        "plugins": [
            {
                "name": f"gym-anything-{env_name}-{skill_mode}",
                "description": f"{skill_mode.capitalize()} skill for {env_name}",
                "source": "./",
                "strict": False,
                "skills": [f"./skills/{skill_name}"],
            }
        ],
    }
    (plugin_root / ".claude-plugin" / "marketplace.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8",
    )

    logger.info("Built plugin dir for skill %s at %s", skill_name, plugin_root)
    return f"{CONTAINER_WORKSPACE}/plugin"

SYSTEM_PROMPT = """\
You are utilising an Ubuntu virtual machine to complete a task autonomously.
The screen resolution is 1280x720.

You MUST interact with applications through their GUI only. \
Do NOT open a terminal, run shell commands, edit config files, or use any programmatic workaround.

You have the following MCP tools to interact with the desktop:
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

After each action, carefully evaluate the returned screenshot to confirm you \
achieved the right outcome before moving on. If not correct, try again.

When you believe the task is complete, simply stop — do not call any signal tool.\
"""


# ── config ──────────────────────────────────────────────────────────────────

DEFAULTS = {
    "model": "claude-opus-4-6",
    "skill_mode": "none",
    "task_timeout": 1800,
    "max_steps": None,
    "bridge_port_base": 8766,
    "result_dir": "scripts/run-gym-anything/workspaces",
    "claude_cli_image": "ga-claude-cli",
    "max_tasks": 0,
    "rerun": False,
    "use_cache": False,
    "log_level": "INFO",
    "num_parallel": 1,
}


def load_config(config_path: str) -> dict:
    """Load YAML config with defaults applied."""
    with open(config_path) as f:
        cfg = yaml.safe_load(f) or {}

    for k, v in DEFAULTS.items():
        cfg.setdefault(k, v)

    # Resolve relative paths against MMSKILLS_ROOT
    for key in ("env_dir", "result_dir"):
        if key in cfg and not Path(cfg[key]).is_absolute():
            cfg[key] = str(MMSKILLS_ROOT / cfg[key])

    return cfg


# ── task discovery ──────────────────────────────────────────────────────────

def discover_tasks(cfg: dict) -> list[str]:
    """Return list of task IDs based on config."""
    # Explicit task_list takes priority
    if cfg.get("task_list"):
        return cfg["task_list"]

    env_path = Path(cfg["env_dir"])
    tasks_dir = env_path / "tasks"

    if cfg.get("split"):
        env_name = env_path.name
        splits_dir = env_path.parent.parent / "splits"
        candidates = [
            splits_dir / f"{env_name}_split.json",
            splits_dir / f"{env_name.removesuffix('_env')}_split.json",
        ]
        for split_file in candidates:
            if split_file.exists():
                split_data = json.loads(split_file.read_text(encoding="utf-8"))
                split = cfg["split"]
                key = f"{split}_tasks" if split != "all" else "all_tasks"
                if key in split_data:
                    task_ids = split_data[key]
                    existing = [t for t in task_ids if (tasks_dir / t).is_dir()]
                    if existing:
                        return existing
                break

    # Fallback: all task directories
    if tasks_dir.is_dir():
        return sorted(d.name for d in tasks_dir.iterdir() if d.is_dir())
    return []


# ── MCP config ──────────────────────────────────────────────────────────────

def _write_mcp_config(
    output_dir: Path,
    bridge_port: int,
    skill_dir: Path | None = None,
) -> None:
    config = {
        "mcpServers": {
            "gym-anything-controller": {
                "command": "python3",
                "args": [MCP_SERVER_PATH],
                "env": {"GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}"},
            }
        }
    }
    # If the chosen skill ships its own MCP server at tools/skill_server.py,
    # register it as an additional MCP server. The skill is mounted read-only
    # under /opt/mmskills/skills/<skill_name>/.
    if skill_dir is not None:
        srv = skill_dir / "tools" / "skill_server.py"
        if srv.exists():
            container_srv_path = (
                f"{CONTAINER_MMSKILLS_ROOT}/skills/{skill_dir.name}"
                "/tools/skill_server.py"
            )
            config["mcpServers"]["skill-loader"] = {
                "command": "python3",
                "args": [container_srv_path],
            }
    (output_dir / "mcp_config.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8"
    )


# ── Claude Docker container ────────────────────────────────────────────────

def _run_claude_in_docker(
    docker_client: docker.DockerClient,
    output_dir: Path,
    bridge_port: int,
    cfg: dict,
    logger: logging.Logger,
    plugin_dir: str | None = None,
    bridge_server=None,
) -> tuple[str, str]:
    """Run Claude CLI in an isolated Docker container. Returns (stdout, stderr)."""
    cli_args = [
        "--mcp-config", "/workspace/mcp_config.json",
        "--output-format", "stream-json",
        "--verbose",
        "--model", cfg["model"],
        "--no-session-persistence",
        "--dangerously-skip-permissions",
        "--disallowed-tools", "Bash,Edit,Write,Glob,Grep,Agent,AskUserQuestion,NotebookEdit",
    ]
    if plugin_dir:
        cli_args.extend(["--plugin-dir", plugin_dir])

    env_vars = {
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}",
    }

    container_name = f"ga-claude-{output_dir.name[:12]}-p{bridge_port}"
    try:
        old = docker_client.containers.get(container_name)
        old.remove(force=True)
    except docker.errors.NotFound:
        pass

    logger.info("Starting Claude container: %s (bridge port %d)", container_name, bridge_port)

    credentials_path = os.path.expanduser("~/.claude/.credentials.json")
    container = docker_client.containers.run(
        cfg["claude_cli_image"],
        command=cli_args,
        name=container_name,
        environment=env_vars,
        extra_hosts={"host.docker.internal": "host-gateway"},
        volumes={
            str(output_dir): {"bind": "/workspace", "mode": "rw"},
            str(MMSKILLS_ROOT): {"bind": "/opt/mmskills", "mode": "ro"},
            credentials_path: {
                "bind": "/home/node/.claude/.credentials.json", "mode": "ro",
            },
        },
        detach=True,
    )

    # Watcher thread: as soon as the env signals episode_done (max_steps
    # reached or timeout), kill the Claude container so it cannot burn
    # tokens on EPISODE-ENDED retries. Polls every 1s.
    killed_by_watcher = threading.Event()

    def _episode_done_watcher() -> None:
        while not killed_by_watcher.is_set():
            if bridge_server is not None and getattr(bridge_server, "episode_done", False):
                logger.info(
                    "Episode done (%s) — killing Claude container",
                    getattr(bridge_server, "done_reason", "?"),
                )
                try:
                    container.kill()
                except Exception:
                    pass
                killed_by_watcher.set()
                return
            time.sleep(1.0)

    watcher = threading.Thread(target=_episode_done_watcher, daemon=True)
    watcher.start()

    try:
        result = container.wait(timeout=cfg["task_timeout"])
        stdout = container.logs(stdout=True, stderr=False).decode(errors="replace")
        stderr = container.logs(stdout=False, stderr=True).decode(errors="replace")
        exit_code = result.get("StatusCode", -1)
        if killed_by_watcher.is_set():
            logger.info("Claude container killed by episode_done watcher")
        else:
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
        killed_by_watcher.set()  # stop the watcher
        try:
            container.remove(force=True)
        except Exception:
            pass

    return stdout, stderr


# ── single task runner ──────────────────────────────────────────────────────

def run_single_task(cfg: dict, task_id: str, bridge_port: int) -> int:
    """Run one task end-to-end. Returns 0 on success, 1 on failure."""
    logger = logging.getLogger(f"task.{task_id}")

    env_name = Path(cfg["env_dir"]).name
    output_dir = Path(cfg["result_dir"]) / cfg["model"] / f"skill-{cfg['skill_mode']}" / env_name / task_id

    # Check existing result
    score_file = output_dir / "score.txt"
    if not cfg["rerun"] and score_file.exists():
        prev = score_file.read_text().strip()
        logger.info("Skipping (existing score=%s)", prev)
        return 0

    # Fresh output dir
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    # ── Phase 1: Environment setup ──
    ga_root = MMSKILLS_ROOT / "vendor" / "gym-anything"
    if str(ga_root / "src") not in sys.path:
        sys.path.insert(0, str(ga_root / "src"))
    from gym_anything.api import from_config

    original_cwd = os.getcwd()
    os.chdir(str(ga_root))
    gapkg_link = ga_root / "gym_anything"
    if not gapkg_link.exists():
        os.symlink("src/gym_anything", str(gapkg_link))

    logger.info("Creating env for task: %s", task_id)
    env = from_config(cfg["env_dir"], task_id=task_id)

    try:
        logger.info("Resetting environment...")
        env.reset(use_cache=cfg["use_cache"])
        # Step budget is the ONLY episode budget. Per-task `init.max_steps`
        # from task.json drives the cap (or yaml override if set). The env
        # time budget (`timeout_sec`) is always disabled here so heavier
        # skill modes are not penalised for slower per-turn inference. The
        # yaml `task_timeout` (docker container-wait) remains the wall-clock
        # safety net — see _run_claude_in_docker.
        max_steps = cfg["max_steps"] if cfg.get("max_steps") is not None else env.max_steps
        env.set_episode_limits(max_steps=max_steps, timeout_sec=None)
        logger.info(
            "Environment ready (env max_steps=%s, env timeout_sec=%s, "
            "docker wait=%ds)",
            env.max_steps,
            getattr(env, "_timeout_sec", None),
            cfg["task_timeout"],
        )
    except Exception as exc:
        logger.error("Failed to set up environment: %s", exc)
        env.close()
        os.chdir(original_cwd)
        result = {"task_id": task_id, "error": str(exc), "score": 0.0}
        (output_dir / "result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
        (output_dir / "score.txt").write_text("0.0\n", encoding="utf-8")
        return 1

    # ── Phase 2: Bridge + Claude ──
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from bridge import start_bridge_server
    bridge_server = start_bridge_server(env, port=bridge_port, workspace=str(output_dir))

    elapsed = 0.0
    try:
        # Build prompt
        task_json_path = Path(cfg["env_dir"]) / "tasks" / task_id / "task.json"
        task_desc = ""
        if task_json_path.exists():
            task_data = json.loads(task_json_path.read_text(encoding="utf-8"))
            task_desc = task_data.get("description", "")

        # Skills are exposed to Claude via a per-task plugin dir. When
        # skill_mode != "none", we build a single-skill plugin dir scoped
        # to the current env so cross-domain skills don't leak in, AND we
        # add a one-line nudge to the prompt instructing Claude to consult
        # the skill before acting (otherwise it tends to ignore registered
        # plugins and proceed straight to GUI actions).
        plugin_dir = None
        skill_dir_resolved: Path | None = None
        skill_nudge = ""
        if cfg["skill_mode"] != "none":
            env_name_for_skill = Path(cfg["env_dir"]).name.removesuffix("_env")
            skill_dir_resolved = _resolve_skill_dir(
                env_name_for_skill, cfg["skill_mode"],
            )
            plugin_dir = _build_plugin_dir(
                env_name_for_skill, cfg["skill_mode"], output_dir, logger,
            )
            if plugin_dir is not None:
                skill_nudge = (
                    "\n\nBefore acting, you have a domain skill installed as a "
                    "plugin (visible in your registered skills list). Search "
                    "your installed skills for one matching this app and "
                    "task; if found, read its SKILL.md and load the topic "
                    "guide(s) most relevant to this task BEFORE issuing any "
                    "GUI actions. The skill contains screenshots and "
                    "step-by-step UI walkthroughs that will save you from "
                    "guessing menu paths."
                )

        prompt = f"{SYSTEM_PROMPT}{skill_nudge}\n\nTask: {task_desc}"
        (output_dir / "prompt.txt").write_text(prompt, encoding="utf-8")

        _write_mcp_config(output_dir, bridge_port, skill_dir=skill_dir_resolved)

        # Project-scoped Claude settings: enforces a <skill_check> block
        # before every action tool call via a PreToolUse hook.  Picked up
        # automatically because CWD inside the container is /workspace,
        # which is bound to output_dir.  Skipped when the skill ships its
        # own MCP loader (tools/skill_server.py) — those experiments use
        # an atomic load_topic tool instead of a per-step gate.
        skill_has_loader = (
            skill_dir_resolved is not None
            and (skill_dir_resolved / "tools" / "skill_server.py").exists()
        )
        if cfg["skill_mode"] != "none" and not skill_has_loader:
            claude_dir = output_dir / ".claude"
            claude_dir.mkdir(exist_ok=True)
            settings_src = (
                Path(__file__).parent / "hooks" / "settings.template.json"
            )
            (claude_dir / "settings.json").write_text(
                settings_src.read_text(), encoding="utf-8"
            )

        start_time = datetime.datetime.now()
        docker_client = docker.from_env()

        # Run Claude with retry on 500 errors
        max_retries = 3
        stdout, stderr = "", ""
        for attempt in range(1, max_retries + 1):
            stdout, stderr = _run_claude_in_docker(
                docker_client, output_dir, bridge_port, cfg, logger,
                plugin_dir=plugin_dir,
                bridge_server=bridge_server,
            )
            if "API Error: 500" in stdout or "API Error: 500" in stderr:
                logger.warning("API 500 on attempt %d/%d, retrying...", attempt, max_retries)
                continue
            break

        elapsed = (datetime.datetime.now() - start_time).total_seconds()

        (output_dir / "container_stdout.txt").write_text(stdout, encoding="utf-8")
        if stderr:
            (output_dir / "container_stderr.txt").write_text(stderr, encoding="utf-8")

    except Exception as exc:
        logger.error("Claude execution failed: %s", exc)
    finally:
        bridge_server.shutdown()

    # ── Phase 3: Verification ──
    episode_dir = getattr(env, "episode_dir", None)
    if episode_dir:
        episode_dir = Path(episode_dir).resolve()

    logger.info("Closing env (running verifier)...")
    env.close()
    os.chdir(original_cwd)

    # Collect results
    score = 0.0
    verifier_result = {}
    if episode_dir:
        summary_path = Path(episode_dir) / "summary.json"
        if summary_path.exists():
            try:
                summary = json.loads(summary_path.read_text(encoding="utf-8"))
                verifier_result = summary.get("verifier", {})
                score = verifier_result.get("score", 100.0 if verifier_result.get("passed") else 0.0)
                if score > 1:
                    score = score / 100.0
                logger.info("Verifier: passed=%s score=%.4f feedback=%s",
                            verifier_result.get("passed"), score,
                            verifier_result.get("feedback", "")[:200])
            except Exception as exc:
                logger.warning("Failed to read summary.json: %s", exc)

    result = {
        "task_id": task_id,
        "score": score,
        "elapsed_seconds": round(elapsed, 1),
        "model": cfg["model"],
        "skill_mode": cfg["skill_mode"],
        "timestamp": datetime.datetime.now().isoformat(),
        "verifier_result": verifier_result,
        "episode_dir": str(episode_dir) if episode_dir else None,
    }
    (output_dir / "result.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (output_dir / "score.txt").write_text(f"{score}\n", encoding="utf-8")

    logger.info("Task %s done: score=%.4f", task_id, score)
    return 0 if score > 0 else 1




# ── summarize ───────────────────────────────────────────────────────────────

def write_summary(cfg: dict) -> int:
    """Collect all result.json files and write a summary."""
    env_name = Path(cfg["env_dir"]).name
    base = Path(cfg["result_dir"]) / cfg["model"] / f"skill-{cfg['skill_mode']}" / env_name

    per_task = {}
    for result_file in sorted(base.glob("*/result.json")):
        try:
            r = json.loads(result_file.read_text(encoding="utf-8"))
            per_task[r["task_id"]] = r["score"]
        except Exception:
            per_task[result_file.parent.name] = 0.0

    scores = list(per_task.values())
    avg = sum(scores) / len(scores) if scores else 0.0

    summary = {
        "model": cfg["model"],
        "skill_mode": cfg["skill_mode"],
        "env": env_name,
        "num_tasks": len(scores),
        "avg_score": round(avg, 4),
        "per_task": per_task,
        "timestamp": datetime.datetime.now().isoformat(),
    }

    summary_dir = Path(cfg["result_dir"]) / cfg["model"] / f"skill-{cfg['skill_mode']}"
    summary_dir.mkdir(parents=True, exist_ok=True)
    summary_path = summary_dir / f"summary_{env_name}.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"\n{'='*60}")
    print(f"Summary: {env_name} | {cfg['model']} | skill={cfg['skill_mode']}")
    print(f"Tasks: {len(scores)} | Avg score: {avg:.4f}")
    print(f"{'='*60}")
    for task_id, score in sorted(per_task.items()):
        status = "PASS" if score > 0 else "FAIL"
        print(f"  {status}  {score:.2f}  {task_id}")
    print(f"\nSaved to: {summary_path}")

    return 0


# ── main ────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="Run a single gym-anything task")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    parser.add_argument("--task", help="Task ID to run")
    parser.add_argument("--bridge_port", type=int, help="Bridge port for this task")
    parser.add_argument("--discover-tasks", action="store_true", help="Print task IDs and exit")
    parser.add_argument("--summarize", action="store_true", help="Write summary and exit")
    args = parser.parse_args()

    cfg = load_config(args.config)

    logging.basicConfig(
        level=getattr(logging, cfg["log_level"]),
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    if args.discover_tasks:
        tasks = discover_tasks(cfg)
        if cfg["max_tasks"] > 0:
            tasks = tasks[:cfg["max_tasks"]]
        for t in tasks:
            print(t)
        return 0

    if args.summarize:
        return write_summary(cfg)

    if not args.task:
        print("ERROR: --task is required (or use --discover-tasks / --summarize)", file=sys.stderr)
        return 1
    if not args.bridge_port:
        print("ERROR: --bridge_port is required", file=sys.stderr)
        return 1

    return run_single_task(cfg, args.task, args.bridge_port)


if __name__ == "__main__":
    raise SystemExit(main())
