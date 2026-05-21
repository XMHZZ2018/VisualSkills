# Renovation Material & Cost Estimation (LibreOffice Calc 7.3.7)

Start by laying out your renovation data in a clean table — room dimensions, unit prices, quantities, and waste percentages each get their own column. Think of each row as one material line item (tiles, paint, lumber, etc.). Type labels in column A and raw numbers in columns B onward. Calc treats any cell as either a data holder or a formula cell, so keep your inputs and calculations separate for clarity.

Formulas always begin with `=`. To calculate total material cost, you'd type something like `=B3*C3` to multiply quantity by unit price. You can use all the standard arithmetic operators — `+`, `-`, `*`, `/`, and even `^` for exponentiation — right in the cell. For a waste factor, just multiply: `=B3*1.10` adds 10% overage to your material quantity. If your formula starts with `+` or `-`, Calc adds the `=` for you automatically.

The spreadsheet shows two states of cell B3 in a simple grid with columns A, B, and C. In the top half, cell B3 is in edit mode displaying the formula `=15+46` as typed text. In the bottom half, after pressing Enter, cell B3 shows the computed result `61`, with the cell selected and its fill handle visible at the lower-right corner.

Cell references are the real power here. Instead of hardcoding a waste percentage into every row, put it in one cell (say, D1) and reference it everywhere with `=B3*$D$1`. The dollar signs lock that reference so it won't shift when you copy the formula down. You can pull data from other sheets too — `=$Sheet2.B12` grabs a price from your supplier quote sheet.

Use `SUM` to total up a column of costs: `=SUM(E2:E25)` gives you the whole project estimate in one shot. `COUNT` tells you how many line items you have, and `MIN` or `MAX` help you quickly spot your cheapest and most expensive materials. For average cost per item, `AVERAGE` does exactly what you'd expect. These functions accept ranges, so you never have to manually add cells one by one.

Conditional logic helps flag budget overruns. An `IF` formula like `=IF(E3>500, "OVER", "OK")` marks any line item exceeding $500. You can nest these or combine them with comparative operators (`>`, `<`, `>=`, `<=`, `<>`) to build simple status dashboards right in your spreadsheet.

When you want to explore "what if" scenarios — say, how total cost changes across different quantities of flooring — the **Multiple Operations** tool is invaluable. Set up your base formula (e.g., profit or total cost), list your alternate input values in a column, then select that range plus the empty results column and open **Data > Multiple Operations**. Point the **Formulas** field at your formula cell and the **Column input cell** at the variable you want to swap, then hit **OK**. Calc fills in every scenario instantly.

The "Multiple operations" dialog has a title bar reading "Multiple operations" and a "Default Settings" section containing three text input fields: "Formulas:", "Row input cell:", and "Column input cell:", each with a shrink/expand button to its right for selecting cell references directly from the sheet. At the bottom of the dialog are three buttons: "Help" on the left, and "OK" (highlighted with a blue border) and "Cancel" on the right.

You can even run two formulas at once — total cost and cost-per-unit, for example — by entering both formulas in adjacent cells and selecting a wider results range. The tool maps each formula to its own output column, so you get a neat comparison table. Plot the results as an XY (Scatter) chart to visualize where costs break even or escalate.

The results table shows columns A through E. Columns A and B hold the base data: "Unit sale price" ($10), "Unit cost" ($2), "Fixed annual cost" ($10,000), "Quantity sold" (2,000), and "Profit" ($6,000) in rows 1–5. Column D lists alternate quantity values from 500 to 5,000 in increments of 500 under the header "Quantity." Column E, headed "Profit," contains the computed profit for each quantity — ranging from -$6,000 (at 500 units) to $30,000 (at 5,000 units), with negative values displayed in red. The formula bar for the selected cell E11 shows `=MULTIPLE.OPERATIONS(B$5,$B$4,$D11)`.

An XY (Scatter) chart titled "Profit over quantity" plots the results from the table. The horizontal axis is labeled "Quantity of toys sold" (ranging from 0 to 6,000) and the vertical axis is labeled "Annual profit" (ranging from -$10,000 to $35,000, with negative values in red). A single data series labeled "Profit" is plotted as blue square markers connected by a straight line, rising from approximately -$6,000 at 500 units through the break-even point near 1,250 units up to $30,000 at 5,000 units.

For project timelines, dedicate a sheet to tasks with start dates, durations, and dependencies. Basic date math works naturally — `=A2+14` adds two weeks to a start date. Format those cells via **Format > Cells**, pick the *Date* category, and choose your preferred display. Combine this with your cost sheet references to tie budget phases to schedule milestones, giving you one workbook that tracks both money and time.

---

## UI Reference  —  Insert Menu

_Scope: Chart for XY Scatter cost break-even plots_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu is shown expanded from the LibreOffice Calc menu bar. It lists items top to bottom: Image…, Chart…, Sparkline…, Pivot Table…, Media, OLE Object, Shape, then a separator, followed by Function…, Named Range or Expression…, then a separator, a checkbox-style Text Box entry, Comment, Fontwork…, then another separator, a checkbox-style Hyperlink… entry, Special Character…, and Formatting Mark. The menu is a narrow single-column dropdown with no submenus visibly expanded.

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

_Scope: Data > Multiple Operations for cost what-if scenario tables_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the LibreOffice Calc menu bar. From top to bottom it lists: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break, then a separator, Delete Cells…, Delete Rows, Delete Columns, Delete Page Break, then a separator, Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, then a greyed-out Delete Sheet…, then a separator, Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, then a separator, and Rename Sheet… with additional items partially visible below (Hide Sheet, etc.).

The Data menu is shown expanded from the LibreOffice Calc menu bar. From top to bottom it lists: Sort…, Sort Ascending, Sort Descending, then a separator, a checkbox-style AutoFilter entry, More Filters, then a separator, Define Range…, Select Range…, a greyed-out Refresh Range, then a separator, Pivot Table, Calculate, Validity…, Subtotals…, Form…, then Streams… partially visible at the bottom of the dropdown.

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
