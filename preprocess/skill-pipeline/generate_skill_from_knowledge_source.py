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
  Phase 2 — Per-topic pages: each topic gets a list of rendered page images —
            300-DPI PDF page renders in PDF/task mode, or full-page playwright
            screenshots in HTML mode.
  Phase 3 — Figures: PDF mode crops figures from rendered pages (bitmap xrefs
            first, LLM bbox detection as fallback). HTML mode downloads
            `<img>` tags directly from each topic's pages.
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
TOC_DPI = 200            # ToC pages render DPI — text-legibility is enough
TOC_RENDER_CAP = 25      # max ToC pages to attach to a Phase 1 prompt
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
    config: dict, taxonomy: dict, ws: Path,
) -> tuple[Path | None, dict[str, list[tuple[int, Path]]]]:
    """Returns (pdf_path, {topic_id: [(0-indexed page_num, rendered_image_path), ...]})."""
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
#   • topic_pages: dict[topic_id, list[(idx, png_path)]] — full-page playwright
#     screenshots, one per URL, in `workspace/<domain>/html_pages/<topic_id>/`.
#   • figures: dict[topic_id, list[fig_dict]] — `<img>` tags downloaded from
#     each topic's pages, into `workspace/<domain>/html_figures/<topic_id>/`.

HTML_DEFAULT_DEPTH = 2
HTML_VIEWPORT_W = 1280
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


def _is_in_scope(url: str, root_url: str) -> bool:
    """Stay within the same docs site/section as the root URL."""
    from urllib.parse import urlparse
    pr, pu = urlparse(root_url), urlparse(url)
    if pr.netloc != pu.netloc:
        return False
    # Same path prefix up to last "/" of root.
    root_prefix = pr.path.rsplit("/", 1)[0] + "/"
    return pu.path.startswith(root_prefix) or pu.path == pr.path


def _select_main(soup):
    """Heuristic: locate the main content container, skipping site chrome."""
    for sel in ("main", "article"):
        node = soup.find(sel)
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
- Use kebab-case slugs for ids. Aim for 4-12 categories, 2-10 topics each.

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


def _crawl_html(root_url: str, depth: int, ws: Path) -> tuple[list[dict], list[str]]:
    """Breadth-first crawl from root_url up to `depth` link-hops.

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
        outline.extend(entries)
        if d + 1 < depth:
            for e in entries:
                u = e.get("url") or ""
                if u and u not in seen and _is_in_scope(u, root_url):
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
    print(f"  Crawling {root_url} (depth={depth})")

    outline, visited = _crawl_html(root_url, depth, ws)
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


def phase_html_pages(
    config: dict, taxonomy: dict, ws: Path,
) -> tuple[None, dict[str, list[tuple[int, Path]]]]:
    """Render each topic URL as a full-page PNG via playwright.

    Returns (None, {topic_id: [(idx, png_path), ...]}) — the leading `None`
    matches phase_pdf_pages's signature so main() can consume both uniformly
    (the PDF path is irrelevant in HTML mode and figures use the cached HTML
    instead of cropping a PDF).
    """
    pages_root = ws / "html_pages"
    pages_root.mkdir(parents=True, exist_ok=True)

    # Collect (topic_id, url) pairs preserving order.
    work: list[tuple[str, str]] = []
    for cat in taxonomy.get("categories", []):
        for topic in cat.get("topics", []):
            for url in topic.get("urls", []):
                work.append((topic["id"], url))

    if not work:
        print("  No URLs in taxonomy.")
        return None, {}

    from playwright.sync_api import sync_playwright

    topic_pages: dict[str, list[tuple[int, Path]]] = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": HTML_VIEWPORT_W, "height": 900},
            user_agent=HTML_USER_AGENT,
        )
        try:
            for topic_id, url in work:
                topic_dir = pages_root / topic_id
                topic_dir.mkdir(parents=True, exist_ok=True)
                idx = len(topic_pages.get(topic_id, []))
                out = topic_dir / f"page_{idx:04d}.png"
                if not out.exists():
                    try:
                        page = ctx.new_page()
                        page.goto(url, wait_until="networkidle", timeout=30000)
                        page.screenshot(path=str(out), full_page=True)
                        page.close()
                    except Exception as e:
                        print(f"    [{topic_id}] screenshot {url[:60]}... ERR {e}")
                        continue
                topic_pages.setdefault(topic_id, []).append((idx, out))
        finally:
            ctx.close()
            browser.close()
    print(f"  Rendered pages for {len(topic_pages)} topics via playwright")
    return None, topic_pages


def phase_html_figures(taxonomy: dict, ws: Path) -> dict[str, list[dict]]:
    """Pull `<img>` tags from each topic's pages and download them.

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
    prompt = TEXT_PROMPT.format(
        app_name=config["app_name"],
        app_version=config["app_version"],
        topic_name=topic["name"],
        topic_description=topic.get("description", ""),
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
    page_images: list[Path], figures: list[dict],
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

    # Prefer the on-disk text-v1 guide if it exists (for byte-for-byte parity);
    # otherwise draft prose internally. Either way the multimodal output is
    # produced without requiring text-v1 to be requested.
    if text_guide.exists():
        text = text_guide.read_text()
    else:
        text = _draft_topic_prose(topic, cat, config, page_images)
        if text is None:
            if not page_images:
                print(f"    [{topic['name']}] multimodal SKIP (no pages)")
            else:
                print(f"    [{topic['name']}] multimodal FAILED (prose draft)")
            return False
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
        if not generate_multimodal_guide(
            topic, cat, config, domain, page_images, figures,
        ):
            ok = False
    return ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Task-driven skill generation (v1)")
    parser.add_argument("--config", required=True, help="Path to domain YAML config")
    parser.add_argument("--mode", choices=["text", "multimodal", "both"], default="both")
    parser.add_argument("--parallel", type=int, default=1)
    parser.add_argument("--task_ids", nargs="*", help="Filter to specific task id prefixes")
    parser.add_argument(
        "--phase", type=int, choices=[1, 2, 3, 4, 5], default=None,
        help=(
            "Run only phase N (1=taxonomy, 2=pages, 3=figures, 4=guides, 5=index). "
            "Earlier phases must already be cached; later phases are skipped. "
            "Default: run all phases."
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
    print(f"Domain: {domain} | {src_label} | Mode: {args.mode} | Parallel: {args.parallel}")
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
        pdf_path, topic_pages = phase_pdf_pages(config, taxonomy, ws)
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
            figures_by_topic = phase_figures(pdf_path, topic_pages, ws)
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
        if target == 4:
            print("Done (phase 4 only).")
            return

    # --- Phase 5: SKILL.md index ---
    if target is None or target == 5:
        print("Phase 5: Index")
        phase_index(config, domain, taxonomy, args.mode)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
