# Diagram Creation (LibreOffice Impress 7.3.7)

The Drawing toolbar is your main workspace for building diagrams. If it's not already visible, turn it on via **View > Toolbars > Drawing**. It docks vertically on the left side of the Impress window by default and gives you quick access to shapes, lines, connectors, and more.

For flowcharts specifically, click the triangle ▼ next to **Flowchart** on the Drawing toolbar to open its sub-toolbar. You'll find all the standard flowchart symbols there — process boxes, decision diamonds, terminators, documents, and so on. The same approach works for **Block Arrows**, **Basic Shapes**, **Symbol Shapes**, and **Callouts**, each hiding behind their own expandable sub-toolbar. To draw any shape, just pick the tool, then click and drag on the slide to size it. Hold *Shift* while dragging to keep equal width and height, or hold *Alt* to draw from the center outward.

Once your shapes are placed, connect them using connectors rather than plain lines — this is the real trick for diagrams. Connectors anchor to glue points on each shape and automatically reroute when you move things around. Click the triangle ▼ next to **Connectors** on the Drawing toolbar to see the full set. There are four families: **Standard** (right-angle bends), **Line** (angled segments near glue points), **Straight** (single direct line), and **Curved** (Bézier curves). Each comes in variants with arrows, circles, or no end caps, so pick whichever suits your diagram's visual language.

The slide shows a simple flowchart-style diagram with several shapes — including rectangles and a diamond decision shape — connected by right-angle connectors with arrowheads. The shapes are laid out vertically and branching horizontally, demonstrating how connectors route automatically between glue points on each shape's edges. The Drawing toolbar is visible docked on the left side of the Impress window.

To draw a connector, select the type you want, hover over a source shape until small crosses appear at its edges — those are its glue points — then click one and drag to a glue point on the target shape. Release, and the connector snaps into place. If you need to tweak the route afterward, click the connector and drag its square control handles to reroute it around other objects. To change a connector's type or spacing, right-click it and select **Connector** from the context menu to open the Connector dialog, where you can adjust the type, line skew, and spacing values.

The Connector dialog box is shown, titled "Connector." It contains a Type dropdown for selecting the connector style (Standard, Line, Straight, or Curved), as well as numeric spin boxes for Line Skew and Spacing values that control the offset and clearance of the connector routing. OK, Cancel, Help, and Reset buttons appear along the bottom or side of the dialog.

Every object has default glue points, but you can add custom ones for more control. Open the Glue Points toolbar via **View > Toolbars > Glue Points** (or **Edit > Glue Points**), click **Insert Glue Point**, then click where you want it on the shape. You can also set the exit direction for each custom glue point — left, top, right, or bottom — which is handy for keeping a complex architecture or process diagram tidy. Toggle **Glue Point Relative** off if you need the point to stay at a fixed distance from an edge rather than scaling with the object.

For funnel or layered diagrams, combine trapezoids from **Basic Shapes** with block arrows, stacking and aligning them manually. Use *Shift*-click to select multiple shapes, then hold *Shift* while drawing to keep angles constrained to 45-degree increments for clean, professional-looking lines. When everything is in place, select all the pieces of your diagram and group them so they move and scale as one unit.

---

## UI Reference  —  Drawing Toolbar

_Scope: Connector, Flowchart, Callout, Shapes, Freeform, Bezier Curves, and basic shape dropdowns_

The second icon row provides drawing tools, shape creation, and quick formatting controls for objects on the slide canvas.

The Drawing toolbar is displayed as a horizontal strip of icon buttons running across the window. From left to right the icons include: a selection arrow, a zoom tool, a connector tool with a dropdown triangle, a line tool with a dropdown, rectangle and ellipse drawing tools, a block arrow dropdown, freeform and Bézier curve dropdowns, a basic shapes diamond dropdown, connector points, a flowchart shapes dropdown, a callouts dropdown, a stars-and-banners dropdown, a 3D objects dropdown, an area fill colour picker (shown as a blue square), an insert-image button, and finally Arrange and Object Alignment dropdowns at the far right. Many icons feature small dropdown triangles indicating expandable sub-toolbars.

## Elements

Row (left → right):

- **Select** (arrow) — Default selection/move tool
- **Zoom** — Zoom tool for canvas
- **Connector** (dropdown ▾) — Draw connector lines between objects
- **Line** (dropdown ▾) — Draw straight lines; dropdown for arrow styles
- **Rectangle** — Draw rectangles/squares
- **Ellipse** — Draw ellipses/circles
- **Arrow** (dropdown ▾) — Block arrows; dropdown for styles
- **Freeform** (dropdown ▾) — Freeform drawing tools
- **Bezier Curves** (dropdown ▾) — Curve drawing tools
- **Diamond** / **Shapes** (dropdown ▾) — Basic shapes palette
- **Connector Points** (dropdown ▾) — Connector shape types
- **Flowchart** (dropdown ▾) — Flowchart shape palette
- **Callout** (dropdown ▾) — Callout shapes palette
- **Stars** (dropdown ▾) — Stars and banners shapes
- **3D Objects** (dropdown ▾) — 3D shape primitives
- **Area Fill Color** (dropdown ▾) — Fill colour picker (blue square icon)
- **Insert Image** — Insert an image from file
- **Arrange** (dropdown ▾) — Object stacking order
- **Object alignment** (dropdown ▾) — Align objects on slide

---

## UI Reference  —  Format Menu

_Scope: Group submenu for grouping diagram objects_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format menu is shown fully expanded as a dropdown from the menu bar. It lists items from top to bottom: Text, Spacing (with a submenu arrow), Align Text (with a submenu arrow), Lists, Clear Direct Formatting (Shift+Ctrl+M), Styles, Character…, Paragraph…, Bullets and Numbering…, Theme…, Table, Image, Text Box and Shape, a Shadow checkbox toggle, Interaction…, Name…, Alt Text…, Distribute Selection, Rotate, Flip, Convert, Align Objects, Arrange, and Group (with a submenu arrow leading to Group, Ungroup, Enter Group, and Exit Group commands).

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

## UI Reference  —  Insert Menu

_Scope: Shape submenu for inserting flowchart/connector shapes_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert menu is shown open as a dropdown from the menu bar. Its entries from top to bottom include: Image…, Audio or Video…, Chart…, Table…, Media (with a submenu arrow), OLE Object (with a submenu arrow), Shape (with a submenu arrow for shape category sub-palettes), Snap Guide…, Text Box (F2), Comment (Ctrl+Alt+C), Fontwork…, Hyperlink… (Ctrl+K), Special Character…, Formatting Mark, Slide Number, Field (with a submenu arrow), Header and Footer…, and Form Control (with a submenu arrow). The Shape entry is highlighted, indicating it expands to reveal sub-categories of shapes such as basic, flowchart, and connector shapes.

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

_Scope: Toolbars > Drawing, Toolbars > Glue Points_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View menu is shown expanded as a dropdown from the menu bar. At the top are radio-button editing mode entries: Normal, Outline, Notes, Slide Sorter, Master Slide, Master Notes, and Master Handout. Below that are checkbox toggles for UI elements: Status Bar (checked), Slide Pane (checked), Views Tab Bar, Rulers (Shift+Ctrl+R), Comments (checked), Sidebar (Ctrl+F5, checked), Color Bar, and Navigator (Shift+Ctrl+F5). Further down are submenus for User Interface…, Toolbars (with a submenu arrow leading to a checklist of available toolbars including Drawing and Glue Points), Grid and Helplines, Snap Guides, and Color/Grayscale. The bottom section includes direct links to sidebar panels — Slide Layout, Slide Transition, Animation, Styles (F11), and Gallery — followed by Zoom options.

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
