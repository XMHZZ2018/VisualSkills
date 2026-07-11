"""Phase 0: Planner.

1.  Spin up a cua-world env, screenshot, tear it down.
2.  Invoke claude CLI (Opus) on the host with that screenshot; it writes
    plan.json with {n_workers} investigation targets.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
RUN_GA_DIR = MMSKILLS_ROOT / "scripts" / "run-cua-world"
sys.path.insert(0, str(RUN_GA_DIR))

from prompts import PLANNER_PROMPT  # noqa: E402


def take_idle_screenshot(env_dir: str, task_id: str, out_path: Path, settle_seconds: float = 6.0) -> None:
    """Spin up env, reset, wait, screenshot, tear down."""
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

    logger = logging.getLogger("plan.screenshot")
    logger.info("creating env (%s)", task_id)
    env = from_config(env_dir, task_id=task_id)
    try:
        env.reset(use_cache=False)
        time.sleep(settle_seconds)

        # capture_screenshot requires a path inside the mounted artifacts dir
        # (the docker `exec ffmpeg > path` writes from container → host via
        # the shared bind mount).  Write there, then copy out.
        import shutil as _shutil
        artifacts_root = Path(env._runner.artifacts_host_root)
        capture_dir = artifacts_root / "ui_explorer_plan"
        capture_dir.mkdir(parents=True, exist_ok=True)
        capture_path = capture_dir / "idle.png"

        logger.info("capturing screenshot -> %s (then copy to %s)", capture_path, out_path)
        ok = env._runner.capture_screenshot(str(capture_path))
        if not ok:
            raise RuntimeError("capture_screenshot returned False")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        _shutil.copy(capture_path, out_path)
    finally:
        try:
            env.close()
        except Exception:
            pass
        os.chdir(original_cwd)


def run_planner_claude(
    screenshot_path: Path,
    plan_out: Path,
    n_workers: int,
    model: str,
    timeout: int,
) -> int:
    """Invoke `claude -p <prompt>` on the host.  It writes plan.json itself
    via the Write tool.  Returns the CLI exit code."""
    workspace = plan_out.parent.resolve()
    workspace.mkdir(parents=True, exist_ok=True)

    # The prompt tells claude to Read the screenshot path and Write plan.json.
    prompt = PLANNER_PROMPT.format(
        n_workers=n_workers,
        screenshot_path=str(screenshot_path.resolve()),
    )
    (workspace / "planner_prompt.txt").write_text(prompt, encoding="utf-8")

    cli = [
        "claude", "-p", prompt,
        "--model", model,
        "--dangerously-skip-permissions",
        "--disallowed-tools", "Bash,Edit,Agent,AskUserQuestion,NotebookEdit",
        "--output-format", "stream-json",
        "--verbose",
    ]

    log = logging.getLogger("plan.claude")
    log.info("invoking claude CLI (model=%s) in %s", model, workspace)

    stdout_path = workspace / "planner_stdout.jsonl"
    stderr_path = workspace / "planner_stderr.txt"

    with stdout_path.open("w") as out_f, stderr_path.open("w") as err_f:
        proc = subprocess.run(
            cli,
            stdout=out_f,
            stderr=err_f,
            cwd=str(workspace),
            timeout=timeout,
        )

    log.info("claude CLI exit=%d", proc.returncode)

    # Validate plan.json
    if not plan_out.exists():
        log.error("plan.json not produced; stdout tail: %s",
                  stdout_path.read_text(errors="replace")[-2000:])
        return 1

    try:
        plan = json.loads(plan_out.read_text(encoding="utf-8"))
    except Exception as exc:
        log.error("plan.json not parseable JSON: %s", exc)
        return 1

    targets = plan.get("targets", [])
    log.info("plan.json OK — %d targets", len(targets))
    if len(targets) != n_workers:
        log.warning("expected %d targets, got %d", n_workers, len(targets))
    return 0


def plan(
    env_dir: str,
    task_id: str,
    plan_dir: Path,
    n_workers: int,
    model: str,
    timeout: int,
) -> int:
    plan_dir.mkdir(parents=True, exist_ok=True)
    idle_png = plan_dir / "idle.png"
    plan_json = plan_dir / "plan.json"

    take_idle_screenshot(env_dir, task_id, idle_png)

    return run_planner_claude(
        screenshot_path=idle_png,
        plan_out=plan_json,
        n_workers=n_workers,
        model=model,
        timeout=timeout,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--env-dir", required=True)
    ap.add_argument("--task-id", required=True)
    ap.add_argument("--plan-dir", type=Path, required=True)
    ap.add_argument("--n-workers", type=int, default=8)
    ap.add_argument("--model", default="claude-opus-4-6")
    ap.add_argument("--timeout", type=int, default=600)
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    return plan(
        env_dir=args.env_dir,
        task_id=args.task_id,
        plan_dir=args.plan_dir,
        n_workers=args.n_workers,
        model=args.model,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    raise SystemExit(main())
