# Fitness & Exercise Tracking (LibreOffice Calc 7.3.7)

Tracking progressive overload and running pace in a spreadsheet is surprisingly satisfying once you get the layout right. Start by organizing your workout log with columns for date, exercise name, sets, reps, and weight. For running, add columns for distance and elapsed time. Keep one row per session (or per exercise, if you want granular detail) — Calc handles either approach well.

For basic progressive overload analysis, you don't need anything fancy. Use simple arithmetic operators right in the cells: `=B3-B2` gives you the weight increase between sessions, and `=B3/B2` shows the percentage change. You can skip the formal SUM or PRODUCT functions for one-off calculations like these — typing `=A1*B1` is quicker and more readable than `=PRODUCT(A1,B1)`.

When you want summary stats across a training block — say, average weight lifted per week or total volume — reach for functions like AVERAGE, MIN, MAX, and COUNT. To find your heaviest squat in a column, `=MAX(C2:C50)` does it instantly. MEDIAN is handy for spotting your "typical" session load without outliers skewing things. If you need to know where a value ranks, the RANK function returns its position in the list.

For running pace, calculate minutes per mile (or km) with a formula like `=(elapsed_time/distance)`. If your time is stored as hours:minutes:seconds, format the pace cell via **Format > Cells** and pick a time format so it displays cleanly. Keep in mind that when plotting time on the X axis of a chart, Calc needs it in a proper date or time format — not plain text. You can verify your locale's date acceptance patterns under **Tools > Options > Language Settings > Languages > Date acceptance patterns**.

To visualize your progress over weeks or months, select your data range and go to **Insert > Chart**. The Chart Wizard opens with a choice of ten chart types. For workout trends, pick **Line** — the "Points and Lines" variant is great because you see each session as a dot while the connecting line reveals the trend. If you want a smoother curve instead of jagged session-to-session jumps, set the Line type dropdown to **Smooth** and Calc will fit a spline through your data points.

The Chart Wizard dialog is shown at its first step, where the left panel lists the available chart types — Column, Bar, Circle, Donut, Area, Line, XY (Scatter), Bubble, Net, Stock, and Column and Line — with "Line" currently selected. To the right of the type list, shape variant icons are displayed, with the "Points and Lines" variant highlighted. Below, a "Shape" selector and a "Line type" dropdown set to "Smooth" are visible. The large preview area on the right side of the dialog renders a sample smooth line chart with data points marked, and navigation buttons (Cancel, Help, Back, Next, Finish) appear along the bottom.

On the Data Range page of the Chart Wizard, double-check that the range includes your headers and that "First row as label" is checked — this keeps your axis labels and legend correct. You can also reference non-adjacent columns (e.g., date and weight only, skipping reps) by separating ranges with a comma or semicolon in the *Data range* field, like `$Sheet1.A1:A50,$Sheet1.D1:D50`.

Once you've accumulated a few months of data, the Descriptive Statistics tool gives you a quick health check on your numbers. Open it via **Data > Statistics > Descriptive Statistics**, point it at your weight or pace column, and it spits out mean, standard deviation, variance, min, max, and more in one shot. This is a fast way to see whether your lifts are actually trending up or just bouncing around.

The Descriptive Statistics dialog is displayed with an "Input range" field at the top referencing the selected data column, a "Results to" field specifying where the output will be placed, and radio buttons to indicate whether data is grouped by columns or rows. Below the input fields, a "Results" area shows the computed output table with labeled rows for statistics including Mean, Standard Error, Median, Mode, Standard Deviation, Sample Variance, Kurtosis, Skewness, Range, Minimum, Maximum, Sum, and Count, each paired with its calculated numeric value.

For an XY (Scatter) chart comparing two variables — say, weekly mileage versus average pace — select both columns and insert a chart choosing the **XY (Scatter)** type. Scatter plots are better than line charts here because both axes carry numeric values rather than categories, which lets you spot correlations at a glance.

---

## UI Reference  —  Format Cells Dialog

_Scope: Numbers tab > Time for running pace cell formatting_

The Format Cells dialog (Ctrl+1 or Format > Cells…) is the central dialog for detailed cell formatting. It has 7 tabs covering number format, font, alignment, borders, background, and protection.

The Format Cells dialog is shown with its seven tabs arranged across the top: Numbers, Font, Font Effects, Alignment, Borders, Background, and Cell Protection. The Numbers tab is currently active, displaying a Category list on the left (with entries such as Number, Percent, Currency, Date, Time, Scientific, and others), a Format list in the center showing available format patterns, and a Preview area on the right. Below these, a Language dropdown is set to "Default - English USA," and fields for Decimal places, Leading zeroes, and a Thousands separator checkbox appear, along with a Format Code text field at the bottom with green checkmark, copy, and delete buttons beside it.

## Tabs

### Numbers
- **Category** list: All, User-defined, Number, Percent, Currency, Date, Time, Scientific, Fraction, Boolean Value
- **Format** list showing preview examples (General, -1235, -1234.57, -1,235, etc.)
- **Language** dropdown (Default - English USA)
- **Preview** box showing the formatted sample
- **Options**: Decimal places spinner, Negative numbers red checkbox, Leading zeroes spinner, Thousands separator checkbox
- **Format Code** field with validate (✓), copy, and delete buttons

### Font
- **Family** field + scrollable font list
- **Style** dropdown: Regular, Italic, Bold, Bold Italic
- **Size** dropdown (default 10pt)
- **Language** dropdown
- **Features…** button for OpenType features
- Preview panel

### Font Effects
- Accessible from the Font Effects tab for underline style, colour, strikethrough, relief, etc.

### Alignment
- **Horizontal**: Default, Left, Center, Right, Justified, Filled, Distributed (with Indent spinner)
- **Vertical**: Default, Top, Middle, Bottom, Justified, Distributed
- **Text Orientation**: Vertically stacked checkbox, Degrees spinner, Reference edge buttons, rotation dial
- **Properties**: Wrap text automatically, Hyphenation active, Shrink to fit cell size
- **Text direction** dropdown

### Borders
- **Line Arrangement Presets**: 5 icons (no border, box, thick box, inner lines, diagonal)
- **User-defined** border editor (click edges to toggle)
- **Adjacent Cells**: Remove border checkbox
- **Line**: Style, Color (Black), Thickness (0.75pt) dropdowns
- **Padding**: Left/Right/Top/Bottom spinners (1.0pt), Synchronize checkbox
- **Shadow Style**: Position icons, Color (Gray), Distance (5pt)

### Background
- **None / Color** sub-buttons
- Palette dropdown, ~120-swatch colour grid
- Recent Colors, Custom Palette (Add/Delete), R/G/B spinners, Hex field, Pick button

### Cell Protection
- **Protection**: Hide all, Protected (checked by default), Hide formula
- **Print**: Hide when printing
- Note: protection only takes effect after Tools > Protect Sheet is enabled

---

## UI Reference  —  Insert Menu

_Scope: Chart for workout trend Line and XY Scatter charts_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu is shown fully expanded as a vertical dropdown from the menu bar. The menu items are listed top to bottom: Image, Chart, Sparkline, Pivot Table, followed by a Media submenu, OLE Object submenu, and Shape submenu. Further down are Function (Ctrl+F2), Named Range or Expression, Text Box, Comment (Ctrl+Alt+C), Fontwork, Hyperlink (Ctrl+K), Special Character, and Formatting Mark submenu. Near the bottom are Date (Ctrl+;), Time (Shift+Ctrl+;), Field submenu, Headers and Footers, Form Control submenu, and Signature Line.

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

_Scope: Data > Statistics > Descriptive Statistics for training block summaries_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown fully expanded as a dropdown from the menu bar. At the top are cell and row/column operations: Insert Cells (Ctrl++), Insert Rows (with submenu arrow), Insert Columns (with submenu arrow), Insert Page Break (with submenu arrow), followed by corresponding Delete entries and Clear Cells (Backspace). Below a separator are Fill Cells (with submenu arrow), Named Ranges and Expressions (with submenu arrow), Cell Comments (with submenu arrow), and Cycle Cell Reference Types (F4). The lower section contains sheet management items: Insert Sheet, Insert Sheet at End, Insert Sheet from File, External Links, Delete Sheet (greyed out), Rename Sheet, Hide Sheet, Show Sheet, Move or Copy Sheet, Duplicate Sheet, Navigate (with submenu arrow), Sheet Tab Color, Sheet Events, and Right-To-Left.

The Data menu is shown fully expanded as a dropdown from the menu bar. At the top are Sort, Sort Ascending, and Sort Descending, followed by AutoFilter (Shift+Ctrl+L) and More Filters (with submenu arrow). Below a separator are Define Range, Select Range, and Refresh Range. Next come Pivot Table (with submenu arrow), Calculate (with submenu arrow), Validity, Subtotals, Form, Streams, XML Source, Multiple Operations, Text to Columns, and Consolidate. Toward the bottom are Group and Outline (with submenu arrow) and Statistics (with submenu arrow pointing to its 13 statistical tools including Descriptive Statistics).

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
