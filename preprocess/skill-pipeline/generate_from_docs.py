"""Documentation-driven skill generation pipeline.

Generates multimodal skills by crawling official HTML documentation.
Unlike generate_from_tasks.py (task-driven, PDF+YouTube), this pipeline
works directly from web docs that already contain screenshots and
step-by-step instructions.

Usage:
  python3 generate_from_docs.py --domain qgis --parallel 4
  python3 generate_from_docs.py --domain qgis --phase crawl   # just crawl
  python3 generate_from_docs.py --domain qgis --phase generate # just generate

Pipeline:
  Phase 1 — Crawl:    fetch doc pages, extract text + download images
  Phase 2 — Organize: group pages into skill topics via Claude
  Phase 3 — Generate: synthesize skill guides (text + multimodal)
  Phase 4 — Index:    generate SKILL.md files

All artifacts cached in workspace/ (gitignored). Re-running skips completed work.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import yaml

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Install dependencies: pip install requests beautifulsoup4 lxml")
    sys.exit(1)

PIPELINE_DIR = Path(__file__).parent
MMSKILLS_ROOT = PIPELINE_DIR.parent.parent
CONFIGS_DIR = PIPELINE_DIR / "configs"
WORKSPACE_DIR = PIPELINE_DIR / "workspace"

# Rate limiting for web requests
REQUEST_DELAY = 0.5  # seconds between requests

# ═══════════════════════════════════════════════════════════════════════════════
# Config
# ═══════════════════════════════════════════════════════════════════════════════

def load_config(domain: str) -> dict:
    path = CONFIGS_DIR / f"{domain}.yaml"
    if not path.exists():
        print(f"Config not found: {path}")
        sys.exit(1)
    return yaml.safe_load(path.read_text())


def ws(domain: str) -> Path:
    d = WORKSPACE_DIR / domain
    d.mkdir(parents=True, exist_ok=True)
    return d


# ═══════════════════════════════════════════════════════════════════════════════
# Claude CLI
# ═══════════════════════════════════════════════════════════════════════════════

def call_claude(prompt: str, images: list[Path] | None = None, timeout: int = 180) -> str | None:
    """Call Claude CLI in pipe mode."""
    full_prompt = prompt
    if images:
        existing = [str(img) for img in images if img.exists()]
        if existing:
            img_refs = "\n".join(existing)
            full_prompt = f"Look at these image files:\n{img_refs}\n\n{prompt}"

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", "claude-sonnet-4-6",
        "--dangerously-skip-permissions",
    ]

    try:
        result = subprocess.run(
            cmd, input=full_prompt, capture_output=True, text=True, timeout=timeout
        )
        if result.returncode != 0:
            print(f"  Claude error: {result.stderr[:200]}")
            return None
        data = json.loads(result.stdout)
        return data.get("result", "")
    except subprocess.TimeoutExpired:
        print("  Claude timeout")
        return None
    except Exception as e:
        print(f"  Claude exception: {e}")
        return None


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 1 — Crawl: fetch pages + images
# ═══════════════════════════════════════════════════════════════════════════════

def _slug(url_path: str) -> str:
    """Convert URL path to filesystem-safe slug."""
    return url_path.replace("/", "_").replace(".html", "").strip("_")


def _download_image(url: str, dest: Path, session: requests.Session) -> bool:
    """Download image to dest. Returns True on success."""
    if dest.exists() and dest.stat().st_size > 0:
        return True
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return True
    except Exception as e:
        print(f"    Failed to download {url}: {e}")
        return False


def _html_to_text_and_images(
    html: str, base_url: str, page_slug: str, images_dir: Path, session: requests.Session
) -> tuple[str, list[dict]]:
    """Parse HTML page, extract readable text and download images.

    Returns:
        (markdown_text, [{"filename": "...", "alt": "...", "caption": "..."}])
    """
    soup = BeautifulSoup(html, "lxml")

    # Remove nav, header, footer, sidebar
    for tag in soup.select("nav, header, footer, .sidebar, .sphinxsidebar, #table-of-contents, .toctree-wrapper"):
        tag.decompose()

    # Find the main content
    content = soup.select_one(".body, .document, main, article, #content")
    if not content:
        content = soup.body or soup

    images_info = []
    img_counter = 0

    # Process images
    for img in content.find_all("img"):
        src = img.get("src", "")
        if not src or src.startswith("data:"):
            continue
        # Skip tiny icons/badges
        width = img.get("width")
        if width and width.isdigit() and int(width) < 30:
            continue

        img_url = urllib.parse.urljoin(base_url, src)
        ext = Path(urllib.parse.urlparse(img_url).path).suffix or ".png"
        img_counter += 1
        filename = f"img_{img_counter:03d}{ext}"
        dest = images_dir / filename

        if _download_image(img_url, dest, session):
            alt = img.get("alt", "").strip()
            # Get caption from parent figure if exists
            caption = ""
            fig = img.find_parent("figure")
            if fig:
                cap = fig.find("figcaption")
                if cap:
                    caption = cap.get_text(strip=True)

            images_info.append({
                "filename": filename,
                "alt": alt,
                "caption": caption or alt,
                "original_src": src,
            })
            # Replace img tag with placeholder
            img.replace_with(f"[IMAGE:{filename}|{caption or alt}]")
        else:
            img.decompose()

    # Convert remaining HTML to markdown-ish text
    text = _soup_to_markdown(content)
    return text, images_info


def _soup_to_markdown(soup) -> str:
    """Simple HTML-to-markdown conversion for documentation pages."""
    lines = []

    for elem in soup.descendants:
        if elem.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(elem.name[1])
            text = elem.get_text(strip=True)
            if text:
                lines.append(f"\n{'#' * level} {text}\n")

        elif elem.name == "p":
            text = elem.get_text(separator=" ", strip=True)
            if text:
                lines.append(f"\n{text}\n")

        elif elem.name == "li":
            text = elem.get_text(separator=" ", strip=True)
            if text and not any(text in line for line in lines[-3:] if lines):
                lines.append(f"- {text}")

        elif elem.name in ("pre", "code"):
            # Only top-level code blocks
            if elem.name == "pre" or (elem.name == "code" and elem.parent.name == "pre"):
                text = elem.get_text()
                if text.strip() and elem.name == "pre":
                    lines.append(f"\n```\n{text.strip()}\n```\n")

        elif elem.name == "table":
            # Simple table extraction
            rows = elem.find_all("tr")
            for row in rows[:20]:  # limit table rows
                cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                if any(cells):
                    lines.append("| " + " | ".join(cells) + " |")

        elif elem.name == "dt":
            text = elem.get_text(strip=True)
            if text:
                lines.append(f"\n**{text}**")

        elif elem.name == "dd":
            text = elem.get_text(separator=" ", strip=True)
            if text:
                lines.append(f"  {text}")

    # Clean up
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def crawl_page(url: str, page_slug: str, work_dir: Path, session: requests.Session) -> dict | None:
    """Crawl a single documentation page. Returns page info dict or None."""
    cache_file = work_dir / "pages" / page_slug / "page.json"
    if cache_file.exists():
        return json.loads(cache_file.read_text())

    print(f"  Crawling: {url}")
    try:
        r = session.get(url, timeout=30)
        r.raise_for_status()
    except Exception as e:
        print(f"    Failed: {e}")
        return None

    page_dir = work_dir / "pages" / page_slug
    page_dir.mkdir(parents=True, exist_ok=True)
    images_dir = page_dir / "images"
    images_dir.mkdir(exist_ok=True)

    # Save raw HTML
    (page_dir / "raw.html").write_text(r.text, encoding="utf-8")

    # Extract text + images
    text, images = _html_to_text_and_images(r.text, url, page_slug, images_dir, session)

    # Extract title
    soup = BeautifulSoup(r.text, "lxml")
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else page_slug

    # Save extracted text
    (page_dir / "content.md").write_text(text, encoding="utf-8")

    page_info = {
        "url": url,
        "slug": page_slug,
        "title": title,
        "images": images,
        "text_length": len(text),
    }
    cache_file.write_text(json.dumps(page_info, indent=2), encoding="utf-8")

    time.sleep(REQUEST_DELAY)
    return page_info


def phase_crawl(config: dict, domain: str) -> list[dict]:
    """Phase 1: Crawl all configured documentation pages."""
    print("\n=== Phase 1: Crawl ===")
    work_dir = ws(domain)
    docs_cfg = config["sources"]["docs"]
    base_url = docs_cfg["base_url"]
    sections = docs_cfg.get("include_sections", [])

    # Check for cached results
    manifest = work_dir / "crawl_manifest.json"
    if manifest.exists():
        pages = json.loads(manifest.read_text())
        print(f"  Using cached crawl: {len(pages)} pages")
        return pages

    session = requests.Session()
    session.headers["User-Agent"] = "MMSkills-SkillGen/1.0"

    pages = []
    for section_path in sections:
        url = urllib.parse.urljoin(base_url, section_path)
        slug = _slug(section_path)
        page = crawl_page(url, slug, work_dir, session)
        if page:
            pages.append(page)

    manifest.write_text(json.dumps(pages, indent=2), encoding="utf-8")
    print(f"  Crawled {len(pages)} pages, {sum(len(p['images']) for p in pages)} images")
    return pages


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 2 — Organize: group pages into skill topics
# ═══════════════════════════════════════════════════════════════════════════════

def phase_organize(config: dict, domain: str, pages: list[dict]) -> dict:
    """Phase 2: Group crawled pages into skill categories and topics."""
    print("\n=== Phase 2: Organize ===")
    work_dir = ws(domain)
    taxonomy_file = work_dir / "docs_taxonomy.json"

    if taxonomy_file.exists():
        taxonomy = json.loads(taxonomy_file.read_text())
        print(f"  Using cached taxonomy: {len(taxonomy['categories'])} categories")
        return taxonomy

    app_name = config["app_name"]

    # Build page summaries for Claude
    page_summaries = []
    for p in pages:
        page_summaries.append(f"- [{p['slug']}] \"{p['title']}\" ({p['text_length']} chars, {len(p['images'])} images)")

    prompt = f"""You are organizing documentation pages for {app_name} into a skill taxonomy.

Here are the documentation pages that were crawled:
{chr(10).join(page_summaries)}

Group these pages into 5-10 skill categories. Each category should map to a coherent
area of the software's GUI (e.g., "Map Navigation", "Layer Management", "Data Editing").

For each category, list:
1. A short id (kebab-case, e.g., "layer-management")
2. A human name
3. A brief description of what GUI workflows this covers
4. Which page slugs belong to this category (a page can appear in multiple categories
   if it covers multiple topics)

Output ONLY valid JSON:
{{
  "categories": [
    {{
      "id": "category-id",
      "name": "Category Name",
      "description": "What this covers",
      "page_slugs": ["slug1", "slug2"]
    }}
  ]
}}"""

    result = call_claude(prompt, timeout=120)
    if not result:
        print("  ERROR: Claude failed to organize pages. Using flat structure.")
        taxonomy = {
            "categories": [
                {
                    "id": _slug(p["slug"]),
                    "name": p["title"],
                    "description": p["title"],
                    "page_slugs": [p["slug"]],
                }
                for p in pages
            ]
        }
    else:
        # Extract JSON from response
        match = re.search(r"\{[\s\S]*\}", result)
        if match:
            try:
                taxonomy = json.loads(match.group())
            except json.JSONDecodeError:
                print("  ERROR: Could not parse taxonomy JSON. Using flat structure.")
                taxonomy = {"categories": [{"id": p["slug"], "name": p["title"], "description": "", "page_slugs": [p["slug"]]} for p in pages]}
        else:
            taxonomy = {"categories": [{"id": p["slug"], "name": p["title"], "description": "", "page_slugs": [p["slug"]]} for p in pages]}

    taxonomy_file.write_text(json.dumps(taxonomy, indent=2), encoding="utf-8")
    print(f"  Created taxonomy: {len(taxonomy['categories'])} categories")
    return taxonomy


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 3 — Generate: create skill guides
# ═══════════════════════════════════════════════════════════════════════════════

def _collect_category_content(category: dict, work_dir: Path) -> tuple[str, list[Path]]:
    """Collect all text content and images for a category."""
    all_text = []
    all_images = []

    for slug in category["page_slugs"]:
        page_dir = work_dir / "pages" / slug
        content_file = page_dir / "content.md"
        if content_file.exists():
            text = content_file.read_text(encoding="utf-8")
            # Limit per-page text to avoid overwhelming the context
            if len(text) > 15000:
                text = text[:15000] + "\n\n[... content truncated ...]"
            all_text.append(f"--- Page: {slug} ---\n{text}")

        images_dir = page_dir / "images"
        if images_dir.exists():
            for img in sorted(images_dir.glob("*")):
                if img.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".webp"):
                    all_images.append(img)

    return "\n\n".join(all_text), all_images


def generate_text_skill(
    category: dict, config: dict, work_dir: Path, skills_root: Path
) -> Path | None:
    """Generate a text-only skill guide for a category."""
    app_name = config["app_name"]
    cat_id = category["id"]
    skill_dir = skills_root / cat_id
    guide_file = skill_dir / "guide.md"

    if guide_file.exists():
        print(f"    [text] {cat_id}: cached")
        return guide_file

    content, _ = _collect_category_content(category, work_dir)
    if not content:
        print(f"    [text] {cat_id}: no content")
        return None

    prompt = f"""You are writing a practical skill guide for {app_name} {config['app_version']}.

Topic: {category['name']}
Description: {category['description']}

Below is extracted documentation content. Synthesize it into a CONCISE, PRACTICAL guide
that helps someone perform GUI tasks in {app_name}. Focus on:

1. **Where things are**: exact menu paths (e.g., "Layer → Properties"), toolbar button names,
   panel locations, keyboard shortcuts
2. **Step-by-step workflows**: the most common operations, written as numbered steps
3. **UI landmarks**: describe what dialogs/panels look like so the reader can identify them
4. **Common pitfalls**: things that aren't obvious from the UI

Rules:
- Be concise. A guide should be 500-2000 words, not a textbook.
- Use markdown headers (## for sections, ### for subsections).
- Start with a one-line summary, then jump into practical content.
- Include keyboard shortcuts where available.
- Do NOT include image references — this is a text-only guide.
- Do NOT include a title header (# Title) — it will be added automatically.
- Write as practical reference, not tutorial prose.

Documentation content:
{content[:30000]}

Write the guide now:"""

    result = call_claude(prompt, timeout=180)
    if not result:
        print(f"    [text] {cat_id}: Claude failed")
        return None

    skill_dir.mkdir(parents=True, exist_ok=True)
    guide_file.write_text(result, encoding="utf-8")
    print(f"    [text] {cat_id}: generated ({len(result)} chars)")
    return guide_file


def generate_multimodal_skill(
    category: dict, config: dict, work_dir: Path, skills_root: Path
) -> Path | None:
    """Generate a multimodal skill guide with images for a category."""
    app_name = config["app_name"]
    cat_id = category["id"]
    skill_dir = skills_root / cat_id
    guide_file = skill_dir / "guide.md"

    if guide_file.exists():
        print(f"    [mm] {cat_id}: cached")
        return guide_file

    content, images = _collect_category_content(category, work_dir)
    if not content:
        print(f"    [mm] {cat_id}: no content")
        return None

    # Limit images to most relevant ones (max 15 per category)
    # Prefer images with captions/alt text
    scored_images = []
    for img in images:
        # Read the page.json to get image metadata
        page_slug = img.parent.parent.name
        page_json = work_dir / "pages" / page_slug / "page.json"
        caption = ""
        if page_json.exists():
            page_info = json.loads(page_json.read_text())
            for img_info in page_info.get("images", []):
                if img_info["filename"] == img.name:
                    caption = img_info.get("caption", "")
                    break
        scored_images.append((img, caption))

    # Sort: images with captions first, then by name
    scored_images.sort(key=lambda x: (not bool(x[1]), x[0].name))
    selected = scored_images[:15]

    if not selected:
        # Fall back to text-only
        print(f"    [mm] {cat_id}: no images, falling back to text")
        return generate_text_skill(category, config, work_dir, skills_root)

    # Copy selected images to skill dir and build reference list
    skill_dir.mkdir(parents=True, exist_ok=True)
    fig_refs = []
    for i, (img_path, caption) in enumerate(selected, 1):
        fig_name = f"fig{i:02d}{img_path.suffix}"
        dest = skill_dir / fig_name
        if not dest.exists():
            shutil.copy2(img_path, dest)
        fig_refs.append(f"- `{fig_name}`: {caption or 'UI screenshot'}")

    prompt = f"""You are writing a practical MULTIMODAL skill guide for {app_name} {config['app_version']}.

Topic: {category['name']}
Description: {category['description']}

You have {len(selected)} screenshots from the official documentation.
Available figures:
{chr(10).join(fig_refs)}

Below is extracted documentation content (with [IMAGE:filename|caption] markers showing
where screenshots appeared in the original docs).

Synthesize this into a CONCISE, PRACTICAL guide. Focus on:

1. **Where things are**: exact menu paths, toolbar buttons, panel locations, keyboard shortcuts
2. **Step-by-step workflows**: the most common operations as numbered steps
3. **UI landmarks**: describe what dialogs/panels look like
4. **Visual references**: where a screenshot helps identify a UI element, reference it like:
   Read the screenshot `fig01.png` in this directory — it shows the Layer Properties dialog

Rules:
- Be concise. 500-2000 words plus image references.
- Use markdown headers (## for sections, ### for subsections).
- Start with a one-line summary.
- Reference images using EXACTLY this format:
  Read the screenshot `figNN.png` in this directory — it shows [what it shows]
- Only reference figures from the list above. Don't invent figure numbers.
- Reference images at points where they genuinely help (showing a dialog, toolbar, panel).
- Do NOT include a title header (# Title).
- Do NOT use markdown image syntax (![](...)). Use the Read format above.

Documentation content:
{content[:30000]}

Write the multimodal guide now:"""

    result = call_claude(prompt, images=[img for img, _ in selected], timeout=240)
    if not result:
        print(f"    [mm] {cat_id}: Claude failed")
        return None

    guide_file.write_text(result, encoding="utf-8")

    # Clean up unused figures
    referenced = set(re.findall(r"fig\d+\.\w+", result))
    for f in skill_dir.glob("fig*"):
        if f.name not in referenced:
            f.unlink()

    print(f"    [mm] {cat_id}: generated ({len(result)} chars, {len(referenced)} figures)")
    return guide_file


def phase_generate(config: dict, domain: str, taxonomy: dict, parallel: int = 4):
    """Phase 3: Generate text and multimodal skill guides."""
    print("\n=== Phase 3: Generate ===")
    work_dir = ws(domain)
    app_slug = domain.replace("_", "-")

    text_root = MMSKILLS_ROOT / "skills" / f"{app_slug}-knowledge-text"
    mm_root = MMSKILLS_ROOT / "skills" / f"{app_slug}-knowledge-multimodal"

    categories = taxonomy["categories"]

    # Generate text skills
    print(f"\n  Generating text skills ({len(categories)} categories)...")
    with ThreadPoolExecutor(max_workers=parallel) as pool:
        futures = {
            pool.submit(generate_text_skill, cat, config, work_dir, text_root): cat["id"]
            for cat in categories
        }
        for fut in as_completed(futures):
            cat_id = futures[fut]
            try:
                fut.result()
            except Exception as e:
                print(f"    [text] {cat_id}: ERROR {e}")

    # Generate multimodal skills
    print(f"\n  Generating multimodal skills ({len(categories)} categories)...")
    with ThreadPoolExecutor(max_workers=parallel) as pool:
        futures = {
            pool.submit(generate_multimodal_skill, cat, config, work_dir, mm_root): cat["id"]
            for cat in categories
        }
        for fut in as_completed(futures):
            cat_id = futures[fut]
            try:
                fut.result()
            except Exception as e:
                print(f"    [mm] {cat_id}: ERROR {e}")


# ═══════════════════════════════════════════════════════════════════════════════
# Phase 4 — Index: generate SKILL.md files
# ═══════════════════════════════════════════════════════════════════════════════

def phase_index(config: dict, domain: str, taxonomy: dict):
    """Phase 4: Generate SKILL.md index files."""
    print("\n=== Phase 4: Index ===")
    app_name = config["app_name"]
    app_version = config["app_version"]
    app_slug = domain.replace("_", "-")

    for variant, label in [("text", "text"), ("multimodal", "multimodal")]:
        skills_root = MMSKILLS_ROOT / "skills" / f"{app_slug}-knowledge-{variant}"
        if not skills_root.exists():
            continue

        # Collect existing guides
        guides = []
        for cat in taxonomy["categories"]:
            guide = skills_root / cat["id"] / "guide.md"
            if guide.exists():
                guides.append((cat["id"], cat["name"], guide.relative_to(skills_root)))

        if not guides:
            continue

        desc = f"Comprehensive {app_name} {app_version} knowledge base"
        if variant == "multimodal":
            desc += " with visual screenshots from official documentation"

        content = f"""---
name: {app_slug}-knowledge-{variant}
description: {desc}
---

# {app_name} {app_version} — {label.title()} Knowledge Base

Practical skill guides for {app_name} {app_version}, covering GUI workflows,
menu paths, keyboard shortcuts, and common operations.

## Sections

"""
        for cat_id, cat_name, guide_path in guides:
            content += f"- [{cat_name}]({guide_path})\n"

        skill_md = skills_root / "SKILL.md"
        skill_md.write_text(content, encoding="utf-8")
        print(f"  {skill_md.relative_to(MMSKILLS_ROOT)}: {len(guides)} sections")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Generate skills from documentation")
    parser.add_argument("--domain", required=True, help="Domain name (matches config filename)")
    parser.add_argument("--phase", choices=["crawl", "organize", "generate", "index", "all"], default="all")
    parser.add_argument("--parallel", type=int, default=4)
    parser.add_argument("--recrawl", action="store_true", help="Force re-crawl (delete cached pages)")
    args = parser.parse_args()

    config = load_config(args.domain)
    print(f"Domain: {args.domain} ({config['app_name']} {config['app_version']})")

    if args.recrawl:
        manifest = ws(args.domain) / "crawl_manifest.json"
        if manifest.exists():
            manifest.unlink()
            print("  Cleared crawl cache")

    # Phase 1: Crawl
    if args.phase in ("crawl", "all"):
        pages = phase_crawl(config, args.domain)
    else:
        manifest = ws(args.domain) / "crawl_manifest.json"
        if manifest.exists():
            pages = json.loads(manifest.read_text())
        else:
            print("No crawl cache found. Run with --phase crawl first.")
            sys.exit(1)

    if args.phase == "crawl":
        return

    # Phase 2: Organize
    if args.phase in ("organize", "all"):
        taxonomy = phase_organize(config, args.domain, pages)
    else:
        tax_file = ws(args.domain) / "docs_taxonomy.json"
        if tax_file.exists():
            taxonomy = json.loads(tax_file.read_text())
        else:
            print("No taxonomy found. Run with --phase organize first.")
            sys.exit(1)

    if args.phase == "organize":
        return

    # Phase 3: Generate
    if args.phase in ("generate", "all"):
        phase_generate(config, args.domain, taxonomy, parallel=args.parallel)

    if args.phase == "generate":
        return

    # Phase 4: Index
    if args.phase in ("index", "all"):
        phase_index(config, args.domain, taxonomy)

    print("\nDone!")


if __name__ == "__main__":
    main()
