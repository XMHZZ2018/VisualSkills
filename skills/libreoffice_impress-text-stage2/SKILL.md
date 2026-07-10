---
name: libreoffice_impress-multimodal-v1
description: "Practical with-screenshots guides for LibreOffice Impress 7.3.7. Consult via the load_topic MCP tool — it returns the guide text and every figure in one atomic call."
---

# LibreOffice Impress 7.3.7 Knowledge (multimodal-v1)

## How to consult this skill

This skill exposes two MCP tools (already registered for you):

- **`load_topic(topic)`** — returns the chosen topic's `guide.md` AND every figure (PNG) in that topic folder as one tool response. **Use this instead of `Read` for any `*.md` or `figXX.png` inside this skill.**
- **`list_topics()`** — returns every topic path available, one per line.

Each entry in the TOC below has the form `[Title](<topic>/guide.md)`. The `<topic>` part (the path before `/guide.md`) is what you pass to `load_topic`.

> You will receive the guide text plus the relevant figures in a single tool result — no extra `Read` calls needed.

**Rules:**

1. Before any GUI action where you are unsure of the menu path / dialog / icon, find the matching topic in the TOC and call `load_topic` first.
2. You may call `load_topic` **at any step** of the trajectory, not only at the start. If the task moves into a new area, call `load_topic` again for the new area.
3. Do **not** issue separate `Read` calls for `figXX.png` files inside this skill — they are delivered by `load_topic` automatically.

## Guides

### Setup & Export

- [Window Setup](setup-and-export/window-setup/guide.md) — How to focus, maximize, and prepare the LibreOffice Impress application window
  - **Use when:** toggling Slides pane and Sidebar visibility, switching Workspace views in Impress, customizing toolbars per view, changing User Interface variant, maximizing editing area with Hide/Show marker, disabling template chooser on startup
- [PDF Export](setup-and-export/pdf-export/guide.md) — How to export a presentation to PDF format with quality settings
  - **Use when:** exporting slides as PDF, setting JPEG compression and image resolution, creating hybrid PDF with embedded ODF, exporting tagged PDF for accessibility, exporting PDF/A archival format, emailing presentation as PDF

### Presentation Structure

- [Create Presentation](presentation-structure/create-presentation/guide.md) — How to create a new multi-slide presentation from scratch or from an outline
  - **Use when:** creating a new presentation, adding and duplicating slides, choosing slide layouts, converting Writer outline to presentation, reordering slides in Slide Sorter, changing slide background
- [Slide Management](presentation-structure/slide-management/guide.md) — How to add, duplicate, reorder, consolidate, or remove slides
  - **Use when:** adding new slides, duplicating slides, reordering slides via drag-and-drop, inserting slides from another file, expanding slide content, creating a summary slide, renaming and deleting slides
- [Master Slides](presentation-structure/master-slides/guide.md) — How to apply master slide designs and templates to specific slides
  - **Use when:** applying master slides to all or selected slides, loading master slides from templates, creating custom master slides, editing master slide properties, clearing direct formatting to revert to master style, changing slide master design
- [Slide Dimensions](presentation-structure/slide-dimensions/guide.md) — How to change slide size, aspect ratio, and orientation
  - **Use when:** changing slide size, setting slide aspect ratio, switching slide orientation, custom slide dimensions, Slide Properties dialog, Sidebar slide format

### Text & Content

- Find & Replace — *(not yet generated)*
- [Text Correction & Language](text-and-content/text-correction/guide.md) — How to fix typos, spelling errors, and set language/locale for text spans
  - **Use when:** spell checking and red wavy underlines, AutoCorrect options and replacement table, setting default language and locale, per-text-span language assignment, Format Character language dropdown, Tools AutoCorrect Options tabs
- [Bullet Formatting](text-and-content/bullet-formatting/guide.md) — How to customize bullet characters, colors, and list styles
  - **Use when:** formatting bullets in Impress, creating ordered and unordered lists, changing bullet styles via gallery, Bullets and Numbering dialog settings, adjusting list indent levels, reordering list items
- [Text Box Formatting](text-and-content/text-box-formatting/guide.md) — How to style text boxes with fonts, backgrounds, and borders for code blocks or special content
  - **Use when:** create text box, format font and character properties, set text box background fill, add border with rounded corners, position and size text box, style code block on slide

### Shapes & Diagrams

- [Diagram Creation](shapes-and-diagrams/diagram-creation/guide.md) — How to create flowcharts, architecture diagrams, process diagrams, and funnel diagrams using shapes and connectors
  - **Use when:** inserting flowchart shapes, drawing and routing connectors, adding custom glue points, using Drawing toolbar sub-toolbars, building funnel diagrams, grouping diagram objects
- [Shape Formatting](shapes-and-diagrams/shape-formatting/guide.md) — How to recolor, rotate, and transform existing shapes on slides
  - **Use when:** formatting shape fill and area, formatting lines and borders, rotating objects precisely, flipping shapes, distorting shapes in perspective, Area and Line dialog settings

### Tables & Data

- [Table Insertion](tables-and-data/table-insertion/guide.md) — How to insert a data table into a slide and populate it with structured data
  - **Use when:** inserting a table in Impress, Table Design panel styles, Table Properties dialog formatting, adding or deleting rows and columns, merging and splitting cells, Table toolbar options
- [Table Creation & Formatting](tables-and-data/table-formatting/guide.md) — How to create a comparison table with aligned text and conditional cell coloring
  - **Use when:** inserting a table in Impress, aligning text in table cells, applying Table Design styles, manual conditional cell coloring, customizing table borders, merging and resizing table cells

### Images & Objects

- [Image Layout & Composition](images-and-objects/image-layout/guide.md) — How to align, distribute, group, rotate, and arrange images on a slide
  - **Use when:** aligning objects on slides, grouping and ungrouping images, rotating and flipping objects, arranging stack order, Position and Size dialog, configuring snap to grid
- [Image Embedding](images-and-objects/image-embedding/guide.md) — How to convert linked external images to embedded images within the presentation
  - **Use when:** inserting images in Impress, embedding vs linking images, Insert as Link checkbox, converting linked image to embedded, Insert > Image dialog, portable self-contained presentations
- [Math Equations](images-and-objects/math-equations/guide.md) — How to insert mathematical formula OLE objects using the LibreOffice Math editor
  - **Use when:** inserting formula objects in slides, editing math equations in Impress, adjusting formula font size, changing formula typeface, positioning formula objects on slides

### Animations & Interactivity

- [Transitions & Animations](animations-and-interactivity/transitions-and-animations/guide.md) — How to add slide transitions and object animation effects
  - **Use when:** adding slide transitions, setting transition duration and variant, playing background music during slideshow, animating slide objects, configuring animation effect options and timing, reordering or removing animations
- [Hyperlinks & Navigation](animations-and-interactivity/hyperlinks-and-navigation/guide.md) — How to create interactive buttons with hyperlinks for slide-to-slide navigation
  - **Use when:** inserting hyperlinks with Ctrl+K, linking to slides within a presentation, setting up interaction buttons on objects, disabling automatic URL recognition, changing hyperlink colors in Application Colors, navigating slides during slideshow
- [Slideshow Configuration](animations-and-interactivity/slideshow-configuration/guide.md) — How to configure automatic slide advancement, looping, and kiosk-style playback with custom orientation
  - **Use when:** setting slideshow range and starting slide, configuring kiosk loop and repeat, setting automatic slide advance timing, rehearsing slide timings, running slideshow in window mode, using Presenter Console with dual monitors

