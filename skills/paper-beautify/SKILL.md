---
name: format-paper
description: Format a LaTeX paper by analyzing reference page images to match the target venue's style. Run setup-paper-refs first. Requires pdf-to-images MCP server.
---

Format a LaTeX paper by analyzing reference page images.

**Prerequisites:** Run `setup-paper-refs` first to populate `assets/searched/`. Optionally add your own references to `assets/curated/`.

## Usage

```
/mmskills:format-paper
```

The main `.tex` file is auto-detected from `scripts/paper-beautify/workspace/` (the file containing `\documentclass`).

## Workflow

### Step 1: Load reference images

First read `skills/paper-beautify/assets/curated/index.md` and `skills/paper-beautify/assets/searched/index.md` to understand what references are available and their annotations. Then:
- If **≤10 images** total: read all images with the Read tool (multimodal).
- If **>10 images**: based on the annotations, select the most relevant ones (prioritize curated, then pick searched images that best match the input paper's venue/topic). Read only those.

Curated references always take priority as they reflect the user's taste. Analyze:

- Column layout, font size, line spacing, margins
- Title block: font weight, author layout, abstract style
- Section headings: numbering, capitalization, spacing
- Figures/tables: caption position, font style
- References: font size, citation style

**Synthesize a formatting profile** of dominant conventions.

### Step 2: Parse the input LaTeX file

Read the `.tex` file. Extract:
- Overall structure: sections, packages used, figure/table count
- Target venue (from `\documentclass` or style files)

### Step 3: Diagnose and apply

Compare input `.tex` against the formatting profile. Apply fixes with the Edit tool:
- Margin/spacing adjustments
- Missing packages (`microtype`, `booktabs`, `caption`, etc.)
- Figure placement, caption formatting
- Heading styles, bibliography style

Only make changes **supported by visual evidence**. Never modify paper content.

### Step 4: Compile and verify

```bash
pdflatex -interaction=nonstopmode -output-directory <output_dir> <latex_file>
bibtex <output_dir>/<basename> 2>/dev/null || true
pdflatex -interaction=nonstopmode -output-directory <output_dir> <latex_file>
pdflatex -interaction=nonstopmode -output-directory <output_dir> <latex_file>
```

If compilation fails, read `.log`, fix, retry (max 3 attempts).

Use `pdf_to_images` on output PDF (first page) and Read for a final visual sanity check.

### Step 5: Write summary and report

Write a `CHANGES.md` file to `scripts/paper-beautify/workspace/` with:
- List of every formatting change made (what, where, why)
- Which reference papers informed each change
- Any warnings or unresolved issues

Then output:
- Path to output PDF
- Path to `CHANGES.md`

## Notes

- Never modify paper **content** (text, equations, citations).
- If venue uses a required `.cls` file, don't replace it — only add compatible packages.
- Prefer reversible edits. If unsure, comment out alternatives.
