"""Top-level orchestrator for the three-phase UI-explorer pipeline.

Phase 0 (planner)   → Phase 1 (N workers in parallel) → Phase 2 (assembler)

Each worker runs in its own Python subprocess so gym-anything env objects
don't share state.  Each worker gets its own bridge port (base + i + 1).
The planner uses bridge port `base`.
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import yaml

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
PIPELINE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE_DIR))

from plan import plan as run_plan  # noqa: E402
from assemble import assemble as run_assemble  # noqa: E402
from map_regions import map_regions as run_map_regions  # noqa: E402


log = logging.getLogger("orchestrator")


def load_config(path: str) -> dict:
    cfg = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    defaults = {
        "n_workers": 8,
        "bridge_port_base": 9000,
        "planner_model": "claude-opus-4-6",
        "worker_model": "claude-sonnet-4-6",
        "assembler_model": "claude-opus-4-6",
        "mapper_model": "claude-opus-4-6",
        "claude_cli_image": "ga-claude-cli",
        "task_timeout": 1200,
        "max_actions": 40,
        "action_wait": 1.0,
        "planner_timeout": 600,
        "assembler_timeout": 1800,
        "mapper_timeout": 900,
    }
    for k, v in defaults.items():
        cfg.setdefault(k, v)

    for key in ("env_dir", "output_dir"):
        if key in cfg and not Path(cfg[key]).is_absolute():
            cfg[key] = str(MMSKILLS_ROOT / cfg[key])

    return cfg


def _run_worker_subprocess(args: dict) -> dict:
    """Invoke worker.py as a subprocess.  Runs in executor pool."""
    cmd = [
        sys.executable,
        str(PIPELINE_DIR / "worker.py"),
        "--worker-id", str(args["worker_id"]),
        "--target-json", args["target_json"],
        "--bridge-port", str(args["bridge_port"]),
        "--output-dir", args["output_dir"],
        "--env-dir", args["env_dir"],
        "--task-id", args["task_id"],
        "--model", args["model"],
        "--claude-cli-image", args["claude_cli_image"],
        "--task-timeout", str(args["task_timeout"]),
        "--max-actions", str(args["max_actions"]),
        "--action-wait", str(args["action_wait"]),
    ]
    log_path = Path(args["output_dir"]) / "worker.log"
    Path(args["output_dir"]).mkdir(parents=True, exist_ok=True)
    with log_path.open("w") as f:
        proc = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, timeout=args["task_timeout"] + 600)
    return {
        "worker_id": args["worker_id"],
        "target_id": args["target_id"],
        "exit_code": proc.returncode,
        "log": str(log_path),
    }


def run(cfg: dict, output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── Phase 0 ──────────────────────────────────────────────────────────
    plan_dir = output_dir / "plan"
    plan_json_path = plan_dir / "plan.json"
    if plan_json_path.exists():
        log.info("plan.json already exists — skipping planner")
    else:
        log.info("═══ Phase 0: planner ═══")
        t0 = time.time()
        rc = run_plan(
            env_dir=cfg["env_dir"],
            task_id=cfg["planner_task_id"],
            plan_dir=plan_dir,
            n_workers=cfg["n_workers"],
            model=cfg["planner_model"],
            timeout=cfg["planner_timeout"],
        )
        log.info("planner done in %.1fs rc=%d", time.time() - t0, rc)
        if rc != 0 or not plan_json_path.exists():
            log.error("planner failed; aborting")
            return 1

    plan_data = json.loads(plan_json_path.read_text(encoding="utf-8"))
    targets = plan_data.get("targets", [])
    if not targets:
        log.error("plan.json has no targets; aborting")
        return 1
    log.info("plan has %d targets", len(targets))

    # ── Phase 1: workers in parallel ────────────────────────────────────
    workers_root = output_dir / "workers"
    workers_root.mkdir(parents=True, exist_ok=True)

    worker_args = []
    for i, target in enumerate(targets):
        worker_dir = workers_root / f"worker_{i:02d}_{target['target_id']}"
        worker_dir.mkdir(parents=True, exist_ok=True)
        target_json = worker_dir / "target.json"
        target_json.write_text(json.dumps(target, indent=2), encoding="utf-8")
        worker_args.append({
            "worker_id": i,
            "target_id": target["target_id"],
            "target_json": str(target_json),
            "bridge_port": cfg["bridge_port_base"] + i + 1,
            "output_dir": str(worker_dir),
            "env_dir": cfg["env_dir"],
            "task_id": cfg["planner_task_id"],
            "model": cfg["worker_model"],
            "claude_cli_image": cfg["claude_cli_image"],
            "task_timeout": cfg["task_timeout"],
            "max_actions": cfg["max_actions"],
            "action_wait": cfg["action_wait"],
        })

    log.info("═══ Phase 1: %d workers in parallel ═══", len(worker_args))
    t1 = time.time()
    results = []
    with ProcessPoolExecutor(max_workers=len(worker_args)) as pool:
        futures = {pool.submit(_run_worker_subprocess, a): a for a in worker_args}
        for fut in as_completed(futures):
            a = futures[fut]
            try:
                res = fut.result()
            except Exception as exc:
                log.error("worker %d (%s) errored: %s", a["worker_id"], a["target_id"], exc)
                res = {"worker_id": a["worker_id"], "target_id": a["target_id"],
                       "exit_code": -1, "log": a["output_dir"] + "/worker.log"}
            results.append(res)
            log.info("worker %d (%s) done exit=%d",
                     res["worker_id"], res["target_id"], res["exit_code"])
    log.info("all workers done in %.1fs", time.time() - t1)

    (output_dir / "workers_summary.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )

    # Count how many actually produced notes.md + notes.json
    note_counts = []
    for a in worker_args:
        wdir = Path(a["output_dir"])
        notes_md = wdir / "notes.md"
        notes_json = wdir / "notes.json"
        note_counts.append({
            "worker_id": a["worker_id"],
            "target_id": a["target_id"],
            "notes_md_size": notes_md.stat().st_size if notes_md.exists() else 0,
            "notes_json_size": notes_json.stat().st_size if notes_json.exists() else 0,
        })
    log.info("notes sizes: %s", note_counts)
    usable = sum(1 for n in note_counts if n["notes_md_size"] > 200)
    if usable == 0:
        log.error("no worker produced usable notes.md; aborting assembler")
        return 1
    with_json = sum(1 for n in note_counts if n["notes_json_size"] > 50)
    log.info("%d/%d workers produced notes.json", with_json, len(note_counts))
    if with_json == 0:
        log.warning("no worker produced notes.json — assembler will have to fall back to narrative notes.md")

    # ── Phase 2: assembler ──────────────────────────────────────────────
    log.info("═══ Phase 2: assembler ═══")
    t2 = time.time()
    rc = run_assemble(
        pipeline_dir=output_dir,
        model=cfg["assembler_model"],
        timeout=cfg["assembler_timeout"],
    )
    log.info("assembler done in %.1fs rc=%d", time.time() - t2, rc)
    if rc != 0:
        log.error("assembler failed; skipping region mapping")
        return rc

    # ── Phase 2b: auto-map regions → mm-v1 guides ───────────────────────
    log.info("═══ Phase 2b: map regions → guides ═══")
    domain = cfg.get("domain") or Path(cfg["env_dir"]).name.removesuffix("_env")
    mm_v1_dir = MMSKILLS_ROOT / "skills" / f"{domain}-knowledge-multimodal-v1"
    if not mm_v1_dir.is_dir():
        log.error("mm-v1 dir not found: %s — skipping mapper", mm_v1_dir)
        return 1
    target_skill_dir_rel = f"skills/{domain}-knowledge-multimodal-v0"
    t2b = time.time()
    rc = run_map_regions(
        pipeline_dir=output_dir,
        mm_v1_dir=mm_v1_dir,
        target_skill_dir_rel=target_skill_dir_rel,
        model=cfg["mapper_model"],
        timeout=cfg["mapper_timeout"],
    )
    log.info("mapper done in %.1fs rc=%d", time.time() - t2b, rc)

    log.info("═══ pipeline complete ═══")
    log.info("output: %s", output_dir)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True)
    ap.add_argument("--output-dir", type=Path, default=None,
                    help="Override the output_dir in config")
    ap.add_argument("--force", action="store_true",
                    help="Wipe output_dir before starting (full re-run)")
    args = ap.parse_args()

    cfg = load_config(args.config)

    # Pillow is required by the assembler's img_tool.py helper.  Fail fast.
    try:
        import PIL  # noqa: F401
    except ImportError:
        print("[orchestrator] ERROR: Pillow not installed; run `pip install Pillow`",
              file=sys.stderr)
        return 2

    output_dir = args.output_dir or Path(cfg["output_dir"])
    if args.force and output_dir.exists():
        import shutil as _shutil
        print(f"[orchestrator] --force: removing {output_dir}", file=sys.stderr)
        _shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Log to both stderr and a file in output_dir
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
        handlers=[
            logging.StreamHandler(sys.stderr),
            logging.FileHandler(str(output_dir / "orchestrator.log")),
        ],
    )
    log.info("loaded config: %s", {k: v for k, v in cfg.items() if not isinstance(v, (dict, list))})

    return run(cfg, output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
