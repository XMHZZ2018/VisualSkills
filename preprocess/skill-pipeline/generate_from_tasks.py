"""Task-driven skill generation pipeline (v1).

Entry point (preferred):
    ./run.sh --config configs/libreoffice_impress.yaml

Direct invocation:
    python3 generate_from_tasks.py --config configs/libreoffice_impress.yaml

Pipeline:
  Phase 1 — Taxonomy: cluster domain tasks into category → topic.
  Phase 2 — PDF pages: map each topic to relevant PDF pages via ToC, render at 300 DPI.
  Phase 3 — Figures: extract clean figure crops from those pages (bitmap xrefs first,
            LLM bbox detection as fallback for vector-only pages).
  Phase 4 — Text skill: generate one concise guide.md per topic from the rendered pages.
            This is the text-skill-v1 content.
  Phase 5 — Multimodal skill: pick figures relevant to the guide and splice explicit
            "Read the screenshot `figNN.png`" paragraphs into the *same* text, byte-for-byte
            identical between the two versions aside from the inserted image-reference
            paragraphs and their copied fig files.
  Phase 6 — Index: write SKILL.md for each -v1 directory.

All LLM calls go through the `claude` CLI (model: claude-opus-4-6). Artifacts are cached
under workspace/<domain>/ so re-running skips completed work.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fitz  # PyMuPDF
import yaml
from PIL import Image

PIPELINE_DIR = Path(__file__).parent
MMSKILLS_ROOT = PIPELINE_DIR.parent.parent
CONFIGS_DIR = PIPELINE_DIR / "configs"
WORKSPACE_DIR = PIPELINE_DIR / "workspace"

CLAUDE_MODEL = "claude-opus-4-6"
PDF_DPI = 300            # page render DPI — high enough for clean figure crops
FIG_CROP_PADDING_PX = 8  # pixel padding around detected figure bboxes
MIN_BITMAP_PT = 60       # min figure side in PDF points (72pt = 1in) — skip tiny icons
MIN_VECTOR_FRAC = 0.08   # min figure area fraction of page for LLM-bbox fallback

# ═══════════════════════════════════════════════════════════════════════════════
# Config & workspace
# ═══════════════════════════════════════════════════════════════════════════════

def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        print(f"Config not found: {config_path}")
        sys.exit(1)
    cfg = yaml.safe_load(config_path.read_text())
    if "domain" not in cfg:
        cfg["domain"] = config_path.stem
    return cfg


def workspace(domain: str) -> Path:
    d = WORKSPACE_DIR / domain
    d.mkdir(parents=True, exist_ok=True)
    return d


# ═══════════════════════════════════════════════════════════════════════════════
# Claude CLI wrapper
# ═══════════════════════════════════════════════════════════════════════════════

def call_claude(prompt: str, images: list[Path] | None = None, timeout: int = 180) -> str | None:
    """Invoke the `claude` CLI in pipe mode. Images are referenced by absolute path."""
    full_prompt = prompt
    if images:
        existing = [str(img) for img in images if img and Path(img).exists()]
        if existing:
            refs = "\n".join(existing)
            full_prompt = f"Here are the image files to look at:\n{refs}\n\n{prompt}"

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", CLAUDE_MODEL,
        "--dangerously-skip-permissions",
    ]

    try:
        result = subprocess.run(
            cmd, input=full_prompt, capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        print(f"      [claude] TIMEOUT after {timeout}s")
        return None
    if result.returncode != 0:
        print(f"      [claude] exit={result.returncode} stderr={result.stderr[:400]}")
        return None
    try:
        payload = json.loads(result.stdout)
    except (json.JSONDecodeError, TypeError):
        print(f"      [claude] JSON parse failed, stdout[:300]={result.stdout[:300]}")
        return None
    text = payload.get("result", "")
    text = re.sub(r"^```(?:markdown|md|json)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)
    return text


def parse_json_response(text: str) -> dict | list | None:
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        pass
    # Try the first {...} or [...] block.
    for pat in (r"\{.*\}", r"\[.*\]"):
        m = re.search(pat, text or "", re.DOTALL)
        if m:
            try:
                return json.loads(m.group())
            except json.JSONDecodeError:
                continue
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# Task loading — gym-anything (cua_world)
# ═══════════════════════════════════════════════════════════════════════════════
#
# Config shape expected under `tasks:` —
#   env_dir:   path to the gym-anything env folder (contains tasks/<name>/task.json)
#              (required)
#   task_list: optional explicit list of task folder names. If given, overrides
#              both disk enumeration and split filtering.
#   split:     optional path to the env's split JSON, used only as a filter
#   use:       which split field to intersect with — e.g. "train_tasks" or
#              "test_tasks". Ignored unless `split` is set.
#
# Default (no task_list, no split): every subfolder of tasks/ that has a valid
# task.json with a non-empty description. This is the canonical "all tasks for
# this environment" set — the split file's all_tasks can be stale.
#
# Each returned task dict: {"task_id": <folder name>, "instruction": <description>}
# ═══════════════════════════════════════════════════════════════════════════════

def _read_task(task_json: Path) -> dict | None:
    if not task_json.exists():
        return None
    try:
        data = json.loads(task_json.read_text())
    except json.JSONDecodeError:
        return None
    instr = (data.get("description") or "").strip()
    if not instr:
        return None
    return {"task_id": task_json.parent.name, "instruction": instr}


def load_tasks(config: dict) -> list[dict]:
    t = config.get("tasks", {})
    env_dir_rel = t.get("env_dir")
    if not env_dir_rel:
        print("Config error: tasks.env_dir is required (points to a gym-anything env folder)")
        sys.exit(1)
    env_dir = MMSKILLS_ROOT / env_dir_rel
    if not env_dir.exists():
        print(f"Config error: env_dir does not exist: {env_dir}")
        sys.exit(1)
    tasks_root = env_dir / "tasks"
    if not tasks_root.exists():
        print(f"Config error: tasks folder missing: {tasks_root}")
        sys.exit(1)

    # 1) Choose the candidate names.
    if t.get("task_list"):
        names = list(t["task_list"])
    else:
        names = sorted(d.name for d in tasks_root.iterdir() if d.is_dir())

    # 2) Optional split filter (for test/train subsets).
    if t.get("split") and t.get("use"):
        split_path = MMSKILLS_ROOT / t["split"]
        if not split_path.exists():
            print(f"Config error: split file not found: {split_path}")
            sys.exit(1)
        split_data = json.loads(split_path.read_text())
        field = t["use"]
        if field not in split_data:
            print(f"Config error: split has no field '{field}'. Available: {list(split_data.keys())}")
            sys.exit(1)
        keep = set(split_data[field] or [])
        names = [n for n in names if n in keep]

    loaded: list[dict] = []
    missing: list[str] = []
    for name in names:
        rec = _read_task(tasks_root / name / "task.json")
        if rec is None:
            missing.append(name)
        else:
            loaded.append(rec)

    if missing:
        print(f"  WARNING: {len(missing)} tasks could not be loaded (missing task.json or description)")
    return loaded


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 1: Taxonomy
# ═══════════════════════════════════════════════════════════════════════════════

TAXONOMY_PROMPT = """\
I have {num_tasks} desktop application tasks for {app_name} {app_version}. \
Organize them into a 2-layer taxonomy: category → topic.

Multiple tasks may map to the same topic (e.g. "change slide 1 bg to red" and \
"set slide 3 background to blue" both belong to topic "slide-background").

Tasks:
{task_list}

Rules:
- 2 layers: category (broad) → topic (specific skill with ONE guide)
- Multiple tasks can map to same topic
- Every task must be assigned to exactly one topic
- Topic IDs: kebab-case slugs
- 4-10 categories, 2-8 topics per category

Output JSON:
{{
    "categories": [
        {{
            "id": "text-formatting",
            "name": "Text Formatting",
            "topics": [
                {{
                    "id": "font-color",
                    "name": "Change Font Color",
                    "description": "How to change text/font color in the application",
                    "task_ids": ["04578141-...", "3b27600c-..."]
                }}
            ]
        }}
    ]
}}
"""


def phase_taxonomy(config: dict, tasks: list[dict], ws: Path) -> dict:
    cache = ws / "taxonomy.json"
    if cache.exists():
        print("  [cached]")
        return json.loads(cache.read_text())

    task_list = "\n".join(f"  - [{t['task_id']}] {t['instruction']}" for t in tasks)
    prompt = TAXONOMY_PROMPT.format(
        num_tasks=len(tasks),
        app_name=config["app_name"],
        app_version=config["app_version"],
        task_list=task_list,
    )
    result = call_claude(prompt, timeout=300)
    if not result:
        print("  FAILED: no response from Claude")
        sys.exit(1)
    taxonomy = parse_json_response(result)
    if not taxonomy:
        print("  FAILED: couldn't parse JSON")
        sys.exit(1)

    assigned = {
        tid
        for cat in taxonomy.get("categories", [])
        for topic in cat.get("topics", [])
        for tid in topic.get("task_ids", [])
    }
    missing = {t["task_id"] for t in tasks} - assigned
    if missing:
        print(f"  WARNING: {len(missing)} tasks unassigned")

    cache.write_text(json.dumps(taxonomy, indent=2) + "\n")
    for cat in taxonomy["categories"]:
        topics = cat["topics"]
        n = sum(len(t.get("task_ids", [])) for t in topics)
        print(f"  {cat['name']}: {len(topics)} topics, {n} tasks")
    return taxonomy


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2: PDF pages per topic
# ═══════════════════════════════════════════════════════════════════════════════

def _download_pdf(config: dict, ws: Path) -> Path | None:
    pdf_conf = config.get("sources", {}).get("pdf_guide")
    if not pdf_conf:
        return None
    pdf_path = ws / "official-guide.pdf"
    if pdf_path.exists() and pdf_path.stat().st_size > 0:
        return pdf_path
    url = pdf_conf["url"]
    print(f"  Downloading PDF from {url[:70]}...")
    try:
        subprocess.run(
            ["curl", "-L", "-o", str(pdf_path), url],
            capture_output=True, timeout=180,
        )
        if pdf_path.exists() and pdf_path.stat().st_size > 0:
            return pdf_path
    except Exception as e:
        print(f"  PDF download failed: {e}")
    return None


def _extract_toc(pdf_path: Path) -> list[dict]:
    doc = fitz.open(str(pdf_path))
    toc = doc.get_toc()
    doc.close()
    return [{"level": t[0], "title": t[1], "page": t[2]} for t in toc]


TOC_MAPPING_PROMPT = """\
I have a PDF guide for {app_name} {app_version}. Here is the table of contents:

{toc_text}

I need to find relevant pages for each of these topics:
{topic_list}

For each topic, identify which page ranges from the ToC are most relevant. \
Return a JSON object mapping topic_id to a list of page numbers.

Output JSON:
{{
    "font-color": [45, 46, 47, 48],
    "slide-background": [120, 121, 122]
}}

Rules:
- Include only the most relevant pages (5-15 per topic)
- Use the actual page numbers from the ToC
- If a topic isn't covered in the guide, use an empty list []
"""


def _map_topics_to_pages(
    toc: list[dict], taxonomy: dict, config: dict, ws: Path,
) -> dict[str, list[int]]:
    cache = ws / "topic_page_mapping_v1.json"
    if cache.exists():
        return json.loads(cache.read_text())

    toc_text = "\n".join(
        f"{'  ' * (t['level'] - 1)}{t['title']} ... page {t['page']}" for t in toc
    )
    topic_list = "\n".join(
        f"  - {topic['id']}: {topic['name']} — {topic.get('description', '')}"
        for cat in taxonomy["categories"]
        for topic in cat["topics"]
    )
    prompt = TOC_MAPPING_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        toc_text=toc_text,
        topic_list=topic_list,
    )
    result = call_claude(prompt, timeout=180)
    if not result:
        print("  ToC mapping failed")
        return {}
    mapping = parse_json_response(result)
    if not isinstance(mapping, dict):
        print("  ToC mapping parse failed")
        return {}
    mapping_0idx = {
        tid: [p - 1 for p in pages if isinstance(p, int)]
        for tid, pages in mapping.items()
    }
    cache.write_text(json.dumps(mapping_0idx, indent=2) + "\n")
    total = sum(len(v) for v in mapping_0idx.values())
    print(f"  Mapped {len(mapping_0idx)} topics to {total} total pages")
    return mapping_0idx


def _render_pdf_pages(pdf_path: Path, pages: list[int], output_dir: Path) -> list[Path]:
    """Render pages at PDF_DPI into PNG files. Returns sorted list of image paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf_path))
    rendered = []
    mat = fitz.Matrix(PDF_DPI / 72, PDF_DPI / 72)
    for page_num in pages:
        if page_num < 0 or page_num >= len(doc):
            continue
        out = output_dir / f"page_{page_num + 1:04d}.png"
        if not out.exists():
            pix = doc[page_num].get_pixmap(matrix=mat)
            pix.save(str(out))
        rendered.append(out)
    doc.close()
    return rendered


def phase_pdf_pages(
    config: dict, taxonomy: dict, ws: Path,
) -> tuple[Path | None, dict[str, list[tuple[int, Path]]]]:
    """Returns (pdf_path, {topic_id: [(0-indexed page_num, rendered_image_path), ...]})."""
    pdf_path = _download_pdf(config, ws)
    if not pdf_path:
        print("  No PDF configured; cannot build v1 skill.")
        return None, {}

    toc = _extract_toc(pdf_path)
    if not toc:
        print("  PDF has no ToC; cannot map topics to pages.")
        return pdf_path, {}
    print(f"  ToC: {len(toc)} entries")

    mapping = _map_topics_to_pages(toc, taxonomy, config, ws)

    pages_root = ws / "pdf_pages"
    topic_pages: dict[str, list[tuple[int, Path]]] = {}
    for topic_id, page_nums in mapping.items():
        if not page_nums:
            continue
        rendered = _render_pdf_pages(pdf_path, page_nums, pages_root / topic_id)
        # Re-zip with original 0-indexed page numbers, skipping any that fell out of range.
        paired: list[tuple[int, Path]] = []
        doc_len = fitz.open(str(pdf_path)).page_count
        for pn in page_nums:
            if pn < 0 or pn >= doc_len:
                continue
            out = pages_root / topic_id / f"page_{pn + 1:04d}.png"
            if out.exists():
                paired.append((pn, out))
        if paired:
            topic_pages[topic_id] = paired
    print(f"  Rendered pages for {len(topic_pages)} topics at {PDF_DPI} DPI")
    return pdf_path, topic_pages


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3: Figure extraction (bitmap xrefs + LLM-bbox fallback)
# ═══════════════════════════════════════════════════════════════════════════════

FIGURE_BBOX_PROMPT = """\
The attached image is a single page from a software user guide (LibreOffice / similar). \
Identify rectangular figure regions — screenshots, dialogs, diagrams, illustrations. \
Ignore body paragraphs, headings, page numbers, and tables of text.

Return normalized bounding boxes where each value is a fraction of the image's width \
or height in the range 0.0-1.0.

Output ONLY this JSON:
{{
    "figures": [
        {{"bbox": [x0, y0, x1, y1], "description": "short description of what's shown"}}
    ]
}}

Rules:
- Skip decorative icons and figures smaller than ~10% of the page area
- If the page has no figures, return {{"figures": []}}
- Use tight bounding boxes — exclude surrounding body text
"""


def _find_caption(page: fitz.Page, rect: fitz.Rect) -> str:
    """Look for a caption block directly below rect."""
    try:
        blocks = page.get_text("blocks")
    except Exception:
        return ""
    best_text = ""
    best_dist = 1e9
    for b in blocks:
        if len(b) < 5:
            continue
        x0, y0, x1, y1, text = b[0], b[1], b[2], b[3], b[4]
        if not isinstance(text, str) or not text.strip():
            continue
        if y0 < rect.y1 - 2:
            continue
        h_overlap = min(x1, rect.x1) - max(x0, rect.x0)
        if h_overlap <= 0:
            continue
        dist = y0 - rect.y1
        if dist < 80 and dist < best_dist:
            best_dist = dist
            best_text = text.strip()
    if not best_text:
        return ""
    first_line = best_text.split("\n")[0].strip()
    return first_line[:200]


def _extract_bitmap_figures(
    page: fitz.Page, page_image: Path, out_dir: Path, start_idx: int,
) -> tuple[list[dict], int]:
    """Crop embedded bitmap figures from page_image using PDF xref rects."""
    results: list[dict] = []
    idx = start_idx
    try:
        img_infos = page.get_images(full=True)
    except Exception:
        img_infos = []
    if not img_infos:
        return results, idx

    page_img = Image.open(page_image)
    W, H = page_img.size
    scale = PDF_DPI / 72.0

    seen_rects: list[fitz.Rect] = []
    for info in img_infos:
        xref = info[0]
        try:
            rects = page.get_image_rects(xref)
        except Exception:
            rects = []
        for rect in rects:
            if rect.width < MIN_BITMAP_PT or rect.height < MIN_BITMAP_PT:
                continue
            # Skip near-duplicates (same image drawn twice)
            dup = False
            for s in seen_rects:
                if abs(s.x0 - rect.x0) < 2 and abs(s.y0 - rect.y0) < 2 \
                   and abs(s.x1 - rect.x1) < 2 and abs(s.y1 - rect.y1) < 2:
                    dup = True
                    break
            if dup:
                continue
            seen_rects.append(rect)

            x0 = max(0, int(rect.x0 * scale) - FIG_CROP_PADDING_PX)
            y0 = max(0, int(rect.y0 * scale) - FIG_CROP_PADDING_PX)
            x1 = min(W, int(rect.x1 * scale) + FIG_CROP_PADDING_PX)
            y1 = min(H, int(rect.y1 * scale) + FIG_CROP_PADDING_PX)
            if x1 - x0 < 80 or y1 - y0 < 80:
                continue
            idx += 1
            out = out_dir / f"raw_{idx:03d}.png"
            page_img.crop((x0, y0, x1, y1)).save(out)
            results.append({
                "path": str(out),
                "page": page.number + 1,
                "source": "bitmap",
                "caption": _find_caption(page, rect),
                "description": "",
            })
    return results, idx


def _extract_vector_figures(
    page: fitz.Page, page_image: Path, out_dir: Path, start_idx: int,
) -> tuple[list[dict], int]:
    """LLM-bbox fallback for pages without embedded bitmaps (vector figures)."""
    resp = call_claude(FIGURE_BBOX_PROMPT, images=[page_image], timeout=120)
    if not resp:
        return [], start_idx
    data = parse_json_response(resp)
    figs = (data or {}).get("figures", []) if isinstance(data, dict) else []
    if not figs:
        return [], start_idx

    page_img = Image.open(page_image)
    W, H = page_img.size
    results: list[dict] = []
    idx = start_idx
    for f in figs:
        bbox = f.get("bbox")
        if not (isinstance(bbox, list) and len(bbox) == 4):
            continue
        try:
            x0n, y0n, x1n, y1n = (float(v) for v in bbox)
        except (TypeError, ValueError):
            continue
        x0 = max(0, int(min(x0n, x1n) * W))
        y0 = max(0, int(min(y0n, y1n) * H))
        x1 = min(W, int(max(x0n, x1n) * W))
        y1 = min(H, int(max(y0n, y1n) * H))
        if x1 - x0 < 100 or y1 - y0 < 100:
            continue
        area_frac = ((x1 - x0) * (y1 - y0)) / float(W * H)
        if area_frac < MIN_VECTOR_FRAC:
            continue
        idx += 1
        out = out_dir / f"raw_{idx:03d}.png"
        page_img.crop((x0, y0, x1, y1)).save(out)
        results.append({
            "path": str(out),
            "page": page.number + 1,
            "source": "vector",
            "caption": "",
            "description": (f.get("description") or "").strip()[:200],
        })
    return results, idx


def phase_figures(
    pdf_path: Path,
    topic_pages: dict[str, list[tuple[int, Path]]],
    ws: Path,
) -> dict[str, list[dict]]:
    """Extract figure crops per topic. Returns {topic_id: [figure dict, ...]}."""
    root = ws / "pdf_figures"
    result: dict[str, list[dict]] = {}
    doc = fitz.open(str(pdf_path))
    try:
        for topic_id, pairs in topic_pages.items():
            topic_dir = root / topic_id
            topic_dir.mkdir(parents=True, exist_ok=True)
            cache = topic_dir / "figures.json"
            if cache.exists():
                figs = json.loads(cache.read_text())
                result[topic_id] = figs
                continue

            idx = 0
            topic_figs: list[dict] = []
            for page_num, page_image in pairs:
                page = doc[page_num]
                bmp, idx = _extract_bitmap_figures(page, page_image, topic_dir, idx)
                if bmp:
                    topic_figs.extend(bmp)
                else:
                    vec, idx = _extract_vector_figures(page, page_image, topic_dir, idx)
                    topic_figs.extend(vec)
            cache.write_text(json.dumps(topic_figs, indent=2) + "\n")
            result[topic_id] = topic_figs
            print(f"    [{topic_id}] {len(topic_figs)} figures")
    finally:
        doc.close()
    return result


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4: Text skill — one guide.md per topic
# ═══════════════════════════════════════════════════════════════════════════════

TEXT_PROMPT = """\
Write a practical reference guide for {app_name} {app_version}.

Topic: {topic_name}
Description: {topic_description}

I'm attaching the relevant pages from the official {app_name} {app_version} guide \
as images. Use them as the primary source of truth.

Write in a casual, readable style — like a colleague explaining over your shoulder. \
Use natural prose with clear actions, not rigid numbered steps.

Rules:
- Title: "# {topic_name} ({app_name} {app_version})"
- Use **bold** for menu paths and button names
- Short paragraphs, each covering one action or concept
- Include exact menu paths (e.g., **Slide > Slide Properties...**)
- Under 25 lines — concise and scannable
- No "Step 1, Step 2" — prose with transitions
- Do NOT reference figures or screenshots in the text

Output ONLY the markdown guide.
"""


def _skills_dir(domain: str, modality: str) -> Path:
    return MMSKILLS_ROOT / "skills" / f"{domain}-knowledge-{modality}-v1"


def generate_text_guide(
    topic: dict, cat: dict, config: dict, domain: str,
    page_images: list[Path],
) -> bool:
    text_dir = _skills_dir(domain, "text") / cat["id"] / topic["id"]
    guide_path = text_dir / "guide.md"
    if guide_path.exists():
        print(f"    [{topic['name']}] text [cached]")
        return True
    if not page_images:
        print(f"    [{topic['name']}] text SKIP (no pages)")
        return False
    prompt = TEXT_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
        topic_description=topic.get("description", ""),
    )
    result = call_claude(prompt, images=list(page_images), timeout=300)
    if not result:
        print(f"    [{topic['name']}] text FAILED")
        return False
    text_dir.mkdir(parents=True, exist_ok=True)
    guide_path.write_text(result.strip() + "\n")
    print(f"    [{topic['name']}] text OK")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 5: Multimodal skill — insert figure references into the same text
# ═══════════════════════════════════════════════════════════════════════════════

FIGURE_SELECT_PROMPT = """\
You have a text guide for {app_name} {app_version} and a set of candidate figure crops \
from the official PDF. Decide which figures are genuinely helpful for a reader of this \
guide, and where each should be referenced.

Guide text (paragraphs numbered):
---
{numbered_guide}
---

Candidate figures (filenames and captions/descriptions, in order of attachment):
{figure_list}

Output JSON:
{{
    "insertions": [
        {{
            "after_paragraph": 2,
            "figure": "raw_003.png",
            "description": "the Background tab of the Slide Properties dialog with the Fill dropdown"
        }}
    ]
}}

Rules:
- Only include figures that clearly illustrate something in that paragraph's action
- `after_paragraph` is 1-indexed; it MUST refer to an existing paragraph number above
- Each `figure` field MUST be one of the candidate filenames exactly
- `description` should be a short phrase describing the visible UI elements — it will be \
spliced into a sentence like "...you will see <description>."
- Omit figures that are irrelevant, redundant, or too generic
- Usually 0-3 figures per guide is plenty; never duplicate the same figure twice
- Return {{"insertions": []}} if no figure materially helps

Output ONLY valid JSON.
"""


def _split_paragraphs(markdown: str) -> list[str]:
    """Split markdown into paragraphs on blank lines. Keeps the title as the first element."""
    parts = re.split(r"\n\s*\n", markdown.strip())
    return [p.strip() for p in parts if p.strip()]


def _number_guide_for_prompt(paragraphs: list[str]) -> str:
    """Produce '[P1] <paragraph>' listing for the prompt (title excluded from numbering)."""
    lines = []
    n = 0
    for p in paragraphs:
        if p.startswith("#"):
            lines.append(p)
            continue
        n += 1
        lines.append(f"[P{n}] {p}")
    return "\n\n".join(lines)


def generate_multimodal_guide(
    topic: dict, cat: dict, config: dict, domain: str,
    figures: list[dict],
) -> bool:
    app = config["app_name"]
    ver = config["app_version"]
    mm_dir = _skills_dir(domain, "multimodal") / cat["id"] / topic["id"]
    text_dir = _skills_dir(domain, "text") / cat["id"] / topic["id"]
    mm_guide = mm_dir / "guide.md"
    text_guide = text_dir / "guide.md"

    if mm_guide.exists():
        print(f"    [{topic['name']}] multimodal [cached]")
        return True
    if not text_guide.exists():
        print(f"    [{topic['name']}] multimodal SKIP (no text guide)")
        return False

    text = text_guide.read_text()
    paragraphs = _split_paragraphs(text)

    # If there are no candidate figures, the multimodal guide is just the text guide verbatim.
    if not figures:
        mm_dir.mkdir(parents=True, exist_ok=True)
        mm_guide.write_text(text)
        print(f"    [{topic['name']}] multimodal OK (no figures)")
        return True

    # Build numbered view for the prompt (paragraphs only; title excluded from numbering).
    body_indices: list[int] = [i for i, p in enumerate(paragraphs) if not p.startswith("#")]
    numbered = _number_guide_for_prompt(paragraphs)

    fig_lines = []
    for f in figures:
        fname = Path(f["path"]).name
        caption = (f.get("caption") or f.get("description") or "").strip()
        fig_lines.append(f"  - {fname}: {caption}" if caption else f"  - {fname}")
    fig_list = "\n".join(fig_lines)

    prompt = FIGURE_SELECT_PROMPT.format(
        app_name=app, app_version=ver,
        numbered_guide=numbered,
        figure_list=fig_list,
    )
    image_paths = [Path(f["path"]) for f in figures]
    resp = call_claude(prompt, images=image_paths, timeout=300)
    data = parse_json_response(resp) if resp else None
    insertions = (data or {}).get("insertions", []) if isinstance(data, dict) else []

    # Validate + order + dedup figures.
    valid_files = {Path(f["path"]).name: Path(f["path"]) for f in figures}
    by_paragraph: dict[int, list[tuple[str, str]]] = {}
    used_src: list[Path] = []
    used_set: set[str] = set()
    for ins in insertions:
        try:
            after = int(ins.get("after_paragraph", 0))
        except (TypeError, ValueError):
            continue
        fname = ins.get("figure", "")
        desc = (ins.get("description") or "").strip()
        if fname not in valid_files:
            continue
        if fname in used_set:
            continue
        if after < 1 or after > len(body_indices):
            continue
        used_set.add(fname)
        used_src.append(valid_files[fname])
        by_paragraph.setdefault(after, []).append((fname, desc))

    if not used_src:
        mm_dir.mkdir(parents=True, exist_ok=True)
        mm_guide.write_text(text)
        print(f"    [{topic['name']}] multimodal OK (0 figs selected)")
        return True

    # Copy chosen figures as fig01.png, fig02.png, ...  (preserve insertion order).
    mm_dir.mkdir(parents=True, exist_ok=True)
    # Clean stale fig*.png if any.
    for old in mm_dir.glob("fig*.png"):
        old.unlink()

    filename_to_fig: dict[str, str] = {}
    for i, src in enumerate(used_src, 1):
        fig_name = f"fig{i:02d}.png"
        shutil.copy2(src, mm_dir / fig_name)
        filename_to_fig[src.name] = fig_name

    # Rebuild markdown: walk original paragraphs, inject "Read `figNN.png`..." paragraphs
    # after the specified body paragraph positions. Original text is preserved byte-for-byte.
    out_paragraphs: list[str] = []
    body_counter = 0
    for para in paragraphs:
        out_paragraphs.append(para)
        if para.startswith("#"):
            continue
        body_counter += 1
        for fname, desc in by_paragraph.get(body_counter, []):
            fig_name = filename_to_fig[fname]
            sentence_desc = desc or "the relevant UI"
            ref = (
                f"Read the screenshot `{fig_name}` in this directory — "
                f"you will see {sentence_desc}."
            )
            out_paragraphs.append(ref)

    mm_guide.write_text("\n\n".join(out_paragraphs).rstrip() + "\n")
    print(f"    [{topic['name']}] multimodal OK ({len(used_src)} figs)")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 6: Index (SKILL.md per modality)
# ═══════════════════════════════════════════════════════════════════════════════

def phase_index(config: dict, domain: str, taxonomy: dict, mode: str) -> None:
    app = config["app_name"]
    ver = config["app_version"]
    modalities = ["text", "multimodal"] if mode == "both" else [mode]
    for modality in modalities:
        skills_dir = _skills_dir(domain, modality)
        mm_suffix = " with screenshots" if modality == "multimodal" else ""
        lines = [
            "---",
            f"name: {domain}-knowledge-{modality}-v1",
            f'description: "Practical{mm_suffix} guides for {app} {ver} tasks. '
            f'{app} {ver} UI may differ from what you expect — '
            f'read the relevant guide before acting."',
            "---\n",
            f"# {app} {ver} Knowledge ({modality}-v1)\n",
            f"Practical{mm_suffix} guides for common {app} tasks.\n",
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
        print(f"  {modality}-v1 SKILL.md updated")


# ═══════════════════════════════════════════════════════════════════════════════
# Orchestration
# ═══════════════════════════════════════════════════════════════════════════════

def process_topic(
    topic: dict, cat: dict, config: dict, domain: str, mode: str,
    page_images: list[Path], figures: list[dict],
) -> bool:
    ok = True
    if mode in ("text", "both"):
        if not generate_text_guide(topic, cat, config, domain, page_images):
            ok = False
    if mode in ("multimodal", "both"):
        # Multimodal depends on the text guide — ensure it exists before proceeding.
        text_guide = _skills_dir(domain, "text") / cat["id"] / topic["id"] / "guide.md"
        if not text_guide.exists():
            print(f"    [{topic['name']}] multimodal SKIP (text guide missing)")
            ok = False
        elif not generate_multimodal_guide(topic, cat, config, domain, figures):
            ok = False
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Task-driven skill generation (v1)")
    parser.add_argument("--config", required=True, help="Path to domain YAML config")
    parser.add_argument("--mode", choices=["text", "multimodal", "both"], default="both")
    parser.add_argument("--parallel", type=int, default=1)
    parser.add_argument("--task_ids", nargs="*", help="Filter to specific task id prefixes")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        # Allow path relative to pipeline dir.
        alt = PIPELINE_DIR / args.config
        if not config_path.exists() and alt.exists():
            config_path = alt
    config = load_config(config_path)
    domain = config["domain"]
    tasks = load_tasks(config)
    if args.task_ids:
        id_prefixes = set(args.task_ids)
        tasks = [t for t in tasks if any(t["task_id"].startswith(p) for p in id_prefixes)]
    ws = workspace(domain)

    print(f"=== Skill Pipeline v1: {config['app_name']} {config['app_version']} ===")
    print(f"Domain: {domain} | Tasks: {len(tasks)} | Mode: {args.mode} | Parallel: {args.parallel}")
    print()

    print("Phase 1: Taxonomy")
    taxonomy = phase_taxonomy(config, tasks, ws)
    print()

    print(f"Phase 2: PDF pages ({PDF_DPI} DPI)")
    pdf_path, topic_pages = phase_pdf_pages(config, taxonomy, ws)
    print()

    figures_by_topic: dict[str, list[dict]] = {}
    if pdf_path and topic_pages and args.mode in ("multimodal", "both"):
        print("Phase 3: Figures (crop from PDF)")
        figures_by_topic = phase_figures(pdf_path, topic_pages, ws)
        print()

    all_topics = [
        (topic, cat)
        for cat in taxonomy["categories"]
        for topic in cat["topics"]
    ]
    print(f"Phase 4/5: Generate ({len(all_topics)} topics)")

    def _one(item):
        topic, cat = item
        pairs = topic_pages.get(topic["id"], [])
        images = [p for _, p in pairs]
        figs = figures_by_topic.get(topic["id"], [])
        return process_topic(topic, cat, config, domain, args.mode, images, figs)

    success = 0
    if args.parallel <= 1:
        for item in all_topics:
            try:
                if _one(item):
                    success += 1
            except Exception as e:
                print(f"    [{item[0]['name']}] ERROR: {e}")
    else:
        with ThreadPoolExecutor(max_workers=args.parallel) as executor:
            futures = {executor.submit(_one, item): item for item in all_topics}
            for f in as_completed(futures):
                try:
                    if f.result():
                        success += 1
                except Exception as e:
                    topic, _cat = futures[f]
                    print(f"    [{topic['name']}] ERROR: {e}")
    print(f"\n  Generated: {success}/{len(all_topics)} topics")
    print()

    print("Phase 6: Index")
    phase_index(config, domain, taxonomy, args.mode)
    print()

    print("Done.")


if __name__ == "__main__":
    main()
