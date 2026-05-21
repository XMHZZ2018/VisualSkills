# Utility & Energy Analysis (LibreOffice Calc 7.3.7)

Start by organizing your raw data — dates in column A, meter readings or bill amounts in subsequent columns. Keep one row per reading period (monthly bills, daily meter snapshots, etc.) with headers like "Date," "kWh," "Gas Therms," "Water Gallons," and "Solar kWh Produced." Consistent column layout is what makes everything downstream work smoothly.

To compute period-over-period consumption, add a column with a simple difference formula. If your electric meter readings are in column B, then `=B3-B2` in a new column gives you the usage for each interval. Do the same for water and gas. Any sudden spike in that delta column is your first clue that something is off — a leak, a billing error, or a malfunctioning appliance.

For spotting anomalies, Calc's Descriptive Statistics tool is your best friend. Select your consumption column, then go to **Data > Statistics > Descriptive Statistics**, set your input range, and pick an empty cell for the results. Calc will generate mean, standard deviation, min, max, and more. Any reading beyond two standard deviations from the mean deserves investigation.

The Descriptive Statistics dialog has a "Data" section at the top with two fields: "Input range" (shown populated with `$Sheet1.$A$1:$C$13`) and "Results to" (set to `$E$1`), each accompanied by a range-picker button. Below that is a "Grouped by" section with radio buttons for "Columns" (selected) and "Rows." The dialog has Help, OK, and Cancel buttons along the bottom.

You can also flag outliers directly in the sheet with a formula like `=IF(ABS(C2-AVERAGE($C$2:$C$13))>2*STDEV($C$2:$C$13),"ANOMALY","OK")`. This gives you an instant visual scan of which months are unusual — great for catching slow water leaks that gradually inflate usage.

To see trends over time, select your date and consumption columns and go to **Insert > Chart**. In the Chart Wizard, choose **Line** as the chart type and pick the **Points and Lines** variant so individual readings stand out against the trend. For smoother curves, set the Line type dropdown to **Smooth** and Calc will interpolate using cubic splines, which makes seasonal patterns in energy use much easier to read.

The Chart Type dialog shows a list of chart types on the left (Column, Bar, Pie, Area, Line, XY (Scatter), Bubble, Net, Stock, Column and Line) with "Line" highlighted. To the right, four line-chart variants are shown as thumbnail previews, with the second variant — "Points and Lines" — selected and outlined with a dashed border. Below the thumbnails is a "Stack series" checkbox (checked, with "On top" selected) and a "Line type" dropdown set to "Smooth" with a "Properties…" button beside it. Help, OK, and Cancel buttons appear at the bottom.

For solar production analysis, an **XY (Scatter)** chart works well when you want to correlate production against an independent variable like temperature or daylight hours. Select **XY (Scatter)** in the Chart Wizard, pick **Points and Lines**, and check **Sort by X values** so the plot reads cleanly left to right. After inserting the chart, double-click it to enter edit mode, then use **Insert > Trend Lines** to overlay a linear or logarithmic regression line — this shows whether your panels are degrading over time.

If you need a more rigorous regression, go to **Data > Statistics > Regression**. Set your independent variable range (e.g., month numbers) as X and your consumption or production data as Y, choose **Linear Regression**, and set a confidence level of 0.95. Calc outputs slope, intercept, R², and residuals, which tell you exactly how well the trend fits and where the outliers live.

The Regression dialog is divided into several sections. The "Data" section at the top has fields for "Independent variable(s) (X) range" (showing `$Sheet1.$A$1:$A$11`) and "Dependent variable (Y) range" (showing `$Sheet1.$B$1:$B$11`), each with a range-picker button, plus a checkbox labeled "Both X and Y ranges have labels" (checked) and a "Results to" field set to `$D$1`. The "Grouped by" section offers "Columns" (selected) and "Rows" radio buttons. Under "Output Regression Types," three radio buttons are available: "Linear Regression" (selected), "Logarithmic Regression," and "Power Regression." The "Options" section at the bottom has a "Confidence level" spinner set to 0.95, a "Calculate residuals" checkbox (checked), and an unchecked "Force intercept to be zero" checkbox. Help, OK, and Cancel buttons line the bottom of the dialog.

For water leak detection specifically, compare your metered usage against your billed usage in a side-by-side column chart. Select both columns, insert a chart via **Insert > Chart**, and pick **Column**. Any persistent gap between metered and billed values points to either a meter issue or unaccounted consumption. Stacked area charts (available as a variant under the **Area** chart type) are also handy for visualizing how electricity, gas, and water costs combine into your total utility spend over the year.

Finally, moving averages help smooth out noise in daily readings. Use **Data > Statistics > Moving Average**, set an interval of 7 for weekly smoothing on daily data, and Calc will produce a new column of averaged values that makes the underlying trend unmistakable. Pair that with conditional formatting on your raw data — highlight cells above a threshold in red — and you have a dashboard that practically shouts when something needs attention.

---

## UI Reference  —  Insert Menu

_Scope: Chart for consumption trend Line and XY Scatter charts_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu is shown expanded from the menu bar. It lists the following items from top to bottom: Image…, Chart…, Sparkline…, Pivot Table…, Media, OLE Object, Shape, Function…, Named Range or Expression…, a checkbox for Text Box, Comment, Fontwork…, a checkbox for Hyperlink…, Special Character…, and Formatting Mark. The menu items are displayed in a single-column dropdown beneath the "Insert" label on the menu bar.

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

_Scope: Data > Statistics (Descriptive Statistics, Regression, Moving Average) for consumption analysis_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar. It lists items organized into logical groups: Insert Cells…, Insert Rows, Insert Columns, and Insert Page Break at the top; then Delete Cells…, Delete Rows, Delete Columns, and Delete Page Break; followed by Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, and External Links…; then Delete Sheet… (greyed out); then Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions…, Cell Comments, and Rename Sheet… with additional items continuing below the visible area.

The Data menu is shown expanded from the menu bar. It lists Sort…, Sort Ascending, Sort Descending at the top, followed by a checkbox for AutoFilter, then More Filters, Define Range…, Select Range…, and Refresh Range (greyed out). Below that are Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… with additional items continuing below the visible portion of the menu.

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
