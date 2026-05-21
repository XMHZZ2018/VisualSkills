"""Skill generation pipeline (v1) from a knowledge source.

Entry point (preferred):
    ./run.sh --config configs/libreoffice_writer.yaml

Direct invocation:
    python3 generate_skill_from_knowledge_source.py --config configs/libreoffice_writer.yaml

Three taxonomy modes, selected by config:

  • Full-PDF mode: the taxonomy comes from the PDF guide's table of contents —
    the resulting skill covers the whole application. Activated when the config
    has `sources.pdf_guide.url` and no `tasks:` block.

  • HTML-docs mode: the taxonomy comes from crawling the documentation site
    starting at a root URL (which acts as the printed ToC). Activated when the
    config has `sources.html_guide.root_url` and no `tasks:` block.

  • Task-filtered mode: domain tasks (from gym-anything) are clustered into a
    taxonomy and only the relevant sections of a PDF guide are used. Activated
    when the config has a `tasks:` block.

Pipeline:
  Phase 1 — Taxonomy: either cluster gym-anything tasks (task mode), refine the
            PDF table of contents (PDF mode), or synthesize categories/topics
            from a crawled HTML outline (HTML mode). All three converge on the
            same taxonomy shape. Cached at workspace/<domain>/taxonomy.json.
  Phase 2 — Per-topic pages: each topic gets a list of source pages —
            300-DPI PDF page renders (.png) in PDF/task mode, or markdown
            extracted via plain-HTTP fetch + markdownify (.md) with all
            inline `<img>` tags downloaded locally in HTML mode.
  Phase 3 — Figures: PDF mode crops figures from rendered pages (bitmap xrefs
            first, LLM bbox detection as fallback). HTML mode does an
            independent `<img>` pass into `html_figures/<topic>/`, which
            is the canonical figure list used by Phase 4 multimodal Call B.
  Phase 4 — Text skill: generate one concise guide.md per topic from the
            rendered pages. This is the text-skill-v1 content.
  Phase 5 — Multimodal skill: pick figures relevant to the guide and splice
            explicit "Read the screenshot `figNN.png`" paragraphs into the
            *same* text, byte-for-byte identical between the two versions
            aside from the inserted image-reference paragraphs and their
            copied fig files.
  Phase 6 — Index: write SKILL.md for each -v1 directory.

All LLM calls go through the `claude` CLI (model: claude-opus-4-6). Artifacts
are cached under workspace/<domain>/ so re-running skips completed work.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fitz  # PyMuPDF
import yaml
from PIL import Image

PIPELINE_DIR = Path(__file__).parent
# This file lives at <repo>/preprocess/skill-pipeline/v1/, so go up 3.
MMSKILLS_ROOT = PIPELINE_DIR.parent.parent.parent
CONFIGS_DIR = PIPELINE_DIR / "configs"
WORKSPACE_DIR = PIPELINE_DIR / "workspace"

CLAUDE_MODEL = "claude-opus-4-6"
PDF_DPI = 300            # page render DPI — high enough for clean figure crops
TOC_DPI = 200            # ToC pages render DPI — text-legibility is enough
TOC_RENDER_CAP = 25      # max ToC pages to attach to a Phase 1 prompt
MIN_FIG_FRAC = 0.05      # min figure area fraction of page (skip decorative icons)
MIN_BITMAP_PT = 60       # min embedded-bitmap side length (PDF points) to be a figure
FIG_CROP_PADDING_PX = 8  # pixel padding around bitmap-rect crops
SPLIT_GAP_PT = 12        # max gap between bitmap rects to call them split panels of one figure

# ═══════════════════════════════════════════════════════════════════════════════
# Config & workspace
# ═══════════════════════════════════════════════════════════════════════════════

# Default parallelism per phase. Configs can override under a `parallel:` block.
DEFAULT_PARALLEL = {
    "phase_2": 8,  # page rendering — local I/O, safe to run high
    "phase_3": 8,  # figure extraction — pure bitmap-xref, no LLM (local I/O)
    "phase_4": 4,  # guide generation — Claude calls per topic, keep modest for rate limits
    "phase_5": 4,  # use-when extraction — Claude calls per guide, same constraint as phase 4
    "phase_6": 4,  # text-v1 derivation — Claude calls per multimodal guide, same constraint
}


def load_config(config_path: Path) -> dict:
    if not config_path.exists():
        print(f"Config not found: {config_path}")
        sys.exit(1)
    cfg = yaml.safe_load(config_path.read_text())
    if "domain" not in cfg:
        cfg["domain"] = config_path.stem
    # Resolve per-phase parallelism, falling back to defaults.
    user_parallel = cfg.get("parallel") or {}
    cfg["parallel"] = {k: int(user_parallel.get(k, v)) for k, v in DEFAULT_PARALLEL.items()}
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

    # Run from a neutral cwd: invoking from this project's directory picks up
    # a broken .claude/settings.local.json symlink and a parent .mcp.json with
    # paths that don't resolve here, which makes the CLI hang silently.
    try:
        result = subprocess.run(
            cmd, input=full_prompt, capture_output=True, text=True, timeout=timeout,
            cwd="/tmp",
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
    result = call_claude(prompt, timeout=600)
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
# Phase 1 (alt): Taxonomy from the PDF table of contents
# ═══════════════════════════════════════════════════════════════════════════════

PAGE_TRANSCRIBE_PROMPT = """\
The attached image is one page from the printed Table of Contents of the
official {app_name} {app_version} user guide. Transcribe every ToC entry
visible on this page, in reading order.

For each entry record:
- level: 1 for chapter-level headings; 2 for top-level sections inside a
  chapter; 3 for sub-sections; 4+ for deeper. Use the visual indentation
  in the printed ToC.
- title: the exact text of the entry (no dot leaders, no trailing page #)
- page: the page number printed at the right end of the entry

Output ONLY this JSON, nothing else:
{{
  "entries": [
    {{"level": 1, "title": "Chapter 1, Introducing Writer", "page": 17}},
    {{"level": 2, "title": "What is Writer?", "page": 18}}
  ]
}}

If the page has no ToC entries (e.g. it's blank or a chapter header), return
{{"entries": []}}.
"""


TAXONOMY_FROM_ENTRIES_PROMPT = """\
Below is the printed Table of Contents from the official {app_name} {app_version}
user guide, transcribed entry by entry. Turn it into a 2-layer skill taxonomy:
category → topic.

Each numbered chapter (level-1 entry) usually becomes a category. Level-2
entries become topics. The list has noise — drop or merge as needed:

- DROP only pure filler: front matter (Copyright, Preface, Acknowledgements,
  Foreword, About this Guide, Contributors, License, Feedback) and back
  matter (Index, Glossary unless useful).
- KEEP every numbered chapter from the guide, even if it looks advanced or
  conceptual. Chapters like "Master Documents", "Fields", "Forms", and
  application-integration chapters all teach concrete workflows and must
  appear as their own category.
- MERGE over-fragmented sub-sections that describe ONE coherent skill.
  Example: "Inserting a table", "Editing a table", "Formatting a table" can
  collapse into a single topic "Working with tables" if they share pages.
- Use kebab-case slugs for ids.
- No upper cap on categories — aim for one category per numbered chapter.
  Topics: 2-10 per category.

For each topic, set `pdf_pages` to the inclusive page range it spans. The end
page is one before the next entry's start page (or the last page of the
chapter). Pages are 1-indexed PDF pages.

ToC entries (level / title / page):
{entries_text}

Output JSON:
{{
    "categories": [
        {{
            "id": "page-layout",
            "name": "Page Layout",
            "topics": [
                {{
                    "id": "page-margins",
                    "name": "Adjusting Page Margins",
                    "description": "How to set page margins in {app_name}",
                    "pdf_pages": [42, 48]
                }}
            ]
        }}
    ]
}}

Output ONLY valid JSON.
"""


def _looks_like_toc_page(text: str) -> bool:
    """Page is ToC-like if many of its non-trivial lines end with a page number.

    Catches both dot-leader lines ("Inserting a header.... 42") and clean
    right-aligned-number lines ("Page Setup        42").
    """
    lines = [l for l in (text or "").splitlines() if len(l.strip()) >= 4]
    if len(lines) < 5:
        return False
    # ToC lines end with a page number, separated by either whitespace or
    # dot-leader characters. e.g. "Inserting a header..........42" or "Page Setup    42".
    leader_re = re.compile(r"[\s.]\d{1,4}\s*$")
    matches = sum(1 for l in lines if leader_re.search(l))
    return matches / len(lines) >= 0.4


def _find_toc_page_range(pdf_path: Path, toc: list[dict]) -> tuple[int, int] | None:
    """Identify the printed Table-of-Contents pages (0-indexed inclusive range).

    Strategy, in order:
      1. Outline entry titled exactly "Contents" / "Table of Contents" —
         take its page as start, next outline entry minus one as end.
      2. Scan front-matter pages (everything before the first real chapter)
         and pick the contiguous run of pages whose text looks like a ToC
         (high fraction of lines ending with a page number).
      3. Fallback: pages [0 .. min(first_chapter_page - 2, TOC_RENDER_CAP-1)].
    Returns None if no front-matter pages exist at all.
    """
    contents_re = re.compile(r"^\s*(table of\s+)?contents\s*$", re.IGNORECASE)
    chapter_re = re.compile(r"^\s*chapter\s*\d+\b", re.IGNORECASE)

    doc = fitz.open(str(pdf_path))
    try:
        doc_pages = doc.page_count

        # Strategy 1: explicit "Contents" outline entry.
        for i, t in enumerate(toc):
            if contents_re.match(t["title"] or ""):
                start = max((t["page"] or 1) - 1, 0)
                if i + 1 < len(toc):
                    end = max((toc[i + 1]["page"] or start + 1) - 2, start)
                else:
                    end = start + TOC_RENDER_CAP - 1
                end = min(end, start + TOC_RENDER_CAP - 1, doc_pages - 1)
                return start, end

        # Find first real chapter to bound the search window.
        first_chapter_page: int | None = None
        for t in toc:
            if t["level"] == 1 and chapter_re.match(t["title"] or ""):
                first_chapter_page = t["page"]
                break
        if first_chapter_page is None:
            first_l1 = next((t for t in toc if t["level"] == 1), None)
            first_chapter_page = first_l1["page"] if first_l1 else None
        if not first_chapter_page or first_chapter_page < 2:
            return None

        search_end = min(first_chapter_page - 2, doc_pages - 1)
        search_pages = list(range(0, search_end + 1))

        # Strategy 2: text-based detection of ToC pages.
        toc_like = [pn for pn in search_pages if _looks_like_toc_page(doc[pn].get_text("text"))]
        if toc_like:
            # Take the longest contiguous run.
            runs: list[list[int]] = []
            cur = [toc_like[0]]
            for p in toc_like[1:]:
                if p == cur[-1] + 1:
                    cur.append(p)
                else:
                    runs.append(cur)
                    cur = [p]
            runs.append(cur)
            best = max(runs, key=len)
            return best[0], min(best[-1], best[0] + TOC_RENDER_CAP - 1)

        # Strategy 3: fallback — last front-matter pages.
        end = search_end
        start = max(end - TOC_RENDER_CAP + 1, 0)
        return start, end
    finally:
        doc.close()


def _render_toc_pages(pdf_path: Path, ws: Path) -> list[Path]:
    """Render the printed-ToC pages at TOC_DPI for use in the Phase 1 prompt."""
    out_dir = ws / "toc_pages"
    out_dir.mkdir(parents=True, exist_ok=True)
    toc_raw = _extract_toc(pdf_path)
    rng = _find_toc_page_range(pdf_path, toc_raw)
    if rng is None:
        return []
    start, end = rng
    doc = fitz.open(str(pdf_path))
    try:
        mat = fitz.Matrix(TOC_DPI / 72, TOC_DPI / 72)
        rendered: list[Path] = []
        for pn in range(start, end + 1):
            if pn < 0 or pn >= doc.page_count:
                continue
            out = out_dir / f"toc_{pn + 1:04d}.png"
            if not out.exists():
                doc[pn].get_pixmap(matrix=mat).save(str(out))
            rendered.append(out)
        return rendered
    finally:
        doc.close()


def _transcribe_toc_pages(
    toc_pages: list[Path], config: dict, ws: Path,
) -> list[dict]:
    """OCR each rendered ToC page in parallel and return a merged entry list.

    Each per-page result is cached as `<page>.json` next to the rendered PNG
    so a partial failure can be resumed by re-running. The merged list is
    cached at workspace/<domain>/toc_transcribed.json.
    """
    merged_cache = ws / "toc_transcribed.json"
    if merged_cache.exists():
        return json.loads(merged_cache.read_text())

    app = config["app_name"]
    ver = config["app_version"]

    def _one(img: Path) -> tuple[Path, list[dict]]:
        cache = img.with_suffix(".json")
        if cache.exists():
            data = json.loads(cache.read_text())
            return img, data.get("entries", [])
        prompt = PAGE_TRANSCRIBE_PROMPT.format(app_name=app, app_version=ver)
        resp = call_claude(prompt, images=[img], timeout=240)
        data = parse_json_response(resp) if resp else None
        entries = (data or {}).get("entries", []) if isinstance(data, dict) else []
        # Sanitize entries to the expected shape.
        clean: list[dict] = []
        for e in entries:
            if not isinstance(e, dict):
                continue
            try:
                lvl = int(e.get("level", 0))
                pg = int(e.get("page", 0))
            except (TypeError, ValueError):
                continue
            title = (e.get("title") or "").strip()
            if not title or lvl < 1 or pg < 1:
                continue
            clean.append({"level": lvl, "title": title, "page": pg})
        cache.write_text(json.dumps({"entries": clean}, indent=2) + "\n")
        return img, clean

    # Serial execution: parallel claude CLI invocations can trip the
    # OAuth client_data burst rate limit on cold start.
    all_entries: list[dict] = []
    for img in toc_pages:
        try:
            _, entries = _one(img)
            print(f"    [{img.name}] {len(entries)} entries")
        except Exception as e:
            print(f"    [{img.name}] ERROR: {e}")
            entries = []
        all_entries.extend(entries)

    merged_cache.write_text(json.dumps(all_entries, indent=2) + "\n")
    return all_entries


def phase_taxonomy_from_pdf_toc(config: dict, pdf_path: Path, ws: Path) -> dict:
    """Build a 2-layer taxonomy from the PDF's table of contents (full-PDF mode).

    Cached at workspace/<domain>/taxonomy.json — delete to regenerate, or
    hand-edit to override. The raw ToC is also saved at toc_raw.json for
    reference.
    """
    cache = ws / "taxonomy.json"
    if cache.exists():
        print("  [cached]")
        return json.loads(cache.read_text())

    toc = _extract_toc(pdf_path)
    if not toc:
        print("  PDF has no ToC; cannot build PDF-mode taxonomy.")
        sys.exit(1)
    (ws / "toc_raw.json").write_text(json.dumps(toc, indent=2) + "\n")
    print(f"  Raw ToC: {len(toc)} entries (saved as toc_raw.json for reference)")

    toc_pages = _render_toc_pages(pdf_path, ws)
    if not toc_pages:
        print("  FAILED: could not render any ToC pages")
        sys.exit(1)
    print(f"  Rendered {len(toc_pages)} ToC page(s) at {TOC_DPI} DPI")

    entries = _transcribe_toc_pages(toc_pages, config, ws)
    if not entries:
        print("  FAILED: no entries transcribed from ToC pages")
        sys.exit(1)
    print(f"  Transcribed {len(entries)} ToC entries")

    entries_text = "\n".join(
        f"L{e['level']} {e['title']} ... page {e['page']}" for e in entries
    )
    prompt = TAXONOMY_FROM_ENTRIES_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        entries_text=entries_text,
    )
    result = call_claude(prompt, timeout=600)
    if not result:
        print("  FAILED: no response from Claude (taxonomy synthesis)")
        sys.exit(1)
    taxonomy = parse_json_response(result)
    if not isinstance(taxonomy, dict) or "categories" not in taxonomy:
        print("  FAILED: couldn't parse JSON")
        sys.exit(1)

    # Normalize pdf_pages: accept either [start, end] range or explicit list of pages.
    for cat in taxonomy["categories"]:
        for topic in cat.get("topics", []):
            pages = topic.get("pdf_pages") or []
            if (
                isinstance(pages, list) and len(pages) == 2
                and all(isinstance(p, int) for p in pages)
                and pages[1] >= pages[0]
            ):
                topic["pdf_pages"] = list(range(pages[0], pages[1] + 1))
            elif isinstance(pages, list):
                topic["pdf_pages"] = [p for p in pages if isinstance(p, int)]
            else:
                topic["pdf_pages"] = []

    cache.write_text(json.dumps(taxonomy, indent=2) + "\n")
    for cat in taxonomy["categories"]:
        topics = cat["topics"]
        n_pages = sum(len(t.get("pdf_pages", [])) for t in topics)
        print(f"  {cat['name']}: {len(topics)} topics, {n_pages} pages")
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


def _mapping_from_taxonomy(taxonomy: dict) -> dict[str, list[int]]:
    """Use topics' built-in `pdf_pages` (PDF-mode taxonomy). 0-indexed output."""
    out: dict[str, list[int]] = {}
    for cat in taxonomy.get("categories", []):
        for topic in cat.get("topics", []):
            pages = topic.get("pdf_pages") or []
            if not pages:
                continue
            out[topic["id"]] = [p - 1 for p in pages if isinstance(p, int) and p > 0]
    return out


def phase_pdf_pages(
    config: dict, taxonomy: dict, ws: Path, parallel: int = 1,
) -> tuple[Path | None, dict[str, list[tuple[int, Path]]]]:
    """Returns (pdf_path, {topic_id: [(0-indexed page_num, rendered_image_path), ...]}).

    Topic rendering is parallelized across `parallel` threads. PyMuPDF page
    reading is thread-safe as long as each thread opens its own Document,
    which `_render_pdf_pages` already does.
    """
    pdf_path = _download_pdf(config, ws)
    if not pdf_path:
        print("  No PDF configured; cannot build v1 skill.")
        return None, {}

    # PDF mode: topics already carry their own pdf_pages — skip ToC mapping.
    if any(
        topic.get("pdf_pages")
        for cat in taxonomy.get("categories", [])
        for topic in cat.get("topics", [])
    ):
        mapping = _mapping_from_taxonomy(taxonomy)
        print(f"  Using pdf_pages from taxonomy for {len(mapping)} topics")
    else:
        toc = _extract_toc(pdf_path)
        if not toc:
            print("  PDF has no ToC; cannot map topics to pages.")
            return pdf_path, {}
        print(f"  ToC: {len(toc)} entries")
        mapping = _map_topics_to_pages(toc, taxonomy, config, ws)

    doc = fitz.open(str(pdf_path))
    doc_len = doc.page_count
    doc.close()

    pages_root = ws / "pdf_pages"

    def _render_one(item: tuple[str, list[int]]) -> tuple[str, list[tuple[int, Path]]]:
        topic_id, page_nums = item
        if not page_nums:
            return topic_id, []
        _render_pdf_pages(pdf_path, page_nums, pages_root / topic_id)
        paired: list[tuple[int, Path]] = []
        for pn in page_nums:
            if pn < 0 or pn >= doc_len:
                continue
            out = pages_root / topic_id / f"page_{pn + 1:04d}.png"
            if out.exists():
                paired.append((pn, out))
        return topic_id, paired

    topic_pages: dict[str, list[tuple[int, Path]]] = {}
    items = list(mapping.items())
    if parallel <= 1:
        for item in items:
            tid, paired = _render_one(item)
            if paired:
                topic_pages[tid] = paired
    else:
        with ThreadPoolExecutor(max_workers=parallel) as executor:
            for tid, paired in executor.map(_render_one, items):
                if paired:
                    topic_pages[tid] = paired
    print(f"  Rendered pages for {len(topic_pages)} topics at {PDF_DPI} DPI (parallel={parallel})")
    return pdf_path, topic_pages


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3: Figure extraction (deterministic, bitmap-xref only — no LLM)
# ═══════════════════════════════════════════════════════════════════════════════
#
# Strategy:
#   1. Use PyMuPDF `page.get_images(full=True)` + `get_image_rects(xref)` to
#      locate every embedded bitmap rectangle on the page (in PDF points).
#   2. Cluster rects that look like split panels of one logical figure
#      (adjacent on one axis, overlapping on the other). Each cluster's
#      union bbox = one figure.
#   3. For each cluster, crop the union bbox from the rendered 300-DPI page
#      PNG, extend the bottom to the matching "Figure N: ..." caption block,
#      and widen the X range to cover any text blocks (legend/key) sitting
#      between the bitmap and the caption.
#
# Pages with no embedded bitmaps contribute no figures. No LLM call is ever
# made — coordinates come straight from the PDF's image-object rects, so
# body-text bleed is structurally impossible.

_FIG_CAPTION_RE = re.compile(r"^\s*Figure\s+(\d+)\b[:.\s\-]*(.*)$", re.IGNORECASE)


def _bitmap_rects_for_page(page) -> list:
    """Embedded-image rectangles on the page, deduped, in PDF points."""
    try:
        infos = page.get_images(full=True)
    except Exception:
        return []
    rects: list = []
    for info in infos:
        xref = info[0]
        try:
            page_rects = page.get_image_rects(xref)
        except Exception:
            continue
        for r in page_rects:
            if r.width < MIN_BITMAP_PT or r.height < MIN_BITMAP_PT:
                continue
            if any(
                abs(s.x0 - r.x0) < 2 and abs(s.y0 - r.y0) < 2
                and abs(s.x1 - r.x1) < 2 and abs(s.y1 - r.y1) < 2
                for s in rects
            ):
                continue
            rects.append(fitz.Rect(r))
    return rects


def _are_split_panels(a, b) -> bool:
    """True if two bitmap rects look like adjacent panels of one figure."""
    y_overlap = min(a.y1, b.y1) - max(a.y0, b.y0)
    x_gap = max(a.x0, b.x0) - min(a.x1, b.x1)
    if x_gap <= SPLIT_GAP_PT and y_overlap > 0.5 * min(a.height, b.height):
        return True
    x_overlap = min(a.x1, b.x1) - max(a.x0, b.x0)
    y_gap = max(a.y0, b.y0) - min(a.y1, b.y1)
    if y_gap <= SPLIT_GAP_PT and x_overlap > 0.5 * min(a.width, b.width):
        return True
    return False


def _cluster_split_panels(rects: list) -> list:
    """Group rects into clusters where members are pairwise split-panel-adjacent
    (transitively). Returns one union `fitz.Rect` per cluster.

    A figure stored as N adjacent strips ends up as one rect; truly separate
    figures stay separate.
    """
    n = len(rects)
    if n == 0:
        return []
    parent = list(range(n))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(i: int, j: int) -> None:
        ri, rj = find(i), find(j)
        if ri != rj:
            parent[ri] = rj

    for i in range(n):
        for j in range(i + 1, n):
            if _are_split_panels(rects[i], rects[j]):
                union(i, j)

    groups: dict[int, list] = {}
    for i, r in enumerate(rects):
        groups.setdefault(find(i), []).append(r)

    merged = []
    for members in groups.values():
        u = fitz.Rect(members[0])
        for m in members[1:]:
            u |= m
        merged.append(u)
    # Stable order: top-to-bottom, then left-to-right.
    merged.sort(key=lambda r: (r.y0, r.x0))
    return merged


def _find_caption(page, rect) -> tuple:
    """Return (figure_number, caption_text, caption_block_y1) for a bitmap rect.

    Searches text blocks immediately below (or above) the bitmap for a line
    matching `^Figure N: ...`. Returns (None, "", None) if no caption found.
    """
    try:
        blocks = page.get_text("blocks")
    except Exception:
        return None, "", None
    best = None
    best_dist = 1e9
    for b in blocks:
        if len(b) < 5:
            continue
        x0, y0, x1, y1, text = b[0], b[1], b[2], b[3], b[4]
        if not isinstance(text, str):
            continue
        for line in text.split("\n"):
            m = _FIG_CAPTION_RE.match(line)
            if not m:
                continue
            if y0 >= rect.y1 - 2:
                dist = y0 - rect.y1
            elif y1 <= rect.y0 + 2:
                dist = rect.y0 - y1
            else:
                continue
            if min(x1, rect.x1) - max(x0, rect.x0) <= 0:
                continue
            if dist < 120 and dist < best_dist:
                best_dist = dist
                best = (int(m.group(1)), line.strip()[:300], float(y1))
    if best is None:
        return None, "", None
    return best


def _extract_bitmap_figures(
    page, rects: list, page_image: Path, out_dir: Path, start_idx: int,
) -> tuple[list[dict], int]:
    """Crop each bitmap rect from the rendered page image; extend to caption."""
    if not rects:
        return [], start_idx
    page_img = Image.open(page_image)
    W, H = page_img.size
    scale = PDF_DPI / 72.0  # PDF points → rendered pixels
    try:
        all_blocks = page.get_text("blocks")
    except Exception:
        all_blocks = []
    results: list[dict] = []
    idx = start_idx
    for r in rects:
        fig_num, caption, cap_y1 = _find_caption(page, r)
        x0_pt, x1_pt = r.x0, r.x1
        y0_pt, y1_pt = r.y0, r.y1
        # Extend bottom to caption line; widen X to cover any text (legend/key)
        # between the bitmap rect and the caption.
        if cap_y1 is not None and cap_y1 > r.y1:
            y1_pt = cap_y1
            for b in all_blocks:
                if len(b) < 5:
                    continue
                bx0, by0, bx1, by1, btext = b[0], b[1], b[2], b[3], b[4]
                if not isinstance(btext, str) or not btext.strip():
                    continue
                if by0 < r.y1 - 2 or by1 > cap_y1 + 2:
                    continue
                x0_pt = min(x0_pt, bx0)
                x1_pt = max(x1_pt, bx1)
        x0 = max(0, int(x0_pt * scale) - FIG_CROP_PADDING_PX)
        y0 = max(0, int(y0_pt * scale) - FIG_CROP_PADDING_PX)
        x1 = min(W, int(x1_pt * scale) + FIG_CROP_PADDING_PX)
        y1 = min(H, int(y1_pt * scale) + FIG_CROP_PADDING_PX)
        if x1 - x0 < 100 or y1 - y0 < 100:
            continue
        idx += 1
        out = out_dir / f"raw_{idx:03d}.png"
        page_img.crop((x0, y0, x1, y1)).save(out)
        results.append({
            "path": str(out),
            "page": page.number + 1,
            "figure_number": fig_num,
            "caption": caption,
        })
    return results, idx


def phase_figures(
    pdf_path: Path,
    topic_pages: dict[str, list[tuple[int, Path]]],
    ws: Path,
    parallel: int = 1,
) -> dict[str, list[dict]]:
    """Extract figure crops per topic, deterministically.

    For each page: get embedded-bitmap rects, cluster split panels into one
    rect per logical figure, then crop the union from the rendered 300-DPI
    PNG with caption-driven Y-extension and X-widening for legends.
    Pages with no embedded bitmaps contribute no figures.
    """
    root = ws / "pdf_figures"

    def _one(item: tuple[str, list[tuple[int, Path]]]) -> tuple[str, list[dict]]:
        topic_id, pairs = item
        topic_dir = root / topic_id
        topic_dir.mkdir(parents=True, exist_ok=True)
        cache = topic_dir / "figures.json"
        if cache.exists():
            return topic_id, json.loads(cache.read_text())

        # Each worker opens its own fitz.Document — PyMuPDF is not thread-safe.
        doc = fitz.open(str(pdf_path))
        try:
            idx = 0
            topic_figs: list[dict] = []
            for page_num, page_image in pairs:
                page = doc[page_num]
                rects = _bitmap_rects_for_page(page)
                merged = _cluster_split_panels(rects)
                figs, idx = _extract_bitmap_figures(
                    page, merged, page_image, topic_dir, idx,
                )
                topic_figs.extend(figs)
        finally:
            doc.close()
        cache.write_text(json.dumps(topic_figs, indent=2) + "\n")
        print(f"    [{topic_id}] {len(topic_figs)} figures")
        return topic_id, topic_figs

    items = list(topic_pages.items())
    result: dict[str, list[dict]] = {}
    if parallel <= 1:
        for item in items:
            tid, figs = _one(item)
            result[tid] = figs
    else:
        with ThreadPoolExecutor(max_workers=parallel) as executor:
            for tid, figs in executor.map(_one, items):
                result[tid] = figs
    return result


# ═══════════════════════════════════════════════════════════════════════════════
# HTML knowledge source: parallels the PDF helpers above
# ═══════════════════════════════════════════════════════════════════════════════
#
# Activated by `sources.html_guide.root_url` in the YAML config. The root URL
# plays the same role as the printed Table of Contents in PDF mode — it lists
# the categories/topics. With `crawl_depth: N` (default 2) we also walk N-1
# link-hops deeper to harvest sub-section structure.
#
# Outputs match the PDF path so downstream phases (4, 5, 6) need no changes:
#   • taxonomy.json: same shape as PDF mode, except topics carry `urls: [str]`
#     instead of `pdf_pages: [int]`.
#   • topic_pages: dict[topic_id, list[(idx, md_path)]] — markdown converted
#     from each URL's main content, one .md per URL, in
#     `workspace/<domain>/html_pages/<topic_id>/page_NNNN.md`. Every inline
#     `<img>` is downloaded as a sibling `images/img_NNN.<ext>` and the
#     markdown's `![alt]` references point at the absolute local path so
#     Claude's Read tool can load them in Phase 4. `call_claude` lists each
#     .md path in the prompt — extension-agnostic vs. .png paths.
#   • figures: dict[topic_id, list[fig_dict]] — same `<img>` downloads,
#     re-emitted as `{path, description, source_url}` for Phase 4
#     multimodal Call B candidates. Cached at
#     `workspace/<domain>/html_pages/<topic_id>/figures.json`.

HTML_DEFAULT_DEPTH = 2
HTML_FETCH_TIMEOUT = 30
HTML_USER_AGENT = "Mozilla/5.0 (compatible; skill-pipeline/1.0)"


def _html_cache_path(url: str, cache_dir: Path) -> Path:
    import hashlib
    h = hashlib.md5(url.encode("utf-8")).hexdigest()[:16]
    return cache_dir / f"{h}.html"


def _fetch_html(url: str, cache_dir: Path) -> str | None:
    """Fetch and cache HTML by URL hash. Returns text or None on failure."""
    import requests
    cache_dir.mkdir(parents=True, exist_ok=True)
    cf = _html_cache_path(url, cache_dir)
    if cf.exists() and cf.stat().st_size > 0:
        return cf.read_text(encoding="utf-8", errors="replace")
    try:
        r = requests.get(
            url, timeout=HTML_FETCH_TIMEOUT,
            headers={"User-Agent": HTML_USER_AGENT},
        )
        if r.status_code == 200 and r.text:
            cf.write_text(r.text, encoding="utf-8")
            return r.text
        print(f"    [fetch] {url[:70]}... HTTP {r.status_code}")
    except Exception as e:
        print(f"    [fetch] {url[:70]}... ERR {e}")
    return None


def _absolutize(href: str, base_url: str) -> str:
    """Resolve href against base_url and strip URL fragments."""
    from urllib.parse import urljoin
    return urljoin(base_url, href).split("#", 1)[0]


def _is_in_scope(url: str, root_url: str, path_prefix: str | None = None) -> bool:
    """Stay within the same docs site/section as the root URL.

    If `path_prefix` is given, additionally require the URL's path to start
    with that prefix (the root URL itself is exempt so the entry-point page
    can still be visited even when its TOC links live in a sub-section).
    """
    from urllib.parse import urlparse
    pr, pu = urlparse(root_url), urlparse(url)
    if pr.netloc != pu.netloc:
        return False
    # Same path prefix up to last "/" of root.
    root_prefix = pr.path.rsplit("/", 1)[0] + "/"
    if not (pu.path.startswith(root_prefix) or pu.path == pr.path):
        return False
    if path_prefix and pu.path != pr.path and not pu.path.startswith(path_prefix):
        return False
    return True


def _select_main(soup):
    """Heuristic: locate the main content container, skipping site chrome."""
    for sel in ("main", "article"):
        node = soup.find(sel)
        if node:
            return node
    # ARIA role="main" — used by Sphinx-readthedocs themes which wrap the
    # body inside `<div role="main">` rather than a semantic <main> tag.
    node = soup.find(attrs={"role": "main"})
    if node:
        return node
    for cid in ("content", "main", "main-content"):
        node = soup.find(id=cid)
        if node:
            return node
    return soup.body or soup


def _parse_html_outline(html: str, page_url: str) -> list[dict]:
    """Extract headings + links from one page in document order.

    Returns entries shaped like ToC entries: {level, title, url, source}.
    Headings get url="" (they only contribute structure); <a> entries get
    a non-empty url that downstream code uses as the topic page.
    """
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    main = _select_main(soup)
    out: list[dict] = []
    for el in main.find_all(["h1", "h2", "h3", "h4", "a"]):
        if el.name in ("h1", "h2", "h3", "h4"):
            text = el.get_text(" ", strip=True)
            if text:
                out.append({
                    "level": int(el.name[1]),
                    "title": text,
                    "url": "",
                    "source": page_url,
                })
        else:
            href = el.get("href")
            if not href or href.startswith(("#", "mailto:", "javascript:")):
                continue
            text = el.get_text(" ", strip=True)
            if not text or len(text) > 200:
                continue
            out.append({
                "level": 5,
                "title": text,
                "url": _absolutize(href, page_url),
                "source": page_url,
            })
    return out


TAXONOMY_FROM_HTML_PROMPT = """\
Below is the documentation outline for {app_name} {app_version}, harvested by
crawling the official documentation site. Each line is one heading or hyperlink
from a docs page, with its visual depth as L1/L2/L3/L4, and (for links) the
target URL it points to.

Turn it into a 2-layer skill taxonomy: category → topic.

- DROP filler entries: navigation chrome ("Edit this page", "Search", "Log in",
  language selectors), breadcrumbs, footers, "See also" cross-references, and
  any heading whose only content is generic ("Overview", "Introduction") and
  has no concrete user action behind it.
- MERGE links that describe ONE coherent skill (e.g. an "Adding Items" page
  with sub-pages for drag-and-drop, browser connector, manual entry — that's
  a single topic "Adding items to your library").
- KEEP topics that map to a concrete user action.
- For each topic, set `urls` to the documentation URLs that contain the
  relevant content for that topic. Order matters: put the most authoritative
  page first.
- Use kebab-case slugs for ids.
- Size the taxonomy to the source: a full documentation crawl typically
  yields 4-12 categories with 2-10 topics each; a single tutorial page
  (a "quick start" or one-page how-to) may legitimately produce just 1-3
  categories with 2-5 topics each. Don't pad with synthetic topics to hit
  a target — fewer well-grounded topics is better than diluted ones.

Outline (L<level> <title> [-> url]):
{entries_text}

Output JSON:
{{
    "categories": [
        {{
            "id": "adding-items",
            "name": "Adding Items to Your Library",
            "topics": [
                {{
                    "id": "drag-and-drop",
                    "name": "Drag and Drop Import",
                    "description": "Drag PDFs and other files into Zotero",
                    "urls": ["https://www.zotero.org/support/adding_items_to_zotero"]
                }}
            ]
        }}
    ]
}}

Output ONLY valid JSON.
"""


def _crawl_html(
    root_url: str,
    depth: int,
    ws: Path,
    path_prefix: str | None = None,
) -> tuple[list[dict], list[str]]:
    """Breadth-first crawl from root_url up to `depth` link-hops.

    `path_prefix` (optional) restricts which links to follow AND which
    outline entries to keep — useful when the root page is a top-level
    index that mixes target docs with out-of-scope siblings (e.g. a docs
    home that lists both User Guide and Developer Guide). The root page
    itself is always visited so its TOC can be harvested.

    Returns (all_outline_entries, ordered_visited_urls). Cached HTML lives in
    workspace/<domain>/html_cache/.
    """
    cache_dir = ws / "html_cache"
    visited: list[str] = []
    seen: set[str] = set()
    outline: list[dict] = []

    queue: list[tuple[str, int]] = [(root_url, 0)]
    while queue:
        url, d = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        html = _fetch_html(url, cache_dir)
        if not html:
            continue
        visited.append(url)
        entries = _parse_html_outline(html, url)
        if path_prefix:
            from urllib.parse import urlparse
            entries = [
                e for e in entries
                if not e.get("url")
                or urlparse(e["url"]).path.startswith(path_prefix)
            ]
        outline.extend(entries)
        if d + 1 < depth:
            for e in entries:
                u = e.get("url") or ""
                if u and u not in seen and _is_in_scope(u, root_url, path_prefix):
                    queue.append((u, d + 1))
    return outline, visited


def phase_taxonomy_from_html_root(config: dict, ws: Path) -> dict:
    """Build a 2-layer taxonomy by crawling an HTML documentation root.

    The root page acts as the printed ToC. With `sources.html_guide.crawl_depth`
    > 1 we also harvest sub-headings from each linked page so the taxonomy can
    reach into level-3 sub-topics. Cached at workspace/<domain>/taxonomy.json.
    """
    cache = ws / "taxonomy.json"
    if cache.exists():
        print("  [cached]")
        return json.loads(cache.read_text())

    src = config.get("sources", {}).get("html_guide") or {}
    root_url = src.get("root_url")
    if not root_url:
        print("  HTML mode requires sources.html_guide.root_url in the config.")
        sys.exit(1)
    depth = int(src.get("crawl_depth", HTML_DEFAULT_DEPTH))
    path_prefix = src.get("path_prefix") or None
    if path_prefix:
        print(f"  Crawling {root_url} (depth={depth}, path_prefix={path_prefix})")
    else:
        print(f"  Crawling {root_url} (depth={depth})")

    outline, visited = _crawl_html(root_url, depth, ws, path_prefix=path_prefix)
    if not outline:
        print("  FAILED: crawl produced no outline entries")
        sys.exit(1)
    (ws / "html_outline_raw.json").write_text(json.dumps(outline, indent=2) + "\n")
    print(f"  Crawled {len(visited)} pages, {len(outline)} outline entries")

    # Build a compact text serialization for the LLM. Cap it to keep prompts
    # under ~50k chars; that's >1000 entries which is plenty for any docs site.
    lines: list[str] = []
    for e in outline:
        lvl = e.get("level", 5)
        title = e.get("title", "").strip()
        url = e.get("url", "")
        if not title:
            continue
        if url:
            lines.append(f"L{lvl} {title} -> {url}")
        else:
            lines.append(f"L{lvl} {title}")
    entries_text = "\n".join(lines)
    if len(entries_text) > 50000:
        entries_text = entries_text[:50000] + "\n... [truncated]"

    prompt = TAXONOMY_FROM_HTML_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        entries_text=entries_text,
    )
    result = call_claude(prompt, timeout=600)
    if not result:
        print("  FAILED: no response from Claude (taxonomy synthesis)")
        sys.exit(1)
    taxonomy = parse_json_response(result)
    if not isinstance(taxonomy, dict) or "categories" not in taxonomy:
        print("  FAILED: couldn't parse JSON")
        sys.exit(1)

    # Normalize urls list per topic.
    for cat in taxonomy["categories"]:
        for topic in cat.get("topics", []):
            urls = topic.get("urls") or []
            if isinstance(urls, list):
                topic["urls"] = [u for u in urls if isinstance(u, str) and u]
            else:
                topic["urls"] = []

    cache.write_text(json.dumps(taxonomy, indent=2) + "\n")
    for cat in taxonomy["categories"]:
        topics = cat["topics"]
        n_urls = sum(len(t.get("urls", [])) for t in topics)
        print(f"  {cat['name']}: {len(topics)} topics, {n_urls} urls")
    return taxonomy


def _extract_main_html(html: str, page_url: str):
    """Return a BeautifulSoup of the page's main content node, with all
    `<a href>` and `<img src>` URLs absolutized in-place."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    main = _select_main(soup)
    # Strip noise that markdownify would otherwise serialize.
    for tag in main.find_all(["script", "style", "noscript"]):
        tag.decompose()
    # Absolutize hrefs / srcs so any reference (in markdown or downloaded
    # image filename derivation) is unambiguous.
    for a in main.find_all("a", href=True):
        a["href"] = _absolutize(a["href"], page_url)
    for img in main.find_all("img", src=True):
        img["src"] = _absolutize(img["src"], page_url)
    return main


def _download_image(abs_src: str, dest_dir: Path, idx: int) -> Path | None:
    """Download one image to `dest_dir/img_{idx:03d}.<ext>`. Returns the
    local Path or None on failure. Skips download if the file already
    exists (cache)."""
    import requests
    from urllib.parse import urlparse
    suffix = Path(urlparse(abs_src).path).suffix.lower()
    if suffix not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
        suffix = ".png"
    dest = dest_dir / f"img_{idx:03d}{suffix}"
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    try:
        r = requests.get(
            abs_src,
            timeout=15,
            headers={"User-Agent": HTML_USER_AGENT},
        )
        if r.status_code != 200 or not r.content:
            return None
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return dest
    except Exception:
        return None


def _html_to_markdown_with_local_images(
    soup, page_url: str, images_dir: Path,
) -> tuple[str, list[dict]]:
    """Walk the soup, replace each `<img src=...>` with a download to
    `images_dir/img_NNN.<ext>` (path absolutized so Claude's Read tool can
    load it), then convert the soup to markdown via `markdownify`. Images
    that fail to download are dropped (their `<img>` tag is removed so the
    markdown stays clean).

    Returns (markdown_text, figures_metadata) where figures_metadata is a
    list of `{path, description, source_url}` dicts in download order —
    consumable by Phase 4 multimodal Call B as figure candidates.
    """
    from markdownify import markdownify
    figures: list[dict] = []
    for idx, img in enumerate(list(soup.find_all("img", src=True))):
        abs_src = img["src"]  # already absolutized in _extract_main_html
        local = _download_image(abs_src, images_dir, idx)
        if local is None:
            img.decompose()
            continue
        # Rewrite to absolute local path so Claude's Read tool can load it.
        img["src"] = str(local.resolve())
        figures.append({
            "path": str(local.resolve()),
            "description": (img.get("alt") or "").strip(),
            "source_url": page_url,
        })
    md = markdownify(str(soup), heading_style="ATX")
    return md, figures


def phase_html_pages(
    config: dict, taxonomy: dict, ws: Path,
) -> tuple[None, dict[str, list[tuple[int, Path]]]]:
    """Fetch each topic URL via plain HTTP, extract main content as
    markdown, and download every inline `<img>` into a sibling `images/`
    dir. The markdown's `<img>` references are rewritten to absolute
    local paths so Claude (in Phase 4, via the Read tool) can load each
    image alongside the prose. Image downloads here are scoped to the
    markdown — Phase 3 (`phase_html_figures`) does an independent pass
    that builds the canonical `html_figures/<topic>/` figure list used
    as Phase 4 multimodal Call B candidates.

    Output per topic:
      `workspace/<domain>/html_pages/<topic_id>/page_NNNN.md`
      `workspace/<domain>/html_pages/<topic_id>/images/img_NNN.<ext>`
    """
    pages_root = ws / "html_pages"
    pages_root.mkdir(parents=True, exist_ok=True)
    cache_dir = ws / "html_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Collect (topic_id, url) pairs preserving order.
    work: list[tuple[str, str]] = []
    for cat in taxonomy.get("categories", []):
        for topic in cat.get("topics", []):
            for url in topic.get("urls", []):
                work.append((topic["id"], url))

    if not work:
        print("  No URLs in taxonomy.")
        return None, {}

    topic_pages: dict[str, list[tuple[int, Path]]] = {}
    for topic_id, url in work:
        topic_dir = pages_root / topic_id
        topic_dir.mkdir(parents=True, exist_ok=True)
        images_dir = topic_dir / "images"
        idx = len(topic_pages.get(topic_id, []))
        out = topic_dir / f"page_{idx:04d}.md"

        if out.exists() and out.stat().st_size > 0:
            topic_pages.setdefault(topic_id, []).append((idx, out))
            continue

        html = _fetch_html(url, cache_dir)
        if not html:
            print(f"    [{topic_id}] fetch {url[:60]}... ERR no html")
            continue
        try:
            main = _extract_main_html(html, url)
            md, _ = _html_to_markdown_with_local_images(main, url, images_dir)
        except Exception as e:
            print(f"    [{topic_id}] convert {url[:60]}... ERR {e}")
            continue

        if not md.strip():
            print(f"    [{topic_id}] convert {url[:60]}... empty markdown, skipping")
            continue

        out.write_text(md, encoding="utf-8")
        topic_pages.setdefault(topic_id, []).append((idx, out))

    print(f"  Wrote markdown for {len(topic_pages)} topics via requests")
    return None, topic_pages


def phase_html_figures(taxonomy: dict, ws: Path) -> dict[str, list[dict]]:
    """Pull `<img>` tags from each topic's pages and download them into
    `html_figures/<topic>/`. Independent of Phase 2's inline-image
    download (which lives in `html_pages/<topic>/images/` and exists to
    back the markdown's `![]()` refs); this canonical list is what
    Phase 4 multimodal Call B uses as figure candidates.

    Output mirrors phase_figures: {topic_id: [{path, description, ...}]}.
    """
    import requests
    from bs4 import BeautifulSoup

    root = ws / "html_figures"
    cache_dir = ws / "html_cache"
    result: dict[str, list[dict]] = {}

    for cat in taxonomy.get("categories", []):
        for topic in cat.get("topics", []):
            topic_id = topic["id"]
            topic_dir = root / topic_id
            topic_dir.mkdir(parents=True, exist_ok=True)
            cache = topic_dir / "figures.json"
            if cache.exists():
                result[topic_id] = json.loads(cache.read_text())
                continue

            figs: list[dict] = []
            seen_src: set[str] = set()
            for url in topic.get("urls", []):
                html = _fetch_html(url, cache_dir)
                if not html:
                    continue
                soup = BeautifulSoup(html, "html.parser")
                main = _select_main(soup)
                for img in main.find_all("img"):
                    src = img.get("src") or img.get("data-src")
                    if not src:
                        continue
                    abs_src = _absolutize(src, url)
                    if abs_src in seen_src:
                        continue
                    seen_src.add(abs_src)
                    ext = abs_src.rsplit(".", 1)[-1].split("?", 1)[0].lower()
                    if ext not in ("png", "jpg", "jpeg", "gif", "webp", "svg"):
                        ext = "png"
                    fname = f"fig_{len(figs):03d}.{ext}"
                    fpath = topic_dir / fname
                    try:
                        r = requests.get(
                            abs_src, timeout=20,
                            headers={"User-Agent": HTML_USER_AGENT},
                        )
                        if r.status_code == 200 and r.content:
                            fpath.write_bytes(r.content)
                            figs.append({
                                "path": str(fpath),
                                "description": (img.get("alt") or "").strip(),
                                "source_url": url,
                            })
                    except Exception:
                        continue
            cache.write_text(json.dumps(figs, indent=2) + "\n")
            result[topic_id] = figs
            print(f"    [{topic_id}] {len(figs)} figures")
    return result


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4: Text skill — one guide.md per topic
# ═══════════════════════════════════════════════════════════════════════════════

# Source-format hint slotted into TEXT_PROMPT and MULTIMODAL_PROSE_PROMPT.
# - "image":   pages are PNGs (PDF mode, task mode).
# - "markdown": pages are .md files with inline absolute-path image refs
#   (HTML mode). Claude must Read each ![](abs_path) reference itself.
SOURCE_FORMAT_HINTS = {
    "image": (
        "I'm attaching the relevant pages from the official {app_name} {app_version} guide "
        "as images. Use them as the primary source of truth."
    ),
    "markdown": (
        "I'm attaching markdown extracted from the official {app_name} {app_version} guide. "
        "The markdown contains inline image references — `![alt](abs_path)`. Use the Read tool "
        "to load each referenced image so you can see the UI screenshots alongside the prose. "
        "Use the markdown text and its referenced images together as the primary source of truth."
    ),
}


def _resolve_source_format(config: dict) -> str:
    """Pick the SOURCE_FORMAT_HINTS key for the current run.

    HTML mode → 'markdown' (Phase 2 produces .md files with inline image refs).
    PDF / task mode → 'image' (Phase 2 produces .png renders).
    """
    sources = config.get("sources", {}) or {}
    if sources.get("html_guide"):
        return "markdown"
    return "image"


TEXT_PROMPT = """\
Write a practical reference guide for {app_name} {app_version}.

Topic: {topic_name}
Description: {topic_description}

{source_format_hint}

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
    return MMSKILLS_ROOT / "skills" / f"{domain}-knowledge-{modality}-stage1"


def _draft_topic_prose(
    topic: dict, cat: dict, config: dict, page_images: list[Path],
) -> str | None:
    """Generate topic prose markdown from page images. Pure: no disk writes.

    Used by both `generate_text_guide` (writes to skills/text-v1/) and
    `generate_multimodal_guide` (uses in-memory when text-v1 isn't requested).
    Cached on disk at workspace/<domain>/text_drafts/<cat>/<topic>.md to avoid
    paying the LLM cost twice when both modalities are produced.
    """
    if not page_images:
        return None
    cache = (
        WORKSPACE_DIR / config["domain"] / "text_drafts"
        / cat["id"] / f"{topic['id']}.md"
    )
    if cache.exists() and cache.stat().st_size > 0:
        return cache.read_text()
    fmt_key = _resolve_source_format(config)
    prompt = TEXT_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
        topic_description=topic.get("description", ""),
        source_format_hint=SOURCE_FORMAT_HINTS[fmt_key].format(
            app_name=config["app_name"], app_version=config["app_version"],
        ),
    )
    result = call_claude(prompt, images=list(page_images), timeout=300)
    if not result:
        return None
    text = result.strip() + "\n"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text)
    return text


def generate_text_guide(
    topic: dict, cat: dict, config: dict, domain: str,
    page_images: list[Path],
) -> bool:
    text_dir = _skills_dir(domain, "text") / cat["id"] / topic["id"]
    guide_path = text_dir / "guide.md"
    if guide_path.exists():
        print(f"    [{topic['name']}] text [cached]")
        return True
    text = _draft_topic_prose(topic, cat, config, page_images)
    if text is None:
        if not page_images:
            print(f"    [{topic['name']}] text SKIP (no pages)")
        else:
            print(f"    [{topic['name']}] text FAILED")
        return False
    text_dir.mkdir(parents=True, exist_ok=True)
    guide_path.write_text(text)
    print(f"    [{topic['name']}] text OK")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4 (multimodal path): two-call design — prose-with-placeholders + anchor
# ═══════════════════════════════════════════════════════════════════════════════
#
# Independent from the text path. Two Claude calls per topic:
#
#   Call A (prose): pages → markdown body. Where a figure would help, Claude
#     inserts a placeholder line of the form
#         <!-- figure: <short description> -->
#     immediately after the relevant sentence. No filenames yet.
#
#   Call B (anchors): the placeholder-marked prose + a small thumbnail per
#     candidate figure (filename + caption attached). For each placeholder,
#     Claude either replaces it with `See \`raw_NNN.png\`.` (or `(see ...)`)
#     using a candidate filename, or deletes the line if no thumbnail matches.
#
# After Call B we extract which raw figures were actually anchored (in order),
# copy them into the topic dir as fig01.png, fig02.png, ..., and rewrite the
# markdown so refs use the renumbered names. Any leftover unresolved
# placeholders are stripped as a safety net.

MULTIMODAL_PROSE_PROMPT = """\
Write a practical reference guide for {app_name} {app_version}.

Topic: {topic_name}
Description: {topic_description}

{source_format_hint}

Write in a casual, readable style — like a colleague explaining over your shoulder. \
Use natural prose with clear actions, not rigid numbered steps.

Rules:
- Title: "# {topic_name} ({app_name} {app_version})"
- Use **bold** for menu paths and button names
- Short paragraphs, each covering one action or concept
- Include exact menu paths (e.g., **Format > Paragraph...**)
- Around 15-25 lines of prose total — concise and scannable
- No "Step 1, Step 2" phrasing — flowing prose with transitions

Figure placeholders:
- Where a figure from the attached pages would clearly help the reader \
understand what the prose just described, insert a SINGLE LINE of the form:

    <!-- figure: <short description of what the figure shows> -->

  immediately after the relevant sentence or paragraph. The description is \
your note about which visual was useful (the dialog name, the screenshot \
content, etc.) — keep it short, under ~15 words.
- 0-3 placeholders is typical; "none" is fine if no figure clearly helps.
- Do NOT pick filenames or use any other format. Only the comment syntax above.
- Do NOT verbalize the figure's content in the prose itself — the figure carries it.

Output ONLY the markdown guide.
"""


MULTIMODAL_ANCHOR_PROMPT = """\
Below is a draft reference guide that contains placeholder lines of the form:

    <!-- figure: <description> -->

You also have a list of candidate figure thumbnails. Each row of the list \
corresponds to one image attached to this message, in the SAME ORDER.

For EACH placeholder in the guide, decide whether any candidate thumbnail \
clearly matches its description (the same dialog, screenshot, or diagram).
- If a thumbnail matches, REPLACE the placeholder line with one of:
      See `<FILENAME>`.
      (see `<FILENAME>`)
      ... See `<FILENAME>` for the <brief noun phrase>.
  Use the candidate filename EXACTLY as listed (e.g. `raw_004.png`).
- If no thumbnail clearly matches the placeholder, DELETE the placeholder \
  line entirely (and the blank line it leaves, if any).

Strict rules:
- Do NOT modify any other text. Only the placeholder lines change.
- A given filename may only be used once across the whole document.
- Do NOT invent filenames. Do NOT use markdown image syntax.
- Do NOT add new figure references at sentences without a placeholder.
- Use the candidate filenames EXACTLY as listed in the text below \
  (the listed extension may be `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, \
  or `.svg` — preserve whatever extension the candidate has). Do NOT use \
  the attached thumbnail filenames.

Output ONLY the resolved markdown — start with the `# Title` line. \
Do NOT add any preamble, summary of thumbnails, or commentary before or \
after the guide. The first character of your reply must be `#`.

--- Guide with placeholders ---
{prose}

--- Candidate figures (in same order as attached thumbnails) ---
{figure_list}
"""


# Matches `See \`raw_004.png\``, `(see \`raw_004.png\`)`, `See \`raw_004.png\` for ...`.
# Source images aren't always .png — HTML mode (and some docs PDFs) include
# .jpeg/.gif/.webp/.svg, so the extension group covers every common image
# format. If this pattern only matched .png, refs to non-PNG sources would
# dangle (Call B emits the ref but post-processing would skip the file copy
# + filename rewrite).
_FIG_REF_PATTERN = re.compile(
    r"\bsee\s+`([A-Za-z0-9_./-]+\.(?:png|jpg|jpeg|gif|webp|svg))`",
    re.IGNORECASE,
)
# Matches Call A's placeholder lines (so Call B can be cleaned up after the fact).
_FIG_PLACEHOLDER_PATTERN = re.compile(
    r"^\s*<!--\s*figure:[^>]*-->\s*\n?",
    re.MULTILINE | re.IGNORECASE,
)
THUMBNAIL_MAX_SIDE = 512
THUMBNAIL_QUALITY = 75


def _make_thumbnail(src: Path, dst_dir: Path, max_side: int = THUMBNAIL_MAX_SIDE) -> Path:
    """Downscale src image to fit within max_side, JPEG output, for cheap LLM input."""
    img = Image.open(src)
    img.thumbnail((max_side, max_side), Image.LANCZOS)
    out = dst_dir / (src.stem + ".jpg")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(out, "JPEG", quality=THUMBNAIL_QUALITY, optimize=True)
    return out


def _multimodal_drafts_dir(config: dict, cat: dict) -> Path:
    return WORKSPACE_DIR / config["domain"] / "multimodal_drafts" / cat["id"]


def _draft_multimodal_prose_only(
    topic: dict, cat: dict, config: dict, page_images: list[Path],
) -> str | None:
    """Call A: pages → prose with `<!-- figure: ... -->` placeholders. Cached."""
    if not page_images:
        return None
    cache = _multimodal_drafts_dir(config, cat) / f"{topic['id']}.prose.md"
    if cache.exists() and cache.stat().st_size > 0:
        return cache.read_text()
    fmt_key = _resolve_source_format(config)
    prompt = MULTIMODAL_PROSE_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
        topic_description=topic.get("description", ""),
        source_format_hint=SOURCE_FORMAT_HINTS[fmt_key].format(
            app_name=config["app_name"], app_version=config["app_version"],
        ),
    )
    result = call_claude(prompt, images=list(page_images), timeout=300)
    if not result:
        return None
    text = result.strip() + "\n"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text)
    return text


def _splice_figure_anchors(
    topic: dict, cat: dict, config: dict, prose: str, figures: list[dict],
) -> str | None:
    r"""Call B: prose-with-placeholders + thumbnails → prose with `See \`X.png\`` anchors.

    If the prose has no placeholders, returns it unchanged (no Claude call).
    If there are placeholders but zero candidate figures, strips them and returns.
    Cached at .md (final draft) — `_FIG_REF_PATTERN` post-processing happens later.
    """
    cache = _multimodal_drafts_dir(config, cat) / f"{topic['id']}.md"
    if cache.exists() and cache.stat().st_size > 0:
        return cache.read_text()

    has_placeholders = bool(_FIG_PLACEHOLDER_PATTERN.search(prose))
    if not has_placeholders:
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(prose)
        return prose
    if not figures:
        # Placeholders but nothing to anchor to — strip them.
        stripped = _FIG_PLACEHOLDER_PATTERN.sub("", prose)
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(stripped)
        return stripped

    # Build thumbnail list in a temp dir; order matches the figure_list lines.
    fig_lines = []
    with tempfile.TemporaryDirectory(prefix="mm_thumbs_") as tmp:
        tmp_path = Path(tmp)
        thumbs: list[Path] = []
        for f in figures:
            fname = Path(f["path"]).name
            caption = (f.get("caption") or f.get("description") or "").strip()
            fig_lines.append(f"  - {fname} : {caption}" if caption else f"  - {fname}")
            thumbs.append(_make_thumbnail(Path(f["path"]), tmp_path))
        fig_list = "\n".join(fig_lines)
        prompt = MULTIMODAL_ANCHOR_PROMPT.format(
            prose=prose, figure_list=fig_list,
        )
        result = call_claude(prompt, images=thumbs, timeout=300)
    if not result:
        return None

    text = result.strip() + "\n"
    # Safety net: trim any preamble before the first `# ` heading.
    h = text.find("\n# ")
    if text.startswith("# "):
        pass
    elif h != -1:
        text = text[h + 1:]
    # Safety net: strip any placeholders Call B left behind.
    text = _FIG_PLACEHOLDER_PATTERN.sub("", text)
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text)
    return text


def _draft_multimodal_prose(
    topic: dict, cat: dict, config: dict,
    page_images: list[Path], figures: list[dict],
) -> str | None:
    """Two-call multimodal draft: (pages → prose+placeholders) → (splice anchors).

    Both calls are cached independently. The .md cache holds the final
    placeholder-resolved markdown; subsequent rebuilds reuse it.
    """
    prose = _draft_multimodal_prose_only(topic, cat, config, page_images)
    if prose is None:
        return None
    return _splice_figure_anchors(topic, cat, config, prose, figures)


def generate_multimodal_guide(
    topic: dict, cat: dict, config: dict, domain: str,
    page_images: list[Path], figures: list[dict],
) -> bool:
    mm_dir = _skills_dir(domain, "multimodal") / cat["id"] / topic["id"]
    mm_guide = mm_dir / "guide.md"

    if mm_guide.exists():
        print(f"    [{topic['name']}] multimodal [cached]")
        return True

    text = _draft_multimodal_prose(topic, cat, config, page_images, figures)
    if text is None:
        if not page_images:
            print(f"    [{topic['name']}] multimodal SKIP (no pages)")
        else:
            print(f"    [{topic['name']}] multimodal FAILED (prose draft)")
        return False

    # Find which raw figures Claude actually referenced, in order of first appearance.
    valid_files = {Path(f["path"]).name: Path(f["path"]) for f in figures}
    referenced: list[str] = []
    seen: set[str] = set()
    for m in _FIG_REF_PATTERN.finditer(text):
        fname = m.group(1)
        if fname in valid_files and fname not in seen:
            seen.add(fname)
            referenced.append(fname)

    mm_dir.mkdir(parents=True, exist_ok=True)
    # Clean stale figXX.<ext> (any image extension we might've written previously).
    for old in mm_dir.glob("fig[0-9][0-9].*"):
        old.unlink()

    if not referenced:
        mm_guide.write_text(text)
        print(f"    [{topic['name']}] multimodal OK (0 figs selected)")
        return True

    # Copy referenced figures as fig01.<ext>, fig02.<ext>, ... preserving the
    # source extension (so JPEG/GIF/WebP/SVG sources keep their format), and
    # substitute the names in the markdown.
    rename_map: dict[str, str] = {}
    for i, fname in enumerate(referenced, 1):
        ext = Path(fname).suffix.lower() or ".png"
        new_name = f"fig{i:02d}{ext}"
        shutil.copy2(valid_files[fname], mm_dir / new_name)
        rename_map[fname] = new_name

    def _sub(m: re.Match) -> str:
        original = m.group(0)
        fname = m.group(1)
        return original.replace(fname, rename_map.get(fname, fname))

    rewritten = _FIG_REF_PATTERN.sub(_sub, text)
    mm_guide.write_text(rewritten)
    print(f"    [{topic['name']}] multimodal OK ({len(referenced)} figs)")
    return True


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 5a: Use-when routing hints (per generated guide)
# ═══════════════════════════════════════════════════════════════════════════════
#
# For each generated guide.md we ask Claude to summarize, in one comma-separated
# line, the concrete user tasks the guide answers. This line is consumed by
# phase_index to enrich SKILL.md so a downstream agent can pick the right
# topic guide for a given task description.
#
# Cached per modality at:
#   workspace/<domain>/use_when/<modality>/<cat>/<topic>.txt
#
# We do NOT mutate the existing guide.md files — the cache is the source of
# truth for the SKILL.md index.

USE_WHEN_PROMPT = """\
Below is a reference guide for {app_name} {app_version}, topic: "{topic_name}".

Summarize, in ONE LINE, the concrete user tasks this guide answers. Output \
3-6 short comma-separated phrases — concrete keywords or noun phrases that \
a routing agent can match against a user's task description.

Examples of good phrases:
  saving with a password, encrypting with GPG, saving to .docx, configuring autorecovery

Rules:
- Output ONLY the comma-separated phrases on a single line. No prefix, no \
quotes, no markdown, no explanation.
- Be specific (mention dialog names, formats, settings) — avoid generic \
filler like "working with documents" or "using Writer".
- Stay grounded in what the guide actually covers — do not invent tasks.

--- Guide ---
{guide_text}
"""


def _use_when_cache_path(
    config: dict, domain: str, modality: str, cat_id: str, topic_id: str,
) -> Path:
    return (
        WORKSPACE_DIR / domain / "use_when" / modality / cat_id / f"{topic_id}.txt"
    )


def _compute_use_when(
    config: dict, domain: str, modality: str,
    cat: dict, topic: dict, guide_path: Path,
) -> tuple[str, str, str | None]:
    """Read guide.md and ask Claude for a one-line use-when summary. Cached."""
    cache = _use_when_cache_path(config, domain, modality, cat["id"], topic["id"])
    if cache.exists() and cache.stat().st_size > 0:
        return cat["id"], topic["id"], cache.read_text().strip()
    if not guide_path.exists():
        return cat["id"], topic["id"], None
    guide_text = guide_path.read_text()
    prompt = USE_WHEN_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
        guide_text=guide_text,
    )
    result = call_claude(prompt, timeout=120)
    if not result:
        return cat["id"], topic["id"], None
    line = result.strip().splitlines()[0].strip() if result.strip() else ""
    if not line:
        return cat["id"], topic["id"], None
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(line + "\n")
    return cat["id"], topic["id"], line


def phase_use_when(
    config: dict, domain: str, taxonomy: dict, mode: str, parallel: int = 4,
) -> None:
    """Populate the use-when cache for every existing guide.md. Idempotent."""
    modalities = ["text", "multimodal"] if mode == "both" else [mode]
    for modality in modalities:
        skills_dir = _skills_dir(domain, modality)
        jobs: list[tuple[dict, dict, Path]] = []
        for cat in taxonomy["categories"]:
            for topic in cat["topics"]:
                guide_path = skills_dir / cat["id"] / topic["id"] / "guide.md"
                if guide_path.exists():
                    jobs.append((cat, topic, guide_path))
        if not jobs:
            print(f"  {modality}-v1: no guides found, skipping use-when")
            continue
        # Skip jobs already cached (avoid spawning futures for cache hits).
        pending = [
            j for j in jobs
            if not _use_when_cache_path(
                config, domain, modality, j[0]["id"], j[1]["id"],
            ).exists()
        ]
        cached = len(jobs) - len(pending)
        print(f"  {modality}-v1: {len(jobs)} guides ({cached} cached, {len(pending)} to compute)")
        if not pending:
            continue
        with ThreadPoolExecutor(max_workers=parallel) as ex:
            futures = {
                ex.submit(
                    _compute_use_when, config, domain, modality, cat, topic, gp,
                ): (cat, topic)
                for cat, topic, gp in pending
            }
            done = 0
            for f in as_completed(futures):
                cat, topic = futures[f]
                try:
                    _, _, line = f.result()
                    done += 1
                    status = "OK" if line else "FAILED"
                    print(f"    [{done}/{len(pending)}] {topic['name']} {status}")
                except Exception as e:
                    print(f"    [{topic['name']}] ERROR: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 5b: Index (SKILL.md per modality)
# ═══════════════════════════════════════════════════════════════════════════════


def _loader_preamble(is_mm: bool) -> str:
    """Standard load_topic / list_topics consultation preamble injected into
    every SKILL.md emitted by Phase 5b. Matched between text and multimodal
    forms — only the figXX.png clause differs.
    """
    if is_mm:
        load_clause = (
            "returns the chosen topic's `guide.md` AND every figure (PNG) in "
            "that topic folder as one tool response. "
            "**Use this instead of `Read` for any `*.md` or `figXX.png` "
            "inside this skill.**"
        )
        example_tail = (
            "You will receive the guide text plus the relevant figures in a "
            "single tool result — no extra `Read` calls needed."
        )
        rule3 = (
            "\n3. Do **not** issue separate `Read` calls for `figXX.png` "
            "files inside this skill — they are delivered by `load_topic` "
            "automatically."
        )
    else:
        load_clause = (
            "returns the chosen topic's `guide.md` as one tool response. "
            "**Use this instead of `Read` for any `*.md` inside this skill.**"
        )
        example_tail = (
            "You will receive the guide text in a single tool result — "
            "no extra `Read` calls needed."
        )
        rule3 = ""

    return (
        "## How to consult this skill\n\n"
        "This skill exposes two MCP tools (already registered for you):\n\n"
        f"- **`load_topic(topic)`** — {load_clause}\n"
        "- **`list_topics()`** — returns every topic path available, one per line.\n\n"
        "Each entry in the TOC below has the form "
        "`[Title](<topic>/guide.md)`. The `<topic>` part (the path before "
        "`/guide.md`) is what you pass to `load_topic`.\n\n"
        f"> {example_tail}\n\n"
        "**Rules:**\n\n"
        "1. Before any GUI action where you are unsure of the menu path / "
        "dialog / icon, find the matching topic in the TOC and call "
        "`load_topic` first.\n"
        "2. You may call `load_topic` **at any step** of the trajectory, "
        "not only at the start. If the task moves into a new area, call "
        "`load_topic` again for the new area."
        f"{rule3}\n"
    )


_SKILL_SERVER_TEMPLATE = Path(__file__).parent / "templates" / "skill_server.py"


def _install_skill_server(skills_dir: Path) -> None:
    """Copy the canonical load_topic MCP server into <skill_dir>/tools/skill_server.py
    so the runner auto-mounts it (see scripts/run-gym-anything/run_task.py).
    """
    if not _SKILL_SERVER_TEMPLATE.exists():
        return
    tools = skills_dir / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    dest = tools / "skill_server.py"
    dest.write_text(_SKILL_SERVER_TEMPLATE.read_text())


def phase_index(config: dict, domain: str, taxonomy: dict, mode: str) -> None:
    app = config["app_name"]
    ver = config["app_version"]
    modalities = ["text", "multimodal"] if mode == "both" else [mode]
    for modality in modalities:
        skills_dir = _skills_dir(domain, modality)
        is_mm = (modality == "multimodal")
        mm_suffix = " with-screenshots" if is_mm else " text-only"
        fig_clause = " and every figure" if is_mm else ""
        desc = (
            f'Practical{mm_suffix} guides for {app} {ver}. '
            f'Consult via the load_topic MCP tool — it returns the guide text'
            f'{fig_clause} in one atomic call.'
        )
        preamble = _loader_preamble(is_mm)
        lines = [
            "---",
            f"name: {domain}-knowledge-{modality}-v1",
            f'description: "{desc}"',
            "---\n",
            f"# {app} {ver} Knowledge ({modality}-v1)\n",
            preamble,
            "## Guides\n",
        ]
        for cat in taxonomy["categories"]:
            lines.append(f"### {cat['name']}\n")
            for topic in cat["topics"]:
                rel = f"{cat['id']}/{topic['id']}/guide.md"
                path = skills_dir / rel
                if path.exists():
                    lines.append(f"- [{topic['name']}]({rel}) — {topic.get('description', '')}")
                    uw_path = _use_when_cache_path(
                        config, domain, modality, cat["id"], topic["id"],
                    )
                    if uw_path.exists():
                        uw = uw_path.read_text().strip()
                        if uw:
                            lines.append(f"  - **Use when:** {uw}")
                else:
                    lines.append(f"- {topic['name']} — *(not yet generated)*")
            lines.append("")
        skills_dir.mkdir(parents=True, exist_ok=True)
        (skills_dir / "SKILL.md").write_text("\n".join(lines) + "\n")
        _install_skill_server(skills_dir)
        print(f"  {modality}-v1 SKILL.md updated (+ tools/skill_server.py)")


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 6 (optional): Derive text-v1 from multimodal-v1
# ═══════════════════════════════════════════════════════════════════════════════
#
# Take each generated multimodal-v1 guide and rewrite the inline figure
# references (lines like `See \`figXX.png\`.`) into a few sentences of verbal
# description grounded in what the screenshot actually shows. The result is
# markdown-only — no images are copied. Topics with zero figure refs are
# copied verbatim (no LLM call).
#
# We also copy the multimodal use-when cache to the text cache (same topic =
# same routing keywords) so phase_index for text mode produces a SKILL.md
# with use-when bullets without an extra Claude pass.

TEXT_V1_PROMPT = """\
Below is a markdown reference guide for {app_name} {app_version}, topic: \
"{topic_name}". It currently references one or more screenshots inline using \
lines like:

    See `fig01.png`.
    (see `fig02.png`)
    ... See `fig03.png` for the dialog.

For each filename mentioned, the actual image is attached to this message \
in the SAME ORDER as the list below — first listed name = first attachment, \
and so on.

Rewrite the guide so that EACH such reference is REPLACED by 1-3 sentences \
that verbally describe what the screenshot shows — the dialog name, key \
fields/buttons visible, layout, anything a reader would need if they cannot \
see the image. Be concrete and grounded in the actual image content.

Strict rules:
- Do NOT modify any other text. Only the figure-reference lines change.
- Do NOT include any image references, markdown image syntax, or filenames \
in your output.
- Do NOT add a "Figure 1: ..." prefix; just describe what's there as prose.
- Output ONLY the rewritten markdown, starting with the `# Title` line. \
The first character of your reply must be `#`.

--- Figures attached, in order ---
{figure_list}

--- Original guide ---
{guide_text}
"""


def _text_v1_drafts_dir(config: dict, cat: dict) -> Path:
    return WORKSPACE_DIR / config["domain"] / "text_v1_drafts" / cat["id"]


def derive_text_for_one_guide(
    mm_guide: Path,
    text_guide: Path,
    cache: Path,
    app_name: str,
    app_version: str,
    topic_name: str,
    fig_ref_pattern: re.Pattern = _FIG_REF_PATTERN,
) -> str:
    """Derive a text-only guide from a multimodal guide.md by replacing each
    inline figure reference (matched by `fig_ref_pattern`, must capture the
    PNG filename in group 1) with 1-3 sentences of verbal description.

    Used by both v1 (Phase 6) and v3 (Phase 5) — see preprocess/skill-pipeline/.

    Returns status ∈ {"OK", "COPIED", "SKIP", "FAILED"}:
      OK     — Claude rewrote refs to verbal descriptions (or already cached)
      COPIED — guide had no fig refs, copied verbatim
      SKIP   — multimodal guide doesn't exist
      FAILED — Claude call failed (or referenced PNG missing on disk)
    """
    if not mm_guide.exists():
        return "SKIP"

    if text_guide.exists():
        return "OK"  # final output already on disk

    if cache.exists() and cache.stat().st_size > 0:
        text_guide.parent.mkdir(parents=True, exist_ok=True)
        text_guide.write_text(cache.read_text())
        return "OK"

    guide_text = mm_guide.read_text()

    # Find fig refs in order of first appearance, dedup.
    fig_names: list[str] = []
    seen: set[str] = set()
    for m in fig_ref_pattern.finditer(guide_text):
        fname = m.group(1)
        if fname not in seen:
            seen.add(fname)
            fig_names.append(fname)

    if not fig_names:
        # No figures to verbalize — copy verbatim.
        text_guide.parent.mkdir(parents=True, exist_ok=True)
        text_guide.write_text(guide_text)
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(guide_text)
        return "COPIED"

    # Verify all referenced figures exist on disk (next to the mm guide).
    fig_paths: list[Path] = []
    for name in fig_names:
        p = mm_guide.parent / name
        if not p.exists():
            return "FAILED"
        fig_paths.append(p)

    figure_list = "\n".join(f"  - {n}" for n in fig_names)
    prompt = TEXT_V1_PROMPT.format(
        app_name=app_name,
        app_version=app_version,
        topic_name=topic_name,
        figure_list=figure_list,
        guide_text=guide_text,
    )
    result = call_claude(prompt, images=fig_paths, timeout=300)
    if not result:
        return "FAILED"

    text = result.strip()
    # Safety net: trim any preamble before the first `# ` heading.
    if not text.startswith("# "):
        h = text.find("\n# ")
        if h != -1:
            text = text[h + 1:]
    # Safety net: strip any leftover figure refs (shouldn't be any).
    text = fig_ref_pattern.sub("", text)
    text = text.rstrip() + "\n"

    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(text)
    text_guide.parent.mkdir(parents=True, exist_ok=True)
    text_guide.write_text(text)
    return "OK"


def _derive_text_v1_for_topic(
    config: dict, domain: str, cat: dict, topic: dict,
) -> tuple[str, str, str]:
    """Rewrite one multimodal-v1 guide into text-v1 prose. v1-specific wrapper
    around `derive_text_for_one_guide` that maps taxonomy entries to disk paths.
    """
    mm_guide = (
        _skills_dir(domain, "multimodal") / cat["id"] / topic["id"] / "guide.md"
    )
    text_guide = (
        _skills_dir(domain, "text") / cat["id"] / topic["id"] / "guide.md"
    )
    cache = _text_v1_drafts_dir(config, cat) / f"{topic['id']}.md"
    status = derive_text_for_one_guide(
        mm_guide=mm_guide,
        text_guide=text_guide,
        cache=cache,
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
    )
    return cat["id"], topic["id"], status


def _mirror_use_when_to_text(config: dict, domain: str, taxonomy: dict) -> int:
    """Copy multimodal use-when cache files to the text cache. Idempotent."""
    copied = 0
    for cat in taxonomy["categories"]:
        for topic in cat["topics"]:
            src = _use_when_cache_path(
                config, domain, "multimodal", cat["id"], topic["id"],
            )
            dst = _use_when_cache_path(
                config, domain, "text", cat["id"], topic["id"],
            )
            if src.exists() and not dst.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(src.read_text())
                copied += 1
    return copied


def derive_text_from_multimodal_dir(
    mm_dir: Path,
    text_dir: Path,
    cache_dir: Path,
    app_name: str,
    app_version: str,
    parallel: int = 4,
    fig_ref_pattern: re.Pattern = _FIG_REF_PATTERN,
) -> dict[str, int]:
    """Glob-based driver: walk `mm_dir/**/guide.md`, derive a text-only twin
    for each into `text_dir/<rel>/guide.md`. Cache files at
    `cache_dir/<rel>.md`. Topic name is taken from the guide's first `# `
    heading (fallback: parent dir name). Returns counts dict.

    v3 uses this directly. v1 prefers the taxonomy-aware path
    (`phase_text_v1_from_multimodal`) which also mirrors use-when caches.
    """
    mm_dir = Path(mm_dir)
    text_dir = Path(text_dir)
    cache_dir = Path(cache_dir)

    guides = sorted(mm_dir.glob("*/*/guide.md"))
    if not guides:
        print(f"  No guides under {mm_dir} — nothing to derive.")
        return {"OK": 0, "COPIED": 0, "SKIP": 0, "FAILED": 0}
    print(f"  {len(guides)} guides to derive (parallel={parallel})")

    counts = {"OK": 0, "COPIED": 0, "SKIP": 0, "FAILED": 0}

    def _job(mm_guide: Path) -> tuple[Path, str]:
        rel = mm_guide.relative_to(mm_dir)
        text_guide = text_dir / rel
        cache = cache_dir / rel.parent / (rel.parent.name + ".md")
        # Topic name from H1 heading.
        topic_name = mm_guide.parent.name
        try:
            for line in mm_guide.read_text().splitlines():
                line = line.strip()
                if line.startswith("# "):
                    topic_name = line[2:].strip()
                    break
        except Exception:
            pass
        status = derive_text_for_one_guide(
            mm_guide=mm_guide,
            text_guide=text_guide,
            cache=cache,
            app_name=app_name,
            app_version=app_version,
            topic_name=topic_name,
            fig_ref_pattern=fig_ref_pattern,
        )
        return mm_guide, status

    with ThreadPoolExecutor(max_workers=parallel) as ex:
        futures = {ex.submit(_job, g): g for g in guides}
        done = 0
        for f in as_completed(futures):
            g = futures[f]
            try:
                _, status = f.result()
                counts[status] = counts.get(status, 0) + 1
                done += 1
                rel = g.relative_to(mm_dir)
                print(f"    [{done}/{len(guides)}] {rel} {status}")
            except Exception as e:
                counts["FAILED"] = counts.get("FAILED", 0) + 1
                print(f"    [{g.relative_to(mm_dir)}] ERROR: {e}")
    print(
        f"  done: OK={counts['OK']} COPIED={counts['COPIED']} "
        f"SKIP={counts['SKIP']} FAILED={counts['FAILED']}"
    )
    return counts


def phase_text_v1_from_multimodal(
    config: dict, domain: str, taxonomy: dict, parallel: int = 4,
) -> None:
    """Derive text-v1 guides from multimodal-v1 guides + figures."""
    jobs: list[tuple[dict, dict]] = []
    mm_skills = _skills_dir(domain, "multimodal")
    for cat in taxonomy["categories"]:
        for topic in cat["topics"]:
            if (mm_skills / cat["id"] / topic["id"] / "guide.md").exists():
                jobs.append((cat, topic))
    if not jobs:
        print("  No multimodal-v1 guides found — run phase 4 first.")
        return
    print(f"  {len(jobs)} multimodal guides to derive into text-v1 (parallel={parallel})")

    counts = {"OK": 0, "COPIED": 0, "SKIP": 0, "FAILED": 0}
    with ThreadPoolExecutor(max_workers=parallel) as ex:
        futures = {
            ex.submit(_derive_text_v1_for_topic, config, domain, cat, topic): (cat, topic)
            for cat, topic in jobs
        }
        done = 0
        for f in as_completed(futures):
            cat, topic = futures[f]
            try:
                _, _, status = f.result()
                counts[status] = counts.get(status, 0) + 1
                done += 1
                print(f"    [{done}/{len(jobs)}] {topic['name']} {status}")
            except Exception as e:
                counts["FAILED"] = counts.get("FAILED", 0) + 1
                print(f"    [{topic['name']}] ERROR: {e}")
    print(
        f"  text-v1: OK={counts['OK']} COPIED={counts['COPIED']} "
        f"SKIP={counts['SKIP']} FAILED={counts['FAILED']}"
    )

    n = _mirror_use_when_to_text(config, domain, taxonomy)
    print(f"  Mirrored {n} use-when cache files multimodal → text")


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
        if not generate_multimodal_guide(
            topic, cat, config, domain, page_images, figures,
        ):
            ok = False
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Task-driven skill generation (v1)")
    parser.add_argument("--config", required=True, help="Path to domain YAML config")
    parser.add_argument("--mode", choices=["text", "multimodal", "both"], default="both")
    parser.add_argument("--task_ids", nargs="*", help="Filter to specific task id prefixes")
    parser.add_argument(
        "--phase", type=int, choices=[1, 2, 3, 4, 5, 6], default=None,
        help=(
            "Run only phase N (1=taxonomy, 2=pages, 3=figures, 4=guides, "
            "5=use-when+index, 6=text-v1 from multimodal [optional]). "
            "Earlier phases must already be cached; later phases are skipped. "
            "Phase 6 is optional and not part of the default flow — request "
            "it explicitly with --phase 6. Default: run phases 1-5."
        ),
    )
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_absolute():
        # Allow path relative to pipeline dir.
        alt = PIPELINE_DIR / args.config
        if not config_path.exists() and alt.exists():
            config_path = alt
    config = load_config(config_path)
    domain = config["domain"]
    ws = workspace(domain)

    task_mode = "tasks" in config
    sources = config.get("sources") or {}
    has_pdf = "pdf_guide" in sources
    has_html = "html_guide" in sources
    if task_mode and has_html:
        print("Task mode + html_guide is not yet supported; use pdf_guide.")
        sys.exit(1)
    if has_pdf and has_html:
        print("Config has both pdf_guide and html_guide; pick one.")
        sys.exit(1)
    if not (task_mode or has_pdf or has_html):
        print("Config must define sources.pdf_guide, sources.html_guide, or a tasks block.")
        sys.exit(1)

    if task_mode:
        tasks = load_tasks(config)
        if args.task_ids:
            id_prefixes = set(args.task_ids)
            tasks = [t for t in tasks if any(t["task_id"].startswith(p) for p in id_prefixes)]
    else:
        if args.task_ids:
            print("--task_ids ignored: config has no `tasks:` block")
        tasks = []

    print(f"=== Skill Pipeline v1: {config['app_name']} {config['app_version']} ===")
    if task_mode:
        src_label = f"Tasks: {len(tasks)}"
    elif has_html:
        src_label = "Source: HTML docs"
    else:
        src_label = "Source: full PDF"
    p = config["parallel"]
    print(
        f"Domain: {domain} | {src_label} | Mode: {args.mode} | "
        f"Parallel: phase_2={p['phase_2']}, phase_3={p['phase_3']}, "
        f"phase_4={p['phase_4']}, phase_5={p['phase_5']}, phase_6={p['phase_6']}"
    )
    print()

    target = args.phase  # None = run all; otherwise run only this phase.

    def header(n: int, label: str) -> None:
        if target is None or target == n:
            print(label)

    pdf_path: Path | None = None

    # --- Phase 1: Taxonomy (always needed for downstream) ---
    header(1, "Phase 1: Taxonomy")
    if task_mode:
        taxonomy = phase_taxonomy(config, tasks, ws)
    elif has_pdf:
        pdf_path = _download_pdf(config, ws)
        if not pdf_path:
            print("  PDF mode requires sources.pdf_guide.url in the config.")
            sys.exit(1)
        taxonomy = phase_taxonomy_from_pdf_toc(config, pdf_path, ws)
    else:  # has_html
        taxonomy = phase_taxonomy_from_html_root(config, ws)
    if target is None or target == 1:
        print()
    if target == 1:
        print("Done (phase 1 only).")
        return

    # --- Phase 2: Per-topic pages (always needed for downstream) ---
    header(2, "Phase 2: Per-topic pages")
    if has_html:
        _, topic_pages = phase_html_pages(config, taxonomy, ws)
    else:
        pdf_path, topic_pages = phase_pdf_pages(
            config, taxonomy, ws, parallel=config["parallel"]["phase_2"],
        )
    if target is None or target == 2:
        print()
    if target == 2:
        print("Done (phase 2 only).")
        return

    # --- Phase 3: Figures (only needed for multimodal) ---
    figures_by_topic: dict[str, list[dict]] = {}
    if topic_pages and args.mode in ("multimodal", "both"):
        header(3, "Phase 3: Figures")
        if has_html:
            figures_by_topic = phase_html_figures(taxonomy, ws)
        elif pdf_path:
            figures_by_topic = phase_figures(
                pdf_path, topic_pages, ws, parallel=config["parallel"]["phase_3"],
            )
        if target is None or target == 3:
            print()
    if target == 3:
        print("Done (phase 3 only).")
        return

    all_topics = [
        (topic, cat)
        for cat in taxonomy["categories"]
        for topic in cat["topics"]
    ]

    # --- Phase 4: Generate per-topic guides ---
    if target is None or target == 4:
        print(f"Phase 4: Generate guides ({len(all_topics)} topics)")

        def _one(item):
            topic, cat = item
            pairs = topic_pages.get(topic["id"], [])
            images = [p for _, p in pairs]
            figs = figures_by_topic.get(topic["id"], [])
            return process_topic(topic, cat, config, domain, args.mode, images, figs)

        phase4_parallel = config["parallel"]["phase_4"]
        success = 0
        if phase4_parallel <= 1:
            for item in all_topics:
                try:
                    if _one(item):
                        success += 1
                except Exception as e:
                    print(f"    [{item[0]['name']}] ERROR: {e}")
        else:
            with ThreadPoolExecutor(max_workers=phase4_parallel) as executor:
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
        if target == 4:
            print("Done (phase 4 only).")
            return

    # --- Phase 5: routing hints (use-when) + SKILL.md index ---
    if target is None or target == 5:
        print("Phase 5a: Use-when routing hints")
        phase_use_when(
            config, domain, taxonomy, args.mode, parallel=p["phase_5"],
        )
        print()
        print("Phase 5b: Index")
        phase_index(config, domain, taxonomy, args.mode)
        print()

    # --- Phase 6 (optional): derive text-v1 from multimodal-v1 ---
    # Not part of the default flow — only runs when explicitly requested.
    if target == 6:
        print("Phase 6: Text-v1 from multimodal-v1")
        phase_text_v1_from_multimodal(
            config, domain, taxonomy, parallel=p["phase_6"],
        )
        print()
        print("Phase 6b: Index (text-v1)")
        phase_index(config, domain, taxonomy, "text")
        print()

    print("Done.")


if __name__ == "__main__":
    main()
