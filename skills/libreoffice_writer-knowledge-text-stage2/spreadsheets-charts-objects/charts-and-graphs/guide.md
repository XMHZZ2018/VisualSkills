# Charts and Graphs (LibreOffice Writer 7.3.7)

Writer lets you embed charts directly into your documents — no need to build them in Calc first (though you can paste from a spreadsheet as an OLE object if you prefer). To insert a fresh chart, go to **Insert > Chart**. Writer drops a generic column chart with sample data right at your cursor, and the menu bar and toolbars switch to chart-editing mode.

The default chart that Writer inserts is a grouped column chart populated with sample data. It shows four categories labeled "Row 1" through "Row 4" along the horizontal axis, with numeric values on the vertical axis ranging from 0 to about 12. Three data series — "Column 1" (dark blue), "Column 2" (red-orange), and "Column 3" (yellow) — are displayed as side-by-side bars for each category, and a legend identifying the three series appears to the right of the plot area. The chart is surrounded by green square selection handles indicating it is in edit mode.

While the chart is selected and in edit mode, you can pick a different chart type by clicking the **Chart Type** icon on the Formatting toolbar, or via **Format > Chart Type**. The dialog lists all the available types — Column, Bar, Pie, Line, Area, XY (Scatter), Bubble, Net, Stock, and Column and Line — with options for 2D, 3D, and various shape variants on the right-hand side. Column charts are great for trends over time, bar charts for quick visual comparisons, pie charts for proportions, and line charts for continuous data. Scatter and bubble charts shine when you're plotting two or three variables against each other.

The Chart Type dialog has a list of chart types on the left — Column, Bar, Pie, Area, Line, XY (Scatter), Bubble, Net, Stock, and Column and Line — each with a small icon, and "Column" is currently selected and highlighted. The upper-right area displays thumbnail previews of layout variants for the selected type (e.g., normal grouped, stacked, and percent-stacked column arrangements), with the first "Normal" variant selected. Below the previews is a "3D Look" checkbox (unchecked) with a "Realistic" dropdown beside it. At the bottom right, a "Shape" list offers Bar, Cylinder, Cone, and Pyramid options, with "Bar" currently highlighted. The dialog has Help, Cancel, and OK buttons along the bottom.

To swap in your own data, click the **Data Table** icon or go to **View > Data Table**. This opens a small spreadsheet-like grid right inside the chart where you can type, paste, or rearrange values. Use the icons in the top-left corner of the Data Table dialog to insert, delete, or move rows and columns.

Every chart comes with two main pieces: a chart wall (the plot background) and a chart legend. You can add or remove elements — titles, grid lines, data labels, and more — by going to **Insert** on the menu bar while in edit mode, or by right-clicking the chart wall or a specific element and choosing from the context menu. To remove something, right-click it and choose **Delete**, or just select it and press the *Del* key.

Formatting works the same way: select the chart (or double-click to enter edit mode), then go to **Format** and pick the element you want to style, or right-click any element directly for its format options. The available settings change depending on whether you've selected the whole chart or a specific part like an axis or data series.

To resize a chart, click it once so the selection handles appear, then drag a handle. Hold **Shift** while dragging a corner handle to keep the aspect ratio. You can also move a chart by clicking it, waiting for the cursor to change, and dragging it to a new spot. For precise control, double-click the chart to enter edit mode, then use **Format > Position and Size** (or right-click and choose **Position and Size**) to type exact coordinates.

---

## UI Reference  —  Insert Menu

_Scope: Chart… OLE object_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown open in the Writer menu bar. It is a single-column dropdown listing the following items from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several entries have a right-pointing arrow indicating a submenu, and a few items such as Hyperlink and Horizontal Line have small icons to their left.

## Elements

- **Page Break** (Ctrl+Return) — Insert a manual page break at cursor.
- **More Breaks** (►) — Manual Row Break (Shift+Return), Column Break (Shift+Ctrl+Return), Manual Break… (dialog to choose break type and page style).
- **Image…** — Open file chooser to insert a raster or vector image.
- **Chart…** — Embed a chart OLE object.
- **Media** (►) — Gallery, Scan, Audio or Video…
- **OLE Object** (►) — Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** (►) — 7 shape categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart — each opens a named-shape palette.
- **Section…** — Opens Insert Section dialog (tabs: Section, Columns, Indents, Area, Footnotes/Endnotes). Supports linked sections, write protection, and conditional hiding.
- **Text from File…** — Insert text from an external file.
- **Text Box** — Draw a floating text frame on the canvas.
- **Comment** (Ctrl+Alt+C) — Insert an annotation balloon.
- **Frame** (►) — Frame Interactively (draw) or Frame… (dialog).
- **Fontwork…** — Decorative text shapes gallery.
- **Hyperlink…** (Ctrl+K) — Hyperlink dialog with 4 type modes: Internet, Mail, Document, New Document.
- **Bookmark…** — Insert/manage bookmarks.
- **Cross-reference…** — Link to headings, bookmarks, figures, or other elements.
- **Special Character…** — Character picker dialog with search, font/block selectors, hex/decimal codes, favorites/recent.
- **Formatting Mark** (►) — No-break Space (Shift+Ctrl+Space), Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner.
- **Horizontal Line** — Insert a horizontal rule.
- **Footnote and Endnote** (►) — Insert Footnote, Endnote, or open the Footnote/Endnote dialog.
- **Table of Contents and Index** (►) — TOC/Index/Bibliography dialog, Index Entry, Bibliography Entry.
- **Page Number…** — Page number insertion dialog.
- **Field** (►) — Page Number, Page Count, Date/Time (fixed or variable), Title, Author, Subject, More Fields… (Ctrl+F2).
- **Header and Footer** (►) — Enable/disable headers and footers per page style.
- **Envelope…** — Envelope configuration dialog.
- **Signature Line…** — Digital-signature placeholder line.
