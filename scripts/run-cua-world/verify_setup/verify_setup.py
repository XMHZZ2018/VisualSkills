"""
Verify task setup scripts by running them in parallel Docker containers
and capturing screenshots.

Usage:
    python3 verify_setup.py --config config.yaml [--num_parallel 8] [--output_dir /tmp/setup_verify]

Config YAML format (same as run.sh configs):
    env_dir: vendor/gym-anything/benchmarks/cua_world/environments/gimp_env_all_fast
    task_list:
      - neon_edges
      - newsprint
      - levels_adjust
    num_parallel: 8   # optional, default 4

Output:
    <output_dir>/
      <task_id>/
        screenshot.png    # screenshot after setup
        setup_log.txt     # setup script stdout/stderr
        status.txt        # PASS/FAIL + details
    summary.txt           # overview of all tasks
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import shutil
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("verify_setup")


def _init_gym_anything():
    """Add CUA-World to sys.path and ensure symlink exists."""
    ga_root = MMSKILLS_ROOT / "vendor" / "cua-world"
    src = str(ga_root / "src")
    if src not in sys.path:
        sys.path.insert(0, src)
    gapkg_link = ga_root / "gym_anything"
    if not gapkg_link.exists():
        os.symlink("src/gym_anything", str(gapkg_link))
    return ga_root


def verify_single_task(
    env_dir: str,
    task_id: str,
    output_dir: Path,
    use_cache: bool = False,
) -> dict:
    """
    Set up a single task in a Docker container, take a screenshot, and tear down.

    Returns a dict with task_id, status, screenshot_path, and details.
    """
    logger = logging.getLogger(f"verify.{task_id}")
    # Flat layout: PNGs at the top of output_dir, auxiliary text files in a
    # _meta/<task_id>/ sibling so the user can browse all screenshots at once.
    task_output = output_dir / "_meta" / task_id
    task_output.mkdir(parents=True, exist_ok=True)
    screenshot_path = output_dir / f"{task_id}.png"

    ga_root = MMSKILLS_ROOT / "vendor" / "cua-world"
    original_cwd = os.getcwd()

    # Resolve env_dir relative to MMSKILLS_ROOT before chdir
    resolved_env_dir = str((MMSKILLS_ROOT / env_dir).resolve())

    os.chdir(str(ga_root))

    result = {
        "task_id": task_id,
        "status": "FAIL",
        "screenshot": None,
        "details": "",
        "elapsed_sec": 0,
    }

    try:
        from gym_anything.api import from_config

        logger.info("Creating environment...")
        env = from_config(resolved_env_dir, task_id=task_id)

        start = time.time()
        logger.info("Running setup (reset)...")
        reset_info = env.reset(use_cache=use_cache)
        elapsed = time.time() - start
        result["elapsed_sec"] = round(elapsed, 1)
        logger.info("Setup completed in %.1fs", elapsed)

        # Check if pre_task hook failed (window list check).
        # We require the *application* main window to be open — not just any
        # window. Modal dialogs like "Profile Missing" are explicit failures.
        # Per-env target window keywords are read from env.json's
        # `verify_setup.window_keywords` (case-insensitive), with a generic
        # default of the env folder basename.
        pre_task_ok = True
        try:
            import subprocess
            cn = env._runner.container_name

            # Resolve target window keywords from env.json if present.
            env_json_path = Path(resolved_env_dir) / "env.json"
            target_keywords: list[str] = []
            blocker_keywords: list[str] = ["profile missing"]
            if env_json_path.exists():
                try:
                    ej = json.loads(env_json_path.read_text(encoding="utf-8"))
                    vs = ej.get("verify_setup", {}) or {}
                    target_keywords = [k.lower() for k in vs.get("window_keywords", [])]
                    blocker_keywords += [k.lower() for k in vs.get("blocker_keywords", [])]
                except Exception:
                    pass
            if not target_keywords:
                stem = Path(resolved_env_dir).name
                if stem.endswith("_env"):
                    stem = stem[:-4]
                target_keywords = [stem.lower()]

            # Poll wmctrl up to 20s for the target keyword to appear. Apps
            # like Zotero briefly show a title of just "Zotero" before
            # settling on "My Library - Zotero"; without polling we race
            # that title transition.
            window_list = ""
            for _ in range(20):
                wm_result = subprocess.run(
                    ["docker", "exec", cn, "bash", "-c",
                     "DISPLAY=:1 wmctrl -l 2>/dev/null"],
                    capture_output=True, text=True, timeout=10,
                )
                window_list = wm_result.stdout.strip()
                wl_lower = window_list.lower()
                if any(k in wl_lower for k in target_keywords):
                    break
                if any(b in wl_lower for b in blocker_keywords):
                    break
                time.sleep(1)

            wl_lower = window_list.lower()
            blocker_hit = next(
                (b for b in blocker_keywords if b in wl_lower), None,
            )
            target_hit = any(k in wl_lower for k in target_keywords)

            if not window_list:
                pre_task_ok = False
                logger.warning("No windows open after setup for %s", task_id)
            elif blocker_hit:
                pre_task_ok = False
                logger.warning(
                    "Blocker window present (%s) for %s", blocker_hit, task_id,
                )
            elif not target_hit:
                pre_task_ok = False
                logger.warning(
                    "Target window (%s) not in window list for %s: %r",
                    "/".join(target_keywords), task_id, window_list,
                )
        except Exception as e:
            logger.debug("wmctrl check failed: %s", e)

        # Before screenshot: dismiss GNOME Activities Overview and any modal
        # dialogs (Escape, twice, with delays for animation to settle), then
        # raise+maximize the target window. Without this, fresh GNOME sessions
        # frequently capture the Overview (workspace thumbnails + "Type to
        # search" bar) instead of the application window. A single Escape
        # isn't enough — the overview has an exit animation, and pressing
        # Escape too soon after `wmctrl -a` can re-trigger the overview.
        #
        # Resolve the target window ID via case-insensitive match on the
        # already-retrieved wmctrl -l output, then drive raise+maximize by
        # ID (`wmctrl -i -r <id> ...`). `wmctrl -r <substring>` is
        # case-sensitive, so passing the lowercase keyword (e.g.
        # "my library - zotero") silently failed to match titles like
        # "My Library - Zotero", leaving the window non-maximized.
        try:
            cn = env._runner.container_name
            win_id = ""
            for line in window_list.splitlines():
                low = line.lower()
                if any(k in low for k in target_keywords):
                    win_id = line.split(None, 1)[0]
                    break
            if win_id:
                cmd = (
                    f"DISPLAY=:1 xdotool key Escape 2>/dev/null; sleep 1; "
                    f"DISPLAY=:1 xdotool key Escape 2>/dev/null; sleep 1; "
                    f"DISPLAY=:1 wmctrl -i -a {win_id} 2>/dev/null; sleep 0.5; "
                    f"DISPLAY=:1 wmctrl -i -r {win_id} -b add,maximized_vert,maximized_horz 2>/dev/null; "
                    f"sleep 1; "
                    f"DISPLAY=:1 xdotool key Escape 2>/dev/null; sleep 0.5"
                )
            else:
                cmd = (
                    f"DISPLAY=:1 xdotool key Escape 2>/dev/null; sleep 1; "
                    f"DISPLAY=:1 xdotool key Escape 2>/dev/null; sleep 0.5"
                )
            subprocess.run(
                ["docker", "exec", cn, "bash", "-c", cmd],
                capture_output=True, text=True, timeout=15,
            )
            # Log final wmctrl + pgrep state right before screenshot for
            # debugging the dual-window Activities-Overview pattern.
            try:
                diag = subprocess.run(
                    ["docker", "exec", cn, "bash", "-c",
                     "echo '--- wmctrl -lG ---'; "
                     "DISPLAY=:1 wmctrl -lG 2>/dev/null; "
                     "echo '--- pgrep zotero ---'; "
                     "pgrep -af /opt/zotero/zotero 2>/dev/null; "
                     "pgrep -af zotero-bin 2>/dev/null; "
                     "echo '--- xdotool active ---'; "
                     "DISPLAY=:1 xdotool getactivewindow getwindowname 2>/dev/null"],
                    capture_output=True, text=True, timeout=10,
                )
                meta_dir = screenshot_path.parent / "_meta" / task_id
                meta_dir.mkdir(parents=True, exist_ok=True)
                (meta_dir / "pre_screenshot_state.txt").write_text(
                    diag.stdout + ("\n" + diag.stderr if diag.stderr else "")
                )
            except Exception as e:
                logger.debug("pre-screenshot diag failed: %s", e)
        except Exception as e:
            logger.debug("pre-screenshot dismiss/raise failed: %s", e)

        # Take screenshot — capture inside container then copy to host
        container_screenshot = "/tmp/_verify_screenshot.png"
        host_screenshot = str(screenshot_path)
        logger.info("Capturing screenshot...")
        ok = env._runner.capture_screenshot(container_screenshot)

        if ok:
            try:
                env._runner.copy_from(container_screenshot, host_screenshot)
            except Exception as e:
                logger.warning("copy_from failed: %s", e)
                ok = False

        if ok and Path(host_screenshot).exists():
            result["screenshot"] = host_screenshot
            if pre_task_ok:
                result["status"] = "PASS"
                result["details"] = f"Setup OK, screenshot captured ({elapsed:.1f}s)"
            else:
                result["status"] = "FAIL"
                result["details"] = f"No application window open after setup ({elapsed:.1f}s)"
            logger.info("Screenshot saved: %s", host_screenshot)
        else:
            result["details"] = f"Setup completed but screenshot capture failed ({elapsed:.1f}s)"
            logger.warning("Screenshot capture failed for %s", task_id)

        # Grab setup logs from container
        try:
            log_paths = [
                "/home/ga/env_setup_pre_start.log",
                "/home/ga/env_setup_post_start.log",
                "/home/ga/env_setup_reset.log",
                "/home/ga/env_setup_pre_task.log",
                "/home/ga/task_pre_task.log",
                "/tmp/gimp_task.log",
                "/tmp/task_setup.log",
                "/tmp/impress_task.log",
                "/tmp/writer.log",
                "/tmp/writer_task.log",
                "/tmp/writer_launch.log",
                "/tmp/writer_audit_task.log",
                "/tmp/writer_inspection_task.log",
                "/tmp/writer_protocol_task.log",
                "/tmp/writer_nih_task.log",
                "/tmp/writer_psa_task.log",
            ]
            setup_log = ""
            for lp in log_paths:
                host_tmp = str(task_output / f"_tmp_{Path(lp).name}")
                try:
                    env._runner.copy_from(lp, host_tmp)
                    content = Path(host_tmp).read_text(errors="replace")
                    if content.strip():
                        setup_log += f"\n=== {lp} ===\n{content}"
                    Path(host_tmp).unlink(missing_ok=True)
                except Exception:
                    pass
            if setup_log:
                (task_output / "setup_log.txt").write_text(setup_log, encoding="utf-8")
        except Exception as e:
            logger.debug("Could not collect setup logs: %s", e)

        # Close environment (tears down container)
        env.close()

    except Exception as exc:
        result["details"] = f"Setup failed: {exc}"
        logger.error("Failed for %s: %s", task_id, exc)
        try:
            env.close()
        except Exception:
            pass
    finally:
        os.chdir(original_cwd)

    # Write status file
    (task_output / "status.txt").write_text(
        f"{result['status']}: {result['details']}\n", encoding="utf-8"
    )

    return result


def discover_tasks(env_dir: str, cfg: dict) -> list[str]:
    """Get task list from config or discover from env_dir."""
    if "task_list" in cfg and cfg["task_list"]:
        return cfg["task_list"]

    tasks_dir = Path(env_dir) / "tasks"
    if not tasks_dir.exists():
        log.error("No tasks directory found at %s", tasks_dir)
        return []

    tasks = []
    for d in sorted(tasks_dir.iterdir()):
        if d.is_dir() and (d / "task.json").exists():
            tasks.append(d.name)
    return tasks


def main():
    parser = argparse.ArgumentParser(description="Verify task setup scripts")
    parser.add_argument("--config", required=True, help="YAML config file")
    parser.add_argument("--num_parallel", type=int, default=None,
                        help="Number of parallel containers (overrides config)")
    parser.add_argument("--output_dir", default=None,
                        help="Output directory (default: /tmp/setup_verify/<env_name>)")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    env_dir = cfg["env_dir"]
    env_name = Path(env_dir).name

    num_parallel = args.num_parallel or cfg.get("num_parallel", 4)
    output_dir = Path(args.output_dir) if args.output_dir else Path(f"/tmp/setup_verify/{env_name}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    _init_gym_anything()

    tasks = discover_tasks(env_dir, cfg)
    if not tasks:
        log.error("No tasks found")
        return 1

    log.info("Verifying %d tasks with %d parallel containers", len(tasks), num_parallel)
    log.info("Output: %s", output_dir)

    results = []

    with ThreadPoolExecutor(max_workers=num_parallel) as pool:
        futures = {
            pool.submit(
                verify_single_task,
                env_dir,
                task_id,
                output_dir,
                cfg.get("use_cache", False),
            ): task_id
            for task_id in tasks
        }

        for future in as_completed(futures):
            task_id = futures[future]
            try:
                result = future.result()
                results.append(result)
                status = result["status"]
                log.info("[%s] %s — %s", status, task_id, result["details"])
            except Exception as exc:
                log.error("[FAIL] %s — %s", task_id, exc)
                results.append({
                    "task_id": task_id,
                    "status": "FAIL",
                    "screenshot": None,
                    "details": str(exc),
                    "elapsed_sec": 0,
                })

    # Sort by task name
    results.sort(key=lambda r: r["task_id"])

    # Write summary
    passed = sum(1 for r in results if r["status"] == "PASS")
    total = len(results)

    summary_lines = [
        f"Setup Verification: {env_name}",
        f"Tasks: {passed}/{total} passed",
        "=" * 60,
    ]
    for r in results:
        line = f"  {r['status']:4s}  {r['task_id']:<40s}  {r['elapsed_sec']:>6.1f}s"
        summary_lines.append(line)

    summary_lines.append("=" * 60)
    summary_text = "\n".join(summary_lines)
    print("\n" + summary_text)
    (output_dir / "summary.txt").write_text(summary_text + "\n", encoding="utf-8")

    # Write JSON results
    (output_dir / "results.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )

    log.info("Screenshots saved to %s", output_dir)
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
