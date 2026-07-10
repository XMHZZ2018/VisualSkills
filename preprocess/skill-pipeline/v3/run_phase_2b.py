"""Phase 2b runner: train-rollouts → review → targeted UI-explorer workers.

Designed to be invoked AFTER Phase 2a (free LLM-planner explorer) has finished
its workers — the targeted workers' notes are written into the SAME `workers/`
subdirectory of the Phase 2a output, so the existing Phase 3 (assemble + map +
inline) picks them up uniformly.

Steps:
  1. Run gym-anything rollouts of N train tasks with the current mm-v1 skill
     (subprocess call to run-gym-anything/run.sh).
  2. Run review.py against those trajectories → targeted_targets.json.
  3. Spawn one worker.py subprocess per target, bounded by --n-workers.
  4. Print summary.

Usage:
  python3 run_phase_2b.py \\
      --v3-config configs/writer.yaml \\
      --rollouts-config writer_train16_mm_skill.yaml \\
      --app-name "LibreOffice Writer"
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

logger = logging.getLogger("phase_2b")


MMSKILLS_ROOT = Path("/home/ziyan/MMSkills")
GA_RUN_SH = MMSKILLS_ROOT / "scripts" / "run-gym-anything" / "run.sh"
V3_DIR = MMSKILLS_ROOT / "preprocess" / "skill-pipeline" / "v3"
REVIEW_PY = V3_DIR / "review.py"
DIAGNOSE_PY = V3_DIR / "diagnose.py"
WORKER_PY = V3_DIR / "worker.py"


def _load_yaml(p: Path) -> dict:
    return yaml.safe_load(p.read_text())


def _run_rollouts(rollouts_config_rel: str, log_dir: Path) -> Path:
    """Call run-gym-anything/run.sh with the given config (path relative to
    scripts/run-gym-anything/). Returns the workspace dir containing per-task
    trajectories.
    """
    cfg_path = MMSKILLS_ROOT / "scripts" / "run-gym-anything" / rollouts_config_rel
    cfg = _load_yaml(cfg_path)
    domain = Path(cfg["env_dir"]).name  # e.g. libreoffice_writer_env
    result_dir = MMSKILLS_ROOT / cfg["result_dir"]
    skill_mode = cfg.get("skill_mode", "none")
    rollouts_dir = result_dir / cfg["model"] / f"skill-{skill_mode}" / domain
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / "rollouts.log"

    # Skip if all task dirs already have result.json
    expected = list(cfg.get("task_list", []))
    if expected:
        done = [(rollouts_dir / t / "result.json").exists() for t in expected]
        if all(done):
            logger.info("rollouts already complete (skipping): %s", rollouts_dir)
            return rollouts_dir

    logger.info("launching rollouts → %s (log: %s)", rollouts_dir, log_path)
    with log_path.open("w") as lf:
        proc = subprocess.run(
            [str(GA_RUN_SH), "--config", str(cfg_path)],
            stdout=lf, stderr=subprocess.STDOUT,
            cwd=str(MMSKILLS_ROOT), text=True,
        )
    if proc.returncode != 0:
        logger.warning("rollouts exited with code %d (continuing — partial trajectories OK)",
                       proc.returncode)
    return rollouts_dir


def _run_diagnose(rollouts_dir: Path, tasks_dir: Path, output_dir: Path,
                  app_name: str, model: str, parallel: int,
                  task_list: list[str] | None = None) -> Path:
    """Call diagnose.py once per failing trajectory; returns the diagnose dir."""
    diag_out = output_dir / "diagnose"
    diag_out.mkdir(parents=True, exist_ok=True)
    logger.info("running diagnose → %s", diag_out)
    cmd = [sys.executable, str(DIAGNOSE_PY),
           "--rollouts-dir", str(rollouts_dir),
           "--tasks-dir", str(tasks_dir),
           "--app-name", app_name,
           "--output-dir", str(diag_out),
           "--model", model,
           "--parallel", str(parallel)]
    if task_list:
        cmd.extend(["--task-list", ",".join(task_list)])
    subprocess.run(cmd, check=True)
    return diag_out


def _run_review(diagnoses_dir: Path, output_dir: Path, app_name: str,
                model: str) -> Path:
    """Call review.py over diagnoses; returns path to targeted_targets.json."""
    review_out = output_dir / "review"
    review_out.mkdir(parents=True, exist_ok=True)
    logger.info("running review (aggregator) → %s", review_out)
    cmd = [sys.executable, str(REVIEW_PY),
           "--diagnoses-dir", str(diagnoses_dir),
           "--app-name", app_name,
           "--output-dir", str(review_out),
           "--model", model]
    subprocess.run(cmd, check=True)
    return review_out / "targeted_targets.json"


def _stage_evidence_for_worker(target: dict, rollouts_dir: Path,
                               worker_dir: Path) -> Path | None:
    """Copy each evidence_screenshot from its source-task rollouts into a
    per-worker evidence/ dir, renaming as <source_task_id>__<step>.png so
    multiple sources don't collide. Returns the evidence dir path (or None
    if no evidence was attached / nothing could be staged)."""
    items = target.get("evidence_screenshots") or []
    if not items:
        return None
    evd = worker_dir / "evidence"
    evd.mkdir(parents=True, exist_ok=True)
    staged = 0
    for e in items:
        sid = e.get("source_task_id")
        shot = e.get("screenshot")
        if not sid or not shot:
            continue
        src = rollouts_dir / sid / "screenshots" / shot
        if not src.exists():
            logger.warning("evidence screenshot missing on disk: %s", src)
            continue
        dst = evd / f"{sid}__{shot}"
        if not dst.exists():
            try:
                import shutil as _sh
                _sh.copy2(src, dst)
                staged += 1
            except Exception as exc:
                logger.warning("could not stage %s -> %s: %s", src, dst, exc)
    if staged == 0:
        return None
    return evd


def _dispatch_workers(
    targets: list[dict],
    v3_cfg: dict,
    output_dir: Path,
    bridge_port_base_offset: int,
    rollouts_dir: Path | None = None,
) -> list[dict]:
    """Spawn one worker.py per target, in parallel up to v3_cfg['n_workers'].

    Each target's `setup_task_id` decides which env task to boot the worker
    on (so the fixture the failing agent worked with is loaded). Falls back
    to v3_cfg.planner_task_id (typically `_warmup`) if no setup is given.

    Each target's `evidence_screenshots` are staged into a per-worker
    `evidence/` dir and mounted into the container at /workspace/evidence/
    so the worker can Read them to see the exact failure state.
    """
    workers_dir = output_dir / "workers"
    workers_dir.mkdir(parents=True, exist_ok=True)

    n_workers = int(v3_cfg.get("n_workers", 8))
    base = int(v3_cfg["bridge_port_base"]) + bridge_port_base_offset
    env_dir = v3_cfg["env_dir"]
    if not Path(env_dir).is_absolute():
        env_dir = str(MMSKILLS_ROOT / env_dir)
    warmup = v3_cfg["planner_task_id"]
    model = v3_cfg.get("worker_model", "claude-sonnet-4-6")
    cli_image = v3_cfg.get("claude_cli_image", "ga-claude-cli")
    task_timeout = int(v3_cfg.get("task_timeout", 1800))
    max_actions = int(v3_cfg.get("max_actions", 80))
    action_wait = float(v3_cfg.get("action_wait", 1.0))

    existing_ids = {
        int(p.name.split("_")[1])
        for p in workers_dir.iterdir() if p.is_dir() and p.name.startswith("worker_")
    } if workers_dir.exists() else set()
    next_id = (max(existing_ids) + 1) if existing_ids else 0
    logger.info("dispatching %d targeted workers starting from worker_%02d (n_workers=%d)",
                len(targets), next_id, n_workers)

    def _run_one(i: int, target: dict) -> dict:
        wid = next_id + i
        tid = target.get("target_id", f"targeted_{wid:02d}")
        worker_out = workers_dir / f"worker_{wid:02d}_{tid}"
        worker_out.mkdir(parents=True, exist_ok=True)
        target_json = worker_out / "target.json"
        target_json.write_text(json.dumps(target, indent=2))

        setup_task = target.get("setup_task_id") or warmup
        evd = None
        if rollouts_dir is not None:
            evd = _stage_evidence_for_worker(target, rollouts_dir, worker_out)

        cmd = [
            sys.executable, str(WORKER_PY),
            "--worker-id", str(wid),
            "--target-json", str(target_json),
            "--bridge-port", str(base + i),
            "--output-dir", str(worker_out),
            "--env-dir", env_dir,
            "--task-id", setup_task,
            "--model", model,
            "--claude-cli-image", cli_image,
            "--task-timeout", str(task_timeout),
            "--max-actions", str(max_actions),
            "--action-wait", str(action_wait),
        ]
        if evd is not None:
            cmd += ["--evidence-dir", str(evd)]
        log_path = worker_out / "worker.log"
        with log_path.open("w") as lf:
            t0 = time.time()
            proc = subprocess.run(cmd, stdout=lf, stderr=subprocess.STDOUT, text=True)
            elapsed = time.time() - t0
        return {
            "worker_id": wid, "target_id": tid,
            "setup_task_id": setup_task,
            "evidence_dir": str(evd) if evd else None,
            "exit_code": proc.returncode, "elapsed_s": elapsed,
            "log": str(log_path),
        }

    results = []
    with ThreadPoolExecutor(max_workers=n_workers) as pool:
        futures = {pool.submit(_run_one, i, t): t for i, t in enumerate(targets)}
        for fut in as_completed(futures):
            t = futures[fut]
            try:
                r = fut.result()
            except Exception as e:
                logger.error("worker for %s errored: %s", t.get("target_id"), e)
                r = {"target_id": t.get("target_id"), "exit_code": -1, "error": str(e)}
            results.append(r)
            logger.info("  ← %s rc=%s (%.1fs)", r.get("target_id"), r.get("exit_code"), r.get("elapsed_s", 0))
    return results


def main() -> int:
    ap = argparse.ArgumentParser(description="Phase 2b: train-rollouts → review → targeted workers")
    ap.add_argument("--v3-config", required=True, type=Path,
                    help="Same v3 config used by orchestrator (writer.yaml).")
    ap.add_argument("--rollouts-config", required=True, type=str,
                    help="gym-anything yaml config (relative to scripts/run-gym-anything/) "
                         "specifying the train tasks to roll out.")
    ap.add_argument("--app-name", required=True)
    ap.add_argument("--skip-rollouts", action="store_true",
                    help="Use existing rollout trajectories (don't re-launch the agent).")
    ap.add_argument("--review-model", default="claude-opus-4-6")
    ap.add_argument("--diagnose-model", default="claude-opus-4-6")
    ap.add_argument("--diagnose-parallel", type=int, default=4)
    ap.add_argument("--skip-diagnose", action="store_true",
                    help="Reuse existing diagnose/ outputs instead of re-running diagnose.py.")
    ap.add_argument("--skip-review", action="store_true",
                    help="Reuse existing review/targeted_targets.json instead of re-running review.py.")
    ap.add_argument("--bridge-port-offset", type=int, default=100,
                    help="Added to v3_cfg.bridge_port_base for targeted workers' base port.")
    ap.add_argument("--stop-after", choices=["diagnose", "review", "workers"], default="workers",
                    help="Stop after the named stage (default: run all the way through workers).")
    args = ap.parse_args()

    logging.basicConfig(level=logging.INFO,
                        format="[%(asctime)s %(levelname)s %(name)s] %(message)s")

    v3_cfg = _load_yaml(args.v3_config)
    if "output_dir" not in v3_cfg:
        logger.error("v3 config missing output_dir"); return 1
    output_dir = Path(v3_cfg["output_dir"])
    if not output_dir.is_absolute():
        output_dir = MMSKILLS_ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load rollouts config once — used for both skip-rollouts dir computation
    # and for the task_list whitelist passed to review.py.
    ga_cfg = _load_yaml(MMSKILLS_ROOT / "scripts" / "run-gym-anything" / args.rollouts_config)
    domain = Path(ga_cfg["env_dir"]).name

    # 1. Rollouts
    if args.skip_rollouts:
        rollouts_dir = (MMSKILLS_ROOT / ga_cfg["result_dir"] / ga_cfg["model"]
                        / f"skill-{ga_cfg.get('skill_mode','none')}" / domain)
        logger.info("--skip-rollouts: reusing %s", rollouts_dir)
    else:
        rollouts_dir = _run_rollouts(args.rollouts_config, output_dir / "rollouts_log")

    # 2a. Per-trajectory diagnose
    tasks_dir = MMSKILLS_ROOT / ga_cfg["env_dir"] / "tasks"
    if args.skip_diagnose:
        diagnoses_dir = output_dir / "diagnose"
        logger.info("--skip-diagnose: reusing %s", diagnoses_dir)
    else:
        diagnoses_dir = _run_diagnose(
            rollouts_dir, tasks_dir, output_dir, args.app_name,
            args.diagnose_model, args.diagnose_parallel,
            task_list=list(ga_cfg.get("task_list", [])),
        )
    if args.stop_after == "diagnose":
        logger.info("--stop-after diagnose: done"); return 0

    # 2b. Aggregate diagnoses → targets
    if args.skip_review:
        targets_json = output_dir / "review" / "targeted_targets.json"
        logger.info("--skip-review: reusing %s", targets_json)
    else:
        targets_json = _run_review(diagnoses_dir, output_dir, args.app_name,
                                   args.review_model)
    targets = json.loads(targets_json.read_text())
    if not targets:
        logger.error("review produced 0 targets — nothing to dispatch")
        return 1
    if args.stop_after == "review":
        logger.info("--stop-after review: %d targets — stopping before workers", len(targets))
        return 0

    # 3. Targeted workers
    results = _dispatch_workers(targets, v3_cfg, output_dir,
                                args.bridge_port_offset,
                                rollouts_dir=rollouts_dir)

    # 4. Summary
    rcs = [r.get("exit_code") for r in results]
    n_ok = sum(1 for rc in rcs if rc == 0)
    logger.info("Phase 2b complete: %d/%d targeted workers exited cleanly", n_ok, len(results))
    (output_dir / "phase_2b_summary.json").write_text(json.dumps({
        "n_targets": len(targets),
        "n_workers_ok": n_ok,
        "workers": results,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
