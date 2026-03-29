---
name: setup-logo-refs
description: Search for reference logos online, download the best ones, and save them with annotations. Run this before logo-design. Requires image-search MCP server.
---

Search for reference logos, save them with annotations for visual analysis.

## Usage

```
/mmskills:setup-logo-refs <description>
```

**Arguments:**
- `$ARGUMENTS` — brief description (e.g., "a logo for MMSkills - an open-source toolkit for multimodal agent skills")

## MCP Tools Available

- **`image-search`**: `search_images`, `download_image`

## Workflow

### Step 1: Infer design context

From the description, infer:
- What the product/project does
- Industry / domain (e.g., AI, developer tools, open-source)
- Likely style direction (e.g., tech = minimalist/geometric, creative = playful/colorful)
- Similar well-known products whose logos are worth referencing

### Step 2: Clean searched assets

Remove all existing files from `skills/logo-design/assets/searched/`.

### Step 3: Search for ~20 reference logos

Run **4 parallel searches** mixing different angles:

1. Logos of similar/competing products (e.g., "Hugging Face logo", "LangChain logo")
2. Style-based search (e.g., "minimalist AI developer tool logo")
3. Industry search (e.g., "open source machine learning project logo")
4. Design inspiration (e.g., "best tech startup logos 2024 minimalist")

### Step 4: Download top 15–20

Use `download_image` to save results to `skills/logo-design/assets/searched/`.

### Step 5: Judge, annotate, and keep top 10

Read each downloaded image with the Read tool (multimodal). Score on:
- Visual quality (clean, professional, not blurry/low-res)
- Relevance to the product's domain
- Design quality (memorable, works at small sizes, balanced)

Delete the bottom ones, keep **top 10**.

For each kept image, write a companion `.md` file with 1–3 sentences:
- What the logo depicts
- What makes it effective or relevant
- Any design elements worth borrowing

Example: for `openai_avatar.jpg`, write `openai_avatar.md`:
```
OpenAI logo — a minimal geometric knot/flower shape.
Strong use of negative space, works at any size.
The abstract form suggests intelligence without being literal.
```

### Step 6: Generate index

Write `skills/logo-design/assets/searched/index.md` listing all kept images with their annotations:

```markdown
# Searched References

## openai_avatar.jpg
OpenAI logo — a minimal geometric knot/flower shape. Strong use of negative space...

## pytorch_avatar.jpg
PyTorch logo — a flame icon in orange. Simple, recognizable...
```

### Step 7: Report

- How many reference logos saved
- Summary of dominant design patterns observed
