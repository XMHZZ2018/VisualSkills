---
name: website-beautify
description: Improve a personal website by learning from reference screenshots of similar sites. Run setup-website-refs first. Requires web-screenshot MCP server.
---

Improve your personal website using reference screenshots.

**Prerequisites:** Run `setup-website-refs` first to populate `assets/searched/`. Optionally add your own references to `assets/curated/`.

## Usage

```
/mmskills:website-beautify <local_repo_path>
```

**Arguments:**
- `$ARGUMENTS` — local path to the website git repo

## MCP Tools Available

- **`web-screenshot`**: `screenshot_url`

## Workflow

### Step 1: Analyze reference screenshots

First read `skills/website-beautify/assets/curated/index.md` and `skills/website-beautify/assets/searched/index.md` to understand what references are available and their annotations. Then:
- If **≤10 images** total: read all images with the Read tool (multimodal).
- If **>10 images**: based on the annotations, select the most relevant ones (prioritize curated, then pick searched screenshots with the best design scores). Read only those.

Curated references always take priority as they reflect the user's taste. Analyze:

- Color schemes (dark vs. light, accent colors)
- Layout patterns (sidebar, hero section, card-based)
- Section ordering and content types
- Navigation style
- Special features (publication filters, project cards, timeline)
- Typography choices

Synthesize a **design brief** of the best patterns.

### Step 2: Read the current website code

Read the HTML/CSS/JS files from the local repo. Understand the current structure and what can be improved.

### Step 3: Apply improvements

Edit the files using the Edit tool:
- Layout and structure changes
- CSS updates (colors, typography, spacing)
- New sections or reorganized content
- Responsive design improvements

Preserve all existing content — only change presentation and structure.

### Step 4: Preview

Serve the site locally and take a screenshot for preview:

```bash
# Start a local server in the background
cd <local_repo_path> && python3 -m http.server 8888 &
```

Use `screenshot_url` on `http://localhost:8888` to capture the updated site, saving to `scripts/website-beautify/workspace/preview.png`.

Kill the server after:
```bash
kill %1
```

Read the preview screenshot and do a final visual check.

### Step 5: Report

Write a `CHANGES.md` in the repo with:
- Changes made and why
- Which reference websites inspired each change

Output:
- Paths to changed files
- Preview screenshot at `scripts/website-beautify/workspace/preview.png`

Do NOT push to remote. The user will review the preview first.

## Notes

- Never remove or alter the user's content (bio, publications, etc.)
- Preserve existing links and URLs
- Keep the site deployable on GitHub Pages
