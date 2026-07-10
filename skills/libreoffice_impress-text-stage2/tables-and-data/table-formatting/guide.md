# Table Creation & Formatting (LibreOffice Impress 7.3.7)

Tables in Impress are a quick way to lay out structured comparisons right on a slide — no need to embed a Calc spreadsheet unless you need formulas or advanced features.

To drop in a table, go to **Insert > Table** on the Menu bar. A small dialog asks for the number of columns and rows — set these to match your comparison (say, 3 columns and 5 rows for a feature comparison), then hit **OK**. The table lands centered on the slide inside a text box. Alternatively, click the **Table** icon on the Standard toolbar and drag across the grid to visually pick your dimensions.

Once the table exists, click inside any cell and start typing. To move between cells, just press Tab. For a comparison layout, you'll typically want a header row across the top and category labels down the first column. Keep text short — slides aren't spreadsheets.

To align text within cells, select the cells you want, then right-click and choose **Align** from the context menu, or use **Format > Align Text** from the Menu bar. You can pick **Align Top**, **Center Vertically**, or **Align Bottom** to get everything sitting neatly. Consistent vertical centering makes comparison tables much easier to scan.

For quick visual styling, open the **Table Design** panel in the Properties deck on the Sidebar. It offers a grid of predefined color schemes. Toggle the checkboxes at the bottom — **Header row**, **Banded rows**, **First column**, **Last column** — to control which parts get accented. Banded rows are on by default and really help readability in dense tables. The Sidebar's Properties deck shows the Table Design section with a scrollable grid of thumbnail previews, each depicting a different color scheme applied to a sample table. Below the grid, a row of checkboxes labeled "Header row," "Banded rows," "First column," and "Last column" lets you toggle which structural parts receive accent styling.

Now for conditional cell coloring — Impress doesn't have automatic conditional formatting like Calc, so you color cells manually. Select the cells you want to highlight, then use the **Area Style/Filling** dropdown on the Table toolbar to choose *Color*, and pick your shade from the second dropdown. For more control, right-click the selected cells and choose **Table Properties**, then switch to the **Background** tab. There you can set a precise color (by palette, hex value, or RGB), or even apply a gradient or pattern.

The Table Properties dialog is open to the Background tab, which displays a large color picker grid showing named palette swatches along with fields for entering a custom color by hex value or RGB sliders. A "Pick" button opens an advanced color chooser, and the bottom of the tab includes a preview strip comparing the old and new background colors side by side.

A practical approach for comparison tables: use green for "yes/pass" cells, red or orange for "no/fail", and a neutral gray for "partial." Select each group of cells and apply the fill color in one pass. If you need to tweak borders — say, to visually separate sections — open **Table Properties** and go to the **Borders** tab, where you can set line style, color, width, and cell padding.

To resize columns evenly, select the columns and use the **Optimize** tool on the Table toolbar, then pick **Distribute Columns Evenly**. Same goes for rows. If you need to merge header cells spanning multiple columns, select them and hit **Merge Cells** on the Table toolbar or via **Format > Table > Merge Cells**. The overall table position and size are controlled through the Position and Size dialog, just like any other graphic object on the slide.

---

## UI Reference  —  Format Menu

_Scope: Table submenu: Merge Cells, Properties, Align Text_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

The Format drop-down menu is shown expanded from the Menu bar. It lists entries from top to bottom including Text, Spacing, Align Text, Lists, Clear Direct Formatting, Styles, Character…, Paragraph…, Bullets and Numbering…, Theme…, Table, Image, Text Box and Shape, Shadow, Interaction…, Name…, Alt Text…, Distribute Selection, Rotate, Flip, Convert, Align Objects, Arrange, and Group — many with right-arrow indicators for submenus and keyboard shortcuts displayed to the right of each item.

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

_Scope: Table... for initial table creation before formatting_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

The Insert drop-down menu is shown expanded from the Menu bar. It lists entries from top to bottom including Image…, Audio or Video…, Chart…, Table…, Media, OLE Object, Shape, Snap Guide…, Text Box, Comment, Fontwork…, Hyperlink…, Special Character…, Formatting Mark, Slide Number, Field, Header and Footer…, and Form Control — with right-arrow indicators on submenu items and keyboard shortcuts such as F2 for Text Box and Ctrl+K for Hyperlink displayed alongside the relevant entries.

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
