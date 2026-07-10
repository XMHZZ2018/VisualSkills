# Tax Deduction & Depreciation (LibreOffice Calc 7.3.7)

Tracking mileage deductions, asset depreciation, and other tax-related records in Calc is really just about building the right formulas on top of well-organized data. Once you have your columns laid out — dates, descriptions, amounts, rates — Calc's built-in functions do the heavy lifting.

Start by setting up a mileage log with columns for date, destination, miles driven, and the per-mile rate. To calculate each trip's deduction, use a simple multiplication formula like `=C2*D2` where C2 holds miles and D2 holds the rate. Then total everything with `=SUM(E2:E100)` at the bottom. If you need to distinguish business from personal trips, add a category column and use an IF formula such as `=IF(F2="Business", C2*D2, 0)` to only count qualifying entries.

For asset depreciation, straight-line is the simplest method: `=(Cost - Salvage) / Life`. Put your asset cost in one cell, salvage value in another, and useful life in a third, then reference them. A formula like `=(B1-B2)/B3` keeps things clean and easy to audit. If you prefer declining-balance depreciation, Calc offers the `DB` and `DDB` functions — just supply cost, salvage, life, and the period you want to calculate.

To keep your depreciation schedule readable, consider using named ranges. Head to **Sheet > Named Ranges and Expressions > Define** and give labels like *AssetCost* or *SalvageValue* to your input cells. Your formulas then read as `=(AssetCost-SalvageValue)/UsefulLife`, which is far easier to follow when you revisit the sheet at tax time.

Rounding matters for tax figures. Wrap your results in `=ROUND(formula, 2)` to lock values to two decimal places. You can also nest calculations — for instance, `=ROUND((B1-B2)/B3, 2)` computes and rounds depreciation in a single cell. Calc's rounding functions include ROUNDUP and ROUNDDOWN if your tax authority requires a specific treatment.

Use comparative operators to flag thresholds. A formula like `=IF(C31>140, "HIGH", "OK")` can highlight when a deduction category exceeds a review threshold. This is handy for spotting entries that might trigger audit scrutiny before you file.

For larger tax workbooks spanning multiple sheets — say one sheet per quarter — reference across sheets with syntax like `=$Sheet2.B12+$Sheet3.B12`. This lets a summary sheet pull totals from each period without manual copying. If any source value changes, the summary updates automatically, or you can force a refresh with **Data > Calculate > Recalculate** or just press *F9*.

Finally, keep a template. Once your depreciation schedules and mileage logs are structured the way you like, save the file as a reusable starting point. Label each formula's input cell clearly in the column to its left so anyone reviewing the sheet — including future you — can follow the logic without deciphering raw cell addresses. See `fig01.png` for the cell references approach.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Sheet > Named Ranges and Expressions > Define for asset and tax-sheet labels, Data > Calculate_

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

