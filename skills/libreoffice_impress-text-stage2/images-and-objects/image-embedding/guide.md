# Image Embedding (LibreOffice Impress 7.3.7)

When you insert an image into Impress, it's embedded by default — the image data lives inside the presentation file itself. That's usually what you want, because it means the file is self-contained and will look right on any machine. But there's also a linking option, and understanding the difference matters if you're sharing your work.

To insert an image, head to **Insert > Image** on the Menu bar. The Insert Image file browser opens, where you can navigate to your file and preview it by checking the **Preview** box on the lower left.

The Insert Image dialog is a standard file browser titled "Insert Image" with a navigation sidebar on the left listing locations such as Recent, Home, Desktop, Documents, Downloads, Music, Pictures, Videos, and Trash. The main area shows a file list with columns for Name, Size, Type, and Modified, displaying various image files (e.g., Beach.jpg, Bahamas Aerial.jpg, Abstract Shapes 2.jpg). When a file is selected (highlighted in orange), a thumbnail preview appears on the right side of the dialog. At the bottom left are two checkboxes: **Preview** (checked) and **Insert as Link** (unchecked). A file-type filter dropdown set to "<All images>" sits at the bottom right, and **Cancel**, search, and **Open** buttons appear along the top of the dialog.

Here's the key detail: at the bottom of that file browser, you'll see an **Insert as Link** checkbox. If you leave it unchecked (the default), the image gets fully embedded into the presentation. If you check it, Impress only stores a reference to the file on disk — the image isn't actually inside the presentation.

Linking makes sense in a few situations. If the image file is very large, linking keeps your presentation file small. It's also handy when the same image appears across many presentations — say, a shared company background — since you maintain one source file. And sometimes you only need the image visible while working locally, like a holiday slideshow you'll only ever open on your own machine.

The downside of linking is portability. Move the presentation to another computer, and any linked images break because the original file paths no longer resolve. So if you plan to share, present on a different machine, or archive your work, embedding is the way to go.

To convert a linked image to an embedded one, the simplest approach is to remove the linked image, then re-insert it through **Insert > Image** without the **Insert as Link** checkbox selected. Once re-inserted, the image data is stored directly in the presentation file. Click **Open** and the image drops onto the center of your slide with selection handles ready for positioning.

After embedding, you can resize, crop, and format the image to fit your presentation needs — the image is now fully self-contained and safe to share.

---

## UI Reference  —  Drawing Toolbar

_Scope: Insert Image button_

The second icon row provides drawing tools, shape creation, and quick formatting controls for objects on the slide canvas.

The Drawing toolbar is a single horizontal row of small icons. From left to right it includes: a pointer/select arrow, a zoom magnifier, then a series of drawing and shape tools — connector, line, rectangle, ellipse, block arrow, freeform, Bezier curve, diamond/basic shapes, connector points, flowchart, callout, stars, and 3D objects — many with small dropdown triangles indicating sub-menus. Toward the right end of the bar are an area fill color swatch (shown as a blue square), an Insert Image icon, and buttons for Arrange and Object alignment, also with dropdown arrows.

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

## UI Reference  —  Insert Menu

_Scope: Image... entry with file chooser and link-to-file option_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert dropdown menu is shown open from the Menu bar. It lists entries from top to bottom: Image..., Audio or Video..., Chart..., Table..., Media (with a submenu arrow), OLE Object (with a submenu arrow), Shape (with a submenu arrow), a separator, Snap Guide..., Text Box, Comment, Fontwork..., another separator, Hyperlink... (with a checkbox to its left), Special Character... (greyed out), and the list continues below the visible area. The **Image...** entry appears at the very top of the menu.

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
