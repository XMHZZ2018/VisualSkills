# Event & Gathering Management (LibreOffice Calc 7.3.7)

When you're wrangling RSVPs, seating charts, auction bids, or volunteer sign-ups, Calc can act as a lightweight database — no fancy software required. The key is setting up your data as a clean table with one record per row and consistent column headers, then leaning on named ranges, sorting, and filtering to keep things manageable.

Start by giving your guest list or sign-up sheet a named range so you can reference it easily in formulas and filters. Select the entire table, then go to **Sheet > Named Ranges and Expressions > Define** on the Menu bar. Type a meaningful name like "GuestList" or "AuctionBids," confirm the cell range, and click **Add**. From that point on, you can use that name in any formula instead of raw cell addresses, and the reference updates automatically if the range moves.

See `fig01.png`.

If your table has clear column headers — Name, RSVP Status, Table Number, Bid Amount — you can create named ranges for every column at once. Select the whole table including headers, go to **Sheet > Named Ranges and Expressions > Create**, and Calc will auto-detect whether headers are in the top row, left column, or both. Check **Top row** and hit **OK**; each column gets its own named range drawn from the header label.

For a more database-oriented setup, use **Data > Define Range** to create a database range. This is handy because it stores sorting, filtering, and subtotal settings right alongside the data. Mark the *Contains column labels* and *Contains totals row* options as needed.

Sorting is where things get practical. Need to arrange guests by last name, or rank auction bids highest-first? Click any cell in the relevant column and hit **Data > Sort Ascending** or **Data > Sort Descending** for a quick one-click sort. For multi-level sorting — say, sort by table number first, then by last name within each table — open **Data > Sort**, and use the *Sort Key 1*, *Sort Key 2*, and *Sort Key 3* drop-downs on the *Sort Criteria* tab. Set each key to the column you want, choose **Ascending** or **Descending**, and click **OK**.

See `fig02.png`.

Filtering lets you zero in on exactly what you need — like showing only guests who haven't RSVP'd, or only bids above a certain amount. Turn on AutoFilters by clicking a cell in your table and selecting **Data > AutoFilter**. Drop-down arrows appear on each header; click one and pick the value you want. The **Top 10** option is great for surfacing, say, the highest auction bids. You can also filter by **Empty** or **Not Empty** to catch missing responses on a sign-up sheet, or use **Text color** and **Background color** filters if you've color-coded statuses.

To clear all filters and see everything again, go to **Data > More Filters > Reset Filter**. For more complex criteria — like "RSVP = Yes AND Meal = Vegetarian" — use **Data > More Filters > Advanced Filter**, which reads filter conditions from a separate cell range you define elsewhere on the sheet.

See `fig03.png`.

Finally, use **Ctrl+F** (or **View > Toolbars > Find**) to quickly locate a specific guest or item. The Find toolbar supports **Match Case** and **Find All** to highlight every occurrence at once — useful when you need to track down every mention of a particular vendor or volunteer across multiple sheets.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > AutoFilter, More Filters > Advanced Filter, Sort, Define Range for RSVP and bid management_

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

