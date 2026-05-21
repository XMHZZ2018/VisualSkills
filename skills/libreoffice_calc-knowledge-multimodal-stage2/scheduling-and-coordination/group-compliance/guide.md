# Group Fairness & Compliance (LibreOffice Calc 7.3.7)

When you're managing shared duties across a team — tracking co-op credits, splitting workloads, or making sure everyone pulls their weight — Calc gives you a solid toolkit without needing anything fancy. Here's how to put it together.

Start with the basics. Functions like `SUM`, `AVERAGE`, `COUNT`, `MIN`, and `MAX` are your first line of defense for spotting imbalances. If you have a column of contribution hours per member, `=AVERAGE(B2:B30)` instantly tells you the expected baseline, while `=MIN(B2:B30)` and `=MAX(B2:B30)` flag outliers. For a quick fairness check, compare each person's total against the group average — anyone falling well below deserves a conversation, not just a formula. You can also use `MEDIAN` and `QUARTILE` to get a distribution-aware picture rather than letting one overachiever skew the mean.

For ongoing compliance tracking, the `SUBTOTAL` function is a real workhorse. Open the **Function Wizard** via **Insert > Function** (or just press *Ctrl+F2*), pick SUBTOTAL from the Mathematical category, and give it a function index — 9 for SUM, 1 for AVERAGE, 2 for COUNT, and so on. The magic is that SUBTOTAL respects AutoFilters: filter your data down to one team member and the subtotal updates automatically, showing only their credits. Use index values 101–111 instead of 1–11 if you want to also ignore manually hidden rows, which is handy when you've tucked away resolved disputes.

See `fig01.png`.

When you need a broader breakdown — say, subtotals by employee and then by activity category — the Subtotals tool is more powerful. Select your data range and go to **Data > Subtotals**. On the *1st Group* tab, set **Group by** to your primary column (like Employee), check the value column under *Calculate subtotals for*, and pick your function (Sum, Count, Average). Flip to the *2nd Group* tab and repeat for a secondary grouping such as Category. Hit **OK** and Calc sorts, groups, and inserts subtotal rows automatically.

See `fig02.png`.

The result includes a collapsible outline to the left of the row numbers — click the numbered buttons at the top to zoom between the grand total, per-person totals, or the full detail view. This makes it trivially easy to present a high-level fairness summary to stakeholders while keeping the raw participation data one click away. To remove the outline later, use **Data > Group and Outline > Remove Outline**, or recreate it with **Data > Group and Outline > AutoOutline**.

See `fig03.png`.

Check the *Options* tab in the Subtotals dialog for a couple of compliance-relevant settings. Enable **Pre-sort area according to groups** so matching entries are gathered together before totals are calculated — without it, scattered entries for the same person won't roll up correctly. Turn on **Case sensitive** if your labels might have inconsistent casing (e.g., "Brigitte" vs. "brigitte"), so nothing slips through the cracks. If you're printing reports per group, **Page break between groups** gives each team member their own page automatically.

For day-to-day policy enforcement, pair these tools with AutoFilter dropdown arrows on your column headers. Filter to a single person or category, glance at the SUBTOTAL result at the bottom of the column, and you've got an instant audit of their standing. It's lightweight, transparent, and keeps everyone honest without building anything complicated.

---

## UI Reference  —  Formula Bar

_Scope: Function Wizard (Ctrl+F2) for SUBTOTAL function index selection_

The Formula bar sits below the Formatting toolbar and provides cell navigation, function insertion, and formula editing.

Read the screenshot `ui-formula-bar.png` in this directory.

## Elements (left to right)

- **Name Box** — displays current cell reference (e.g. "A1"). Click to edit, type an address and press Enter to navigate. Dropdown (▼) lists defined named ranges and "Manage Names…". During formula entry, switches to a function-name selector.

- **Function Wizard** (fx button) — opens the Function Wizard dialog with:
  - Search field to filter functions by name
  - Category dropdown (All, plus 13 categories: Math, Statistical, Text, etc.)
  - Full alphabetical function list (ABS, ACCRINT, ACOS, ADDRESS, AGGREGATE, …)
  - Formula and Result preview panels
  - Array checkbox, Back/Next navigation, Help/Cancel/OK

- **Select Function** (Σ button) — main click inserts SUM. Dropdown (▼) shows 11 common functions: Sum, Average, Min, Max, Count, CountA, Product, Stdev, StdevP, Var, VarP

- **Formula Button** (= button) — activates formula entry mode:
  - Inserts "=" in the active cell
  - Name Box changes to function-name selector (shows "SUM")
  - Σ button is replaced by **Cancel** (×, red) and **Accept** (✓, green)
  - Press Escape to cancel, Enter to accept

- **Input Line** — wide text area showing raw cell content (formula or value). Click to enter edit mode. Supports multi-line expansion.

- **Expand/Collapse Formula Bar** (▼/▲ chevron, far right) — toggles the input line between single-line and multi-line height for editing long formulas

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Subtotals for per-employee grouping, Group and Outline for collapsible summaries_

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

