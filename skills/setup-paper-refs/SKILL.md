---
name: setup-paper-refs
description: Search for reference papers by venue and topic, download them, convert to images, and save with annotations. Run this before format-paper. Requires paper-search and pdf-to-images MCP servers.
---

Search for reference papers (by venue and by topic) and save their page images for formatting analysis.

## Usage

```
/mmskills:setup-paper-refs
```

The main `.tex` file is auto-detected from `scripts/paper-beautify/workspace/` (the file containing `\documentclass`).

## MCP Tools Available

- **`paper-search`**: `search_papers`, `search_arxiv`, `download_paper`
- **`pdf-to-images`**: `pdf_to_images`, `pdf_page_count`

## Workflow

### Step 0: Parse the LaTeX file

Read the `.tex` file. Extract:
- Paper title and abstract (for topic)
- Target venue (from `\documentclass`, style files, or filename)

### Step 1: Clean assets

Remove all existing files from `skills/paper-beautify/assets/searched/`.

### Step 2: Search for ~20 papers

Run **4 parallel searches** — mix of venue-based and topic-based:

1. `search_papers` with venue name + year range (2023–2025)
2. `search_papers` with topic keywords from the paper
3. `search_arxiv` with venue-specific terms
4. `search_arxiv` with topic keywords

### Step 3: Select top 5–10

Pick a mix: some for **venue match** (same formatting), some for **topic match** (similar content/figures). Prefer papers with downloadable PDFs.

### Step 4: Download and convert to images

For each selected paper:
1. `download_paper` to `/tmp/mmskills_refs/`
2. `pdf_to_images` first 4 pages → PNGs to `skills/paper-beautify/assets/searched/`

### Step 5: Annotate

For each downloaded paper, write a companion `.md` file for its page images with:
- Paper title, venue, year
- What formatting elements are notable (layout, headings, figures, captions)

Example: for `colpali_page_1.png` through `colpali_page_4.png`, write `colpali.md`:
```
ColPali (TMLR 2024) — single-column layout, clean title block.
Uses booktabs tables, small caption font. Figures placed at top of page.
Good example of consistent heading spacing.
```

### Step 6: Generate index

Write `skills/paper-beautify/assets/searched/index.md` listing all papers with their annotations.

### Step 7: Report

- Which papers were downloaded (title, venue, year)
- How many page images saved
- Any failures
