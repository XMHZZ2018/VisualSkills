# Sleep Quality Analysis (LibreOffice Calc 7.3.7)

Got a pile of sleep data — bedtimes, wake times, hours slept, maybe caffeine intake or screen time — and you want to make sense of it? Calc's built-in statistics and charting tools can get you surprisingly far without any add-ons.

Start with the basics. Use `=AVERAGE()` on your hours-slept column to get your mean sleep duration, and pair it with `=MEDIAN()` to see if outliers are skewing things. Throw in `=MIN()`, `=MAX()`, and `=COUNT()` to round out the picture. For sleep efficiency — time asleep divided by time in bed — a simple formula like `=B2/C2*100` in a new column does the trick. You can use `=MODE()` to find your most common sleep duration, or `=QUARTILE()` to see where the 25th and 75th percentile boundaries land.

To spot whether something like caffeine intake actually correlates with sleep quality, head to **Data > Statistics > Correlation**. Set your *Input range* to cover both columns (say, caffeine and hours slept), pick **Columns** under *Grouped by*, and point *Results to* an empty cell. Hit **OK** and you'll get a coefficient between −1 and +1. Anything close to zero means there's no linear relationship; closer to −1 or +1 means you're onto something.

The Correlation dialog is a compact window with a "Data" section at the top containing an "Input range" field (here set to `$Sheet1.$A$2:$C$13`) and a "Results to" field (set to `$E$1`), each with a shrink/expand button for selecting ranges on the sheet. Below that is a "Grouped by" section with radio buttons for "Columns" (selected) and "Rows", and the dialog finishes with Help, OK, and Cancel buttons along the bottom.

If you want to go further and actually model the relationship — predict sleep duration from exercise minutes, for example — use **Data > Statistics > Regression**. Put your independent variable (exercise) in the *X range* and your dependent variable (sleep hours) in the *Y range*. Check **Both X and Y ranges have labels** if your columns have headers. Choose **Linear Regression**, leave the confidence level at 0.95, and tick **Calculate residuals** to see how far off each prediction is. The output gives you slopes, intercept, R-squared, and more.

The Regression dialog is a taller window divided into four sections. The "Data" section has fields for "Independent variable(s) (X) range" (set to `$Sheet1.$A$1:$A$11`), "Dependent variable (Y) range" (set to `$Sheet1.$B$1:$B$11`), a checked checkbox for "Both X and Y ranges have labels", and a "Results to" field (set to `$D$1`). The "Grouped by" section offers "Columns" (selected) or "Rows". The "Output Regression Types" section provides three radio buttons: "Linear Regression" (selected), "Logarithmic Regression", and "Power Regression". Finally, the "Options" section contains a "Confidence level" spinner set to 0.95, a checked "Calculate residuals" checkbox, and an unchecked "Force intercept to be zero" checkbox, with Help, OK, and Cancel buttons at the bottom.

For a quick visual gut-check, scatter charts are your best friend. Select your two columns, go to **Insert > Chart**, and pick **XY (Scatter)** from the chart type list. The "Points and Lines" variant works well for sleep data — you can see clusters, outliers, and trends at a glance. After inserting, double-click the chart to enter edit mode, then use **Insert > Trend Lines** to overlay a regression line right on the plot.

The Chart Type dialog shows a list of chart categories on the left — Column, Bar, Pie, Area, Line, XY (Scatter), Bubble, Net, Stock, and Column and Line — with "XY (Scatter)" highlighted in blue. To the right, four sub-type thumbnails are displayed: Points Only, Points and Lines (currently selected, outlined in bold), Lines Only, and 3D Lines. Below the thumbnails the label reads "Points and Lines", with a "Line type" dropdown set to "Straight", a greyed-out "Properties…" button, and a checked "Sort by X values" checkbox. Help, OK, and Cancel buttons appear at the bottom.

Want to smooth out nightly noise and see weekly trends? The moving average tool under **Data > Statistics > Moving Average** lets you set an interval (try 7 for a weekly window) and outputs the smoothed values. Plot those alongside your raw data for a clear before-and-after view of your sleep patterns over time.

---

## UI Reference  —  Insert Menu

_Scope: Chart for XY Scatter sleep correlation plots_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu is shown expanded from the menu bar. It lists items top to bottom: Image…, Chart…, Sparkline…, Pivot Table…, Media, OLE Object, Shape, Function…, Named Range or Expression…, then a separator followed by Text Box (with a checkbox), Comment, Fontwork…, another separator, Hyperlink… (with a checkbox), Special Character…, and Formatting Mark. The menu appears over a spreadsheet with partial cell content visible behind it.

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

_Scope: Data > Statistics > Correlation, Regression, Moving Average for sleep pattern analysis_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar. From top to bottom it lists: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break, then a separator, Delete Cells…, Delete Rows, Delete Columns, Delete Page Break, then another separator, Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet… (greyed out), then a separator, Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, then a separator, Rename Sheet… — with the list continuing below the visible area. The menu overlays a spreadsheet showing partial cell content and the status bar reading "4.2 of LibreO…".

The Data menu is shown expanded from the menu bar. From top to bottom it lists: Sort…, Sort Ascending, Sort Descending, then a separator, AutoFilter (with a checkbox), More Filters, then a separator, Define Range…, Select Range…, Refresh Range (greyed out), then a separator, Pivot Table, Calculate, Validity…, Subtotals…, Form…, Streams… — with the list continuing below the visible area. The menu overlays a spreadsheet with partial cell content visible behind it.

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
