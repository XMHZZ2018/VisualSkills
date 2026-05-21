# Shape Formatting (LibreOffice Impress 7.3.7)

Every shape on a slide has a handful of visual properties you can tweak — fill color, line style, rotation, and more. Most of the time you'll work through either the **Properties** deck on the Sidebar or a dedicated dialog, depending on how much control you need.

## Recoloring a shape's fill

Select your shape, then look at the **Area Style/Filling** drop-down on the **Line and Filling** toolbar (show it via **View > Toolbars > Line and Filling** if it's hidden). From that drop-down you can pick among **None**, **Color**, **Gradient**, **Hatching**, **Bitmap**, and **Pattern** fills. Choose a type, then select the specific preset from the adjacent list. For quick color swaps, the Sidebar is even faster — open **Properties > Area**, pick a fill type from the *Fill* drop-down, and choose your color or gradient right there.

The Sidebar's Properties panel is shown with the **Area** section expanded on the right side of the Impress window. A shape is selected on the slide canvas, and the Area section displays a **Fill** drop-down (set to "Color"), a color picker button showing the currently applied fill color, and a Recent Colors row beneath it. Below that, a **Transparency** slider is available to adjust fill opacity.

When you need finer control — custom RGB values, transparency, or creating your own gradients — open the full Area dialog via **Format > Object and Shape > Area**, or right-click the shape and choose **Area**. The **Color** tab lets you pick from a palette or enter exact hex/RGB values, while the **Gradient**, **Image**, **Pattern**, and **Hatch** tabs each offer their own customization options. Click **OK** to apply.

## Formatting lines and borders

A shape's outline is controlled separately from its fill. The quickest route is the **Line and Filling** toolbar: pick a style from the **Line Style** list, set the **Line Width**, and choose a **Line Color**. You can also add arrowheads to either end via the **Arrow Style** drop-downs. For full control, open the Line dialog through **Format > Object and Shape > Line** (or right-click and choose **Line**). It has four tabs — **Line**, **Shadow**, **Line Styles**, and **Arrow Styles** — covering everything from transparency and corner styles to creating entirely custom dash patterns.

The Line dialog is displayed with its four tabs visible at the top: **Line**, **Shadow**, **Line Styles**, and **Arrow Styles**. The **Line** tab is active, showing drop-downs and fields for Line Style (e.g., solid, dashed), Line Color, Line Width, and Transparency. Below those, Corner Style and Cap Style drop-downs control how line joints and endpoints render. An Arrow Styles section at the bottom provides separate Start Style and End Style drop-downs with width fields for each end of the line. A preview area at the bottom of the dialog shows how the current settings will look, with **OK**, **Cancel**, and **Help** buttons along the bottom edge.

## Rotating objects

The fastest way to rotate a shape is with the cursor. Select the object, click the triangle next to **Transformations** on the Line and Filling toolbar, then choose **Rotate**. The selection handles turn into round rotation handles — drag any corner handle to spin the shape freely. Hold **Shift** while dragging to snap to 15-degree increments, which is great for getting exact right-angle rotations. You can also drag the pivot point (the small circle at the center) to rotate around a different anchor.

For precise rotation, press **F4** (or go to **Format > Object and Shape > Position and Size**) and switch to the **Rotation** tab. Enter an exact angle in the **Angle** field, adjust the **Pivot Point** if needed, and hit **OK**. The same rotation controls are available in the **Position and Size** panel on the Sidebar.

## Flipping shapes

To mirror a shape, right-click it and choose **Flip > Vertically** or **Flip > Horizontally** — done. The same options live under **Format > Flip** on the Menu bar. If you need to flip along a custom axis, use the **Flip** tool on the **Transformations** toolbar: it places a dashed symmetry axis through your shape that you can reposition and angle before dragging a handle across it to complete the flip. Impress doesn't have a true mirror-copy command, but you can fake it by copying the shape, flipping the copy, then aligning both with **right-click > Alignment**.

## Distorting shapes

Three tools on the **Transformations** toolbar let you warp shapes in perspective. **Distort** lets you drag corner, vertical, or horizontal handles independently for a perspective skew. **Set in Circle (perspective)** and **Set to circle (slant)** both bend the shape into a pseudo-3D curve. Note that the shape must be converted to a curve first — Impress will prompt you automatically, but be aware this conversion is one-way (only **Undo** can reverse it).

Four versions of the same shape are displayed side by side to illustrate the distortion modes. The leftmost shape is the undistorted original. Next to it, a corner-distorted version shows the shape skewed as though one corner has been dragged outward, giving a perspective tilt. The third shows a vertical distortion where the top or bottom edge has been shifted independently, creating a tapered or trapezoidal appearance. The fourth shows a horizontal distortion where the left or right edge has been shifted, producing a sideways skew. Each shape has visible green selection handles at corners and edges indicating the active distortion tool.

---

## UI Reference  —  Drawing Toolbar

_Scope: Area Fill Color picker and shape selection tools_

The second icon row provides drawing tools, shape creation, and quick formatting controls for objects on the slide canvas.

The Drawing toolbar is a horizontal icon bar spanning the bottom of the Impress window. From left to right it contains: a **Select** arrow tool, a **Zoom** magnifying glass, then a series of drawing-tool icons each with small dropdown triangles — **Connector**, **Line**, **Rectangle**, **Ellipse**, **Block Arrow**, **Freeform**, **Bezier Curves**, followed by shape palette dropdowns for **Basic Shapes** (diamond icon), **Connector Points**, **Flowchart**, **Callouts**, **Stars and Banners**, and **3D Objects**. Toward the right end, an **Area Fill Color** button (shown as a colored square with a dropdown arrow) opens a color picker, followed by an **Insert Image** icon, an **Arrange** dropdown for stacking order, and an **Object Alignment** dropdown. Each tool with a small triangle offers a flyout sub-palette when clicked.

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

_Scope: Rotate, Flip, Shadow toggle, Align Objects, Arrange submenus_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format dropdown menu is shown fully expanded from the menu bar. It is a single-column list of menu items. Near the top are **Text**, **Spacing**, **Align Text**, and **Lists** submenus (each with a right-pointing arrow indicating child menus), followed by **Clear Direct Formatting** (with the shortcut Shift+Ctrl+M). Below that are **Styles**, **Character...**, **Paragraph...**, and **Bullets and Numbering...** entries that open dialogs. The middle section contains **Theme...**, **Table**, **Image**, and **Text Box and Shape** submenus, then a **Shadow** checkbox toggle, **Interaction...**, **Name...**, and **Alt Text...** dialog entries. The lower section includes **Distribute Selection**, **Rotate**, **Flip** (with a submenu arrow), **Convert** (submenu arrow), **Align Objects** (submenu arrow), **Arrange** (submenu arrow), and **Group** (submenu arrow) at the bottom.

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

## UI Reference  —  View Menu

_Scope: Toolbars > Line and Filling, Toolbars > Transformations_

The View menu controls presentation editing modes, UI panel visibility, and zoom settings.

The View dropdown menu is shown expanded from the menu bar as a single-column list. At the top, a group of radio-button entries lists the editing modes: **Normal** (currently selected), **Outline**, **Notes**, **Slide Sorter**, **Master Slide**, **Master Notes**, and **Master Handout**. Below a separator, checkbox toggle entries include **Status Bar** (checked), **Slide Pane** (checked), **Views Tab Bar**, **Rulers**, **Comments** (checked), **Sidebar** (checked), and **Color Bar**. Further down are **Navigator**, **User Interface...**, and the **Toolbars** submenu (with a right-pointing arrow leading to a checklist of available toolbars including Drawing, Presentation, and Standard enabled by default). The menu continues with **Grid and Helplines**, **Snap Guides**, and **Color/Grayscale** submenus, then sidebar panel shortcuts for **Slide Layout**, **Slide Transition**, **Animation**, **Styles**, and **Gallery**, and finally a **Zoom** submenu at the bottom.

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
