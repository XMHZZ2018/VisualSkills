# Craft Material Calculation (LibreOffice Calc 7.3.7)

Setting up a spreadsheet for your quilting or knitting project is really just a matter of putting your material specs in cells and letting formulas do the tedious math. Start by laying out your known values — fabric width, pattern repeat length, price per yard, skeins needed — each in its own labeled row. Think of column A as your labels and column B as your data holders; this keeps everything readable and makes your formulas easy to follow.

To calculate something like total fabric yardage, click a cell, type `=`, and reference your data cells directly. For instance, if B1 holds the number of quilt blocks and B2 holds yards per block, just type `=B1*B2` in B3 to get total yardage. Calc resolves the references automatically, so when you tweak your block count later the total updates instantly. You can use `+` for addition, `*` for multiplication, `/` for division, and `^` for exponentiation — all the standard arithmetic operators work right in the formula bar.

See `fig01.png`.

For material cost totals, `SUM` is your best friend. If you have yarn costs listed down column C from rows 2 through 10, typing `=SUM(C2:C10)` gives you the full project cost in one shot. Need the average price per skein? Use `=AVERAGE(C2:C10)`. To find your most expensive single material, `=MAX(C2:C10)` pulls it right out. These functions save you from manually adding up long lists and are far less error-prone.

When budgeting, you'll often want a conditional check — say, flagging when your total exceeds a spending limit. An IF formula handles that nicely: `=IF(C11>140,"OVER BUDGET","OK")` displays a plain-English warning based on your threshold. This is handy for keeping quilting fabric purchases in check before you hit the checkout.

The real power comes when you want to explore "what if" scenarios, like how project cost changes across different yardage amounts. Set up your base formula (say, `=B4*(B1-B2)-B3` for profit on a craft fair batch), list your alternate quantities in a column, then select that range plus an adjacent empty column. Open **Data > Multiple Operations** and point the **Formulas** field at your base formula cell, and the **Column input cell** at the variable you want to sweep. Hit **OK** and Calc fills in all the results at once — perfect for comparing costs across 5, 10, or 20 skeins without rewriting anything.

See `fig02.png`.

If you're running two formulas simultaneously — total cost and cost per unit, for example — just place both formula cells side by side, select a wider results range to include an extra output column, and enter both into the **Formulas** field as a range (like `$B$5:$C$5`). Calc generates a neat table with both answers for every quantity you listed.

See `fig03.png` for the results table showing profit and per-item cost across quantities.

One practical tip: label everything. Keep your formulas, variable ranges, and result tables on the same sheet with clear headers. It makes the Multiple Operations tool far easier to set up and means you (or a guild mate) can revisit the spreadsheet months later without deciphering cryptic cell addresses. If you ever need to reference data from another sheet — say, a separate yarn stash inventory — use the format `=$Sheet2.B12` to pull values across sheets seamlessly.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Multiple Operations for material quantity scenario tables_

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

