# Hobby & Activity Log Analysis (LibreOffice Calc 7.3.7)

Tracking hobbies — books read, practice sessions, hikes completed, photos taken — is satisfying, but a flat list of entries only gets you so far. Calc gives you the tools to turn raw logs into something you can actually learn from: spotting trends, comparing periods, and summarizing effort across activities.

Start by laying out your log with consistent column headers — Date, Activity, Category, Duration, Notes — one entry per row. Keeping the structure clean from the beginning makes everything downstream easier. Use **Data > Sort** to reorder your log whenever you add new entries at the bottom; on the *Sort Criteria* tab, pick your Date column as Sort Key 1 and set it to **Ascending** so the timeline reads naturally. If your log mixes activity types, add a second sort key on the Category column to group related entries together.

See `fig01.png`.

Once your log grows, you'll want to zero in on specific activities without losing the rest of your data. Turn on **Data > AutoFilter** to get drop-down arrows on each header — click one and select, say, "Photography" or "Reading" to instantly hide everything else. For more complex slicing (e.g., all outdoor activities longer than 60 minutes), use **Data > More Filters > Advanced Filter**, where you define criteria in a separate cell range and reference it in the dialog.

To quickly locate a specific entry — a particular book title or trail name — press *Ctrl+F* to pop open the Find toolbar. Type your term, toggle **Match Case** if needed, and click **Find Next** to jump right to it.

For summarizing your logs numerically, basic functions go a long way. `=COUNT(D2:D500)` tells you how many sessions you've logged, `=SUM(D2:D500)` totals your hours, and `=AVERAGE(D2:D500)` gives you a per-session average. Use `=MIN()` and `=MAX()` to find your shortest and longest sessions, and `=COUNTIF(C2:C500,"Music Practice")` to count entries for a single category.

When you want a full statistical snapshot — mean, median, standard deviation, and more — all at once, go to **Data > Statistics > Descriptive Statistics**. Point the *Input range* at your duration column, set a *Results to* cell, and hit **OK**. Calc generates a complete report including variance, kurtosis, and skewness, which can reveal whether your practice habits are consistent or wildly uneven.

See `fig02.png`.

For the richest view of your data, pivot tables are hard to beat. Select your log range and go to **Insert > Pivot Table**. In the Select Source dialog, keep **Current selection** checked and click **OK** to open the Pivot Table Layout dialog. Drag "Category" into the *Row Fields* area, "Date" into *Column Fields*, and "Duration" into *Data Fields* (it defaults to Sum). Now you have a matrix showing total time per activity per period — instantly revealing where your hours actually go.

See `fig03.png`.

To refine the pivot table further, drag a field like "Location" or "Rating" into the *Filters* area — this adds a drop-down at the top of the resulting table so you can slice the summary without rebuilding it. You can revisit the layout anytime by clicking inside the pivot table and selecting **Data > Pivot Table > Insert or Edit**.

That's really the whole workflow: structure your log, sort and filter to focus, use functions and descriptive statistics to summarize, and pivot tables to cross-analyze. Keep logging consistently and Calc handles the rest.

---

## UI Reference  —  Insert Menu

_Scope: Pivot Table for cross-analyzing activity logs by category and period_

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

_Scope: Data > Sort, AutoFilter, More Filters > Advanced Filter, Statistics > Descriptive Statistics, Pivot Table_

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

