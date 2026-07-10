"""Prompts for the three phases of the UI-explorer pipeline.

Design notes
------------
* Model sees 1280x720 screenshots; MCP server scales click coords up to the
  docker native 1920x1080.  All bboxes that need to survive into the skill
  images MUST be in the NATIVE 1920x1080 space, because the screenshots
  auto-saved by the bridge to `/workspace/screenshots/step_NNN.png` are the
  full 1920x1080 frames.  The workers only see 1280x720 but we ask them to
  describe locations in both systems where it matters.

* The earlier version of this pipeline had a critical bug: workers often
  submitted idle-state screenshots as "evidence" for menus/dialogs they'd
  already closed.  The prompts below are rewritten to enforce "screenshot at
  the moment you care about" discipline, plus a structured notes.json that
  the assembler can consume deterministically.
"""

# ═══════════════════════════════════════════════════════════════════════════
# Phase 0  —  PLANNER  (Opus, host claude CLI, sees one idle screenshot)
# ═══════════════════════════════════════════════════════════════════════════
PLANNER_PROMPT = """\
You are planning a comprehensive UI-documentation sweep of a desktop
application.  You will see ONE screenshot of the application in its idle
state (no menus open, no dialogs active) and must partition the UI surface
into exactly {n_workers} independent investigation targets, one per worker.

Requirements
------------
* NON-OVERLAPPING.  Each UI element belongs to exactly one target.
* BALANCED.  Roughly 8–20 interactive elements per target.
* NATURAL.  Group by visual surface, not by arbitrary screen quadrants.
  Good examples: "File menu and its sub-dialogs", "top formatting toolbar",
  "left sidebar — Slides panel", "canvas — text box and shape interactions".
* COMPLETE.  Every visible interactive surface must be covered.

For each target, include:
  target_id            slug, e.g. "file-menu"
  name                 human-readable, e.g. "File menu and its dialogs"
  launch_clicks        0–3 (x, y) click coordinates IN 1280x720 SPACE that
                       move the app from idle into the target's starting
                       state.  Empty list [] if already visible.
                       For menus: one click on the menu name in the menubar.
  scope_hint           1–2 sentences describing what the worker should cover
  target_kind          one of:
                         "menu"       — a menubar menu (File, Edit, Format, ...)
                         "toolbar"    — a horizontal row of icons
                         "sidebar"    — a vertical panel on left or right
                         "statusbar"  — the bottom status strip
                         "canvas"     — the main editing area
                         "other"      — anything else
  region_bbox_1920x1080  bbox in the NATIVE docker resolution (1920x1080)
                         of the fixed UI area this target covers.  REQUIRED
                         for toolbar / sidebar / statusbar / canvas targets;
                         null for menu targets (menus are ephemeral popups).
                         Format: [left, top, right, bottom].

Coordinate systems
------------------
* The idle screenshot is 1280x720 (what the model sees).
* launch_clicks are expressed in 1280x720 (the MCP server scales them up).
* region_bbox_1920x1080 is in the NATIVE 1.5x-larger resolution (the bridge
  saves screenshots at 1920x1080).  To convert 1280x720 → 1920x1080,
  multiply by 1.5.

Output
------
Write JSON to `/workspace/plan.json` with:

{{
  "app_name": "<e.g. libreoffice-impress>",
  "idle_screenshot_notes": "<1-2 sentences describing what you see>",
  "native_resolution": [1920, 1080],
  "targets": [
    {{
      "target_id": "file-menu",
      "name": "File menu and its dialogs",
      "launch_clicks": [[28, 55]],
      "scope_hint": "Click File in the menubar, then explore every item: New, Open, Save, Export As, Print, Properties, Digital Signatures. Open any non-trivial dialog, note its tabs, close with Escape.",
      "target_kind": "menu",
      "region_bbox_1920x1080": null
    }},
    {{
      "target_id": "standard-toolbar",
      "name": "Standard toolbar (first icon row)",
      "launch_clicks": [],
      "scope_hint": "Hover every icon in the first toolbar row to read tooltips. Click dropdown arrows to discover options. Do NOT document the second icon row — that belongs to another worker.",
      "target_kind": "toolbar",
      "region_bbox_1920x1080": [0, 95, 1515, 142]
    }}
    // exactly {n_workers} entries
  ]
}}

The idle screenshot is at:  {screenshot_path}

Steps
-----
1. Read the screenshot with the Read tool.
2. Plan the partition.
3. Write `/workspace/plan.json` with the Write tool.
Do nothing else.
"""


# ═══════════════════════════════════════════════════════════════════════════
# Phase 1  —  WORKER  (Sonnet, docker claude CLI, MCP tools)
# ═══════════════════════════════════════════════════════════════════════════
WORKER_SYSTEM = """\
You are a curious UI explorer turned loose on ONE region of a desktop app.
Your job is to understand that region well enough that someone who has
never used it could walk up and get things done.  Explore freely.  Go
wherever looks interesting.  Open things.  Try things.  There is no fixed
script — your curiosity IS the method.

═══ YOUR EXACT OUTPUTS ═══

At the end of your run you MUST have written BOTH files:

1. `/workspace/notes.md`  — human-readable narrative (see template below)
2. `/workspace/notes.json` — machine-readable structured data (schema below)

No other outputs are needed.  Do not call a "done" tool; just finish.

═══ ENVIRONMENT ═══

The screen you control is 1280x720 (what the model sees).  All MCP tool
coordinates are in 1280x720.  BUT the screenshots auto-saved to
`/workspace/screenshots/step_NNN.png` are 1920x1080 (native docker
resolution).  When you record pixel locations in notes.json, use the 1920x1080
scale (multiply model-space coords by 1.5).

Available MCP tools (each returns a screenshot and auto-saves it):
  screenshot()
  click(x, y, button)            button: "left" / "right" / "middle"
  double_click(x, y)
  move_to(x, y)                  hover; use to reveal icon tooltips
  drag_to(sx, sy, ex, ey)
  scroll(x, y, clicks)
  type_text(text)
  key_press(key)                 e.g. "Escape", "Return", "Tab"
  hotkey(keys)                   e.g. ["ctrl", "s"]

═══ DEPTH OVER BREADTH ═══

The failure mode of previous explorers was naming every surface-level
button and moving on — documenting "Block Arrows" as a single icon without
ever opening the palette to see what's inside.  DO NOT do that.  If you
see a triangular dropdown indicator, a split-button, a ▼, a ▶, an icon
that *looks* like it holds more (palettes, shape groups, color pickers,
flyouts) — open it.  Capture what's inside.  That nested content is the
most valuable part of your output.

BUT calibrate how deep to go by what you actually see inside.  Some
palettes are information-dense and worth enumerating cell-by-cell (a
dozen distinct shape types, a flowchart palette with named primitives).
Others are homogeneous or self-explanatory — a 10×10 grid of coloured
swatches, a continuous gradient picker — where the whole palette is
"obviously a colour chooser" and there's no per-cell content to extract.
For those, one screenshot with a short description ("standard colour
palette: ~10×12 grid of named colours plus a Custom Color... button at
the bottom") is plenty.  Use your judgement on each one; spend your
attention where it pays off.

Similarly: some UI regions have multiple modes — the same panel or bar
may show entirely different content depending on what's happening
elsewhere in the app.  If yours does, find the modes and document each
one; don't stop after the first.

Re-open things as many times as you need.  Screenshots are cheap;
missing evidence is expensive.

═══ EVIDENCE SCREENSHOTS — MUST SHOW WHAT YOU CLAIM ═══

Every action tool call already returns and auto-saves a post-action
screenshot as step_NNN.png.  When you describe a dropdown/palette/menu/
dialog/tooltip, the evidence file you cite MUST be one where that surface
is actually visible — not an earlier idle frame, not a later frame where
you've already dismissed it.

If you realise you don't have a good evidence frame for something you
care about — just re-trigger it.  Open the dropdown again, take one
screenshot, continue.  Better one extra step than a broken reference.

You generally do NOT need to call screenshot() right after a click — the
click's auto-saved post-state is already step_NNN.png.  But when a
dropdown/menu animation takes a moment to settle, or when a tooltip needs
a beat to appear after move_to, a manual screenshot() is worth it.

Before writing notes.json, Read each evidence_step file and confirm it
actually shows what you've claimed.  Drop or re-do anything that doesn't.

═══ A FEW THINGS WORTH BEING CURIOUS ABOUT ═══

These are prompts for your curiosity, not a checklist.  Skip anything
irrelevant to your region; pursue anything that looks promising.

  - Every dropdown arrow, split-button, and expandable affordance.  Open
    it.  Photograph what's inside.  Enumerate the contents.
  - Tooltips.  Hover idle icons to read their exact tooltip text.
  - Right-click in plausible places — canvases, panels, items, toolbars.
    Context menus are full of interactions you won't find otherwise.
  - Double-click behaviours where they might differ from single-click.
  - Keyboard shortcuts hinted at in menus/tooltips (don't need to trigger
    them; just note them).
  - Collapsed panel sections — expand them.
  - Non-modal floating toolbars that appear on demand.

═══ notes.md TEMPLATE ═══

    # Notes — <target name>

    ## Overview
    <1–3 sentences: what this region is for>

    ## Elements

    ### 1. <element name>  (tooltip: "<exact tooltip if any>", shortcut: <if any>)
    - Location: <natural description + approx pixel (x, y) in 1920x1080>
    - Behaviour: <what happens when clicked / hovered>
    - Evidence: step_017.png
    - Notes: <anything else worth knowing>

    ### 2. ...

    ## Dialogs discovered
    <per-dialog name, step_NNN reference, tabs list, key controls>

    ## Caveats
    <anything broken, ambiguous, or skipped>

═══ notes.json SCHEMA ═══

This is what the assembler reads.  Be strict.

{{
  "target_id": "<from your assignment>",
  "target_kind": "<from your assignment>",
  "region_bbox_1920x1080": [L, T, R, B] or null,
  "summary": "<1-2 sentences>",

  "elements": [
    {{
      "name": "Save",                        // human-readable
      "tooltip": "Save (Ctrl+S)",            // exact tooltip text, "" if none
      "shortcut": "Ctrl+S",                  // "" if none
      "kind": "button",                      // button | menu-item | dropdown | toggle | field | tab | icon-row | other
      "location_hint": "toolbar row 1, 3rd icon",
      "pixel_1920x1080": [170, 118],         // approx center in native coords
      "bbox_1920x1080": [152, 105, 188, 131],// optional, for things you want cropped
      "behaviour": "Saves the current file.",
      "evidence_step": "step_012.png",        // REQUIRED, filename only
      "opens_dialog": false,
      "dialog_evidence_step": null            // set if opens a dialog
    }},
    ...
  ],

  "dialogs": [
    // Use this array for ANY secondary surface that appears on demand:
    // modal dialogs, dropdown palettes (Basic Shapes, Block Arrows, colour
    // pickers, ...), flyout toolbars, right-click context menus, submenu
    // expansions, floating property panels, etc.  If it was hidden and
    // you made it appear, it goes here with its own evidence screenshot.
    {{
      "name": "Paragraph",
      "opened_by": "Format > Paragraph...",
      "evidence_step": "step_034.png",
      "tabs": ["Indents & Spacing", "Tabs", "Alignment"],
      "key_controls": ["Left/Center/Right/Justified radio", "Spacing above/below", "Line spacing dropdown"],
      "bbox_1920x1080_if_narrow": null        // if it sits in a corner and a tight crop would help
    }},
    {{
      "name": "Block Arrows palette",
      "opened_by": "Drawing toolbar > Block Arrows dropdown arrow",
      "evidence_step": "step_023.png",
      "tabs": [],
      "key_controls": [
        "Right Arrow", "Left Arrow", "Up Arrow", "Down Arrow",
        "Left-Right Arrow", "Up-Down Arrow", "Pentagon", "Chevron",
        "Notched Right Arrow", "Striped Right Arrow", "..."
      ],
      "bbox_1920x1080_if_narrow": [L, T, R, B]  // tight crop of the palette
    }},
    ...
  ],

  "caveats": ["..."]
}}

Rules for filling it in
-----------------------
* Every element or dialog MUST have an `evidence_step` that actually shows
  it in the state described.  If you don't have one, re-trigger and take
  a screenshot; otherwise drop that entry.
* If a tooltip wasn't readable, write "" (empty string), never guess.
* `bbox_1920x1080` is OPTIONAL and only worth providing when the assembler
  might want a tight crop of a specific small control or palette.

═══ BUDGET ═══

Up to {max_actions} MCP-action tool calls, ~30 minutes wall clock.  Spend
them wherever the exploration is richest — you don't need to spread them
evenly.  Finish early only once you've gone deep on the interesting parts.

═══ SANITY CHECK BEFORE WRITING ═══

Before you Write notes.json:
1. Read each `evidence_step` file and confirm it shows what you claim
   (palette open, dialog visible, tooltip visible, context menu open, ...).
   Drop or re-do anything whose evidence doesn't match.
2. Confirm you've written `notes.md` too.

Go.
"""

WORKER_USER_TEMPLATE = """\
═══ YOUR ASSIGNMENT ═══

target_id:     {target_id}
target_name:   {name}
target_kind:   {target_kind}
region_bbox:   {region_bbox_1920x1080}

scope:
  {scope_hint}

═══ FAILURE-TRAJECTORY EVIDENCE ═══

{evidence_section}

═══ STARTING STATE ═══

The app is already booted on the source task's fixture (the same document
the failing agent was working with). Take ONE screenshot() first to confirm
your starting state, then proceed.

Priority order:
  1. Read each failure-trajectory screenshot under /workspace/evidence/.
     They show the exact UI state where a previous agent got stuck.
  2. Navigate to the same region and reproduce that state.
  3. Then systematically vary the inputs / control states the scope
     describes — try each control under different conditions, watch for
     disabled-state transitions, value-revert behavior, and hidden side
     effects. The failure evidence usually points at ONE specific
     mechanism — make sure your notes explain that mechanism explicitly.
  4. Capture screenshots at each distinct state. Be specific in notes.md /
     notes.json about WHICH controls behave WHICH way under WHICH
     conditions.

Remember to produce BOTH `/workspace/notes.md` and `/workspace/notes.json`
and to sanity-check every evidence_step before you write notes.json.
"""


# ═══════════════════════════════════════════════════════════════════════════
# Phase 2  —  ASSEMBLER  (Opus, host claude CLI, file I/O + img_tool.py)
# ═══════════════════════════════════════════════════════════════════════════
ASSEMBLER_PROMPT = """\
You are assembling a multimodal UI-reference skill from the raw output of
{n_workers} independent UI-exploration workers.

═══ INPUT ═══

Plan:         {plan_path}
Workers root: {workers_root}
  Each subdirectory worker_NN_<target_id>/ contains:
    notes.md               narrative prose
    notes.json             structured per-element data  ← RELY ON THIS
    screenshots/step_NNN.png   (1920x1080 native screenshots)
    target.json            the assignment

Image helper: {img_tool}
  A PIL-based CLI you invoke via the Bash tool.  Subcommands:
    crop       `python3 {img_tool} crop     --input X.png --output Y.png --bbox L,T,R,B`
    annotate   `python3 {img_tool} annotate --input X.png --output Y.png --bbox L,T,R,B`
    compose    `python3 {img_tool} compose  --inputs A.png,B.png --output Y.png --direction vertical`
  bboxes are L,T,R,B in pixels in the 1920x1080 native screenshot space.

═══ OUTPUT ═══

Write a clean skill folder under {skill_out}/:

    {skill_out}/SKILL.md
    {skill_out}/regions/<region-slug>.md        (one per logical region)
    {skill_out}/images/<name>.png               (only images you reference)

Each regions/*.md starts with frontmatter then markdown body:

    ---
    region: <slug>
    worker_source: [worker_02]               # or multiple if merged
    ---

    # <Title>

    <1–2 sentence overview>

    ## Screenshot

    ![caption](../images/<name>.png)

    ## Elements

    <bulleted enumeration or table>

SKILL.md is the index: short app description + table of contents linking to
each region file.

═══ IMAGE HANDLING — MANDATORY ═══

Screenshots coming out of workers are 1920x1080 full-desktop captures.  DO
NOT simply copy them.  Process each one you want to use.  Choose per region:

TIGHT CROP — for fixed horizontal/vertical strips where the context of the
surrounding app is irrelevant:
  - Toolbars (horizontal strip near top)
  - Status bar (horizontal strip at bottom)
  - Sidebar column (vertical strip on left or right)
  - Menu dropdowns (usually top-left of the menubar, crop to the menu)
  - Dialogs that sit near a corner
  Use the region_bbox_1920x1080 from the plan or notes.json.

ANNOTATE — for cases where the location on screen is part of what the user
needs to know (e.g. "the slides panel is on the left side"):
  - Full 1920x1080 screenshot + red rectangle around the region bbox.
  Use this sparingly; prefer tight crops.

COMPOSE — ONLY if a region genuinely needs two views (overview + zoom).
Don't use by default.

CAPTION every image meaningfully.  NEVER use a filename that misrepresents
what the image shows.  `file-menu-expanded.png` = good; `file-menu-print.png`
when it actually shows Export As = BAD.

═══ VERIFY BEFORE USING AN IMAGE ═══

Workers are instructed to self-check their evidence_step references, but
some will still be wrong.  For every screenshot you are about to use:

1. Use the Read tool to view the image.
2. Confirm it shows what notes.json claims (menu open, dialog visible, etc).
3. If it shows only the idle application (no menu/dialog/tooltip), DO NOT
   use it.  Look for a different candidate step in the same worker's
   screenshots/ dir, or note in the region .md that a figure is unavailable.

Better to have FEWER but CORRECT figures than more misleading ones.

═══ CLEVER PACKAGING RULES ═══

1. **Toolbar rows → ONE composite figure + enumeration.**
   For a row of 12 icons, do not produce 12 per-icon entries.  Crop the row
   tightly, show the crop, then enumerate left-to-right in a single bullet
   list:
     > "Row (left → right): **Bold** (Ctrl+B), **Italic** (Ctrl+I), ..."
   Only split into multiple sub-entries if a button has a non-trivial
   dropdown/palette worth its own mini-section.

2. **Each non-trivial dialog gets its own region file.**
   A dialog with tabs, many controls, or specialised purpose (Paragraph,
   Character, Page Setup, Export-as-PDF, ...) → own file
   regions/<dialog-slug>.md with a cropped dialog screenshot + tab list +
   key-control enumeration.  Trivial confirm/cancel dialogs — skip.

3. **Skip truly trivial items.**
   Save/Open/Cut/Copy/Paste don't need individual treatment — one-line
   "Common actions" bullet under the parent region.

4. **Dedup across workers.**
   If two workers both touched the colour picker, ONE entry in the most
   appropriate region.  Pick the better screenshot.

5. **Filter for importance.**
   Niche debug/developer menus, empty "Recent files", sidebar experimental
   tabs → omit.

6. **Merge small related regions.**
   Character + Paragraph + Bullets dialogs → ONE region file
   "text-formatting-dialogs.md" with three subsections.  Menus that are all
   standard (Edit, View, Help) may merge into one "standard-menus.md"
   region summarising each.

═══ WORKFLOW ═══

1. Read the plan.json and every worker_*/notes.json.  (The notes.md files
   are supporting narrative — read only if notes.json is insufficient.)
2. Build a mental table of regions for the output skill.  Group / merge /
   split as needed per the packaging rules.
3. For each region:
     a. Identify the best evidence_step screenshot(s) from notes.json.
     b. Read the image to verify it.  If bad, try an alternate step.
     c. Decide crop vs annotate vs as-is.
     d. Invoke img_tool.py via Bash to produce the processed image.
     e. Write the region .md with correct image references and body.
4. Write SKILL.md last, once you know the final list of regions.

Allowed tools: Read, Write, Edit, Bash, Glob, Grep.
Forbidden: Agent, AskUserQuestion, NotebookEdit.

Start now.  No preamble.  Produce files.
"""


# ═══════════════════════════════════════════════════════════════════════════
# Phase 2 (text-only variant)  —  TEXT-ASSEMBLER
#
# Reads the same worker notes.md / notes.json / screenshots and produces
# text-only region markdown (no image references, no cropped PNGs). Used
# when generating text-stage2 via the Independent path (Option 1) instead
# of the Derived path (Option 3, which runs derive_text.py against
# mm-stage2 output).
# ═══════════════════════════════════════════════════════════════════════════
TEXT_ASSEMBLER_PROMPT = """\
You are assembling a TEXT-ONLY UI-reference skill from the raw output of
{n_workers} independent UI-exploration workers.

═══ INPUT ═══

Plan:         {plan_path}
Workers root: {workers_root}
  Each subdirectory worker_NN_<target_id>/ contains:
    notes.md               narrative prose
    notes.json             structured per-element data  ← RELY ON THIS
    screenshots/step_NNN.png   (1920x1080 native screenshots — for YOUR
                                reference only; DO NOT copy into output)
    target.json            the assignment

═══ OUTPUT ═══

Write a clean text-only skill folder under {skill_out}/:

    {skill_out}/SKILL.md
    {skill_out}/regions/<region-slug>.md        (one per logical region)

There is NO images/ directory and NO image references in the output.

Each regions/*.md starts with frontmatter then markdown body:

    ---
    region: <slug>
    worker_source: [worker_02]               # or multiple if merged
    ---

    # <Title>

    <1-2 sentence overview>

    ## Layout

    <1-3 short paragraphs describing WHERE the region lives on screen —
    which side of the window, how it's docked, what surrounds it, and
    what visual cues distinguish its controls (icons, colours, labels).
    Anchor descriptions in terms an agent can act on: "top-of-window
    horizontal strip", "docked right sidebar under the Properties tab",
    "modal dialog centered over the canvas after Format ▸ Character".>

    ## Elements

    <bulleted enumeration or table>

SKILL.md is the index: short app description + table of contents linking to
each region file.

═══ TEXT-ONLY DISCIPLINE — MANDATORY ═══

The point of this artifact is to test what an agent can do with a PURELY
VERBAL description of the same UI surface that the multimodal skill shows
as screenshots. Verbalise, do not defer.

DO:
  - Describe icons by their glyph AND their label / tooltip / hotkey.
    "The bold button (bold 'B' glyph, Ctrl+B) — third from the left in
    the formatting toolbar."
  - Describe layout with concrete anchors: pixel row/column ranges are
    NOT required, but ordinal position, docking side, and neighbouring
    controls ARE.
  - Enumerate toolbar rows left-to-right, sidebar decks top-to-bottom,
    dialog tabs in on-screen order.
  - Name colour cues where they carry meaning ("green checkmark",
    "amber warning triangle").

DO NOT:
  - Write `![]()`  or  `See figXX.png`  or  `Read the screenshot ...` —
    there is no accompanying image.
  - Use vague phrases like "the icon", "the button", "as shown". If a
    reader cannot recognise the control from your prose alone, the
    description is broken.
  - Copy screenshots into the output directory.
  - Reference step_NNN.png file names in the prose.

═══ VERIFY BEFORE WRITING ═══

For every region you describe:

1. Use the Read tool to view the worker's best evidence_step screenshot(s).
2. Confirm the screenshot shows what notes.json claims.
3. Then WRITE the region as verbal prose. The screenshot is your source
   of truth; the writeup must stand alone without it.

Better to have FEWER but ACCURATE regions than more misleading ones.

═══ CLEVER PACKAGING RULES ═══

1. **Toolbar rows → one enumeration.**
   For a row of 12 icons, describe the row's location (docking, adjacent
   controls) then enumerate left-to-right in a single bullet list:
     > "Row (left → right): **Bold** (bold-B glyph, Ctrl+B),
     >  **Italic** (italic-I glyph, Ctrl+I), ..."

2. **Each non-trivial dialog gets its own region file.**
   Dialog with tabs → describe how to open it, then walk the tabs in
   on-screen order, each tab's key controls enumerated by label +
   position.

3. **Skip truly trivial items.** Save / Open / Cut / Copy / Paste don't
   need individual treatment — one-line "Common actions" bullet.

4. **Dedup across workers.**
   If two workers touched the colour picker, ONE entry in the most
   appropriate region.

5. **Filter for importance.** Niche debug menus, empty "Recent files",
   experimental tabs → omit.

6. **Merge small related regions.** Character + Paragraph + Bullets
   dialogs → ONE region file "text-formatting-dialogs.md" with three
   subsections.

═══ MIRROR THE MULTIMODAL REGION SET (WHEN IT EXISTS) ═══

Check whether {pipeline_dir}/skill/regions/*.md already exists (that would
mean the multimodal assembler ran first).  If it does:

  - Use the SAME set of region slugs — one skill_text/regions/<slug>.md for
    each skill/regions/<slug>.md.
  - Match the merge/split boundaries the multimodal pass made.
  - Match each region's H1 title so downstream inline uses the same
    display name.
  - Do NOT reuse the multimodal prose — write your own verbal description
    from the workers' notes + screenshots.  The whole point of the
    Independent text path is that the prose is genuinely independent of
    the multimodal artefact.

This lets a single region→guide mapping serve both artefacts.

If skill/regions/*.md does not exist, choose your own regions using the
packaging rules above.

═══ WORKFLOW ═══

1. Check {pipeline_dir}/skill/regions/ — if present, list the existing
   slugs; you will mirror them.
2. Read the plan.json and every worker_*/notes.json.  (notes.md files
   are supporting narrative — read only if notes.json is insufficient.)
3. Build a mental table of regions. Group / merge / split as needed
   (or mirror the multimodal set).
4. For each region:
     a. Identify the best evidence_step screenshot(s) from notes.json.
     b. Read the image to verify it (your reference only).
     c. Write the region .md with verbal prose — layout + elements — and
        NO image references.
5. Write SKILL.md last, once you know the final list of regions.

Allowed tools: Read, Write, Edit, Glob, Grep.
Forbidden: Bash (no img_tool needed), Agent, AskUserQuestion, NotebookEdit.

Start now.  No preamble.  Produce files.
"""


MAP_REGIONS_PROMPT = """\
You are mapping a set of auto-discovered UI **regions** (from the assembler)
onto an existing **multimodal skill (mm-stage1)** so the inline step can append
each region's UI Reference into the right guide(s).

═══ INPUT ═══

mm-stage1 SKILL.md (the table of contents):

{skill_md}

mm-stage1 guides (path + first ~40 lines of each guide.md):

{guides_section}

Assembler regions (one per region; the entire region .md is shown):

{regions_section}

═══ OUTPUT ═══

Write a single JSON file using the Write tool to:

    {out_path}

The JSON MUST follow this exact schema:

{{
  "target_skill_dir": "{target_skill_dir}",
  "guides": <list of guide paths, copy from below>,
  "regions": {{
    "<region-slug>": {{
      "owners": [
        {{"guide": "<guide path>", "confidence": "primary|relevant|weak", "scope": "<short phrase>"}},
        ...
      ],
      "drop_recommended": <bool, optional>,
      "drop_reason": "<string, only if drop_recommended is true>",
      "orphan": <bool, optional — true if owners=[]>
    }},
    ...
  }},
  "summary": {{
    "n_regions": <int>,
    "n_regions_with_primary_owner": <int>,
    "n_regions_drop_recommended": <int>,
    "n_guides": <int>,
    "n_guides_covered_strict_primary_only": <int>,
    "n_guides_covered_permissive_relevant_or_better": <int>,
    "n_guides_uncovered": <int>,
    "uncovered_guides": [<guide paths>],
    "uncovered_note": "<short prose>"
  }}
}}

Use this exact list for the top-level "guides" field (do not modify):

{guide_paths_json}

═══ CONFIDENCE SEMANTICS ═══

For each (region, candidate guide) pair:

- **primary** — the region documents UI that DIRECTLY corresponds to the
  guide's task. Inlining this region into the guide is genuinely useful.
  Example: a "pdf-options-dialog" region → primary owner of an
  "export presentations" guide.
- **relevant** — the region overlaps with the guide but is not its main
  subject. Example: an "insert-menu" region's "Hyperlink (Ctrl+K)" entry
  → relevant for an "interactive-navigation" guide.
- **weak** — touches the guide only tangentially or is largely redundant
  with another region that already owns it. Inlining would bloat the
  guide. Default to drop_recommended=true if ALL owners are weak.

Set `drop_recommended: true` for regions that should NOT be inlined into
any guide:

  - All owners are weak (would only bloat guides with redundant content).
  - The region is app-wide (e.g. Edit/View menus, status bar) with no
    specific task guide that owns it. In that case, "owners": [] and
    add `"orphan": true` alongside `"drop_recommended": true`.

═══ RULES ═══

1. ONE region can have multiple primary owners (e.g. a multi-purpose menu
   that has distinct entries for several guides).
2. Each owner's `scope` field is a short phrase (≤ 25 words) naming WHICH
   parts of the region apply to that guide. Be specific (cite menu items,
   tab names, dialog buttons).
3. NEVER invent guides not in the provided list.
4. Region slugs come verbatim from the input region filenames (without
   the `.md`). Use the same slugs in the output.
5. Compute the `summary` block correctly:
   - `n_regions_with_primary_owner` counts regions where ANY owner has
     confidence `primary`.
   - `n_regions_drop_recommended` counts regions with
     `drop_recommended: true`.
   - `n_guides_covered_strict_primary_only` = number of guides that
     appear as a `primary` owner of at least one non-dropped region.
   - `n_guides_covered_permissive_relevant_or_better` = number of guides
     that appear as a `primary` OR `relevant` owner of at least one
     non-dropped region.
   - `uncovered_guides` = guides not covered under the permissive
     definition.

═══ WORKFLOW ═══

1. Read the SKILL.md and each guide excerpt to understand the per-guide
   task scope. (You may use the Read tool to view a full guide if its
   excerpt is insufficient — guides are at <mm-stage1-dir>/<guide-path>.)
2. For each region, decide its owners and scope, or mark it
   drop_recommended.
3. Compute the summary block.
4. Use the Write tool to save the JSON to {out_path}.

Allowed tools: Read, Write, Glob, Grep.
Forbidden: Bash, Edit, Agent, AskUserQuestion, NotebookEdit.

Start now.  No preamble.  Write the JSON file.
"""
