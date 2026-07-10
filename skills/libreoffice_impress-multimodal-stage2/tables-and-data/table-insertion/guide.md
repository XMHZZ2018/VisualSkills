# Table Insertion (LibreOffice Impress 7.3.7)

Tables in Impress are a quick way to present structured data right on a slide without embedding a Calc spreadsheet. They're a bit simpler than what you'd get in Calc or Writer, but for most presentation needs they work great.

To insert a table, head to **Insert > Table** on the Menu bar. A small dialog pops up asking for the number of columns and rows — set those and hit **OK**. The table lands in the center of your slide inside a text box, ready for you to start typing.

There's also a visual shortcut: click the **Table** icon on the Standard toolbar and a grid graphic appears. Just drag across the grid to select how many rows and columns you want, then release. If the grid isn't big enough, click **More Options** at the bottom to fall back to the dialog approach.

Once the table is on your slide, click into any cell and start typing your data. Use **Tab** to move forward through cells and **Shift+Tab** to go back. The table auto-sizes cells to match the default style, so you can focus on content first and worry about formatting later.

To polish the look, open the **Table Design** panel in the Properties deck on the Sidebar. You'll find a gallery of predefined color schemes, plus checkboxes for **Header row**, **Total row**, **Banded rows**, **First column**, **Last column**, and **Banded columns** — toggle these to get alternating shading or highlighted headers without any manual color-picking.

See `fig01.png`.

For finer control, right-click the table and choose **Table Properties** (or go to **Format > Table > Properties**). This opens a dialog with five tabs — **Font**, **Font Effects**, **Borders**, **Background**, and **Shadow** — letting you dial in everything from typeface and cell padding to border styles and drop shadows.

Need to adjust the table structure after creation? Right-click a cell and use the **Insert** submenu to add rows above or below, or columns before or after. To remove structure, the same context menu offers **Delete Row**, **Delete Column**, or **Delete Table**. You can also merge cells by selecting them and choosing **Merge Cells** from the right-click menu, or split a cell via **Split Cells** to subdivide it horizontally or vertically.

The Table toolbar appears automatically when a table is selected (if not, enable it via **View > Toolbars > Table**). It gives one-click access to border styles, cell colors, merge/split, row and column sizing with the **Optimize** dropdown, and text alignment — pretty much everything you need without diving into menus.

---

## UI Reference  —  Format Menu

_Scope: Table submenu for post-insertion formatting_

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

_Scope: Table... entry opening Insert Table dialog with columns/rows spinners_

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

## UI Reference  —  Insert Table

_Scope: Insert Table dialog, Table Design sidebar panel, cell editing toolbar, context menus, navigation_

Insert > Table creates a table on the slide with configurable rows and columns. Once inserted, the Properties sidebar shows Table Design options and a specialized toolbar appears at the bottom.

Read the screenshot `ui-table-inserted.png` in this directory.

## Insert Table Dialog

- **Number of columns** — spin field (default 5, min 1)
- **Number of rows** — spin field (default 2, min 1)
- Help / Cancel / OK buttons

## Table Design (Properties Sidebar)

- **Style thumbnails** — two rows of predefined color schemes; clicking applies immediately
- **Header row** (default: checked) — distinct styling on first row
- **First column** / **Last column** — distinct styling on edge columns
- **Total row** — distinct styling on last row
- **Banded rows** (default: checked) / **Banded columns** — alternating row/column shading

## Cell Editing Toolbar (bottom of window)

Appears when a table cell is active:

- **Merge Cells** / **Split Cells** (opens dialog: split count, horizontal/vertical, equal proportions)
- **Optimize** (split button) — Minimal Column Width, Minimal Row Height, Optimal Column Width, Optimal Row Height
- **Align Top / Center Vertically / Align Bottom** — vertical text alignment in cells
- **Insert Row Above/Below**, **Insert Column Before/After**
- **Delete Row / Delete Columns / Delete Table**
- **Table Properties** — opens 5-tab dialog: Font, Font Effects, Borders, Background, Shadow

## Context Menus

- **Table selected**: Cut/Copy/Paste, Insert (6 options), Delete, Size, Character, Paragraph, Align Objects, Arrange, Table Position and Size, Table Properties
- **Cell editing**: adds Merge Cells, Split Cells; Delete expands to Delete Row/Columns/Table

## Navigation

- Tab moves between cells; Tab in last cell appends a new row
- Escape returns from cell-edit to table-selected mode

---

## UI Reference  —  Standard Toolbar

_Scope: Table quick-insert icon with drag grid_

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

