"""PDF-first skill generation pipeline.

Uses the official LibreOffice Impress Guide PDF as the single source of truth.
Text and images are extracted directly from the PDF — no Claude interpretation
of rendered page images, no YouTube-sourced screenshots.

Usage:
  python3 generate_pdf_first.py --domain libreoffice_impress --mode both

Pipeline:
  Phase 1 — Taxonomy: reuse existing taxonomy.json (task-driven)
  Phase 2 — Extract: extract text + embedded images from PDF per topic
  Phase 3 — Generate: Claude reformats extracted text into skills
  Phase 4 — Index: generate SKILL.md files
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import fitz  # PyMuPDF
import yaml

PIPELINE_DIR = Path(__file__).parent
MMSKILLS_ROOT = PIPELINE_DIR.parent.parent
CONFIGS_DIR = PIPELINE_DIR / "configs"
WORKSPACE_DIR = PIPELINE_DIR / "workspace"


# ═══════════════════════════════════════════════════════════════════════════════
# Shared utilities (from generate_from_tasks.py)
# ═══════════════════════════════════════════════════════════════════════════════

def load_config(domain: str) -> dict:
    path = CONFIGS_DIR / f"{domain}.yaml"
    if not path.exists():
        print(f"Config not found: {path}")
        sys.exit(1)
    return yaml.safe_load(path.read_text())


def workspace(domain: str) -> Path:
    d = WORKSPACE_DIR / domain
    d.mkdir(parents=True, exist_ok=True)
    return d


def call_claude(prompt: str, timeout: int = 120) -> str | None:
    """Call Claude CLI in pipe mode. Text-only — no images."""
    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", "claude-sonnet-4-6",
    ]
    try:
        result = subprocess.run(
            cmd, input=prompt, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        print(f"      [claude] TIMEOUT after {timeout}s")
        return None
    if result.returncode != 0:
        print(f"      [claude] exit={result.returncode} stderr={result.stderr[:500]}")
        return None
    try:
        response = json.loads(result.stdout)
    except (json.JSONDecodeError, TypeError):
        print(f"      [claude] JSON parse failed, stdout[:300]={result.stdout[:300]}")
        return None
    text = response.get("result", "")
    text = re.sub(r"^```(?:markdown|md|json)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)
    return text


def load_tasks(config: dict) -> list[dict]:
    tasks_path = MMSKILLS_ROOT / config["tasks"]["json"]
    domain_key = config["tasks"]["domain_key"]
    all_tasks = json.loads(tasks_path.read_text())
    return [t for t in all_tasks if t.get("domain") == domain_key]


def _skills_dir(domain: str, modality: str) -> Path:
    return MMSKILLS_ROOT / "skills" / f"{domain.replace('_', '-')}-knowledge-{modality}"


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 1: Taxonomy (reuse cached)
# ═══════════════════════════════════════════════════════════════════════════════

def phase_taxonomy(ws: Path) -> dict:
    """Load existing taxonomy.json. Must already exist from the task-driven pipeline."""
    path = ws / "taxonomy.json"
    if not path.exists():
        print("ERROR: taxonomy.json not found. Run generate_from_tasks.py first.")
        sys.exit(1)
    taxonomy = json.loads(path.read_text())
    n_topics = sum(len(c["topics"]) for c in taxonomy["categories"])
    print(f"  Loaded taxonomy: {len(taxonomy['categories'])} categories, {n_topics} topics")
    return taxonomy


def load_page_mapping(ws: Path) -> dict[str, list[int]]:
    """Load existing topic_page_mapping.json."""
    path = ws / "topic_page_mapping.json"
    if not path.exists():
        print("ERROR: topic_page_mapping.json not found. Run generate_from_tasks.py first.")
        sys.exit(1)
    return json.loads(path.read_text())


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2: PDF Text + Image Extraction
# ═══════════════════════════════════════════════════════════════════════════════

def _find_pdf(ws: Path) -> Path:
    """Find the official guide PDF in the workspace."""
    for name in ("official-guide.pdf", "pdf_guide.pdf"):
        p = ws / name
        if p.exists():
            return p
    pdfs = list(ws.glob("*.pdf"))
    if pdfs:
        return pdfs[0]
    print("ERROR: No PDF found in workspace")
    sys.exit(1)


def extract_section_text(doc: fitz.Document, pages: list[int]) -> str:
    """Extract raw text from specific pages (0-indexed)."""
    texts = []
    for page_num in sorted(set(pages)):
        if 0 <= page_num < len(doc):
            page = doc[page_num]
            texts.append(page.get_text("text"))
    return "\n\n".join(texts)


def strip_figure_references(text: str) -> str:
    """Remove figure references for text-only skills."""
    # Remove "(Figure N)" and "(see Figure N)"
    text = re.sub(r"\s*\((?:see\s+)?Figure\s+\d+\)", "", text)
    # Remove "Figure N shows..." or "Figure N:" sentences
    text = re.sub(r"Figure\s+\d+\s+shows\s+[^.]+\.", "", text)
    # Remove standalone "See Figure N for..."
    text = re.sub(r"See\s+Figure\s+\d+\s+[^.]+\.", "", text)
    # Remove "as shown in Figure N"
    text = re.sub(r"\s*as\s+shown\s+in\s+Figure\s+\d+", "", text)
    # Clean up extra whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_section_images(
    doc: fitz.Document, pages: list[int], output_dir: Path,
    dpi: int = 150,
) -> list[dict]:
    """Render PDF pages as PNG images.

    Each page becomes one image. Returns list of dicts: {filename, width, height, page, caption}
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    extracted = []

    for page_num in sorted(set(pages)):
        if page_num < 0 or page_num >= len(doc):
            continue
        page = doc[page_num]
        page_text = page.get_text("text")

        # Render page as PNG
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(matrix=mat)
        filename = f"page{page_num + 1:03d}.png"
        img_path = output_dir / filename
        pix.save(str(img_path))

        # Try to find a caption like "Figure N: description"
        caption = ""
        cap_match = re.search(
            r"Figure\s+(\d+)[.:]\s*(.+?)(?:\n|$)", page_text,
        )
        if cap_match:
            caption = f"Figure {cap_match.group(1)}: {cap_match.group(2).strip()}"

        extracted.append({
            "filename": filename,
            "width": pix.width,
            "height": pix.height,
            "page": page_num + 1,
            "caption": caption,
        })

    return extracted


def phase_extract(ws: Path, taxonomy: dict, page_mapping: dict) -> dict:
    """Extract text and images from PDF for each topic.

    Returns: {topic_id: {"text": str, "images": list[dict]}}
    """
    pdf_path = _find_pdf(ws)
    doc = fitz.open(str(pdf_path))
    extract_dir = ws / "pdf_extract"
    extract_dir.mkdir(parents=True, exist_ok=True)

    results = {}

    for cat in taxonomy["categories"]:
        for topic in cat["topics"]:
            tid = topic["id"]
            pages = page_mapping.get(tid, [])
            if not pages:
                print(f"    [{topic['name']}] SKIP (no page mapping)")
                continue

            # Check cache
            text_cache = extract_dir / f"{tid}.txt"
            img_dir = extract_dir / tid
            meta_cache = extract_dir / f"{tid}_images.json"

            if text_cache.exists() and meta_cache.exists():
                raw_text = text_cache.read_text()
                images = json.loads(meta_cache.read_text())
                print(f"    [{topic['name']}] cached ({len(pages)} pages, {len(images)} images)")
            else:
                raw_text = extract_section_text(doc, pages)
                images = extract_section_images(doc, pages, img_dir)
                text_cache.write_text(raw_text)
                meta_cache.write_text(json.dumps(images, indent=2))
                print(f"    [{topic['name']}] extracted ({len(pages)} pages, {len(images)} images)")

            results[tid] = {"text": raw_text, "images": images, "img_dir": str(img_dir)}

    doc.close()
    return results


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3: Skill Generation
# ═══════════════════════════════════════════════════════════════════════════════

TEXT_PROMPT = """\
You are reformatting content from the official {app_name} {app_version} guide into a concise, practical guide.

Topic: {topic_name}
Description: {topic_desc}

Here is the EXACT text extracted from the official guide (pages {pages}):
---
{pdf_text}
---

Reformat this into a clean, practical guide for someone who needs to perform \
this task in {app_name} {app_version}. Rules:
- Title: "# {topic_name} ({app_name} {app_version})"
- Keep ALL menu paths, shortcuts, and procedures EXACTLY as stated in the source
- Do NOT add information not present in the source text
- Do NOT invent features, dialogs, or behaviors not described in the source
- Use **bold** for menu paths and button names
- Keep it concise — under 40 lines, scannable
- Output ONLY the markdown guide, no commentary
"""

MM_PROMPT = """\
You are creating a visual guide from the official {app_name} {app_version} guide.

Topic: {topic_name}
Description: {topic_desc}

Here is the text from the official guide (pages {pages}):
---
{pdf_text}
---

The following images were extracted from the same guide section:
{image_list}

Create a guide that:
1. Follows the same structure as the source text
2. Keeps ALL menu paths, shortcuts, and procedures EXACTLY as stated
3. References the extracted images where they illustrate a step
4. When referencing an image, use this format: \
"Read the screenshot `FILENAME` in this directory — it shows DESCRIPTION"
5. Do NOT use markdown image syntax like ![](). The reader is an AI agent \
that will use its Read tool to view image files.
6. Do NOT add information not present in the source text
7. Keep it concise — under 50 lines

Title: "# {topic_name} ({app_name} {app_version})"

Output ONLY the markdown guide, no commentary.
"""


def generate_text_skill(
    topic: dict, cat: dict, config: dict, domain: str,
    pdf_text: str, pages: list[int],
) -> bool:
    """Generate text-only skill from PDF extracted text."""
    app = config["app_name"]
    ver = config["app_version"]
    out_dir = _skills_dir(domain, "text") / cat["id"] / topic["id"]
    guide_path = out_dir / "guide.md"

    if guide_path.exists():
        print(f"    [{topic['name']}] text [cached]")
        return True

    cleaned_text = strip_figure_references(pdf_text)
    page_str = ", ".join(str(p + 1) for p in sorted(set(pages)))

    prompt = TEXT_PROMPT.format(
        app_name=app, app_version=ver,
        topic_name=topic["name"], topic_desc=topic.get("description", ""),
        pages=page_str, pdf_text=cleaned_text,
    )

    result = call_claude(prompt, timeout=180)
    if result:
        out_dir.mkdir(parents=True, exist_ok=True)
        guide_path.write_text(result.strip() + "\n")
        print(f"    [{topic['name']}] text OK")
        return True
    else:
        print(f"    [{topic['name']}] text FAILED")
        return False


def generate_mm_skill(
    topic: dict, cat: dict, config: dict, domain: str,
    pdf_text: str, pages: list[int],
    images: list[dict], img_dir: str,
) -> bool:
    """Generate multimodal skill from PDF text + embedded images."""
    app = config["app_name"]
    ver = config["app_version"]
    out_dir = _skills_dir(domain, "multimodal") / cat["id"] / topic["id"]
    guide_path = out_dir / "guide.md"

    if guide_path.exists():
        print(f"    [{topic['name']}] multimodal [cached]")
        return True

    if not images:
        print(f"    [{topic['name']}] multimodal SKIP (no images)")
        return False

    page_str = ", ".join(str(p + 1) for p in sorted(set(pages)))

    # Build image list description for the prompt
    img_lines = []
    for i, img in enumerate(images, 1):
        cap = img.get("caption", "")
        desc = f"  {i}. `{img['filename']}` ({img['width']}x{img['height']}, page {img['page']})"
        if cap:
            desc += f" — {cap}"
        img_lines.append(desc)
    image_list = "\n".join(img_lines)

    prompt = MM_PROMPT.format(
        app_name=app, app_version=ver,
        topic_name=topic["name"], topic_desc=topic.get("description", ""),
        pages=page_str, pdf_text=pdf_text,
        image_list=image_list,
    )

    result = call_claude(prompt, timeout=180)
    if result:
        out_dir.mkdir(parents=True, exist_ok=True)

        # Copy relevant images to skill directory, renaming to fig01.png etc.
        img_dir_path = Path(img_dir)
        fig_idx = 0
        filename_map = {}  # old_filename -> new_filename
        for img in images:
            src = img_dir_path / img["filename"]
            if src.exists():
                fig_idx += 1
                new_name = f"fig{fig_idx:02d}.png"
                shutil.copy2(src, out_dir / new_name)
                filename_map[img["filename"]] = new_name

        # Replace original filenames in the guide with figNN.png names
        guide_text = result
        for old_name, new_name in filename_map.items():
            guide_text = guide_text.replace(old_name, new_name)

        guide_path.write_text(guide_text.strip() + "\n")
        print(f"    [{topic['name']}] multimodal OK ({fig_idx} figs)")
        return True
    else:
        print(f"    [{topic['name']}] multimodal FAILED")
        return False


def phase_generate(
    config: dict, domain: str, taxonomy: dict,
    page_mapping: dict, extracts: dict, mode: str,
):
    """Generate skills from extracted PDF content."""
    success = True
    for cat in taxonomy["categories"]:
        for topic in cat["topics"]:
            tid = topic["id"]
            if tid not in extracts:
                continue

            data = extracts[tid]
            pages = page_mapping.get(tid, [])

            if mode in ("text", "both"):
                if not generate_text_skill(
                    topic, cat, config, domain, data["text"], pages,
                ):
                    success = False

            if mode in ("multimodal", "both"):
                if not generate_mm_skill(
                    topic, cat, config, domain,
                    data["text"], pages,
                    data["images"], data["img_dir"],
                ):
                    success = False

    return success


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4: Index (SKILL.md)
# ═══════════════════════════════════════════════════════════════════════════════

def phase_index(config: dict, domain: str, taxonomy: dict, mode: str):
    """Generate SKILL.md files."""
    app = config["app_name"]
    ver = config["app_version"]

    for modality in (["text", "multimodal"] if mode == "both" else [mode]):
        skills_dir = _skills_dir(domain, modality)
        mm = " with screenshots" if modality == "multimodal" else ""

        lines = [
            "---",
            f"name: {domain.replace('_', '-')}-knowledge",
            f'description: "Practical{mm} guides for {app} {ver} tasks. '
            f'{app} {ver} UI may differ from what you expect — '
            f'read the relevant guide before acting."',
            "---\n",
            f"# {app} {ver} Knowledge\n",
            f"Practical{mm} guides for common {app} tasks.\n",
            "## Guides\n",
        ]

        for cat in taxonomy["categories"]:
            lines.append(f"### {cat['name']}\n")
            for topic in cat["topics"]:
                rel = f"{cat['id']}/{topic['id']}/guide.md"
                path = skills_dir / rel
                if path.exists():
                    lines.append(f"- [{topic['name']}]({rel}) — {topic.get('description', '')}")
                else:
                    lines.append(f"- {topic['name']} — *(not yet generated)*")
            lines.append("")

        skills_dir.mkdir(parents=True, exist_ok=True)
        (skills_dir / "SKILL.md").write_text("\n".join(lines) + "\n")
        print(f"  {modality} SKILL.md updated")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="PDF-first skill generation")
    parser.add_argument("--domain", required=True)
    parser.add_argument("--mode", choices=["text", "multimodal", "both"], default="both")
    args = parser.parse_args()

    config = load_config(args.domain)
    ws = workspace(args.domain)

    domain = args.domain.replace("_", "-")

    print(f"=== PDF-First Pipeline: {config['app_name']} {config['app_version']} ===")
    print(f"Mode: {args.mode}")
    print()

    # Phase 1: Taxonomy (reuse cached)
    print("Phase 1: Taxonomy")
    taxonomy = phase_taxonomy(ws)
    page_mapping = load_page_mapping(ws)
    print()

    # Phase 2: Extract text + images from PDF
    print("Phase 2: PDF Extraction")
    extracts = phase_extract(ws, taxonomy, page_mapping)
    print()

    # Phase 3: Generate skills
    print("Phase 3: Generate Skills")
    # Clear old skills so we don't use cached guides from the old pipeline
    for modality in (["text", "multimodal"] if args.mode == "both" else [args.mode]):
        old_dir = _skills_dir(domain, modality)
        if old_dir.exists():
            shutil.rmtree(old_dir)
            print(f"  Cleared old {modality} skills")

    phase_generate(config, domain, taxonomy, page_mapping, extracts, args.mode)
    print()

    # Phase 4: Index
    print("Phase 4: Index")
    phase_index(config, domain, taxonomy, args.mode)
    print()

    print("Done!")


if __name__ == "__main__":
    main()
