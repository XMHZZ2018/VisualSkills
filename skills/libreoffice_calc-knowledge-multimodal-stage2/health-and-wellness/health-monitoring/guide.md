# Health & Nutrition Monitoring (LibreOffice Calc 7.3.7)

Start by laying out your tracking sheet with columns for date, vital signs (temperature, heart rate, blood pressure), symptoms, hydration intake, feeding times, and macronutrient totals (protein, carbs, fat). Put labels in the first row and keep each day's entry on its own row — this simple structure is what makes everything else work.

For quick daily summaries, lean on basic arithmetic and statistics functions. Use `=AVERAGE(B2:B30)` to get a mean resting heart rate for the month, or `=MIN()` and `=MAX()` to spot extremes in temperature readings. `COUNT` tells you how many entries you actually logged, which is handy for spotting gaps. If you prefer operators over functions, something like `=B2+B3+B4` works fine for small ranges — it's more readable than `=SUM()` when you're only adding a few cells.

To dig deeper into your nutrition data, use **Data > Statistics > Descriptive Statistics**. Point the *Input range* at your macronutrient columns, pick a *Results to* cell off to the side, and hit **OK**. Calc will generate a full report — mean, median, standard deviation, quartiles, and more — so you can see at a glance whether your protein intake is consistent or all over the place.

See `fig01.png` for the Descriptive Statistics dialog. See `fig02.png` for the output report.

Visualizing trends is where things get really useful. Select your date column and one or more vital-sign columns, then go to **Insert > Chart**. The Chart Wizard opens and lets you pick a chart type on the first page. For time-series data like daily weight or hydration, choose **Line** — the "Points and Lines" variant is great because you see both the individual readings and the overall trend. If you want a smoother curve instead of jagged segments, set the *Line type* dropdown to **Smooth** and click **Properties** to fine-tune the spline.

See `fig03.png` for the Chart Type dialog with Line selected.

On the wizard's second page (*Data Range*), confirm Calc picked up the right cells. You can type a range directly into the *Data range* box or click the **Select data range** button to drag over cells on the sheet. Make sure "Data series in columns" is selected and that the first row and first column are flagged as labels, so your dates appear on the X axis and each metric gets its own legend entry.

When you want to compare macronutrient proportions — say, what percentage of calories came from fat versus protein on a given day — a stacked area chart or percentage stacked chart works well. Right-click the chart after creation, choose **Chart Type**, select **Area**, and enable **Stack series > Percent** to normalize everything to 100%.

For scatter analysis (e.g., does hydration correlate with symptom severity?), pick **XY (Scatter)** in the Chart Wizard. Unlike line charts, scatter plots treat both axes as numeric values, which is what you need when neither axis is a simple category. One tip: make sure date or time values on the X axis are actual numbers, not text — check your locale formats under **Tools > Options > Language Settings > Languages > Date acceptance patterns** if points aren't plotting correctly.

Once your charts and summary statistics are in place, you've got a living dashboard. Just keep appending rows, and everything — averages, ranges, and charts — updates automatically.

---

## UI Reference  —  Insert Menu

_Scope: Chart for vital-sign Line charts and stacked area nutrition charts_

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

_Scope: Data > Statistics > Descriptive Statistics for nutrition and vital-sign summaries_

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

