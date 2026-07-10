# Home Inventory Management (LibreOffice Calc 7.3.7)

Tracking everything your household owns — from pantry staples to insurance-worthy electronics — is one of those tasks Calc handles surprisingly well. Think of your spreadsheet as a flat database: each row is an item, each column a field like Category, Item Name, Location, Purchase Date, Value, and Expiration Date. Keep your header row consistent and descriptive, because almost every useful feature in Calc keys off those headers.

Once your table is laid out, give it a name so Calc can treat it as a proper data range. Select all your inventory cells (headers included), then go to **Sheet > Named Ranges and Expressions > Define** and type something like "HomeInventory." This makes sorting, filtering, and formula references far cleaner — you can write `=SUMIF(HomeInventory.Category,"Electronics",HomeInventory.Value)` instead of juggling raw cell addresses. You can revisit or edit these ranges anytime via **Sheet > Named Ranges and Expressions > Manage** or just press *Ctrl+F3*.

The Define Name dialog has a "Name" text field at the top (here showing "ExamResults" as an example), a "Range or formula expression" field below it displaying the absolute cell reference (e.g. `$Sheet1.$A$1:$H$11`), and a "Scope" dropdown set to "Document (Global)." A collapsible "Range Options" section at the bottom provides checkboxes for Print range, Filter, Repeat column, and Repeat row. The dialog is completed with Help, Add, and Cancel buttons along the bottom edge.

For a large inventory, you'll want to zero in on specific categories fast. Turn on AutoFilter by clicking anywhere in your table and selecting **Data > AutoFilter** (or press *Ctrl+Shift+L*). Drop-down arrows appear on every header — click one to show only "Kitchen" items, or only things purchased from a particular store. You can even filter by **Text color** or **Background color** if you've been color-coding expiration urgency.

The AutoFilter combo box drops down from a column header (here column A, "Student") and presents several sections: Sort Ascending and Sort Descending at the top, then quick-filter options (Top 10, Empty, Not Empty), followed by Text color and Background color entries — each shown with colored swatches (green, red, yellow) to the right — and a "Standard Filter…" link. Below that is a "Search items…" text field, an "All" checkbox with select-all/deselect-all buttons, and a scrollable checklist of individual values (Andrew, Bethany, Charles, David, Emily, Ferdinand, Georgia, Haley, etc.) each with its own checkbox. OK and Cancel buttons sit at the bottom.

When AutoFilter isn't enough — say you need all items worth over $100 that are also in the "Living Room" — open **Data > More Filters > Standard Filter**. This dialog lets you chain up to eight conditions with AND/OR logic across different fields. Set the Field name, Condition, and Value for each row, then hit **OK** to narrow your view.

The Standard Filter dialog is titled "Standard Filter" and contains a "Filter Criteria" section with four condition rows arranged in columns: Operator (a dropdown for AND/OR logic, blank on the first row), Field name (a dropdown, with the first row set to "Category"), Condition (a dropdown defaulting to "="), and Value (a dropdown for entering the comparison value). Each row has a red X button to clear it, and the remaining rows show "- none -" in the Field name column. Below the criteria rows is a collapsible "Options" section with checkboxes for Case sensitive, Range contains column labels (checked by default), Copy results to, Regular expressions, No duplications, and Keep filter criteria. The dialog finishes with Help, Clear, OK, and Cancel buttons at the bottom.

Sorting keeps things tidy as your list grows. Select your data range, go to **Data > Sort**, and pick your sort column — expiration date ascending is great for emergency-preparedness kits, while value descending helps prioritize insurance documentation. Check **Range contains column labels** on the Options tab so your headers stay put.

For expiration monitoring specifically, a simple formula does wonders. In a "Status" column, something like `=IF(E2="","—",IF(E2<TODAY(),"EXPIRED",IF(E2<TODAY()+30,"Expiring Soon","OK")))` gives you an at-a-glance flag. Pair that with conditional formatting — red background for "EXPIRED," yellow for "Expiring Soon" — and nothing slips through the cracks.

If you want to separate concerns, use multiple sheets within the same file: one for household supplies, one for insurance valuables, one for emergency kit items. Database ranges defined via **Data > Define Range** let each sheet behave independently for sorting and filtering while still living in a single document. Just remember that database range names can only contain letters, numbers, and underscores — no spaces or hyphens.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > AutoFilter, More Filters > Standard Filter, Sort, Define Range; Sheet > Named Ranges_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is expanded from the menu bar, showing a single-column list of entries grouped by function. At the top are cell and row/column insertion items (Insert Cells…, Insert Rows, Insert Columns, Insert Page Break), followed by their deletion counterparts (Delete Cells…, Delete Rows, Delete Columns, Delete Page Break). Below a separator are sheet-insertion entries (Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…) with "Delete Sheet…" greyed out. The lower portion contains Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet…, with additional items continuing below the visible area.

The Data menu is expanded from the menu bar, displaying a single-column list. The top group contains Sort…, Sort Ascending, and Sort Descending. Next is AutoFilter (with an unchecked checkbox icon to its left), followed by More Filters and then Define Range…, Select Range…, and Refresh Range (greyed out). Further down are Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams…, with additional entries continuing below the visible portion of the menu.

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
