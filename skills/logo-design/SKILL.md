---
name: logo-design
description: Design a logo using reference images as visual inspiration. Run setup-logo-refs first to populate assets. Requires image-gen MCP server.
---

Design a logo using reference images as visual inspiration.

**Prerequisites:** Run `setup-logo-refs` first to populate `assets/searched/`. Optionally add your own references to `assets/curated/`.

## Usage

```
/mmskills:logo-design <description>
```

**Arguments:**
- `$ARGUMENTS` — brief description (e.g., "a logo for MMSkills - an open-source toolkit for multimodal agent skills")

## MCP Tools Available

- **`image-gen`**: `generate_image`, `edit_image`

## Workflow

### Step 1: Analyze reference logos

First read `skills/logo-design/assets/curated/index.md` and `skills/logo-design/assets/searched/index.md` to understand what references are available and their annotations. Then:
- If **≤10 images** total: read all images with the Read tool (multimodal).
- If **>10 images**: based on the annotations, select the most relevant ones (prioritize curated, then pick searched images closest to the desired style/industry). Read only those.

Curated references always take priority as they reflect the user's taste. Analyze:

- **Shape language**: geometric vs. organic, symmetry, negative space
- **Color palette**: primary/accent colors, gradients vs. flat
- **Typography**: serif vs. sans-serif, weight, integration with icon
- **Style**: minimalist, detailed, abstract, literal, 3D, flat
- **Composition**: icon-only, text-only, icon+text, emblem

Synthesize a **design brief** summarizing the best patterns and ideas.

### Step 2: Infer design direction

From the user's description, infer:
- Appropriate colors, mood, and style
- What visual metaphors fit the product
- Whether icon+text or icon-only is better

Combine with the design brief from Step 1.

### Step 3: Generate logo

Use `generate_image` with:
- A detailed prompt combining the design brief + inferred direction
- Select 3–5 best reference images from `assets/curated/` and `assets/searched/` as style guidance
- Aspect ratio `1:1`
- Save to `skills/logo-design/assets/generated_logo.png`

### Step 4: Show and iterate

Read the generated logo and present it. Ask if the user wants changes. If so, use `edit_image` or `generate_image` with adjusted prompts. Save iterations as `generated_logo_v2.png`, `v3`, etc.

### Step 5: Report

- Show the final logo
- Summarize design choices and which references informed them
- Path to the final logo file
