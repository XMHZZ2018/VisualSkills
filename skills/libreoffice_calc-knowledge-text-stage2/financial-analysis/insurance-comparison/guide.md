# Insurance Plan Comparison (LibreOffice Calc 7.3.7)

Comparing insurance plans means juggling premiums, deductibles, copays, and out-of-pocket maximums across multiple scenarios. LibreOffice Calc's data analysis tools make this surprisingly manageable — you can model different usage levels and see which plan actually saves you money.

Start by laying out your plan parameters in a clean table: column A for labels (monthly premium, annual deductible, copay percentage, out-of-pocket max), and columns B, C, D for each plan you're comparing. Below that, build a formula that calculates total annual cost for a given level of medical expenses — something like `=B1*12 + MIN(expenses, B2) + (expenses - B2)*B3`. Keep your formulas referencing one "expected expenses" cell so you can easily vary it.

To see how each plan performs across a range of expense levels, use the Multiple Operations tool. Enter your expense scenarios (say, $0 to $20,000 in $1,000 increments) in a single column, then select that column plus the adjacent empty columns where results will land. Open it with **Data > Multiple Operations**, point the **Formulas** field at your cost formula cells, and set the **Column input cell** to your expected-expenses cell. Hit **OK** and Calc fills the entire results table instantly.

The Multiple Operations dialog is titled "Multiple operations" and contains a "Default Settings" section with three input fields: "Formulas:", "Row input cell:", and "Column input cell:", each paired with a small cell-picker button on its right side for selecting cell references directly from the sheet. At the bottom of the dialog are three buttons: Help on the left, and OK (highlighted with a blue border) and Cancel on the right.

This is where it gets powerful. If you want to compare plans across both expense levels *and* varying copay rates (or different deductible tiers you're negotiating), use Multiple Operations with two variables. Put one variable's range in a column and the other across a row, then fill in both the **Row input cell** and **Column input cell** fields in the dialog. Calc generates a full two-dimensional comparison grid showing total costs for every combination.

The spreadsheet shows a two-variable Multiple Operations result table. Columns A and B hold the input parameters (unit sale price, unit cost, fixed annual cost, quantity sold, and profit), while column D lists quantity values from 500 to 5,000 in increments of 500 down the rows, and row 1 contains varying unit sale prices ($8, $10, $15, $20) across columns E through H. The body of the grid displays the computed profit for each combination, with negative values shown in red; the formula bar for the selected cell (H11) reads `=MULTIPLE.OPERATIONS($B$5,$B$4,$D11,$B$1,H$1)`, showing how Calc references both the row and column input variables.

For the reverse question — "how much would I need to spend before Plan B becomes cheaper than Plan A?" — reach for **Tools > Goal Seek**. Select the cell containing the cost difference between two plans, set the **Target value** to 0, and point the **Variable cell** at your expected-expenses input. Calc solves for the exact break-even amount.

Once your results table is populated, use functions like `MIN()` across each scenario row to flag the cheapest plan, or `AVERAGE()` across all scenarios to find which plan wins on balance. `RANK()` can order plans from least to most expensive at each expense tier if you're presenting this to someone else.

To make the comparison visual, select your results range and insert an XY (Scatter) chart — total annual cost on the vertical axis, expected expenses on the horizontal. The crossover points where plan lines intersect are your break-even thresholds, immediately obvious in the graph.

The XY (Scatter) chart is titled "Profit over quantity" with the horizontal axis labeled "Quantity of toys sold" (ranging from 0 to 6,000) and the vertical axis labeled "Annual profit" (ranging from −$10,000 to $35,000). A single data series labeled "Profit" is plotted as connected blue square markers forming a straight ascending line, starting at approximately −$7,000 at 500 units and rising to about $30,000 at 5,000 units, crossing the zero line around 1,250 units. A legend on the right side of the chart identifies the series.

A practical tip: keep your raw plan data, formulas, variable ranges, and results tables all on the same sheet with clear labels. The Multiple Operations tool works best when everything is organized and easy to reference, and it makes your spreadsheet self-documenting for anyone else who needs to review your analysis.

---

## UI Reference  —  Insert Menu

_Scope: Chart for XY Scatter plan cost crossover visualization_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu dropdown is shown expanded from the menu bar, listing items top to bottom: Image…, Chart…, Sparkline…, Pivot Table…, Media, OLE Object, Shape, Function…, Named Range or Expression…, then a checkbox-style Text Box entry, Comment, Fontwork…, a checkbox-style Hyperlink… entry, Special Character…, and Formatting Mark at the bottom. The menu appears over a spreadsheet background with the standard LibreOffice toolbar visible behind it.

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

_Scope: Data > Multiple Operations for expense-level scenario grids_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu dropdown is shown expanded, listing items in grouped sections: Insert Cells…, Insert Rows, Insert Columns, and Insert Page Break at the top; then Delete Cells…, Delete Rows, Delete Columns, and Delete Page Break; followed by Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, and Delete Sheet… (greyed out). Below a separator are Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet…, with additional items partially visible below the dropdown boundary.

The Data menu dropdown is shown expanded, listing items top to bottom: Sort…, Sort Ascending, Sort Descending, AutoFilter (with a checkbox, unchecked), More Filters, Define Range…, Select Range…, Refresh Range (greyed out), Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams…, with additional items partially visible below. The menu appears over a spreadsheet with the standard LibreOffice toolbar visible in the background.

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

---

## UI Reference  —  Tools, Window, and Help Menus

_Scope: Tools > Goal Seek for break-even expense amount between plans_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu dropdown is shown expanded, listing items top to bottom: Spelling…, Automatic Spell Checking (with a checked checkbox), Thesaurus… (greyed out), Language, AutoCorrect Options…, AutoInput (with a checked checkbox), ImageMap (greyed out), Redact, Auto-Redact, Goal Seek…, Solver…, Detective, Scenarios… (greyed out), Forms, Share Spreadsheet…, Protect Sheet… (with an unchecked checkbox), and Protect Spreadsheet… partially visible at the bottom. The menu appears over a spreadsheet with the standard LibreOffice toolbar in the background.

## Tools Menu Elements

- **Spelling…** (F7) — spell-check dialog
- **Automatic Spell Checking** (Shift+F7) — toggle, enabled by default
- **Thesaurus…** (Ctrl+F7)
- **Language** — submenu for language settings
- **AutoCorrect Options…**
- **AutoInput** — toggle auto-completion from existing column values (on by default)
- **ImageMap** (greyed), **Redact**, **Auto-Redact**
- **Goal Seek…** — set a formula cell to a target by changing an input cell
- **Solver…** — optimisation with multiple constraints
- **Detective** — formula auditing submenu: Trace Precedents (Shift+F9), Trace Dependents (Shift+F5), Remove All/Precedents/Dependents Traces, Trace Error, Refresh Traces, Fill Mode (toggle), AutoRefresh (toggle, on), Mark Invalid Data
- **Scenarios…** (greyed)
- **Forms** — submenu: Design Mode, Control Wizards, Control/Form Properties, Form Navigator, Activation Order, Add Field, Open in Design Mode, Automatic Control Focus
- **Share Spreadsheet…**
- **Protect Sheet…** — password-protect the active sheet
- **Protect Spreadsheet Structure…** — prevent sheet add/delete/rename
- **Macros** — submenu: Run Macro…, Edit Macros…, Organize Macros, Digital Signature…, Organize Dialogs…
- **Development Tools** (toggle)
- **XML Filter Settings…**
- **Extensions…** (Ctrl+Alt+E) — Extension Manager
- **Customize…** — customise menus, toolbars, keyboard, events
- **Options…** (Alt+F12) — global LibreOffice settings

## Window Menu

- **New Window** — opens a second view of the current document
- **Close Window** (Ctrl+W)
- Document list — radio-button list of open document windows; click to switch

## Help Menu

- **LibreOffice Help** (F1), **What's This?**, **User Guides**
- **Show Tip of the Day**
- **Search Commands** (Shift+Escape) — command search bar
- **Get Help Online**, **Send Feedback**, **Restart in Safe Mode…**
- **Get Involved**, **Donate to LibreOffice**, **License Information**
- **About LibreOffice** — version 24.2 Community
