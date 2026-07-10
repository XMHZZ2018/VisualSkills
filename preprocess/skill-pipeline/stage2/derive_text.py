"""Phase 5 (Stage 2): derive text-skill-stage2 from multimodal-skill-stage2.

For every `guide.md` under `skills/<domain>-multimodal-stage2/`, replace
each inline image reference with 1-3 sentences of verbal description. Output is
markdown-only — no PNGs are copied to the text-stage2 tree.

This phase delegates to Stage 1's `derive_text_from_multimodal_dir` (defined in
`stage1/generate_skill_from_knowledge_source.py`) so the prompt, caching, and
parallel/idempotent semantics are shared between Stage 1 (Phase 6) and Stage 2 (Phase 5).
The only Stage 2-specific bit is the `FIG_REF_PATTERN`: mm-stage2 mixes mm-stage1's
``See `figXX.png``` style with the assembler's
``Read the screenshot `ui-foo.png` in this directory.`` and
``(see screenshot `bar.png`)`` styles, all of which we want to verbalize.

Usage:
    python3 derive_text.py --domain libreoffice_impress \\
        --app-name "LibreOffice Impress" --app-version "7.3.7" \\
        --parallel 4
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from pathlib import Path
import shutil

REPO_ROOT = Path(__file__).resolve().parents[3]
STAGE1_DIR = Path(__file__).resolve().parents[1] / "stage1"
sys.path.insert(0, str(STAGE1_DIR))

# Reuse Stage 1's derivation core (prompt, single-guide rewriter, parallel driver).
from generate_skill_from_knowledge_source import (  # noqa: E402
    derive_text_from_multimodal_dir,
)

logger = logging.getLogger("derive_text")


# Matches all three reference styles found in mm-stage2 guides:
#   - `See \`fig01.png\``           (mm-stage1 inline anchor)
#   - `(see \`fig01.png\`)`         (mm-stage1 inline anchor variant)
#   - `Read the screenshot \`X\``   (assembler appended UI Reference)
#   - `(see screenshot \`X\`)`      (assembler inline image rewrite)
# The PNG filename is captured in group 1 in every case.
FIG_REF_PATTERN = re.compile(
    r"\b(?:read\s+the\s+screenshot|see(?:\s+(?:the\s+)?screenshot)?)\s+"
    r"`([A-Za-z0-9_./-]+\.png)`",
    re.IGNORECASE,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--domain", required=True,
                    help="e.g. libreoffice_impress")
    ap.add_argument("--app-name", required=True,
                    help='e.g. "LibreOffice Impress"')
    ap.add_argument("--app-version", required=True,
                    help='e.g. "7.3.7"')
    ap.add_argument("--parallel", type=int, default=4,
                    help="Concurrent Claude calls (rate-limit bound; default 4)")
    ap.add_argument("--mm-dir", type=Path, default=None,
                    help="Override input dir (default: skills/<domain>-multimodal-stage2)")
    ap.add_argument("--text-dir", type=Path, default=None,
                    help="Override output dir (default: skills/<domain>-text-stage2)")
    ap.add_argument("--cache-dir", type=Path, default=None,
                    help="Override cache dir (default: workspace/<domain>/text_stage2_drafts)")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    mm_dir = args.mm_dir or (REPO_ROOT / "skills" / f"{args.domain}-multimodal-stage2")
    text_dir = args.text_dir or (REPO_ROOT / "skills" / f"{args.domain}-text-stage2")
    cache_dir = args.cache_dir or (
        Path(__file__).resolve().parent / "workspace" / args.domain / "text_stage2_drafts"
    )

    if not mm_dir.exists():
        logger.error("mm-stage2 dir not found: %s", mm_dir)
        logger.error("Run phase 4 (inline_into_stage1.py) first.")
        return 1

    logger.info("Deriving text-stage2 from %s", mm_dir)
    logger.info("Writing to %s", text_dir)
    logger.info("Cache at %s", cache_dir)

    text_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Copy SKILL.md verbatim if mm-stage2 has one (text-stage2 inherits the same index).
    mm_skill_md = mm_dir / "SKILL.md"
    if mm_skill_md.exists():
        (text_dir / "SKILL.md").write_text(mm_skill_md.read_text())
        logger.info("Copied SKILL.md verbatim")

    # Copy tools/skill_server.py so the text variant also exposes the
    # load_topic MCP tool.  Without this, load_topic is silently unavailable
    # for the text-only skill and the matched-pair comparison degrades to
    # text-with-Read vs multimodal-with-load_topic, which is no longer a
    # clean modality contrast.
    mm_tools = mm_dir / "tools"
    if mm_tools.is_dir():
        text_tools = text_dir / "tools"
        text_tools.mkdir(parents=True, exist_ok=True)
        for f in mm_tools.iterdir():
            if f.is_file() and not f.name.startswith("__pycache__"):
                shutil.copy2(f, text_tools / f.name)
        logger.info("Copied tools/ (load_topic MCP server) verbatim")

    counts = derive_text_from_multimodal_dir(
        mm_dir=mm_dir,
        text_dir=text_dir,
        cache_dir=cache_dir,
        app_name=args.app_name,
        app_version=args.app_version,
        parallel=args.parallel,
        fig_ref_pattern=FIG_REF_PATTERN,
    )
    return 0 if counts.get("FAILED", 0) == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
