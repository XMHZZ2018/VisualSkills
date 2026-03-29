"""
Run OSWorld evaluation with Claude CLI + osworld-controller MCP.

Architecture:
  1. This script creates one or more DesktopEnv (OSWorld VM connections).
  2. An HTTP bridge server runs in a background thread per VM, exposing
     env.controller methods over localhost HTTP.
  3. For each task, Claude CLI is invoked with --mcp-config pointing
     to a temp config that registers the osworld-controller MCP server.
     The MCP server connects back to the HTTP bridge to take screenshots
     and execute actions in the VM.
  4. After Claude exits, env.evaluate() scores the result.

Memory isolation:
  - CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 prevents auto-memory writes/reads
  - -p (print mode) runs non-interactively with no session persistence
  - Each task gets a fresh Claude process with no shared state

Parallel execution:
  - Use --parallel N with --path_to_vm pointing to a directory of .vmx files
  - Each worker gets its own VM + bridge, tasks are distributed round-robin

Usage:
    # Single task
    python scripts/run-osworld/run.py \\
        --osworld_root /path/to/OSWorld \\
        --path_to_vm /path/to/vm.vmx \\
        --specific_task_id <task_id>

    # All Chrome tasks, parallel on 4 VMs
    python scripts/run-osworld/run.py \\
        --osworld_root /path/to/OSWorld \\
        --path_to_vm /path/to/vms/ \\
        --domain chrome --parallel 4

    # Ablation: text vs multimodal vs none
    python scripts/run-osworld/run.py ... --skill_mode text
    python scripts/run-osworld/run.py ... --skill_mode multimodal
    python scripts/run-osworld/run.py ... --skill_mode none
"""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import datetime
import json
import logging
import os
import socket
import subprocess
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[2]
MCP_SERVER = MMSKILLS_ROOT / "tools" / "osworld-controller" / "server.py"
PLUGIN_DIRS = {
    "text": MMSKILLS_ROOT / "plugins" / "osworld-text",
    "multimodal": MMSKILLS_ROOT / "plugins" / "osworld-multimodal",
}


SYSTEM_PROMPT = """\
You are controlling an Ubuntu desktop inside a virtual machine to complete a task autonomously.

IMPORTANT RULES:
- Never ask the user for clarification or confirmation. Make a decision and act on it.
- Never present multiple options or ask which approach to use. Pick the most direct approach and execute it.
- Complete the task fully by yourself without any interaction.

You have the following tools to interact with the desktop:
- screenshot(): take a screenshot to see the current desktop state
- get_accessibility_tree(): get all visible UI elements and their screen coordinates
- click(x, y, button): click at pixel coordinates ("left"/"right"/"middle")
- double_click(x, y): double-click at coordinates
- move_to(x, y): move the mouse without clicking
- drag_to(start_x, start_y, end_x, end_y): click and drag
- scroll(x, y, clicks): scroll up (positive) or down (negative)
- type_text(text): type text (newlines become Enter key presses)
- key_press(key): press a single key (e.g. "enter", "tab", "escape")
- hotkey(keys): press a shortcut (e.g. ["ctrl", "c"], ["alt", "f4"])
- run_bash(script): run a bash command inside the VM

When finished:
- Call task_done() after verifying the task goal has been achieved.
- Call task_fail() if the task is impossible or you have exhausted all options.

Start by taking a screenshot to see the current state, then proceed step by step.\
"""


# ── HTTP bridge ───────────────────────────────────────────────────────────────

class _BridgeState:
    """Shared mutable state between the HTTP bridge thread and the main loop."""
    def __init__(self) -> None:
        self.controller = None   # set to env.controller before each task
        self.signal: str | None = None  # "DONE" or "FAIL", set by task_done/task_fail tool
        self.output_dir: Path | None = None  # set before each task for per-step logging
        self.step: int = 0
        self.logger: logging.Logger | None = None



def _make_handler(state: "_BridgeState"):
    """Create a request handler class bound to a specific bridge state instance."""

    class _BridgeHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            if self.path == "/screenshot":
                png = state.controller.get_screenshot()
                b64 = base64.b64encode(png).decode() if png else ""
                if png and state.output_dir:
                    state.step += 1
                    screenshots_dir = state.output_dir / "screenshots"
                    screenshots_dir.mkdir(exist_ok=True)
                    (screenshots_dir / f"step_{state.step:03d}.png").write_bytes(png)
                    if state.logger:
                        state.logger.info("[step %03d] screenshot", state.step)
                self._json({"data": b64, "mime": "image/png"})
            elif self.path == "/accessibility_tree":
                if state.logger:
                    state.logger.info("[step ---] get_accessibility_tree")
                tree = state.controller.get_accessibility_tree()
                self._json({"tree": tree or ""})
            else:
                self.send_error(404)

        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers.get("Content-Length", 0))
            body: dict = json.loads(self.rfile.read(length)) if length else {}

            if self.path == "/execute_python":
                if state.logger:
                    state.logger.info("[step ---] execute_python: %s", body.get("command", ""))
                try:
                    state.controller.execute_python_command(body["command"])
                    self._json({"ok": True})
                except Exception as exc:
                    self._json({"ok": False, "error": str(exc)}, status=500)
            elif self.path == "/run_bash":
                script = body.get("script", "")
                if state.logger:
                    state.logger.info("[step ---] run_bash: %s", script[:200])
                result = state.controller.run_bash_script(script)
                self._json(result or {"output": "", "returncode": 0})
            elif self.path == "/signal":
                state.signal = body.get("signal", "DONE")
                if state.logger:
                    state.logger.info("[step ---] signal: %s", state.signal)
                self._json({"ok": True})
            else:
                self.send_error(404)

        def _json(self, data: dict, status: int = 200) -> None:
            body = json.dumps(data, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt, *args) -> None:  # suppress noisy HTTP logs
            pass

    return _BridgeHandler


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


# ── argument parsing ──────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run OSWorld evaluation with Claude CLI + computer-use MCP"
    )
    parser.add_argument(
        "--osworld_root",
        default=os.environ.get("OSWORLD_ROOT", str(Path.home() / "Documents/OSWorld")),
        help="Path to the OSWorld repository root (default: ~/Documents/OSWorld or $OSWORLD_ROOT)",
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
    parser.add_argument("--cli_path", default="claude", help="Path to the Claude CLI binary")
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
        help="Number of parallel workers. Use with --path_to_vm pointing to a directory of .vmx files",
    )
    parser.add_argument(
        "--log_level", default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR"]
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


# ── MCP config helper ─────────────────────────────────────────────────────────

def _write_mcp_config(bridge_port: int) -> str:
    """Write a temp MCP config JSON and return its path."""
    config = {
        "mcpServers": {
            "osworld-controller": {
                "command": "python3",
                "args": [str(MCP_SERVER)],
                "env": {"OSWORLD_BRIDGE_URL": f"http://127.0.0.1:{bridge_port}"},
            }
        }
    }
    fd, path = tempfile.mkstemp(prefix="osworld_mcp_", suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(config, f)
    except Exception:
        os.close(fd)
        raise
    return path


# ── task runner ───────────────────────────────────────────────────────────────

def run_task(
    env,
    example: dict,
    args: argparse.Namespace,
    output_dir: Path,
    bridge_port: int,
    bridge_state: _BridgeState | None = None,
) -> float:
    if bridge_state is None:
        bridge_state = _BridgeState()
    task_id: str = example["id"]
    instruction: str = example["instruction"]
    lg = task_logger(task_id, output_dir)

    # Reset the VM to a clean state for this task
    lg.info("Resetting environment for task: %s", task_id)
    env.reset(task_config=example)
    bridge_state.controller = env.controller
    bridge_state.signal = None
    bridge_state.output_dir = output_dir
    bridge_state.step = 0
    bridge_state.logger = lg

    # Start screen recording
    try:
        env.controller.start_recording()
    except Exception:
        lg.warning("Could not start recording")

    # Build prompt: system context + task instruction
    # Skills are loaded automatically by Claude CLI via --plugin-dir
    prompt = f"{SYSTEM_PROMPT}\n\nTask: {instruction}"

    # Write temp MCP config with the bridge URL
    mcp_config_path = _write_mcp_config(bridge_port)
    start_time = datetime.datetime.now()

    # Memory isolation: disable auto-memory and session persistence
    env_vars = {
        **os.environ,
        "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1",
    }

    # Resolve plugin directory for skill injection based on skill_mode
    # "none" → no --plugin-dir (baseline)
    # "text" / "multimodal" → point to MMSkills repo, CLI auto-discovers skills
    cmd = [
        args.cli_path,
        "-p", prompt,
        "--mcp-config", mcp_config_path,
        "--output-format", "text",
        "--model", args.model,
        "--no-session-persistence",
        "--dangerously-skip-permissions",
    ]
    if args.skill_mode in PLUGIN_DIRS:
        cmd.extend(["--plugin-dir", str(PLUGIN_DIRS[args.skill_mode])])
    lg.info("Invoking Claude CLI: %s", " ".join(cmd))

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=args.task_timeout,
                env=env_vars,
            )
            if "API Error: 500" in (proc.stdout or "") or "API Error: 500" in (proc.stderr or ""):
                lg.warning("API 500 error on attempt %d/%d, retrying...", attempt, max_retries)
                bridge_state.signal = None  # reset signal for retry
                continue
            break
        except subprocess.TimeoutExpired:
            lg.warning("Claude CLI timed out after %ds", args.task_timeout)
            bridge_state.signal = bridge_state.signal or "FAIL"
            break
    else:
        lg.error("All %d attempts failed with API 500 errors", max_retries)

    try:
        os.unlink(mcp_config_path)
    except OSError:
        pass

    elapsed = (datetime.datetime.now() - start_time).total_seconds()
    signal = bridge_state.signal or "DONE"
    lg.info("Claude exited (%.1fs), signal=%s", elapsed, signal)

    # Record final stdout from Claude
    if "proc" in dir():
        (output_dir / "claude_output.txt").write_text(proc.stdout or "", encoding="utf-8")
        if proc.stderr:
            lg.debug("Claude stderr: %s", proc.stderr[:2000])

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

    # Each worker gets its own bridge
    bridge_port = _free_port()
    bridge_state = _BridgeState()
    server = HTTPServer(("127.0.0.1", bridge_port), _make_handler(bridge_state))
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    logger.info("Worker %d: bridge on port %d, vm=%s, %d tasks", worker_id, bridge_port, vm_path, len(task_queue))

    results = []
    env = None

    try:
        env = _make_desktop_env(args, vm_path)

        for idx, (domain, example) in enumerate(task_queue, start=1):
            task_id = example["id"]
            logger.info("Worker %d [%d/%d] %s / %s", worker_id, idx, len(task_queue), domain, task_id)
            output_dir = task_result_dir(args, domain, task_id)
            try:
                score = run_task(env, example, args, output_dir, bridge_port, bridge_state)
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
        server.shutdown()

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
        # ── Sequential mode (single VM) ──
        bridge_port = _free_port()
        bridge_state = _BridgeState()
        server = HTTPServer(("127.0.0.1", bridge_port), _make_handler(bridge_state))
        t = threading.Thread(target=server.serve_forever, daemon=True)
        t.start()
        logger.info("HTTP bridge running on port %d", bridge_port)

        scores: list[float] = []
        env = None
        try:
            env = _make_desktop_env(args, args.path_to_vm)
            for idx, (domain, example) in enumerate(tasks, start=1):
                task_id = example["id"]
                logger.info("[%d/%d] %s / %s", idx, len(tasks), domain, task_id)
                output_dir = task_result_dir(args, domain, task_id)
                try:
                    score = run_task(env, example, args, output_dir, bridge_port, bridge_state)
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
            server.shutdown()
    else:
        # ── Parallel mode (multiple VMs) ──
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
