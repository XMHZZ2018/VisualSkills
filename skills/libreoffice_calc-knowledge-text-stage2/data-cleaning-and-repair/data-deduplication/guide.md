# Data Deduplication & Consolidation (LibreOffice Calc 7.3.7)

When you've got data scattered across multiple sheets or littered with duplicate rows, Calc has a few built-in tools that'll get you to a clean, unified dataset without much fuss. The main weapons here are the **Consolidate** feature and the various **Filter** options.

## Consolidating Data from Multiple Sheets

If you need to merge data from several sheets — say, departmental budgets or quarterly sales — head to **Data > Consolidate**. In the dialog, click the *Source data ranges* field and point it at your first range (you can type a reference or select it with the **Shrink / Expand** button). Hit **Add** to push it into the *Consolidation ranges* list, then repeat for each additional source. Set the *Copy results to* field to wherever you want the merged output to land.

The Consolidate dialog has a *Function* dropdown at the top (set to "Sum" in this example), followed by a *Consolidation ranges* list showing two added source ranges (e.g., $'Year 1'.$A$1:$E$5 and $'Year 2'.$A$1:$E$5). Below that are the *Source data ranges* field with a dropdown and a Shrink/Expand button, the *Copy results to* field (here pointing to $'Consolidated Sales'.$A$1), and **Add** and **Delete** buttons. At the bottom, an expanded *Options* section shows **Consolidate by** checkboxes for "Row labels" and "Column labels" (both checked), and an **Options** group with a "Link to source data" checkbox (also checked). The dialog finishes with **Help**, **OK**, and **Cancel** buttons.

Pick an aggregation function from the *Function* dropdown — **Sum** is the default, but you've also got Count, Average, Max, Min, Product, and several statistical options. Expand the **Options** section to fine-tune how ranges are matched: check **Row labels** and/or **Column labels** if your sources share headers but the rows and columns aren't in the same order. Without these checked, Calc consolidates purely by cell position. Enabling **Link to source data** inserts live formulas so your consolidated sheet updates automatically when the source data changes.

If you consolidate the same ranges often, convert them to named ranges first — it saves time on repeat runs.

## Removing Duplicates with Filters

For deduplication, the Standard Filter is your best friend. Select your data range and go to **Data > More Filters > Standard Filter**. In the dialog, set your field name, condition, and value to target the rows you care about, then check the **No duplications** option under *Options*. This strips duplicate rows right out of the filtered results.

The Standard Filter dialog is titled "Standard Filter" and contains a *Filter Criteria* section at the top with four rows of filter conditions, each consisting of an **Operator** dropdown, a **Field name** dropdown (the first row shows "Category"), a **Condition** dropdown (defaulting to "="), a **Value** dropdown, and a red X button to clear that row. Below the filter rows is an expanded *Options* section with checkboxes for "Case sensitive," "Range contains column labels" (checked), "Copy results to" (with a greyed-out destination field and Shrink/Expand button), "Regular expressions," "No duplications" (unchecked), and "Keep filter criteria" (checked). The dialog has **Help**, **Clear**, **OK**, and **Cancel** buttons along the bottom.

For a quicker, lighter-weight approach, use **AutoFilter** via **Data > AutoFilter** (or **Ctrl+Shift+L**). This drops arrow buttons onto each column header, letting you toggle individual values on or off with checkboxes. It's great for eyeballing duplicates and selectively hiding them, though it doesn't have the explicit "no duplications" toggle that the Standard Filter offers.

If your filtering logic is complex or reusable, try **Data > More Filters > Advanced Filter**. You define your criteria in a separate cell range on the sheet — column headers on top, conditions beneath — then point the Advanced Filter dialog at that range. Like the Standard Filter, it supports **No duplications** to exclude repeated entries. You can also tick **Copy results to** and redirect the clean output to a different location, keeping your original data untouched.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Consolidate, AutoFilter, More Filters > Standard/Advanced Filter with No duplications option_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the LibreOffice Calc menu bar. It lists items in order from top to bottom: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break, then a separator followed by Delete Cells…, Delete Rows, Delete Columns, Delete Page Break. After another separator: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, and Delete Sheet… (greyed out). Then: Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet… with additional items continuing below the visible area.

The Data menu is shown expanded from the LibreOffice Calc menu bar. It lists items from top to bottom: Sort…, Sort Ascending, Sort Descending, then a checkbox-style AutoFilter entry, followed by More Filters. After a separator: Define Range…, Select Range…, Refresh Range (greyed out). Then: Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… with additional items continuing below.

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
