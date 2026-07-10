"""Phase 3a: Assembler.

Invokes `claude -p <prompt>` (Opus) on the host with CWD = pipeline output
dir.  Claude reads every worker's notes.md + (selectively) screenshots and
writes the final skill/ folder itself via Write / Bash cp.

Two modes:
  --mode multimodal (default) — produces skill/{regions,images}/ with cropped
    UI screenshots. Feeds the Derived text path (Option 3, mm-stage2 →
    derive_text.py → text-stage2) and the multimodal-stage2 inline.
  --mode text — produces skill_text/regions/ with text-only region markdown
    (no images). Feeds the Independent text path (Option 1, direct inline
    into a copy of text-stage1).
  --mode both — runs both passes sequentially.
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prompts import ASSEMBLER_PROMPT, TEXT_ASSEMBLER_PROMPT  # noqa: E402


def _run_assembler(
    *,
    prompt: str,
    pipeline_dir: Path,
    skill_out: Path,
    model: str,
    timeout: int,
    log_tag: str,
) -> int:
    logger = logging.getLogger(f"assemble.{log_tag}")

    (pipeline_dir / f"assembler_prompt_{log_tag}.txt").write_text(
        prompt, encoding="utf-8"
    )

    cli = [
        "claude", "-p", prompt,
        "--model", model,
        "--dangerously-skip-permissions",
        "--disallowed-tools", "Agent,AskUserQuestion,NotebookEdit",
        "--output-format", "stream-json",
        "--verbose",
    ]

    logger.info("invoking assembler claude (model=%s) → %s", model, skill_out)
    stdout_path = pipeline_dir / f"assembler_stdout_{log_tag}.jsonl"
    stderr_path = pipeline_dir / f"assembler_stderr_{log_tag}.txt"

    with stdout_path.open("w") as out_f, stderr_path.open("w") as err_f:
        proc = subprocess.run(
            cli,
            stdout=out_f,
            stderr=err_f,
            cwd=str(pipeline_dir),
            timeout=timeout,
        )

    logger.info("assembler claude exit=%d", proc.returncode)

    skill_md = skill_out / "SKILL.md"
    regions = list((skill_out / "regions").glob("*.md"))
    logger.info(
        "output: SKILL.md=%s, regions=%d", skill_md.exists(), len(regions)
    )
    return proc.returncode


def assemble_multimodal(pipeline_dir: Path, model: str, timeout: int) -> int:
    workers_root = pipeline_dir / "workers"
    plan_path = pipeline_dir / "plan" / "plan.json"
    skill_out = pipeline_dir / "skill"
    skill_out.mkdir(parents=True, exist_ok=True)
    (skill_out / "regions").mkdir(exist_ok=True)
    (skill_out / "images").mkdir(exist_ok=True)

    img_tool = Path(__file__).resolve().parent / "img_tool.py"
    prompt = ASSEMBLER_PROMPT.format(
        n_workers=len(list(workers_root.glob("worker_*"))),
        workers_root=str(workers_root.resolve()),
        plan_path=str(plan_path.resolve()),
        skill_out=str(skill_out.resolve()),
        img_tool=str(img_tool.resolve()),
    )
    return _run_assembler(
        prompt=prompt, pipeline_dir=pipeline_dir, skill_out=skill_out,
        model=model, timeout=timeout, log_tag="mm",
    )


def assemble_text(pipeline_dir: Path, model: str, timeout: int) -> int:
    workers_root = pipeline_dir / "workers"
    plan_path = pipeline_dir / "plan" / "plan.json"
    skill_out = pipeline_dir / "skill_text"
    skill_out.mkdir(parents=True, exist_ok=True)
    (skill_out / "regions").mkdir(exist_ok=True)

    prompt = TEXT_ASSEMBLER_PROMPT.format(
        n_workers=len(list(workers_root.glob("worker_*"))),
        workers_root=str(workers_root.resolve()),
        plan_path=str(plan_path.resolve()),
        skill_out=str(skill_out.resolve()),
        pipeline_dir=str(pipeline_dir.resolve()),
    )
    return _run_assembler(
        prompt=prompt, pipeline_dir=pipeline_dir, skill_out=skill_out,
        model=model, timeout=timeout, log_tag="text",
    )


def assemble(
    pipeline_dir: Path,
    model: str,
    timeout: int,
    mode: str = "multimodal",
) -> int:
    if mode == "multimodal":
        return assemble_multimodal(pipeline_dir, model, timeout)
    if mode == "text":
        return assemble_text(pipeline_dir, model, timeout)
    if mode == "both":
        rc_mm = assemble_multimodal(pipeline_dir, model, timeout)
        rc_tx = assemble_text(pipeline_dir, model, timeout)
        return rc_mm or rc_tx
    raise ValueError(f"unknown assemble mode: {mode}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pipeline-dir", type=Path, required=True)
    ap.add_argument("--model", default="claude-opus-4-6")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument(
        "--mode", choices=["multimodal", "text", "both"], default="multimodal",
        help="multimodal: skill/ with images (default). text: skill_text/ verbal-only. both: run both.",
    )
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )
    return assemble(
        pipeline_dir=args.pipeline_dir,
        model=args.model,
        timeout=args.timeout,
        mode=args.mode,
    )


if __name__ == "__main__":
    raise SystemExit(main())
