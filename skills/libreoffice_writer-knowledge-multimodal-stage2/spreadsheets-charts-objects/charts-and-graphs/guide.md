# Charts and Graphs (LibreOffice Writer 7.3.7)

Writer lets you embed charts directly into your documents — no need to build them in Calc first (though you can paste from a spreadsheet as an OLE object if you prefer). To insert a fresh chart, go to **Insert > Chart**. Writer drops a generic column chart with sample data right at your cursor, and the menu bar and toolbars switch to chart-editing mode.

See `fig01.png`.

While the chart is selected and in edit mode, you can pick a different chart type by clicking the **Chart Type** icon on the Formatting toolbar, or via **Format > Chart Type**. The dialog lists all the available types — Column, Bar, Pie, Line, Area, XY (Scatter), Bubble, Net, Stock, and Column and Line — with options for 2D, 3D, and various shape variants on the right-hand side. Column charts are great for trends over time, bar charts for quick visual comparisons, pie charts for proportions, and line charts for continuous data. Scatter and bubble charts shine when you're plotting two or three variables against each other.

See `fig02.png`.

To swap in your own data, click the **Data Table** icon or go to **View > Data Table**. This opens a small spreadsheet-like grid right inside the chart where you can type, paste, or rearrange values. Use the icons in the top-left corner of the Data Table dialog to insert, delete, or move rows and columns.

Every chart comes with two main pieces: a chart wall (the plot background) and a chart legend. You can add or remove elements — titles, grid lines, data labels, and more — by going to **Insert** on the menu bar while in edit mode, or by right-clicking the chart wall or a specific element and choosing from the context menu. To remove something, right-click it and choose **Delete**, or just select it and press the *Del* key.

Formatting works the same way: select the chart (or double-click to enter edit mode), then go to **Format** and pick the element you want to style, or right-click any element directly for its format options. The available settings change depending on whether you've selected the whole chart or a specific part like an axis or data series.

To resize a chart, click it once so the selection handles appear, then drag a handle. Hold **Shift** while dragging a corner handle to keep the aspect ratio. You can also move a chart by clicking it, waiting for the cursor to change, and dragging it to a new spot. For precise control, double-click the chart to enter edit mode, then use **Format > Position and Size** (or right-click and choose **Position and Size**) to type exact coordinates.

---

## UI Reference  —  Chart Editing Mode

_Scope: Entire chart editing mode: toolbar, Chart Type dialog, Data Table editor, formatting menus, context menus_

Insert > Chart inserts a default grouped-column chart (4 rows x 3 series) and immediately enters chart editing mode. The menu bar, toolbar, and status bar all change to chart-specific variants. Double-click a chart to re-enter editing mode; click outside or press Escape to return to Writer.

Read the screenshot `ui-chart-editing-mode.png` in this directory.

## Chart Editing Toolbar (left to right)

- **Element selector** dropdown — Lists all chart sub-elements: Chart Area, Chart, Legend, X/Y/Z Axes, Grids, Data Series. Selecting changes the active element.
- **Format Selection** — Opens a formatting dialog for the currently selected element.
- **Chart Type** — Opens Chart Type dialog (10 categories: Column, Bar, Pie, Area, Line, XY Scatter, Bubble, Net, Stock, Column and Line; sub-type grid; 3D Look; shape variants).
- **Chart Area** / **Chart Wall** — Quick-select buttons for the outermost frame or plot background.
- **3D View** — Opens 3D rotation/perspective dialog (requires 3D mode).
- **Data Ranges** — Data range configuration (requires externally linked data).
- **Data Table** — Opens spreadsheet-like data editor for embedded chart data.
- **Titles** — Set chart title, subtitle, and axis labels.
- **Legend On/Off** — Toggle legend visibility.
- **Legend** — Select legend for formatting.
- **Horizontal Grids** / **Vertical Grids** — Toggle grid line visibility.
- **X Axis** / **Y Axis** / **Z Axis** / **All Axes** — Quick-select axis elements.

## Chart-Specific Menus

**Insert menu** (in chart editing mode): Titles..., Legend..., Axes..., Grids..., Data Table..., Data Labels..., Trend Line..., Mean Value Lines, X/Y Error Bars..., Special Character...

**Format menu** (in chart editing mode): Title (submenu with Main/Sub/all axis titles), Legend..., Axis (submenu: X/Y/Z/Secondary/All), Grid (submenu), Chart Wall..., Chart Floor..., Chart Area..., Chart Type..., Data Ranges..., 3D View..., Format Selection..., Position and Size... (F4), Arrangement.

## Key Dialogs

**Chart Type:** Category list + sub-type thumbnail grid. Column/Bar support shape variants (Bar/Cylinder/Cone/Pyramid). Line chart adds Stack/Properties. 3D Look checkbox with Realistic/Simple rendering.

**Data Table (editing):** Spreadsheet grid with toolbar: Insert/Delete Row/Series, Move Series Left/Right, Move Row Up/Down. Column headers show series names with color swatches. Changes apply live.

**Titles:** Text fields for chart title, subtitle, and X/Y/Z axis labels plus secondary axis labels.

**Axes (Insert/Delete):** Checkboxes for X/Y/Z axes and secondary X/Y axes.

**Chart Wall / Chart Area:** 3-tab dialog (Borders, Area, Transparency). Area tab supports None/Color/Gradient/Image/Pattern/Hatch fills.

**Format Data Series:** Options tab (align to primary/secondary Y axis, spacing/overlap %, missing value handling, hide legend entry), Area tab (fill options), Transparency tab, Borders tab.

## Context Menus

- **Right-click chart wall:** Format Wall..., Position and Size..., Insert Titles..., Insert/Delete Axes..., Delete Legend, Chart Type..., Data Table...
- **Right-click data series:** Format Data Series..., Insert Data Labels, Insert Trend Line/Mean Value Line/Error Bars..., Arrangement, Chart Type..., Data Table...
- **Right-click chart as Writer object** (outside editing mode): Cut, Copy, Paste, Anchor, Wrap, Align Objects, Arrange, Insert Caption..., Properties..., Edit.

---

## UI Reference  —  Insert Menu

_Scope: Chart… command to embed chart OLE object_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

Read the screenshot `ui-insert-menu.png` in this directory.

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

