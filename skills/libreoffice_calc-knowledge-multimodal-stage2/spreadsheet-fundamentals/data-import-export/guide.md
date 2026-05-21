# Data Import, Export & Transformation (LibreOffice Calc 7.3.7)

When you need to pull a CSV into Calc, just go to **File > Open** (or hit *Ctrl+O*), find your .csv or .txt file, and click **Open**. Calc will pop up the Text Import dialog, which is where the magic happens. Pick your character set (UTF-8 is usually a safe bet), choose whether fields are separated by commas, tabs, semicolons, or a fixed width, and glance at the preview at the bottom to make sure columns are lining up the way you expect. If your file has header rows you want to skip, bump the **From row** value. You can also toggle **Merge delimiters** to collapse consecutive separators, and **Trim spaces** to clean up padding in fields. Under the **Fields** preview, click any column to set its type — *Standard*, *Text*, *Date*, or even *Hide* if you want to skip importing it entirely.

See `fig01.png`.

Once the data is inside Calc, you'll eventually want to get it back out. To save in a non-ODF format like Excel, go to **File > Save As** (or *Ctrl+Shift+S*), then pick your format from the **Save as type** dropdown — say, *Excel 2007–2019 (.xlsx)*. Calc will warn you with a Confirm File Format dialog if some formatting might not survive the conversion; just click **Use [xxx] Format** to proceed. If you'd rather export as a CSV, choose *Text CSV (.csv)* and you'll get the Export Text File dialog where you can set the field delimiter, string delimiter, and character set. Keep in mind that once you save as a different format, Calc treats that as your working file — if you need the .ods version back, save again as ODF.

See `fig02.png`.

For sharing data as a PDF, the quickest route is the **Export Directly as PDF** toolbar button, which uses your last-used settings. For more control, go to **File > Export as PDF** to open the PDF Options dialog. The *General* tab lets you pick a page range, choose image compression quality, and toggle options like **Tagged PDF** for accessibility or **Whole Sheet Export** to render an entire sheet as one continuous page. Note that unlike **Save As**, the **Export** command writes a copy — your current .ods stays open and untouched.

When your flat data needs reshaping — say, pivoting sales figures by region and employee — pivot tables are your friend. Select your data range, then go to **Insert > Pivot Table**. In the Select Source dialog, confirm **Current selection** and click **OK**. The Pivot Table Layout dialog opens with your field names listed under *Available Fields*. Just drag and drop: pull a field like *Region* into *Row Fields*, *Category* into *Column Fields*, and *Sales Value* into *Data Fields* (it defaults to a sum). Fields dropped into the *Filters* area become dropdown filters at the top of the resulting table. Rearranging is easy — drag a field to a different area or back to *Available Fields* to remove it.

See `fig03.png`.

Expand the *Options* section at the bottom of that dialog if you need to toggle **Total columns**, **Total rows**, or **Ignore empty rows**. The *Source and Destination* section lets you point the output to a new sheet or a specific cell range. Once you click **OK**, Calc generates the pivot table — and you can always re-edit it later by right-clicking any cell in the table and choosing **Properties**.

To email a spreadsheet directly, go to **File > Send** and pick a format: *Email Document* sends it as-is, *Email as Microsoft Excel* converts to .xlsx on the fly, and *Email as PDF* runs through the PDF export first. It's a handy shortcut when a colleague just needs a quick copy and you don't want to fuss with manual export steps.

---

## UI Reference  —  Export as PDF Dialog

_Scope: File > Export as PDF dialog: General tab page range, image compression, Tagged PDF, Whole Sheet Export_

The PDF Options dialog (File > Export as PDF…) provides comprehensive control over PDF generation with 6 tabs.

Read the screenshot `ui-pdf-options-dialog.png` in this directory.

## Tabs

### General
- **Range**: All / Pages (text field) / Selection/Selected sheet(s)
- **View PDF after export** checkbox
- **Images**: Lossless compression / JPEG compression (Quality 90%) / Reduce image resolution (300 DPI dropdown)
- **Watermark**: Sign with watermark checkbox + text field
- **General settings**: Hybrid PDF (embed ODF), Archival PDF/A (version PDF/A-3b), Universal Accessibility (PDF/UA), Tagged PDF (checked), Create PDF form (Submit format: FDF), Allow duplicate field names
- **Structure**: Export outlines (checked), Comments as PDF annotations, Comments in margin, Whole sheet export, Export automatically inserted blank pages, Use reference XObjects

### Initial View
- **Panes**: Page only / Outline and page (selected) / Thumbnails and page
- **Open on page**: spinner (default 1)
- **Page Layout**: Default / Single page / Continuous / Continuous facing
- **Magnification**: Default / Fit in window / Fit width / Fit visible / Zoom factor (100)

### User Interface
- **Window Options**: Resize window to initial page, Center window, Open in full screen, Display document title (checked)
- **User Interface Options**: Hide menubar, Hide toolbar, Hide window controls
- **Transitions**: Use transition effects (checked)
- **Collapse Outlines**: Show All / Visible levels spinner

### Links
- Export bookmarks as named destinations, Convert document references to PDF targets, Export URLs relative to file system (checked)
- **Cross-document Links**: Default mode / Open with PDF reader / Open with Internet browser

### Security
- **File Encryption**: Set Passwords… button
- **Printing**: Not permitted / Low resolution (150 dpi) / High resolution (selected)
- **Changes**: Not permitted / Inserting pages / Filling forms / Commenting / Any except extracting (selected)
- **Content**: Enable copying (checked), Enable text access for accessibility (checked)

### Digital Signatures
- Certificate: Select…/Clear buttons, certificate field
- Certificate password, Location, Contact information, Reason fields
- Time Stamp Authority dropdown

---

## UI Reference  —  File Menu

_Scope: File > Open for CSV import, Save As for format conversion, Export as PDF, Send submenu for emailing_

The File menu provides document lifecycle operations: creating, opening, saving, exporting, printing, and managing document properties.

Read the screenshot `ui-file-menu-expanded.png` in this directory.

## Elements

- **New** (Ctrl+N) — submenu listing document types: Spreadsheet, Text Document, Presentation, Drawing, Formula, Database, HTML Document, XML Form Document, Labels, Business Cards, Master Document, Templates
- **Open…** (Ctrl+O) — file picker to open an existing document
- **Open Remote…** — connect to and open a file from a remote server
- **Recent Documents** — submenu of recently opened files
- **Close** — closes the current document
- **Wizards** — submenu: Letter, Fax, Agenda, Document Converter, Address Data Source
- **Templates** — submenu: Edit Template, Save as Template (Shift+F11), Manage Templates (Shift+Ctrl+N)
- **Reload** — reloads from disk (greyed on unsaved documents)
- **Versions…** — document version manager (greyed on unsaved documents)
- **Save** (Ctrl+S), **Save As…** (Shift+Ctrl+S), **Save Remote…**, **Save a Copy…**, **Save All**
- **Export…** — export in various formats via file picker
- **Export as PDF…** — opens the PDF Options dialog (see [export-pdf-dialog](export-pdf-dialog.md))
- **Send** — submenu: Email Document, Email as ODS/Excel/PDF, Send via Bluetooth
- **Preview in Web Browser** — exports to temporary HTML and opens in browser
- **Print Preview** (Shift+Ctrl+O) — toggles print preview mode
- **Print…** (Ctrl+P) — opens Print dialog (General + LibreOffice Calc tabs)
- **Printer Settings…** — printer selection and configuration
- **Properties…** — document metadata dialog (6 tabs: General, Description, Custom Properties, Security, Font, Statistics)
- **Digital Signatures** — submenu: Digital Signatures…, Sign Existing PDF…
- **Exit LibreOffice** (Ctrl+Q)

### Save As Format Options

The Save As dialog supports 16 file formats:
ODS, OTS, FODS, UOS, XLSX, XLTX, XLS, XLT, DIF, DBF, HTML, SLK, CSV, Office Open XML (.xlsx), XLSM.

---

## UI Reference  —  Insert Menu

_Scope: Pivot Table for data transformation and reshaping_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

Read the screenshot `ui-insert-menu-expanded.png` in this directory.

## Elements

- **Image…** — file browser to insert an image
- **Chart…** — inserts a chart object from selected data
- **Sparkline…** — inserts a mini-chart within a cell
- **Pivot Table…** — inserts or edits a pivot table
- **Media** — submenu: Gallery, Scan (Select Source, Request), Audio or Video…
- **OLE Object** — submenu: Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** — submenu with 7 categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart
- **Function…** (Ctrl+F2) — opens Function Wizard dialog with search, category filter, and full function library
- **Named Range or Expression…** — opens Paste Names dialog showing defined named ranges
- **Text Box** — checkbox toggle to insert a text box
- **Comment** (Ctrl+Alt+C) — inserts a cell comment
- **Fontwork…** — decorative text effects
- **Hyperlink…** (Ctrl+K) — opens Hyperlink dialog (4 tabs: Internet, Mail, Document, New Document)
- **Special Character…** — Unicode character picker
- **Formatting Mark** — submenu: No-break Space, Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner (all greyed in normal cell mode)
- **Date** (Ctrl+;), **Time** (Shift+Ctrl+;) — insert current date/time
- **Field** — submenu: Date, Sheet Name, Document Title
- **Headers and Footers…** — opens headers/footers editor dialog
- **Form Control** — submenu with 21 form controls: Label, Text Box, Check Box, Option Button, List Box, Combo Box, Push Button, Image Button, Formatted Field, Date/Time/Numerical/Currency/Pattern Field, Group Box, Image Control, File Selection, Table Control, Navigation Bar, Spin Button, Scrollbar
- **Signature Line…**

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Pivot Table submenu for refreshing and managing pivot tables_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

(see screenshot `ui-sheet-menu-expanded.png`)

(see screenshot `ui-data-menu-expanded.png`)

## Sheet Menu Elements

### Cell/Row/Column Operations
- **Insert Cells…** (Ctrl++) — dialog: Shift cells down/right, Entire row/column
- **Insert Rows** — submenu: Rows Above, Rows Below
- **Insert Columns** — submenu: Columns Before, Columns After
- **Insert Page Break** — submenu: Row Break, Column Break
- **Delete Cells…** (Ctrl+-), **Delete Rows**, **Delete Columns**, **Delete Page Break**
- **Clear Cells…** (Backspace) — selective content clearing
- **Cycle Cell Reference Types** (F4) — toggles absolute/relative references

### Fill and Ranges
- **Fill Cells** — submenu: Fill Down (Ctrl+D), Fill Right/Up/Left, Fill Sheets…, Fill Series…, Fill Random Number…
- **Named Ranges and Expressions** — submenu: Define…, Manage… (Ctrl+F3), Insert…, Create…, Labels…
- **Cell Comments** — submenu: Edit Comment (Ctrl+Alt+C), Hide/Show/Delete Comment, Delete All Comments

### Sheet Management
- **Insert Sheet…**, **Insert Sheet at End…**, **Insert Sheet from File…**
- **External Links…**, **Delete Sheet…** (greyed with single sheet)
- **Rename Sheet…**, **Hide Sheet**, **Show Sheet…**
- **Move or Copy Sheet…**, **Duplicate Sheet**
- **Navigate** — submenu: Go to Sheet…, To Previous Sheet (Shift+Ctrl+Tab), To Next Sheet (Ctrl+Tab)
- **Sheet Tab Color…** — colour picker for sheet tab
- **Sheet Events…**, **Right-To-Left**

## Data Menu Elements

- **Sort…** — multi-level sort dialog
- **Sort Ascending**, **Sort Descending** — one-click sort
- **AutoFilter** (Shift+Ctrl+L) — toggles filter dropdowns on column headers
- **More Filters** — submenu: Standard Filter…, Advanced Filter…, Reset Filter, Hide AutoFilter
- **Define Range…**, **Select Range…**, **Refresh Range**
- **Pivot Table** — submenu: Insert or Edit…, Refresh, Delete
- **Calculate** — submenu: Recalculate (F9), Recalculate Hard (Shift+Ctrl+F9), Formula to Value, AutoCalculate (toggle, on by default)
- **Validity…** — input validation rules and error alerts
- **Subtotals…** — automatic subtotal insertion
- **Form…**, **Streams…**, **XML Source…**, **Multiple Operations…**
- **Text to Columns…** — split cell text by delimiter
- **Consolidate…**
- **Group and Outline** — submenu: Group… (F12), Ungroup… (Ctrl+F12), AutoOutline, Remove Outline, Hide/Show Details
- **Statistics** — 13 statistical tools: Sampling, Descriptive Statistics, ANOVA, Correlation, Covariance, Exponential Smoothing, Moving Average, Regression, Paired t-test, F-test, Z-test, Chi-square Test, Fourier Analysis

