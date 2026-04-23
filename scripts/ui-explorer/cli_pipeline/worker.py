"""One UI-explorer worker.

Lifecycle:
    1. Create gym-anything env for the impress environment (any task_id).
    2. env.reset() — spins up its own docker container with a unique UUID.
    3. start_bridge_server on bridge_port.
    4. Perform `launch_clicks` via bridge._handle_execute_action so the app
       is already in the target's starting state before Claude takes over.
    5. Write prompt.txt and mcp_config.json into the worker's workspace.
    6. Run ga-claude-cli docker container with those mounts.
    7. Collect /workspace/notes.md and /workspace/screenshots/*.png.
    8. Shutdown bridge, env.close().

This module is invoked as a subprocess by the orchestrator so each worker has
its own Python interpreter (and thus its own gym_anything import and docker
client).
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import shutil
import sys
import time
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
RUN_GA_DIR = MMSKILLS_ROOT / "scripts" / "run-gym-anything"

# Reuse the existing claude-cli docker invocation machinery.
sys.path.insert(0, str(RUN_GA_DIR))

from prompts import WORKER_SYSTEM, WORKER_USER_TEMPLATE  # noqa: E402

# Paths used by the existing ga-claude-cli container.
MCP_SERVER_PATH = "/opt/mmskills/tools/gym-anything-controller/server.py"
CONTAINER_MMSKILLS_ROOT = "/opt/mmskills"
CONTAINER_WORKSPACE = "/workspace"


def _write_mcp_config(workspace: Path, bridge_port: int) -> None:
    config = {
        "mcpServers": {
            "gym-anything-controller": {
                "command": "python3",
                "args": [MCP_SERVER_PATH],
                "env": {"GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}"},
            }
        }
    }
    (workspace / "mcp_config.json").write_text(
        json.dumps(config, indent=2), encoding="utf-8"
    )


def _run_claude_in_docker(
    workspace: Path,
    bridge_port: int,
    model: str,
    task_timeout: int,
    claude_cli_image: str,
    logger: logging.Logger,
) -> tuple[str, str, int]:
    """Run claude CLI in docker.  Worker variant: allows the Write tool so
    the agent can produce notes.md; still blocks Bash/Agent/etc."""
    import docker

    cli_args = [
        "--mcp-config", "/workspace/mcp_config.json",
        "--output-format", "stream-json",
        "--verbose",
        "--model", model,
        "--no-session-persistence",
        "--dangerously-skip-permissions",
        # Allow Write (for notes.md) and Read (for re-reading own notes).
        # Keep Bash / Edit / Glob / Grep / Agent / AskUserQuestion /
        # NotebookEdit blocked — worker only needs MCP tools + Write/Read.
        "--disallowed-tools", "Bash,Edit,Glob,Grep,Agent,AskUserQuestion,NotebookEdit",
    ]

    env_vars = {
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
        "GA_BRIDGE_URL": f"http://host.docker.internal:{bridge_port}",
    }

    container_name = f"uix-worker-{workspace.name[:16]}-p{bridge_port}"
    docker_client = docker.from_env()
    try:
        old = docker_client.containers.get(container_name)
        old.remove(force=True)
    except docker.errors.NotFound:
        pass

    logger.info("Starting claude container %s (bridge port %d)", container_name, bridge_port)
    credentials_path = os.path.expanduser("~/.claude/.credentials.json")
    container = docker_client.containers.run(
        claude_cli_image,
        command=cli_args,
        name=container_name,
        environment=env_vars,
        extra_hosts={"host.docker.internal": "host-gateway"},
        volumes={
            str(workspace): {"bind": "/workspace", "mode": "rw"},
            str(MMSKILLS_ROOT): {"bind": "/opt/mmskills", "mode": "ro"},
            credentials_path: {
                "bind": "/home/node/.claude/.credentials.json", "mode": "ro",
            },
        },
        detach=True,
    )

    try:
        result = container.wait(timeout=task_timeout)
        exit_code = result.get("StatusCode", -1)
    except Exception as exc:
        logger.warning("claude container timed out / errored: %s", exc)
        try:
            container.kill()
        except Exception:
            pass
        exit_code = -1

    stdout = container.logs(stdout=True, stderr=False).decode(errors="replace")
    stderr = container.logs(stdout=False, stderr=True).decode(errors="replace")
    try:
        container.remove(force=True)
    except Exception:
        pass

    return stdout, stderr, exit_code


def run_worker(
    worker_id: int,
    target: dict,
    bridge_port: int,
    output_dir: Path,
    env_dir: str,
    task_id: str,
    model: str,
    claude_cli_image: str,
    task_timeout: int,
    max_actions: int,
    action_wait: float,
) -> int:
    """Run one worker.  Returns 0 on success."""
    logger = logging.getLogger(f"worker.{worker_id}.{target['target_id']}")

    workspace = output_dir  # already the per-worker dir
    workspace.mkdir(parents=True, exist_ok=True)

    # ── env setup ────────────────────────────────────────────────────────
    ga_root = MMSKILLS_ROOT / "vendor" / "gym-anything"
    if str(ga_root / "src") not in sys.path:
        sys.path.insert(0, str(ga_root / "src"))

    original_cwd = os.getcwd()
    os.chdir(str(ga_root))
    gapkg_link = ga_root / "gym_anything"
    if not gapkg_link.exists():
        try:
            os.symlink("src/gym_anything", str(gapkg_link))
        except FileExistsError:
            pass

    from gym_anything.api import from_config
    from bridge import start_bridge_server  # from run-gym-anything/

    logger.info("Creating env for worker %d (task %s)", worker_id, task_id)
    env = from_config(env_dir, task_id=task_id)

    bridge_server = None
    exit_code = 1
    try:
        logger.info("Resetting env...")
        env.reset(use_cache=False)
        env.set_episode_limits(timeout_sec=task_timeout + 120)

        bridge_server = start_bridge_server(env, port=bridge_port, workspace=str(workspace))
        logger.info("Bridge up on %d", bridge_port)

        # ── launch_clicks: steer env into the target's starting state ───
        launch_clicks = target.get("launch_clicks") or []
        for (x, y) in launch_clicks:
            logger.info("launch_click (%d, %d)", x, y)
            try:
                env.step([{"mouse": {"left_click": [int(x), int(y)]}}])
            except Exception as exc:
                logger.warning("launch_click failed: %s", exc)
            time.sleep(action_wait)

        # ── prompt + mcp_config ────────────────────────────────────────
        system_prompt = WORKER_SYSTEM.format(max_actions=max_actions)
        user_prompt = WORKER_USER_TEMPLATE.format(
            target_id=target["target_id"],
            name=target["name"],
            scope_hint=target.get("scope_hint", ""),
        )
        full_prompt = system_prompt + "\n\n" + user_prompt
        (workspace / "prompt.txt").write_text(full_prompt, encoding="utf-8")
        _write_mcp_config(workspace, bridge_port)

        # Copy target metadata for downstream assembler convenience.
        (workspace / "target.json").write_text(
            json.dumps(target, indent=2), encoding="utf-8"
        )

        # ── run claude ─────────────────────────────────────────────────
        t0 = datetime.datetime.now()
        stdout, stderr, exit_code = _run_claude_in_docker(
            workspace=workspace,
            bridge_port=bridge_port,
            model=model,
            task_timeout=task_timeout,
            claude_cli_image=claude_cli_image,
            logger=logger,
        )
        elapsed = (datetime.datetime.now() - t0).total_seconds()
        logger.info("claude finished in %.1fs (exit=%d)", elapsed, exit_code)

        (workspace / "container_stdout.txt").write_text(stdout, encoding="utf-8")
        if stderr:
            (workspace / "container_stderr.txt").write_text(stderr, encoding="utf-8")

        notes_path = workspace / "notes.md"
        if notes_path.exists():
            logger.info("notes.md size = %d bytes", notes_path.stat().st_size)
        else:
            logger.warning("notes.md was NOT produced")

    except Exception as exc:
        logger.error("worker failed: %s", exc, exc_info=True)
    finally:
        if bridge_server is not None:
            try:
                bridge_server.shutdown()
            except Exception:
                pass
        try:
            env.close()
        except Exception:
            pass
        os.chdir(original_cwd)

    return 0 if exit_code == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--worker-id", type=int, required=True)
    ap.add_argument("--target-json", required=True, help="Path to a JSON file with the target dict")
    ap.add_argument("--bridge-port", type=int, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--env-dir", required=True)
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--model", default="claude-sonnet-4-6")
    ap.add_argument("--claude-cli-image", default="ga-claude-cli")
    ap.add_argument("--task-timeout", type=int, default=1200)  # 20 min
    ap.add_argument("--max-actions", type=int, default=40)
    ap.add_argument("--action-wait", type=float, default=1.0)
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    target = json.loads(Path(args.target_json).read_text(encoding="utf-8"))

    return run_worker(
        worker_id=args.worker_id,
        target=target,
        bridge_port=args.bridge_port,
        output_dir=args.output_dir,
        env_dir=args.env_dir,
        task_id=args.task_id,
        model=args.model,
        claude_cli_image=args.claude_cli_image,
        task_timeout=args.task_timeout,
        max_actions=args.max_actions,
        action_wait=args.action_wait,
    )


if __name__ == "__main__":
    raise SystemExit(main())
