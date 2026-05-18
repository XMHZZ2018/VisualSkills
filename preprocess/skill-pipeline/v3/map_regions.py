"""Phase 3b: auto-generate region_to_guides.json.

Reads the assembler's per-region docs under <pipeline_dir>/skill/regions/*.md
and the mm-v1 source skill (SKILL.md + per-topic guide.md files), then calls
`claude -p` (Opus) to emit <pipeline_dir>/region_to_guides.json matching the
schema consumed by inline_into_mm_v1.py.

This replaces the previous hand-edited mapping file.
"""

from __future__ import annotations

import argparse
import json
import logging
import subprocess
import sys
from pathlib import Path

MMSKILLS_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from prompts import MAP_REGIONS_PROMPT  # noqa: E402

logger = logging.getLogger("map_regions")


def _list_guides(mm_v1_dir: Path) -> list[Path]:
    return sorted(mm_v1_dir.rglob("guide.md"))


def _guide_excerpt(guide_path: Path, n_lines: int = 40) -> str:
    """First N non-empty lines of a guide.md, used as context for the mapper."""
    text = guide_path.read_text(encoding="utf-8", errors="replace")
    lines = [ln.rstrip() for ln in text.splitlines()]
    out: list[str] = []
    for ln in lines:
        out.append(ln)
        if len(out) >= n_lines:
            break
    return "\n".join(out)


def build_prompt(
    pipeline_dir: Path,
    mm_v1_dir: Path,
    target_skill_dir_rel: str,
) -> str:
    regions_dir = pipeline_dir / "skill" / "regions"
    region_files = sorted(regions_dir.glob("*.md"))
    if not region_files:
        raise FileNotFoundError(
            f"No assembler regions at {regions_dir}; run phase 3a first."
        )

    region_blocks = []
    for rf in region_files:
        slug = rf.stem
        body = rf.read_text(encoding="utf-8", errors="replace")
        region_blocks.append(f"### Region: `{slug}` (file: skill/regions/{rf.name})\n\n{body}")
    regions_section = "\n\n---\n\n".join(region_blocks)

    guides = _list_guides(mm_v1_dir)
    guide_rels = [g.relative_to(mm_v1_dir).as_posix() for g in guides]
    guide_blocks = []
    for g, rel in zip(guides, guide_rels):
        guide_blocks.append(f"### Guide: `{rel}`\n\n```md\n{_guide_excerpt(g)}\n```")
    guides_section = "\n\n---\n\n".join(guide_blocks)

    skill_md = (mm_v1_dir / "SKILL.md").read_text(encoding="utf-8", errors="replace")

    out_path = pipeline_dir / "region_to_guides.json"

    return MAP_REGIONS_PROMPT.format(
        target_skill_dir=target_skill_dir_rel,
        out_path=str(out_path.resolve()),
        guide_paths_json=json.dumps(guide_rels, indent=2),
        skill_md=skill_md,
        guides_section=guides_section,
        regions_section=regions_section,
    )


def map_regions(
    pipeline_dir: Path,
    mm_v1_dir: Path,
    target_skill_dir_rel: str,
    model: str,
    timeout: int,
) -> int:
    prompt = build_prompt(pipeline_dir, mm_v1_dir, target_skill_dir_rel)
    (pipeline_dir / "map_regions_prompt.txt").write_text(prompt, encoding="utf-8")

    # The full prompt is large (~hundreds of KB: 8 region bodies + 112 guide
    # excerpts + the whole SKILL.md). Passing it as a CLI arg trips Linux
    # ARG_MAX (E2BIG / "Argument list too long"). Pipe via stdin instead.
    cli = [
        "claude", "--print",
        "--model", model,
        "--dangerously-skip-permissions",
        "--disallowed-tools", "Agent,AskUserQuestion,NotebookEdit,Bash",
        "--output-format", "stream-json",
        "--verbose",
    ]
    logger.info("invoking mapper claude (model=%s) in %s", model, pipeline_dir)
    stdout_path = pipeline_dir / "map_regions_stdout.jsonl"
    stderr_path = pipeline_dir / "map_regions_stderr.txt"
    with stdout_path.open("w") as out_f, stderr_path.open("w") as err_f:
        proc = subprocess.run(
            cli,
            input=prompt,
            stdout=out_f,
            stderr=err_f,
            cwd=str(pipeline_dir),
            timeout=timeout,
            text=True,
        )
    logger.info("mapper claude exit=%d", proc.returncode)

    out_path = pipeline_dir / "region_to_guides.json"
    if not out_path.exists():
        logger.error("mapper did not produce %s", out_path)
        return 1

    # Sanity-validate the JSON.
    try:
        data = json.loads(out_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        logger.error("region_to_guides.json is not valid JSON: %s", exc)
        return 1
    n_regions = len(data.get("regions", {}))
    n_guides = len(data.get("guides", []))
    logger.info("mapped %d regions over %d guides → %s", n_regions, n_guides, out_path)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pipeline-dir", type=Path, required=True)
    ap.add_argument("--mm-v1-dir", type=Path, default=None,
                    help="mm-v1 source dir; default derived from --domain")
    ap.add_argument("--domain", default=None,
                    help="Used to derive mm-v1 dir if --mm-v1-dir is not given")
    ap.add_argument("--model", default="claude-opus-4-6")
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    if args.mm_v1_dir is None:
        if not args.domain:
            print("--mm-v1-dir or --domain is required", file=sys.stderr)
            return 2
        args.mm_v1_dir = MMSKILLS_ROOT / "skills" / f"{args.domain}-knowledge-multimodal-stage1"

    if not args.mm_v1_dir.is_dir():
        print(f"mm-v1 dir does not exist: {args.mm_v1_dir}", file=sys.stderr)
        return 2

    target_rel = f"skills/{args.mm_v1_dir.name.replace('-multimodal-v1', '-multimodal-v0')}"

    return map_regions(
        pipeline_dir=args.pipeline_dir,
        mm_v1_dir=args.mm_v1_dir,
        target_skill_dir_rel=target_rel,
        model=args.model,
        timeout=args.timeout,
    )


if __name__ == "__main__":
    raise SystemExit(main())
