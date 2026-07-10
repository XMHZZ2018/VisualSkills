# Slide Management (LibreOffice Impress 7.3.7)

To add a new slide, select the slide you want it to appear after, then go to **Slide > New Slide** on the Menu bar — or just press *Ctrl+M*. You can also right-click a slide in the Slides pane and choose **New Slide** from the context menu. If nothing is selected, the new slide lands at the end of the deck. The inserted slide inherits the master slide of whichever slide is currently active.

If you need a copy of an existing slide — same layout, formatting, and content — select it and go to **Slide > Duplicate Slide**, or right-click and pick **Duplicate Slide**. This is handy when a slide is getting too dense: duplicate it and split the content across two slides so your audience can breathe.

Reordering slides is pure drag-and-drop. In the Slides pane or in **Slide Sorter** view, just click a slide and drag it to its new position. Slide Sorter gives you the best bird's-eye view for rearranging a large deck. To select multiple slides, hold *Ctrl* and click each one, or hold *Shift* to grab a contiguous range.

To pull slides in from another presentation file, go to **Slide > Insert Slide from File**. Browse to the file, click **Open**, and the Insert Slides/Objects dialog appears — expand the file tree, check the slides you want, and hit **OK**. You can optionally tick **Link** to embed the slide as an OLE object instead of copying it outright.

The Insert Slides/Objects dialog is a compact window with a tree-view list on the left where each slide in the source file is shown as a named, checkable entry. At the bottom of the dialog there is a **Link** checkbox for embedding slides as OLE objects rather than copying them. The dialog has **OK** and **Cancel** buttons in the lower-right corner to confirm or abort the import.

Moving slides between two open presentations is also straightforward. Open both files in **Slide Sorter** view, then drag slides from one window to the other. Hold *Ctrl* while dragging to copy rather than move. Alternatively, use the classic **Edit > Copy** and **Edit > Paste** workflow across presentations.

When a slide has gotten too long, select it and go to **Slide > Expand Slide**. Impress splits the content into multiple new slides based on the first outline level — each top-level bullet becomes its own slide title. Rearrange the results afterward if needed.

For a quick agenda or overview, select your starting slide and choose **Slide > Summary Slide**. Impress generates a new slide at the end containing bullet points built from the titles of all slides in the presentation.

To rename a slide, right-click it and select **Rename Slide**, type a descriptive name in the dialog, and click **OK**. Giving slides meaningful names makes the Slides pane far easier to navigate. To delete a slide you no longer need, right-click it and choose **Delete Slide** — or select it and hit the *Delete* key.

---

## UI Reference  —  Slide Menu

_Scope: New Slide, Duplicate Slide, Delete Slide, Insert Slide from File, Rename Slide, Move/Navigate submenus, Summary/Expand Slide_

The Slide menu manages slide creation, duplication, deletion, layout, master slides, visibility, and transitions.

The Slide menu is a standard drop-down menu showing a vertical list of items including New Slide (with the Ctrl+M shortcut shown to the right), Duplicate Slide, Insert Slide from File, a Layout submenu arrow, Delete Slide (greyed out when only one slide exists), Save Background Image and Set Background Image entries, Slide Properties, Change Slide Master, New Master, Delete Master, checkmarked Master Background and Master Objects toggles, Master Elements, Show/Hide Slide, Rename Slide, Jump to Last Edited Slide (Shift+Alt+F5), Move and Navigate submenus indicated by right-pointing arrows, Summary Slide and Expand Slide (both greyed out), and Slide Transition at the bottom. Several items have separator lines grouping them into logical sections.

## Elements

- **New Slide** (Ctrl+M) — Insert a blank slide after the current one
- **Duplicate Slide** — Create an identical copy of the current slide
- **Insert Slide from File...** — Import slides from another presentation
- **Layout** `▸` — 16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart
- **Delete Slide** — Remove the selected slide (only available with 2+ slides)
- **Save Background Image...** — Save slide background (greyed unless custom background set)
- **Set Background Image...** — Set a background image for the slide
- **Slide Properties...** — Opens Slide Properties dialog (Slide, Background, Transparency tabs)
- **Change Slide Master...** — Change the master slide template
- **New Master** / **Delete Master** — Create or remove master slides
- **Master Background** ✓ / **Master Objects** ✓ — Toggle master background/objects visibility
- **Master Elements...** — Edit master slide elements
- **Show Slide** / **Hide Slide** — Toggle slide visibility during slideshow
- **Rename Slide...** — Rename the slide (opens dialog with name field)
- **Jump to Last Edited Slide** (Shift+Alt+F5) — Navigate to last edited slide
- **Move** `▸` — Slide to Start, Slide Up, Slide Down, Slide to End (context-sensitive)
- **Navigate** `▸` — To First/Previous/Next/Last Slide (context-sensitive)
- **Summary Slide** / **Expand Slide** — (greyed in normal conditions)
- **Slide Transition** — Opens the Slide Transition sidebar panel

---

## UI Reference  —  Slides Panel

_Scope: Thumbnails for drag-reorder, context menu: Cut/Copy/Paste, Delete Slide, New Slide, Duplicate, Rename, Hide, Navigate, Move_

The Slides panel is a resizable left-side thumbnail strip showing all slides. Click to select/navigate, right-click for a context menu, drag to reorder.

The Slides panel is shown on the left side of the Impress window, headed by a "Slides" label with a small close (X) button beside it. Below the header, numbered slide thumbnails are stacked vertically. A right-click context menu is open over the panel, displaying items in order: Cut, Copy, Paste, a separator, Delete Slide, New Slide, Duplicate Slide, Rename Slide, a separator, Hide Slide, a separator, Layout with a submenu arrow, Navigate with a submenu arrow, Move with a submenu arrow, and Slide Properties at the bottom. The currently selected slide thumbnail is highlighted with a blue border.

## Panel Controls

- **Slides header label** — Non-interactive "Slides" text at top of panel
- **Close Pane button** (X) — Closes the panel entirely; restore via View > Slide Pane
- **Hide/Show strip** — Thin vertical strip at right edge; click to collapse to ~6px, click again to restore; drag to resize panel width
- **Slide thumbnails** — Numbered thumbnails; click to select, drag to reorder; hidden slides show a diagonal hatched overlay

## Right-Click Context Menu

When only 1 slide exists:
- Copy, Paste, New Slide, Duplicate Slide, Rename Slide..., Hide Slide, Layout `▸`, Slide Properties...

With 2+ slides (additional items):
- Cut, Delete Slide, Navigate `▸`, Move `▸`

### Layout Submenu
16 layout options: Blank Slide, Title Only, Title Slide, Title Content, Centered Text, Title and 2 Content, Title Content and 2 Content, Title 2 Content and Content, Title Content over Content, Title 2 Content over Content, Title 4 Content, Title 6 Content, Vertical Title Vertical Text, Vertical Title Text Chart, Title Vertical Text, Title 2 Vertical Text Clipart

### Navigate Submenu (context-sensitive)
- First slide: To Next Slide, To Last Slide
- Last slide: To First Slide, To Previous Slide
- Middle slides: all four options

### Move Submenu (context-sensitive)
- First slide: Slide Down, Slide to End
- Last slide: Slide to Start, Slide Up
- Middle slides: all four options

---

## UI Reference  —  View Menu

_Scope: Slide Sorter view mode for reordering slides_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View menu drop-down displays a list of editing mode options at the top — Normal (currently selected, shown in bold or highlighted), Outline, Notes, Slide Sorter, Master Slide, Master Notes, and Master Handout — followed by a separator and a series of checkable UI toggles: Status Bar (checked), Slide Pane (checked), Views Tab Bar, Rulers with the Shift+Ctrl+R shortcut, and Comments (checked). Below another separator are Sidebar (Ctrl+F5, checked), Color Bar, Navigator (Shift+Ctrl+F5), User Interface, and Toolbars, Grid and Helplines, Snap Guides, and Color/Grayscale submenus. Further down, shortcut entries for Slide Layout, Slide Transition, Animation, Styles (F11), and Gallery open their respective sidebar panels. The Zoom submenu appears at the bottom of the menu.

## Elements

### Editing Modes (radio buttons)
- **Normal** — Default slide editing mode with canvas, slides panel, and properties sidebar
- **Outline** — Text-only outline editor; toolbar switches to outline navigation tools
- **Notes** — Portrait layout with slide thumbnail + speaker notes area
- **Slide Sorter** — Grid of all slide thumbnails for reordering
- **Master Slide** — Edit the master slide template (title, outline levels, date/footer/number areas)
- **Master Notes** / **Master Handout** — Edit notes/handout master layouts

### UI Toggles (checkboxes)
- **Status Bar** ✓ — Toggle the bottom status bar
- **Slide Pane** ✓ — Toggle the left slide thumbnail panel
- **Views Tab Bar** — Tab bar with Normal/Outline/Notes/Slide Sorter tabs
- **Rulers** (Shift+Ctrl+R) — Horizontal and vertical rulers along the canvas
- **Comments** ✓ — Show/hide comment annotations
- **Sidebar** (Ctrl+F5) ✓ — Properties sidebar on the right
- **Color Bar** — Colour swatch bar at the bottom
- **Navigator** (Shift+Ctrl+F5) — Floating navigation panel

### Submenus
- **User Interface...** — UI mode selector
- **Toolbars** `▸` — Checklist of 30+ toolbars; enabled by default: Drawing, Presentation, Standard
- **Grid and Helplines** `▸` — Grid and guideline display options
- **Snap Guides** `▸` — Snap guide settings
- **Color/Grayscale** `▸` — Switch between Color, Grayscale, Black & White display

### Sidebar Panels
- **Slide Layout** / **Slide Transition** / **Animation** — Open the corresponding sidebar panel directly
- **Styles** (F11) — Opens the Styles panel
- **Gallery** — Opens the Gallery panel

### Zoom
- **Zoom** `▸` — Entire Page, Page Width, Optimal View, 50%–200%, Zoom & Pan, custom Zoom dialog
