# Competition & League Scoring (LibreOffice Calc 7.3.7)

Scoring a league or competition usually starts with a table of raw data — contestants in rows, judges or rounds in columns, scores in cells. Calc gives you everything you need to summarize that data, normalize it, and produce final rankings without leaving the spreadsheet.

**Getting summary stats on scores.** For any column of scores, `=AVERAGE(B2:B50)` gives you the arithmetic mean, while `=MEDIAN(B2:B50)` is better when you suspect outliers from a generous or harsh judge. Use `=MIN()` and `=MAX()` to spot the range, and `=STDEV()` to see how spread out the scores are. If you want to toss the highest and lowest judge scores before averaging — a common contest normalization — combine `=SUM()`, `=MIN()`, and `=MAX()` like `=(SUM(B2:B6)-MIN(B2:B6)-MAX(B2:B6))/(COUNT(B2:B6)-2)`.

**Ranking contestants.** The `=RANK()` function is your friend here. Enter `=RANK(B2,B$2:B$50)` next to a contestant's total and it returns their position, with 1 being the highest. By default RANK uses descending order (biggest score = rank 1); pass a third argument of `1` if lower scores should win. For ties, RANK assigns the same position to both — you can break ties with a helper column using `COUNTIF`.

**Filtering and sorting standings.** Once you have totals and ranks, select your data range and open **Data > Sort** to reorder by final score or rank. On the *Sort Criteria* tab, pick your score column as Sort Key 1 and set it to **Descending**. Check **Range contains column labels** on the *Options* tab so your header row stays put. For a quick one-click sort, just click a cell in the score column and hit **Data > Sort Descending**.

See `fig01.png`.

**Using AutoFilter to view a single division or category.** Click anywhere in your data and go to **Data > AutoFilter**. Drop-down arrows appear on each column header — click the one on your "Division" or "Category" column and select the group you want to inspect. Only matching rows stay visible, which is perfect for reviewing one league at a time.

**SUBTOTAL for filtered results.** Plain `SUM` or `AVERAGE` ignores the filter and calculates on all rows. Use `=SUBTOTAL(9,B2:B200)` instead — function index 9 means SUM, and it automatically skips hidden (filtered-out) rows. Swap in index 1 for AVERAGE or 4 for MAX. If you also hide rows manually and want those excluded too, use indices 101–111 instead.

See `fig02.png`.

**The Subtotals tool for grouped standings.** When you need category-level summaries inserted right into the sheet — say, a sum per team or per region — select your range and open **Data > Subtotals**. On the *1st Group* tab, set *Group by* to your category column (e.g., "Team"), check the score column under *Calculate subtotals for*, and pick **Sum** (or **Average**) as the function. Click **OK** and Calc sorts the data, inserts subtotal rows, and adds an outline in the margin so you can collapse detail rows and see only the group totals.

See `fig03.png`.

**Normalizing judge scores.** If different judges use different scales, normalize each judge's column to a 0–100 range with `=(B2-MIN(B$2:B$50))/(MAX(B$2:B$50)-MIN(B$2:B$50))*100`. This min-max scaling puts every judge on equal footing before you sum or average across columns. Alternatively, convert to z-scores with `=(B2-AVERAGE(B$2:B$50))/STDEV(B$2:B$50)` to center each judge at zero.

**Keeping it tidy.** Use `=LARGE(B2:B6,2)` or `=SMALL(B2:B6,2)` when you need the 2nd-highest or 2nd-lowest score specifically — handy for "best N of M rounds" formats. Combine these building blocks and your league table practically maintains itself: enter scores, and the rankings update instantly.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Sort, AutoFilter, Subtotals for grouped standings and filtered SUBTOTAL_

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

