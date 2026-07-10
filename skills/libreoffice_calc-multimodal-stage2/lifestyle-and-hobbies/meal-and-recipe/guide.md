# Meal Planning & Recipe Scaling (LibreOffice Calc 7.3.7)

Calc makes a surprisingly good kitchen companion. The trick is to treat each recipe as a small formula-driven model: list your base ingredients in one column, your base quantities in another, and let cell references do the heavy lifting when you need to feed a crowd — or just yourself.

Start by entering your recipe's base serving count in a dedicated cell (say B1), then put your target serving count in B2. For each ingredient quantity, write a formula like `=C5*($B$2/$B$1)` — that multiplies the original amount by the scaling ratio. The dollar signs lock the reference so you can copy the formula down the entire ingredient list without it drifting. This is just basic cell-reference arithmetic: Calc treats `*` as multiplication and `/` as division, exactly as you'd expect.

See `fig01.png`.

For a weekly meal rotation, give each day its own column across the top and list every possible ingredient down column A. Under each day, enter the scaled quantity of that ingredient if the day's recipe calls for it; leave the cell blank otherwise. At the end of each ingredient row, use `=SUM(B5:H5)` to roll up the week's total. That single SUM across the row becomes your consolidated shopping list quantity — no manual addition needed.

To quickly scan your shopping list for outliers, lean on the statistics functions. `=MAX(I5:I30)` flags the ingredient you need the most of, while `=MIN(I5:I30)` catches anything suspiciously low. Wrapping the totals in `=ROUND(I5,1)` keeps quantities at one decimal place so your list stays readable rather than showing six-decimal-place flour weights.

When you want to compare costs or nutrition across several scaling factors at once, reach for the Multiple Operations tool. Set up your base recipe formula in one cell, then list your candidate serving counts in a column nearby. Select the range covering those candidates plus an empty results column, then open **Data > Multiple Operations**. Point the **Formulas** field at your recipe formula cell and the **Column input cell** at your base serving count. Hit **OK** and Calc fills the results column instantly — one row per scenario, no copy-pasting required.

See `fig02.png` for the Multiple Operations dialog.

If you want to track both total cost *and* per-serving cost simultaneously, you can feed two formulas into the same Multiple Operations run. Just place both formula cells in a row, select a wider results range with a column for each formula, and enter both into the **Formulas** field as a range (e.g., `$B$5:$C$5`). Calc will generate a results column for each formula side by side.

See `fig03.png` for the results table.

For conditional logic — say, flagging when an ingredient exceeds a budget threshold — use an IF formula: `=IF(C31>140,"OVER BUDGET","OK")`. Comparative operators like `>`, `<`, and `>=` all work inside IF, letting you build simple alerts directly into your planning sheet. You can also name frequently referenced ranges via **Sheet > Named Ranges and Expressions > Define** so that formulas read like plain English — `=AVERAGE(WeeklyCalories)` is a lot friendlier than `=AVERAGE($J$5:$J$11)`.

That's really all you need: cell references for scaling, SUM for consolidation, Multiple Operations for what-if comparisons, and a sprinkle of IF for guardrails. Keep your base recipes on one sheet, your weekly plan on another, and reference across sheets with `=$Sheet2.B5` syntax when you need to pull data between them.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Multiple Operations for serving-count cost comparisons_

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

