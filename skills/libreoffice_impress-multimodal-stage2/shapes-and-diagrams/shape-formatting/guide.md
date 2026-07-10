# Shape Formatting (LibreOffice Impress 7.3.7)

Every shape on a slide has a handful of visual properties you can tweak — fill color, line style, rotation, and more. Most of the time you'll work through either the **Properties** deck on the Sidebar or a dedicated dialog, depending on how much control you need.

## Recoloring a shape's fill

Select your shape, then look at the **Area Style/Filling** drop-down on the **Line and Filling** toolbar (show it via **View > Toolbars > Line and Filling** if it's hidden). From that drop-down you can pick among **None**, **Color**, **Gradient**, **Hatching**, **Bitmap**, and **Pattern** fills. Choose a type, then select the specific preset from the adjacent list. For quick color swaps, the Sidebar is even faster — open **Properties > Area**, pick a fill type from the *Fill* drop-down, and choose your color or gradient right there.

See `fig01.png`.

When you need finer control — custom RGB values, transparency, or creating your own gradients — open the full Area dialog via **Format > Object and Shape > Area**, or right-click the shape and choose **Area**. The **Color** tab lets you pick from a palette or enter exact hex/RGB values, while the **Gradient**, **Image**, **Pattern**, and **Hatch** tabs each offer their own customization options. Click **OK** to apply.

## Formatting lines and borders

A shape's outline is controlled separately from its fill. The quickest route is the **Line and Filling** toolbar: pick a style from the **Line Style** list, set the **Line Width**, and choose a **Line Color**. You can also add arrowheads to either end via the **Arrow Style** drop-downs. For full control, open the Line dialog through **Format > Object and Shape > Line** (or right-click and choose **Line**). It has four tabs — **Line**, **Shadow**, **Line Styles**, and **Arrow Styles** — covering everything from transparency and corner styles to creating entirely custom dash patterns.

See `fig02.png`.

## Rotating objects

The fastest way to rotate a shape is with the cursor. Select the object, click the triangle next to **Transformations** on the Line and Filling toolbar, then choose **Rotate**. The selection handles turn into round rotation handles — drag any corner handle to spin the shape freely. Hold **Shift** while dragging to snap to 15-degree increments, which is great for getting exact right-angle rotations. You can also drag the pivot point (the small circle at the center) to rotate around a different anchor.

For precise rotation, press **F4** (or go to **Format > Object and Shape > Position and Size**) and switch to the **Rotation** tab. Enter an exact angle in the **Angle** field, adjust the **Pivot Point** if needed, and hit **OK**. The same rotation controls are available in the **Position and Size** panel on the Sidebar.

## Flipping shapes

To mirror a shape, right-click it and choose **Flip > Vertically** or **Flip > Horizontally** — done. The same options live under **Format > Flip** on the Menu bar. If you need to flip along a custom axis, use the **Flip** tool on the **Transformations** toolbar: it places a dashed symmetry axis through your shape that you can reposition and angle before dragging a handle across it to complete the flip. Impress doesn't have a true mirror-copy command, but you can fake it by copying the shape, flipping the copy, then aligning both with **right-click > Alignment**.

## Distorting shapes

Three tools on the **Transformations** toolbar let you warp shapes in perspective. **Distort** lets you drag corner, vertical, or horizontal handles independently for a perspective skew. **Set in Circle (perspective)** and **Set to circle (slant)** both bend the shape into a pseudo-3D curve. Note that the shape must be converted to a curve first — Impress will prompt you automatically, but be aware this conversion is one-way (only **Undo** can reverse it).

See `fig03.png` for the distortion examples showing original shape with corner, vertical, and horizontal distortions.

---

## UI Reference  —  Area Fill (Properties Sidebar)

_Scope: Fill dropdown (Color/Gradient/Hatching/Bitmap/Pattern), Transparency controls, full Area dialog_

The Area section in the Properties sidebar controls the fill type and transparency of the selected object. It appears only when an object is selected in object-selection mode.

Read the screenshot `ui-area-fill-sidebar.png` in this directory.

## Fill Types

The **Fill** dropdown offers 7 modes:

| Fill Type | Secondary Controls |
|---|---|
| **None** | No fill |
| **Color** | Color swatch + dropdown palette (11 named palettes, Custom Color... button with full RGB/HSB/CMYK picker) |
| **Gradient** | Style dropdown (Linear/Axial/Radial/Ellipsoid/Square/Rectangular), angle field, from/to color selectors |
| **Hatching** | 15 preset patterns (e.g., Black 0°, Blue 45° Crossed, Red -45° Triple) |
| **Bitmap** | 25 preset textures (e.g., Painted White, Brick Wall, Marble, Sand), Import button for custom images |
| **Pattern** | 15 geometric patterns (e.g., 5/10/20 Percent, Dotted Grid, Zig Zag, Weave) |
| **Use Slide Background** | Inherits the slide background |

## Transparency

The **Transparency** dropdown below the fill controls:

- **None** — fully opaque
- **Solid** — flat percentage slider (0% opaque to 100% transparent)
- **Linear / Axial / Radial / Ellipsoid / Quadratic / Square** — gradient transparency

## Full Area Dialog

Right-click > Area... opens a modal dialog with three tabs:
- **Area** — same fill types as sidebar but with more controls (preview panel, gradient presets)
- **Shadow** — Use shadow checkbox, 3x3 direction picker, color, distance, blur, transparency
- **Transparency** — No transparency / flat % / gradient with full Type/Center/Angle controls

---

## UI Reference  —  Drawing Toolbar

_Scope: Line Color and Fill Color split-buttons for quick recoloring_

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

_Scope: Rotate, Flip, Shadow toggle, Text Box and Shape > Area/Line/Position and Size, Convert submenu_

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

## UI Reference  —  Position and Size Dialog

_Scope: Rotation tab (angle, pivot point), Slant & Corner Radius tab for shape distortion_

A 3-tab modal dialog (opened via **F4** or Format > Text Box and Shape > Position and Size) providing precise numeric control over a selected object's position, size, rotation, slant, and corner radius.

Read the screenshot `ui-position-size-dialog.png` in this directory.

## Tab 1: Position and Size

- **Position X / Y** — coordinates in inches, with base point selector (3x3 grid of 9 anchor points)
- **Width / Height** — object dimensions with +/- spinners; Height greyed for text frames with "Fit height to text" enabled
- **Keep ratio** — maintain aspect ratio when resizing (greyed for text frames)
- **Size Base Point** — 3x3 grid controlling which anchor the object grows/shrinks from
- **Protect Position** — locks X/Y (auto-checks Protect Size and greys all fields)
- **Protect Size** — locks Width/Height independently
- **Fit width to text** / **Fit height to text** — auto-size to text content (text frames only; greyed for shapes)

## Tab 2: Rotation

- **Pivot Point X / Y** — rotation center coordinates with 3x3 snap selector
- **Rotation Angle** — degrees (0-360), positive = counter-clockwise
- **Rotation Dial** — interactive circular control linked to the angle field

## Tab 3: Slant & Corner Radius

- **Corner Radius** — rounding for rectangle corners (greyed for standard shapes)
- **Slant Angle** — horizontal shear in degrees
- **Control Point 1 / 2** — bezier control points (greyed for non-bezier shapes)

## Access

- **F4** key with an object selected
- Format > Text Box and Shape > Position and Size...
- Right-click on object > Position and Size...

---

## UI Reference  —  View Menu

_Scope: Toolbars > Line and Filling, Toolbars > Transformations_

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

