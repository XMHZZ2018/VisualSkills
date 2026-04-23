"""Prompts for the three phases of the UI-explorer pipeline.

No prior skill context is loaded anywhere.  Each prompt is self-contained.
"""

# ═══════════════════════════════════════════════════════════════════════════
# Phase 0  —  PLANNER  (Opus, host claude CLI, sees one idle screenshot)
# ═══════════════════════════════════════════════════════════════════════════
PLANNER_PROMPT = """\
You are planning a comprehensive UI-documentation sweep of a desktop application.

You will see ONE screenshot of the application in its idle state (no menus
open, no dialogs active).  Your job is to produce a plan that partitions the
visible UI surface into exactly {n_workers} independent "investigation targets".
Each target will then be handed to a separate worker agent that will freely
click around inside it to discover and describe every interactive element.

The targets must be:
  - NON-OVERLAPPING.  Each UI element belongs to exactly one target.
  - BALANCED.  Try to give each worker a comparable amount of material
    (roughly 8–20 interactive elements to investigate).
  - NATURAL.  Group by visual surface, not by arbitrary screen quadrants.
    Good examples of a single target: "File menu and its sub-dialogs",
    "top formatting toolbar", "left sidebar — Slides panel",
    "canvas — text box and shape interactions".
  - COMPLETE.  Every visible interactive surface must be covered by some
    target.  Don't leave anything out.

For menus: assign one worker per menu (File, Edit, Format…) unless some menus
are very small — in that case bundle them into one "misc menus" target.

For each target, provide a short `launch_clicks` list of (x, y) click
coordinates (0–3 clicks) that take the app from its idle state into the state
where the target is visible.  If the target is already visible in the idle
screenshot (e.g. a toolbar), launch_clicks can be an empty list [].
For menus, launch_clicks is a single click on the menu name in the menubar.

Look carefully at the screenshot.  Identify menus in the menubar, toolbars,
sidebars, status bars, and the main canvas.  Use pixel coordinates accurate to
~10 pixels.

Write your result as JSON to `/workspace/plan.json` using the Write tool.
Schema:

{{
  "app_name": "<e.g. libreoffice-impress>",
  "idle_screenshot_notes": "<1-2 sentences describing what you see>",
  "targets": [
    {{
      "target_id": "file-menu",
      "name": "File menu and its dialogs",
      "launch_clicks": [[42, 51]],
      "scope_hint": "Click File in menubar, then explore every item: New, Open, Save, Export, Print, Properties, etc.  Note what each does."
    }},
    ... (exactly {n_workers} entries)
  ]
}}

The idle screenshot is at: `{screenshot_path}`
Read it first with the Read tool, then write plan.json.  Do not do anything
else.
"""


# ═══════════════════════════════════════════════════════════════════════════
# Phase 1  —  WORKER  (Sonnet, docker claude CLI, MCP tools)
# ═══════════════════════════════════════════════════════════════════════════
#
# Injected into the claude CLI container as /workspace/prompt.txt.  The CLI
# invokes this via `claude -p "$PROMPT"`.  Screenshots are auto-saved by the
# bridge to /workspace/screenshots/step_NNN.png, so the worker only needs to
# write /workspace/notes.md describing everything it found.

WORKER_SYSTEM = """\
You are a UI-documentation worker exploring a single region of a desktop
application.  Your GOAL is to produce a complete inventory of the interactive
elements in your assigned region, so that later a human writer can build a
reference skill from your notes.

The screen resolution is 1280x720.  You interact with the GUI through MCP tools:

  - screenshot()
  - click(x, y, button)         button is "left" / "right" / "middle"
  - double_click(x, y)
  - move_to(x, y)               hover without clicking — USE THIS to reveal
                                 tooltip names of icon-only toolbar buttons
  - drag_to(start_x, start_y, end_x, end_y)
  - scroll(x, y, clicks)
  - type_text(text)
  - key_press(key)              e.g. "Escape", "Return", "Tab"
  - hotkey(keys)                e.g. ["ctrl", "s"], ["alt", "F4"]

Every action tool returns a screenshot after execution.  The bridge
automatically saves every screenshot to /workspace/screenshots/step_NNN.png.
You do NOT need to save screenshots yourself.

═══ HOW TO EXPLORE ═══

1.  Start with a fresh screenshot() to see where you are.
2.  For your assigned region, systematically uncover every interactive element:
      - For menus: click the menu, read each item, hover submenus, open any
        dialog that looks non-trivial (examine its tabs / controls), then
        close it with Escape and try the next item.
      - For toolbars: move_to every icon to read its tooltip.  Click
        dropdown arrows to see their options.  For icon-only buttons whose
        tooltip you can't read, click once to observe the effect, then
        undo (Ctrl+Z) or close any dialog that appears.
      - For sidebars: scroll through them, expand every collapsible section,
        hover every icon.
      - For canvases: try right-click for context menus, drag to select,
        draw a shape or text box if the tool allows it, and examine any
        handles / resize grips that appear.
3.  Between probing elements, return to your region's idle state (Escape to
    close dialogs / menus).  If the app is stuck, try Escape a few times.
4.  If you trigger a destructive change (unwanted file creation, modified
    document), do your best to undo it with Ctrl+Z — but don't obsess; the
    environment will be reset after you finish.

═══ HOW TO WRITE NOTES ═══

As you go, keep a running NOTES buffer.  At the END of your exploration,
use the Write tool to save it to `/workspace/notes.md` with this structure:

    # Notes — <target name>

    ## Overview
    <1–3 sentences: what this region is for, what surfaces it contains>

    ## Elements

    ### 1. <element name>  (tooltip: "<exact tooltip if any>")
      - Location: toolbar-row-1, 3rd icon from left.  pixel ~(180, 92).
      - Behaviour: <what happened when you clicked / hovered>
      - Evidence: see step_017.png (after-click) and step_018.png (dialog).
      - Notes: <anything a reader might want to know — modifier-key
               variants, typical use, tabs inside dialog, etc.>

    ### 2. ...

    ## Dialogs discovered
    <list each dialog you opened, with step_NNN refs to its screenshot,
     and a short enumeration of its tabs / key controls>

    ## Caveats
    <anything that broke, was ambiguous, or you couldn't test>

Be thorough but efficient.  Aim for one NUMBERED ENTRY per distinct
interactive element.  If two elements are identical (e.g. 12 colour swatches
in a palette), summarise as ONE entry: "palette of 12 colour swatches".

═══ BUDGET ═══

You have up to {max_actions} action tool calls, and roughly 20 minutes of
wall-clock time.  Finish early if you've covered everything.  Do NOT waste
actions re-exploring areas outside your assigned region.

When you are done, Write `/workspace/notes.md` and stop.  Do not signal
completion any other way.
"""

WORKER_USER_TEMPLATE = """\
═══ YOUR ASSIGNMENT ═══

target_id:   {target_id}
target_name: {name}

scope:
  {scope_hint}

You are ALREADY positioned at your starting state (any necessary pre-click
navigation has been performed before this agent started).  Take a screenshot
first to confirm, then explore.

Remember: produce `/workspace/notes.md` at the end.  Go.
"""


# ═══════════════════════════════════════════════════════════════════════════
# Phase 2  —  ASSEMBLER  (Opus, host claude CLI, file I/O only)
# ═══════════════════════════════════════════════════════════════════════════
ASSEMBLER_PROMPT = """\
You are assembling a multimodal UI-reference skill from the raw notes of
{n_workers} independent UI-exploration workers.

═══ INPUT ═══

Under {workers_root}/ you will find:
    worker_0/notes.md   + worker_0/screenshots/step_NNN.png
    worker_1/notes.md   + worker_1/screenshots/step_NNN.png
    ...

Under {plan_path} you have the plan.json that originally assigned each worker
their region.

═══ OUTPUT ═══

Write a clean skill folder under {skill_out}/ with this layout:

    {skill_out}/SKILL.md
    {skill_out}/regions/<region-slug>.md       (one per logical region)
    {skill_out}/images/<slug>.png              (only images you use)

Every regions/*.md file should start with frontmatter:

    ---
    region: <slug>
    worker_source: [worker_2]                  # or multiple if merged
    ---

    # <Human-readable region title>

    <1–2 sentence overview>

    ## Screenshot

    ![overall](../images/<slug>-overall.png)

    ## Elements

    <either a table or a bulleted enumeration>

SKILL.md should have the overall index — short description of the app, a
table of contents linking to each regions/*.md.

═══ CLEVER PACKAGING RULES ═══

1.  **Toolbar rows → ONE composite figure.**
    If a worker documented a row of 12 toolbar icons, do NOT produce 12
    per-icon entries.  Instead:
      - Copy the worker's best full-row screenshot into images/.
      - If the row is mixed in with other UI, use the Bash tool with the
        `sips` command (macOS) or simply reference the worker screenshot
        as-is with coordinates noted in the markdown caption.
      - Write the entry as a left-to-right enumeration:
          > "Row (left → right): **Bold** (Ctrl+B), **Italic** (Ctrl+I),
          >  **Underline**, font color, highlight color, …"

2.  **Complex dialogs → own region file.**
    A dialog with tabs, many controls, or specialized purpose
    (Paragraph, Character, Page Setup, etc.) gets its own
    regions/<dialog-slug>.md with a full dialog screenshot + enumeration
    of tabs and their main controls.

3.  **Skip trivial items.**
    Standard actions (Save, Open, Cut/Copy/Paste) don't need individual
    treatment — mention them in a one-line "Common actions" bullet under
    the parent menu's region.

4.  **Dedup across workers.**
    Two workers both stumbled into the colour picker → keep ONE entry in
    the most appropriate region.  Don't duplicate.  Read both workers'
    notes and pick the best screenshot.

5.  **Filter for importance.**
    A user reading this skill wants to know "how do I do X with this app".
    Niche debug menus, empty "Recent files", developer-only options → cut.

═══ HOW TO WORK ═══

- Start by using Read to read every worker_*/notes.md.  Text-first.
- Don't open screenshots unless you need to decide between candidates or
  verify something ambiguous in the notes.
- Use Write to produce the output files.
- Use Bash only for simple file copies (cp worker_N/screenshots/step_XYZ.png
  {skill_out}/images/<slug>.png).  Do NOT run image-editing commands unless
  absolutely necessary.

Start now.  No preamble.  Produce the files.
"""
