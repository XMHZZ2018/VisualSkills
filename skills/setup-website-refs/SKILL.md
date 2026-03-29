---
name: setup-website-refs
description: Search for similar personal academic websites, screenshot them, and save the best as references. Run this before website-beautify. Requires web-screenshot MCP server.
---

Search for similar personal academic websites, screenshot them, and save the best as references.

## Usage

```
/mmskills:setup-website-refs <your_website_url>
```

**Arguments:**
- `$ARGUMENTS` — your website URL (e.g., `https://yourname.github.io`)

## MCP Tools Available

- **`web-screenshot`**: `screenshot_url`, `screenshot_urls`

## Workflow

### Step 1: Screenshot and analyze your website

Use `screenshot_url` to capture your current website. Read the screenshot with the Read tool (multimodal). Extract:
- Your name, research area, affiliation
- Field and subfield (e.g., CS / AI / NLP)
- Current design style

### Step 2: Clean assets

Remove all existing files from `skills/website-beautify/assets/searched/`.

### Step 3: Search for ~20 similar personal websites

Use WebSearch with **3–4 parallel searches**:

1. `"<research area> researcher personal website github.io"`
2. `"<field> professor homepage"`
3. `"best academic personal website computer science AI"`
4. `"<specific subfield> researcher site:github.io OR site:netlify.app"`

Collect ~20 candidate URLs.

### Step 4: Screenshot all candidates

Use `screenshot_urls` to capture all candidates, saving to `/tmp/mmskills_websites/`.

### Step 5: Judge and select top 10

Read each screenshot with the Read tool (multimodal). Score on:

- **Visual design**: clean, modern, professional
- **Layout**: logical structure, good use of space
- **Typography**: readable, consistent
- **Content organization**: easy to find publications, projects, contact
- **Personality**: distinctive but professional

Delete the bottom ones, copy **top 10** to `skills/website-beautify/assets/searched/`.

For each kept screenshot, write a companion `.md` file with:
- Website URL and researcher name/field
- What makes the design good
- Specific elements worth borrowing

Example: for `screenshot_3.png`, write `screenshot_3.md`:
```
jonbarron.info — Jon Barron, Google Research / Computer Vision.
Clean single-page layout, publication list with thumbnail previews.
Elegant dark theme, great use of whitespace. Worth borrowing the pub layout.
```

### Step 6: Generate index

Write `skills/website-beautify/assets/searched/index.md` listing all kept websites with their annotations.

### Step 7: Report

- How many reference websites saved
- Common design patterns observed
