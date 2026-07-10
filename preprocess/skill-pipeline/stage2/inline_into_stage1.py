"""Phase 4 (deterministic): inline the per-region UI Reference into mm-stage1.

Replaces the previous "drop ui-reference/ as a sibling subfolder" approach.

Reads (all under <pipeline_dir> = output_dir from the config):
  - <pipeline_dir>/region_to_guides.json  (curated mapping table; specifies
    target_skill_dir, which regions own which guides, and per-region drop
    policy.  Hand-edited after inspecting Phase 3 assembler output.)
  - <pipeline_dir>/skill/regions/<region>.md  (assembler output; LLM-curated
    per-region UI Reference)
  - <pipeline_dir>/skill/images/<region>-*.png  (assembler output; cropped
    screenshots)
  - skills/<domain>-knowledge-multimodal-stage1/ (mm-stage1 source)

Writes:
  - skills/libreoffice_impress-knowledge-multimodal-stage2/ (mm-stage2, fresh copy)
    Each owning guide.md gets a  "## UI Reference — <region>"  section
    appended in place.  Cropped screenshots are copied next to the guide
    with a  ui-  prefix.  SKILL.md is unchanged from mm-stage1.

Owner confidence policy:
  - primary, relevant  → append the full UI Reference block
  - weak               → skip
  Regions with drop_recommended=true or owners=[] are skipped entirely.

Image references inside the appended content use the mm-stage1 convention
("Read the screenshot `xxx.png` in this directory") rather than markdown
images, because the agent does not auto-fetch ![]() syntax.
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[3]
# Mapping path is now derived from --pipeline-dir at runtime
# (<pipeline_dir>/region_to_guides.json).  Pipeline_dir is per-domain so
# the suffix in the filename is no longer needed.
MAPPING_FILENAME = "region_to_guides.json"

logger = logging.getLogger("inline_into_stage1")


# ---------- region.md transformation ----------

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n+", re.DOTALL)
SCREENSHOT_BLOCK_RE = re.compile(
    r"##\s+Screenshot\s*\n+(?:!\[[^\]]*\]\([^)]+\)\s*\n*)+",
    re.IGNORECASE,
)
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def replace_screenshot_block(text: str, ui_image_filenames: list[str]) -> str:
    """Remove the existing  '## Screenshot \\n ![]()'  block and insert a
    'Read the screenshot ...' line per renamed image right after the heading."""
    read_lines = [
        f"Read the screenshot `{name}` in this directory."
        for name in ui_image_filenames
    ]
    replacement = "\n".join(read_lines) + "\n\n" if read_lines else ""
    return SCREENSHOT_BLOCK_RE.sub(replacement, text, count=1)


def strip_inline_md_images(text: str, ui_image_filenames: list[str]) -> str:
    """Any leftover ![](../images/foo.png) (e.g., in element bullets) gets
    rewritten to a 'Read ...' inline reference using the renamed filename."""
    def repl(m: re.Match) -> str:
        src = m.group(2)
        # Map the original filename to the renamed copy if we have it.
        original = Path(src).name
        for renamed in ui_image_filenames:
            # renamed == "ui-<region>-<suffix>.png"; source == "<region>-<suffix>.png"
            if renamed == "ui-" + original:
                return f"(see screenshot `{renamed}`)"
        return f"(see screenshot `{original}`)"
    return MD_IMAGE_RE.sub(repl, text)


def transform_region_md(
    region_md_text: str,
    region_id: str,
    ui_image_filenames: list[str],
) -> tuple[str, str]:
    """Convert  skill/regions/<region>.md  into  (display_name, body)  ready
    to glue into a mm-stage1 guide.md as a "## UI Reference — <display_name>"
    section.  The original H1 of the region.md becomes the display name; the
    body has its frontmatter and screenshot block stripped, image references
    rewritten to mm-stage1's "Read the screenshot ..." convention, and any
    remaining sections kept as ## subsections."""
    body = strip_frontmatter(region_md_text).strip()
    body = replace_screenshot_block(body, ui_image_filenames)
    body = strip_inline_md_images(body, ui_image_filenames)
    # Pop the H1 → use as display_name and drop from body
    lines = body.splitlines()
    display_name = region_id
    for i, line in enumerate(lines):
        if line.startswith("# "):
            display_name = line[2:].strip()
            del lines[i]
            # also drop any blank line right after
            while i < len(lines) and not lines[i].strip():
                del lines[i]
            break
    return display_name, "\n".join(lines).strip() + "\n"


# ---------- main driver ----------

def collect_region_images(images_dir: Path, region_md_text: str) -> list[Path]:
    """Image filenames are extracted from the region.md's own ![](../images/X.png)
    references, not assumed from the region_id prefix (the assembler does not
    always prefix images with the region id — e.g. character-paragraph-dialogs
    uses character-dialog-overall.png and bullets-dialog-overall.png)."""
    seen: list[Path] = []
    seen_names: set[str] = set()
    for m in MD_IMAGE_RE.finditer(region_md_text):
        src = m.group(2)
        name = Path(src).name
        if name in seen_names:
            continue
        seen_names.add(name)
        path = images_dir / name
        if path.exists():
            seen.append(path)
        else:
            logger.warning("image referenced in region.md but not on disk: %s", path)
    return seen


def fresh_copy_mm_v1(src: Path, dst: Path) -> None:
    if src.resolve() == dst.resolve():
        raise SystemExit(
            f"refuse to overwrite source: src and dst resolve to the same path: {src}"
        )
    if not src.exists():
        raise SystemExit(f"mm-stage1 source not found: {src}")
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    logger.info("copied mm-stage1 → %s", dst)


def append_section_to_guide(
    guide_path: Path,
    region_id: str,
    region_name: str,
    scope: str,
    transformed_body: str,
) -> None:
    if not guide_path.exists():
        logger.warning("guide not found, skipping: %s", guide_path)
        return
    existing = guide_path.read_text(encoding="utf-8").rstrip()
    section = (
        f"\n\n---\n\n"
        f"## UI Reference  —  {region_name}\n\n"
        f"_Scope: {scope}_\n\n"
        f"{transformed_body}"
    )
    guide_path.write_text(existing + section + "\n", encoding="utf-8")
    logger.info("appended %s → %s", region_id, guide_path.relative_to(guide_path.parents[3]))


def inline(
    mapping_path: Path,
    pipeline_dir: Path,
    mm_v1_dir: Path,
    out_dir: Path,
    confidences: Iterable[str] = ("primary", "relevant"),
    dry_run: bool = False,
) -> None:
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    regions_md_dir = pipeline_dir / "skill" / "regions"
    images_dir = pipeline_dir / "skill" / "images"

    if not dry_run:
        fresh_copy_mm_v1(mm_v1_dir, out_dir)

    confidences = set(confidences)
    n_appended = 0
    n_skipped = 0
    n_orphan = 0

    # Each region's display name comes from plan.json (assembler input)
    plan_path = pipeline_dir / "plan" / "plan.json"
    region_names: dict[str, str] = {}
    if plan_path.exists():
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        for tgt in plan.get("targets", []):
            region_names[tgt["target_id"]] = tgt.get("name", tgt["target_id"])

    for region_id, region_info in mapping["regions"].items():
        if region_info.get("drop_recommended") or region_info.get("orphan"):
            n_skipped += 1
            logger.info("SKIP region %s (drop_recommended/orphan)", region_id)
            continue

        owners = [
            o for o in region_info.get("owners", [])
            if o.get("confidence") in confidences
        ]
        if not owners:
            n_orphan += 1
            logger.info("SKIP region %s (no qualifying owners)", region_id)
            continue

        region_md_path = regions_md_dir / f"{region_id}.md"
        if not region_md_path.exists():
            logger.warning("region.md missing for %s; skipping", region_id)
            continue

        region_md_text = region_md_path.read_text(encoding="utf-8")
        region_name = region_names.get(region_id, region_id)
        src_images = collect_region_images(images_dir, region_md_text)

        for owner in owners:
            guide_rel = owner["guide"]
            scope = owner.get("scope", "")
            target_guide = out_dir / guide_rel
            target_dir = target_guide.parent

            # Renamed filenames so they slot into the guide directory next to
            # the existing fig*.png assets without colliding.
            renamed = [f"ui-{img.name}" for img in src_images]

            if dry_run:
                logger.info(
                    "[DRY] would append %s → %s  (%d images: %s)",
                    region_id, guide_rel, len(src_images), ", ".join(renamed),
                )
                continue

            target_dir.mkdir(parents=True, exist_ok=True)
            for src_img, new_name in zip(src_images, renamed):
                shutil.copy2(src_img, target_dir / new_name)

            display_name, transformed = transform_region_md(
                region_md_text, region_id, renamed,
            )
            append_section_to_guide(
                target_guide,
                region_id,
                display_name,
                scope,
                transformed,
            )
            n_appended += 1

    logger.info(
        "DONE.  appended=%d  regions_skipped=%d  regions_no_owners=%d",
        n_appended, n_skipped, n_orphan,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--pipeline-dir", type=Path, required=True,
                    help="Per-domain output_dir from the Stage 2 config; contains "
                         "region_to_guides.json, skill/regions/, skill/images/, plan/")
    ap.add_argument("--mapping", type=Path, default=None,
                    help="Mapping JSON (default: <pipeline-dir>/region_to_guides.json)")
    ap.add_argument("--mm-v1", type=Path, default=None,
                    help="Source mm-stage1 skill directory (default: derived from mapping)")
    ap.add_argument("--out", type=Path, default=None,
                    help="Output dir (default: derived from mapping target_skill_dir)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--include-relevant", action="store_true", default=True,
                    help="Append regions with confidence='relevant' too (default on)")
    ap.add_argument("--primary-only", action="store_true",
                    help="Only append regions with confidence='primary'")
    args = ap.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s %(levelname)s %(name)s] %(message)s",
    )

    mapping_path = args.mapping or (args.pipeline_dir / MAPPING_FILENAME)
    if not mapping_path.exists():
        raise SystemExit(
            f"mapping file not found: {mapping_path}\n"
            f"Phase 4 requires a hand-curated region→guide mapping; create it "
            f"at <pipeline_dir>/{MAPPING_FILENAME} after reviewing Phase 3 output."
        )
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))

    mm_v1_dir = args.mm_v1
    if mm_v1_dir is None:
        # mm-stage1 lives next to the mm-stage2 target: replace -multimodal-stage2 → -multimodal-stage1
        target = mapping["target_skill_dir"]
        mm_v1_rel = target.replace("-multimodal-stage2", "-multimodal-stage1")
        mm_v1_dir = REPO_ROOT / mm_v1_rel

    out_dir = args.out
    if out_dir is None:
        out_dir = REPO_ROOT / mapping["target_skill_dir"]

    confidences = ("primary",) if args.primary_only else ("primary", "relevant")

    inline(
        mapping_path=mapping_path,
        pipeline_dir=args.pipeline_dir,
        mm_v1_dir=mm_v1_dir,
        out_dir=out_dir,
        confidences=confidences,
        dry_run=args.dry_run,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
