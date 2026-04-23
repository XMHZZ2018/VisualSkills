"""Phase 2: Assembler.

Invokes `claude -p <prompt>` (Opus) on the host with CWD = pipeline output
dir.  Claude reads every worker's notes.md + (selectively) screenshots and
writes the final skill/ folder itself via Write / Bash cp.
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prompts import ASSEMBLER_PROMPT  # noqa: E402


def assemble(
    pipeline_dir: Path,
    model: str,
    timeout: int,
) -> int:
    logger = logging.getLogger("assemble")

    workers_root = pipeline_dir / "workers"
    plan_path = pipeline_dir / "plan" / "plan.json"
    skill_out = pipeline_dir / "skill"
    skill_out.mkdir(parents=True, exist_ok=True)
    (skill_out / "regions").mkdir(exist_ok=True)
    (skill_out / "images").mkdir(exist_ok=True)

    prompt = ASSEMBLER_PROMPT.format(
        n_workers=len(list(workers_root.glob("worker_*"))),
        workers_root=str(workers_root.resolve()),
        plan_path=str(plan_path.resolve()),
        skill_out=str(skill_out.resolve()),
    )
    (pipeline_dir / "assembler_prompt.txt").write_text(prompt, encoding="utf-8")

    # Allow Write + Bash (for cp) + Read + Glob/Grep (for finding worker files).
    cli = [
        "claude", "-p", prompt,
        "--model", model,
        "--dangerously-skip-permissions",
        "--disallowed-tools", "Agent,AskUserQuestion,NotebookEdit",
        "--output-format", "stream-json",
        "--verbose",
    ]

    logger.info("invoking assembler claude (model=%s) in %s", model, pipeline_dir)
    stdout_path = pipeline_dir / "assembler_stdout.jsonl"
    stderr_path = pipeline_dir / "assembler_stderr.txt"

    with stdout_path.open("w") as out_f, stderr_path.open("w") as err_f:
        proc = subprocess.run(
            cli,
            stdout=out_f,
            stderr=err_f,
            cwd=str(pipeline_dir),
            timeout=timeout,
        )

    logger.info("assembler claude exit=%d", proc.returncode)

    # Report output
    skill_md = skill_out / "SKILL.md"
    regions = list((skill_out / "regions").glob("*.md"))
    images = list((skill_out / "images").glob("*.png"))
    logger.info("skill output: SKILL.md=%s, regions=%d, images=%d",
                skill_md.exists(), len(regions), len(images))

    return proc.returncode


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pipeline-dir", type=Path, required=True)
    ap.add_argument("--model", default="claude-opus-4-6")
    ap.add_argument("--timeout", type=int, default=1800)
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )
    return assemble(
        pipeline_dir=args.pipeline_dir,
        model=args.model,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    raise SystemExit(main())
