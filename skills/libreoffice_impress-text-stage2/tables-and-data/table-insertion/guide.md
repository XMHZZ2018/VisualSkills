# Table Insertion (LibreOffice Impress 7.3.7)

Tables in Impress are a quick way to present structured data right on a slide without embedding a Calc spreadsheet. They're a bit simpler than what you'd get in Calc or Writer, but for most presentation needs they work great.

To insert a table, head to **Insert > Table** on the Menu bar. A small dialog pops up asking for the number of columns and rows — set those and hit **OK**. The table lands in the center of your slide inside a text box, ready for you to start typing.

There's also a visual shortcut: click the **Table** icon on the Standard toolbar and a grid graphic appears. Just drag across the grid to select how many rows and columns you want, then release. If the grid isn't big enough, click **More Options** at the bottom to fall back to the dialog approach.

Once the table is on your slide, click into any cell and start typing your data. Use **Tab** to move forward through cells and **Shift+Tab** to go back. The table auto-sizes cells to match the default style, so you can focus on content first and worry about formatting later.

To polish the look, open the **Table Design** panel in the Properties deck on the Sidebar. You'll find a gallery of predefined color schemes, plus checkboxes for **Header row**, **Total row**, **Banded rows**, **First column**, **Last column**, and **Banded columns** — toggle these to get alternating shading or highlighted headers without any manual color-picking.

The Properties sidebar is shown with collapsed sections for Character, Lists, and Paragraph at the top, and an expanded Table Design section below. The Table Design area displays a gallery of eleven predefined table style thumbnails arranged in a grid — styles range from a plain black-and-white scheme to colored variants in red, teal, blue, purple, orange, green, and yellow, each showing banded rows and a darker header row. Below the gallery are six checkboxes in two columns: "Header row" and "Banded rows" are checked, while "Total row," "First column," "Last column," and "Banded columns" are unchecked.

For finer control, right-click the table and choose **Table Properties** (or go to **Format > Table > Properties**). This opens a dialog with five tabs — **Font**, **Font Effects**, **Borders**, **Background**, and **Shadow** — letting you dial in everything from typeface and cell padding to border styles and drop shadows.

Need to adjust the table structure after creation? Right-click a cell and use the **Insert** submenu to add rows above or below, or columns before or after. To remove structure, the same context menu offers **Delete Row**, **Delete Column**, or **Delete Table**. You can also merge cells by selecting them and choosing **Merge Cells** from the right-click menu, or split a cell via **Split Cells** to subdivide it horizontally or vertically.

The Table toolbar appears automatically when a table is selected (if not, enable it via **View > Toolbars > Table**). It gives one-click access to border styles, cell colors, merge/split, row and column sizing with the **Optimize** dropdown, and text alignment — pretty much everything you need without diving into menus.

---

## UI Reference  —  Format Menu

_Scope: Table submenu for post-insertion formatting_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format menu is shown open from the menu bar. It lists entries from top to bottom: Text, Spacing, Align Text (currently highlighted in blue), Lists, Clear Direct Formatting, Styles, Character…, Paragraph…, Bullets and Numbering…, Theme…, Table, Image, Text Box and Shape, a Shadow checkbox, Interaction…, Name…, Alt Text…, and the list continues with Distribute Selection partially visible at the bottom. Submenu arrows appear next to items that expand into further options.

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

_Scope: Table... entry opening Insert Table dialog_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert menu is shown open from the menu bar. Its entries from top to bottom are: Image…, Audio or Video…, Chart…, Table…, Media, OLE Object, Shape, a separator, Snap Guide…, Text Box, Comment, Fontwork…, a Hyperlink… entry with an unchecked checkbox, and Special Character… grayed out at the bottom. Several entries such as Media, OLE Object, and Shape have submenu arrows indicating expandable submenus.

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

## UI Reference  —  Standard Toolbar

_Scope: Table quick-insert icon with drag grid_

The first icon row below the menu bar. Provides quick access to common file and editing operations.

The Standard toolbar is displayed as a single horizontal row of small icons. From left to right, it includes icons for New (with dropdown arrow), Open (with dropdown), Save (with dropdown), Email Document, Edit File, PDF export, and Print, followed by Cut, Copy, and Paste icons. Next come the Paint Format (clone formatting) brush, Undo and Redo arrows, a Find & Replace magnifying glass, and a Spelling check icon. The right portion of the toolbar contains view-mode toggle buttons, a Presentation (slideshow) button, then quick-insert icons for Table (highlighted with an orange border indicating it is active), Insert Chart, Insert Text Box, a Hyperlink icon, a Sidebar toggle, and a Start Center button at the far right.

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
