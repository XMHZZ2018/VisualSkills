# Diagram Creation (LibreOffice Impress 7.3.7)

The Drawing toolbar is your main workspace for building diagrams. If it's not already visible, turn it on via **View > Toolbars > Drawing**. It docks vertically on the left side of the Impress window by default and gives you quick access to shapes, lines, connectors, and more.

For flowcharts specifically, click the triangle ▼ next to **Flowchart** on the Drawing toolbar to open its sub-toolbar. You'll find all the standard flowchart symbols there — process boxes, decision diamonds, terminators, documents, and so on. The same approach works for **Block Arrows**, **Basic Shapes**, **Symbol Shapes**, and **Callouts**, each hiding behind their own expandable sub-toolbar. To draw any shape, just pick the tool, then click and drag on the slide to size it. Hold *Shift* while dragging to keep equal width and height, or hold *Alt* to draw from the center outward.

Once your shapes are placed, connect them using connectors rather than plain lines — this is the real trick for diagrams. Connectors anchor to glue points on each shape and automatically reroute when you move things around. Click the triangle ▼ next to **Connectors** on the Drawing toolbar to see the full set. There are four families: **Standard** (right-angle bends), **Line** (angled segments near glue points), **Straight** (single direct line), and **Curved** (Bézier curves). Each comes in variants with arrows, circles, or no end caps, so pick whichever suits your diagram's visual language.

See `fig01.png`.

To draw a connector, select the type you want, hover over a source shape until small crosses appear at its edges — those are its glue points — then click one and drag to a glue point on the target shape. Release, and the connector snaps into place. If you need to tweak the route afterward, click the connector and drag its square control handles to reroute it around other objects. To change a connector's type or spacing, right-click it and select **Connector** from the context menu to open the Connector dialog, where you can adjust the type, line skew, and spacing values.

See `fig02.png`.

Every object has default glue points, but you can add custom ones for more control. Open the Glue Points toolbar via **View > Toolbars > Glue Points** (or **Edit > Glue Points**), click **Insert Glue Point**, then click where you want it on the shape. You can also set the exit direction for each custom glue point — left, top, right, or bottom — which is handy for keeping a complex architecture or process diagram tidy. Toggle **Glue Point Relative** off if you need the point to stay at a fixed distance from an edge rather than scaling with the object.

For funnel or layered diagrams, combine trapezoids from **Basic Shapes** with block arrows, stacking and aligning them manually. Use *Shift*-click to select multiple shapes, then hold *Shift* while drawing to keep angles constrained to 45-degree increments for clean, professional-looking lines. When everything is in place, select all the pieces of your diagram and group them so they move and scale as one unit.

---

## UI Reference  —  Align and Distribute

_Scope: Align Objects for positioning flowchart shapes and connectors_

LibreOffice Impress provides alignment and distribution via two Format menu submenus, mirrored in the right-click context menu, and as optional floating toolbars.

Read the screenshot `ui-align-objects-submenu.png` in this directory.

## Align Objects (6 commands)

Available via Format > Align Objects, right-click > Align Objects, or the Align Objects floating toolbar (View > Toolbars > Align Objects):

- **Left** — align left edges
- **Centered** — center horizontally
- **Right** — align right edges
- **Top** — align top edges
- **Center** — center vertically
- **Bottom** — align bottom edges

The Align Objects toolbar includes a **Slide reference toggle** — when active, objects align relative to the slide boundaries instead of relative to each other.

## Distribute Selection (8 commands)

Available via Format > Distribute Selection or right-click > Distribute Selection. Requires 3+ selected objects.

- **Horizontally**: Left, Center, Spacing, Right — equalise horizontal spacing by edges, centers, or gaps
- **Vertically**: Top, Center, Spacing, Bottom — equalise vertical spacing by edges, centers, or gaps

An optional Distribute Selection floating toolbar is available via View > Toolbars > Distribute Selection.

---

## UI Reference  —  Drawing Toolbar

_Scope: Flowchart, Connectors, Basic Shapes, Block Arrows, Symbol Shapes palettes and drawing tools_

The Drawing toolbar is a horizontal row of split-button tools below the standard toolbar for inserting shapes, lines, and connectors. Each split-button activates the last-used sub-type on click, and opens a floating palette via the dropdown arrow.

Read the screenshot `ui-drawing-toolbar-shapes.png` in this directory.

## Elements (left to right)

- **Select** — pointer/selection tool for clicking and moving objects
- **Zoom & Pan** — zoom in (Ctrl = zoom out, Shift = pan)
- **Line Color** (split) — click applies current color; dropdown opens color picker
- **Fill Color** (split) — click applies current fill; dropdown opens color picker
- **Insert Line** — draw a line (double-click locks tool for repeated drawing)
- **Rectangle** — draw a rectangle (Shift = square)
- **Ellipse** — draw an ellipse (Shift = circle)
- **Lines and Arrows** (split) — 10-item palette: arrows with various endpoints, dimension line, 45-degree line
- **Curves and Polygons** (split) — 8-item palette: curves, polygons, freeform lines (filled and open variants)
- **Connectors** (split) — 10-item palette: smart connectors that snap to shape connection points and re-route when shapes move
- **Basic Shapes** (split) — 24-item palette (4x6 grid): Rectangle, Rounded Rectangle, Parallelogram, Trapezoid, Ellipse, Circle, Triangle, Diamond, Pentagon, Hexagon, Octagon, Cylinder, Cube, Cross, Frame, Ring, and more
- **Symbol Shapes** (split) — decorative symbols (faces, hearts, lightning, music notes)
- **Block Arrows** (split) — 30-item palette: directional arrows, chevrons, circular arrows
- **Flowchart** (split) — 28-item palette: Process, Decision, Data, Terminator, Document, and all standard flowchart symbols

All drawing tools support double-click to lock for multi-selection (drawing multiple shapes without re-selecting the tool).

---

## UI Reference  —  Format Menu

_Scope: Group submenu for grouping diagram objects_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

Read the screenshot `ui-format-menu.png` in this directory.

## Elements

- **Text** `▸` — Text layout options
- **Spacing** `▸` — Line Spacing: 1 (Ctrl+1) / 1.5 (Ctrl+5) / 2 (Ctrl+2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent
- **Align Text** `▸` — Left (Ctrl+L), Center (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J), Top, Center, Bottom
- **Lists** `▸` — List formatting options
- **Clear Direct Formatting** (Shift+Ctrl+M) — Remove manual formatting
- **Styles** `▸` — Style application submenu
- **Character...** — Opens Character formatting dialog
- **Paragraph...** — Opens Paragraph formatting dialog
- **Bullets and Numbering...** — List style configuration dialog
- **Theme...** — Presentation theme settings
- **Table** `▸` — Table formatting options
- **Image** `▸` — Image adjustment options
- **Text Box and Shape** `▸` — Text box and shape formatting
- **Shadow** (checkbox) — Toggle drop shadow on selected object
- **Interaction...** — Configure click actions on objects
- **Name...** — Name the selected object
- **Alt Text...** — Set alternative text for accessibility
- **Distribute Selection** `▸` — Distribute objects evenly
- **Rotate** — Enter rotation mode for selected object
- **Flip** `▸` — Flip horizontally or vertically
- **Convert** `▸` — Convert object types
- **Align Objects** `▸` — Align objects relative to each other or the slide
- **Arrange** `▸` — Bring forward, send backward, etc.
- **Group** `▸` — Group, ungroup, enter/exit group

---

## UI Reference  —  Group and Ungroup Objects

_Scope: Grouping completed diagram objects as a single unit_

Combines multiple drawing objects into a single logical unit that can be moved, resized, and transformed together. Supports entering group editing mode to modify individual members without ungrouping.

Read the screenshot `ui-group-menu.png` in this directory.

## Operations

| Action | Menu Path | Shortcut | Condition |
|---|---|---|---|
| **Group** | Format > Group > Group | Shift+Ctrl+G | 2+ drawing objects selected |
| **Ungroup** | Format > Group > Ungroup | Shift+Ctrl+Alt+G | Grouped object selected |
| **Enter Group** | Format > Group > Enter Group | F3 (or double-click) | Grouped object selected |
| **Exit Group** | Format > Group > Exit Group | Ctrl+F3 | Inside group editing mode |

All four are also available in the right-click context menu when applicable.

## Workflow States

1. **Multiple objects selected** — status bar shows "2 Shapes selected"; Group is available
2. **Group selected** — status bar shows "Group object selected"; Enter Group and Ungroup available; can move/resize/rotate the group as a whole
3. **Inside group editing** — selected member shows handles, other members appear dimmed; Exit Group available

## Constraints

- **Text placeholder frames** (title, content) cannot be grouped with drawing objects — produces error: "This function cannot be run with the selected objects."
- Minimum 2 objects required for grouping
- Escape inside group editing mode deselects the current member but does NOT exit group mode — use Ctrl+F3 or right-click > Exit Group

---

## UI Reference  —  Insert Menu

_Scope: Shape submenu for inserting diagram shapes_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

Read the screenshot `ui-insert-menu.png` in this directory.

## Elements

- **Image...** — File chooser dialog with preview and link-to-file options
- **Audio or Video...** — File chooser for media files
- **Chart...** — Inserts an editable default column chart as an embedded OLE object
- **Table...** — Opens Insert Table dialog (columns/rows spinners, default 5×2)
- **Media** `▸` — Gallery, Photo Album, Scan `▸`, Animated Image...
- **OLE Object** `▸` — Formula Object (Shift+Alt+E), QR and Barcode..., OLE Object...
- **Shape** `▸` — Shape category submenu
- **Snap Guide...** — Insert a snap guideline
- **Text Box** (F2) — Draw a text frame on the slide
- **Comment** (Ctrl+Alt+C) — Insert a yellow sticky-note comment
- **Fontwork...** — Decorative text effects gallery
- **Hyperlink...** (Ctrl+K) — Opens non-modal Hyperlink dialog with four link types: Internet, Mail, Document, New Document
- **Special Character...** — Character picker with search, font/block filters, favourites (greyed unless editing a text frame)
- **Formatting Mark** `▸` — Non-printing formatting marks
- **Slide Number** — Insert slide-number field at cursor
- **Field** `▸` — Date, time, and other field types
- **Header and Footer...** — Dialog with Slides and Notes and Handouts tabs for date/time, footer text, slide/page numbers, and "do not show on first slide" option
- **Form Control** `▸` — Form control insertion

---

## UI Reference  —  View Menu

_Scope: Toolbars > Drawing and Toolbars > Glue Points_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

Read the screenshot `ui-view-menu.png` in this directory.

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

