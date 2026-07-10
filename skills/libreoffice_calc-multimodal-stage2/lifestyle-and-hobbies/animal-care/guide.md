# Animal & Pet Care Tracking (LibreOffice Calc 7.3.7)

Calc works surprisingly well as a lightweight database for pet and animal care records. A single spreadsheet can hold vaccination schedules, medication inventories, water quality logs, and hive inspection notes — each on its own sheet tab. The trick is structuring your data like a flat database table: one record per row, one field per column, with a clear header row at the top.

Start by entering dates in ISO format (YYYY-MM-DD) or with slashes — Calc recognizes common date patterns automatically. You can fine-tune how dates display by going to **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns**. For vaccination due dates or medication expiry, having consistent date formatting matters, so pick one style and stick with it.

To keep data entry clean — especially if others will use the sheet — set up cell validation. Select the target cells, then open **Data > Validity**. On the *Criteria* tab, choose what's allowed: pick *List* and type your valid entries (like vaccine names or medication types) to create a dropdown, or choose *Date* to restrict a column to dates only. Check **Show selection list** so users get a clickable dropdown right in the cell.

See `fig01.png`.

The *Input Help* tab is handy for guidance — enable **Show input help when cell is selected**, then type a short message like "Enter pH between 6.5 and 8.5" for your aquarium water quality column. On the *Error Alert* tab, you can choose whether bad data gets rejected outright (*Stop*) or just flagged with a *Warning*.

See `fig02.png`.

Once your tables grow, give them named ranges so formulas stay readable. Select your vaccination table, click in the Name Box (left of the Formula Bar), type something like "Vaccinations", and press *Enter*. You can also go to **Sheet > Named Ranges and Expressions > Define** to set this up through a dialog. Now a formula like `=COUNTIF(Vaccinations.Status,"Overdue")` instantly makes sense.

For a more database-oriented setup — where sorting and filtering settings should stick to the range — use **Data > Define Range** instead. This creates a database range that remembers its column labels, totals row, and filter state. It's ideal for a medication inventory where you'll frequently sort by expiry date or filter by medication type.

If your tracking sheets share common column headers across tabs (say "Date", "Notes", "Status"), you can auto-generate named ranges from those headers. Select the whole table including headers, then go to **Sheet > Named Ranges and Expressions > Create**. Calc reads the headers and creates one named range per column automatically.

See `fig03.png`.

For special characters — like the degree symbol (°) in aquarium temperature readings — just go to **Insert > Special Character**, find the symbol you need, and hit **Insert**. You can add frequently used symbols to your *Favorite Characters* for quick access later.

Keeping each tracking area on a separate sheet, with validated inputs and named ranges tying everything together, gives you a tidy system that's easy to maintain and hard to mess up. It won't replace a full veterinary management app, but for a small practice, hobby farm, or home aquarium setup, it's more than enough.

---

## UI Reference  —  Formula Bar

_Scope: Name Box for typing named range names directly_

The Formula bar sits below the Formatting toolbar and provides cell navigation, function insertion, and formula editing.

Read the screenshot `ui-formula-bar.png` in this directory.

## Elements (left to right)

- **Name Box** — displays current cell reference (e.g. "A1"). Click to edit, type an address and press Enter to navigate. Dropdown (▼) lists defined named ranges and "Manage Names…". During formula entry, switches to a function-name selector.

- **Function Wizard** (fx button) — opens the Function Wizard dialog with:
  - Search field to filter functions by name
  - Category dropdown (All, plus 13 categories: Math, Statistical, Text, etc.)
  - Full alphabetical function list (ABS, ACCRINT, ACOS, ADDRESS, AGGREGATE, …)
  - Formula and Result preview panels
  - Array checkbox, Back/Next navigation, Help/Cancel/OK

- **Select Function** (Σ button) — main click inserts SUM. Dropdown (▼) shows 11 common functions: Sum, Average, Min, Max, Count, CountA, Product, Stdev, StdevP, Var, VarP

- **Formula Button** (= button) — activates formula entry mode:
  - Inserts "=" in the active cell
  - Name Box changes to function-name selector (shows "SUM")
  - Σ button is replaced by **Cancel** (×, red) and **Accept** (✓, green)
  - Press Escape to cancel, Enter to accept

- **Input Line** — wide text area showing raw cell content (formula or value). Click to enter edit mode. Supports multi-line expansion.

- **Expand/Collapse Formula Bar** (▼/▲ chevron, far right) — toggles the input line between single-line and multi-line height for editing long formulas

---

## UI Reference  —  Insert Menu

_Scope: Special Character for degree symbol in aquarium temperature readings_

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

_Scope: Data > Validity for dropdown lists, Sheet > Named Ranges, Data > Define Range_

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

