# Text Box Formatting (LibreOffice Impress 7.3.7)

Every piece of text on an Impress slide lives inside a text box, so knowing how to style them is essential — especially when you want something like a code block or a callout to stand out visually. Here's how to work with fonts, backgrounds, and borders to get the look you need.

**Creating a text box** is straightforward: click **Insert Text Box** on the Standard or Drawing toolbar, then either click the slide for a single-line box that grows as you type, or click and drag to define a fixed-width area where text wraps automatically. You can also just press *F2* to drop a horizontal text box onto the current slide.

Once you're inside a text box, the **Text Formatting** toolbar appears automatically, giving you quick access to font family, size, bold, italic, underline, and more. For finer control, select your text and go to **Format** on the Menu bar — options like **Character** and **Paragraph** open dialogs where you can set exact font properties, spacing, and alignment. You can also tweak these from the **Character** and **Paragraph** panels in the Properties deck on the Sidebar.

To give a text box a **background fill** — great for making code blocks or highlighted content pop — right-click the text box border and choose the **Area** option, or expand the **Area** panel in the Properties Sidebar. From there you can pick a solid color, gradient, hatching, or bitmap. A light gray fill with a monospace font, for instance, instantly signals "code" to your audience.

**Adding a border** makes the box's edges visible. The quickest way is via the **Line and Filling** toolbar: select the text box, then set **Line Style**, **Line Width**, and **Line Color** directly on the toolbar. If it's not visible, enable it through **View > Toolbars > Line and Filling**. For more options — like transparency or corner rounding — right-click the border, select **Line**, and use the Line dialog's full set of controls under the **Line** tab. Set the style, color, width, and pick a **Corner Style** such as "Rounded" for a softer look. For rounded corners to be clearly visible, keep the line width above about 0.35 cm.

See `fig01.png` for the Line dialog showing style, color, width, and corner style options.

You can also manage borders from the **Line** panel in the Properties Sidebar, which exposes the same line style, width, color, and transparency settings in a more compact form.

For **precise positioning and sizing**, press *F4* or go to **Format > Object and Shape > Position and Size**. The dialog lets you enter exact coordinates, dimensions, and even lock the position or size to prevent accidental changes. Check **Fit width to text** or **Fit height to text** under the Adapt section if you want the box to resize dynamically as content changes.

When you're building something like a styled code block, the recipe is simple: create a text box, set a monospace font (via the Text Formatting toolbar), apply a subtle background color (via **Area**), add a thin border with rounded corners (via the **Line** dialog or toolbar), and adjust internal spacing through **Format > Paragraph**. Direct formatting like this overrides any applied style, so it works even on AutoLayout boxes — just keep in mind that Impress leans more on manual formatting than Writer does, since Presentation Styles are fairly restrictive and don't support character-level styling.

---

## UI Reference  —  Area Fill (Properties Sidebar)

_Scope: Fill type and color for text box background styling_

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

_Scope: Insert Text Box available from Drawing toolbar_

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

_Scope: Character..., Paragraph..., Text Box and Shape submenu_

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

## UI Reference  —  Insert Menu

_Scope: Text Box (F2) insertion entry_

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

## UI Reference  —  Position and Size Dialog

_Scope: Fit width/height to text, precise positioning and sizing of text boxes_

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

## UI Reference  —  Standard Toolbar

_Scope: Insert Text Box button_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (dropdown ▾) — Create a new document (dropdown lists all document types)
- **Open** (dropdown ▾) — Open an existing file; dropdown shows recent documents
- **Save** (dropdown ▾) — Save the current document
- **Email Document** — Send document via email
- **Edit File** — Toggle read-only / edit mode
- **PDF** — Export directly as PDF
- **Print** — Print the document
- **Cut** / **Copy** / **Paste** — Clipboard operations
- **Paint Format** (Clone Formatting) — Copy formatting to other objects
- **Undo** / **Redo** — Step through undo/redo history
- **Find & Replace** — Open Find and Replace dialog
- **Spelling** — Run the spelling checker
- **Display Views** — Normal, Outline, Notes, Slide Sorter mode toggles
- **Presentation** — Start slideshow (F5)
- **Table** / **Insert Chart** / **Insert Text Box** — Quick insertion tools
- **Hyperlink** — Insert or edit hyperlinks
- **Sidebar** — Toggle the Properties sidebar
- **Start Center** — Return to the LibreOffice Start Center

