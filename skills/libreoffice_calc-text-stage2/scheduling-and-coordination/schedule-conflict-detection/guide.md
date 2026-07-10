# Schedule Conflict Detection (LibreOffice Calc 7.3.7)

When you're juggling rooms, people, or equipment across overlapping time slots, Calc can help you spot conflicts before they become problems. The trick is setting up your schedule data cleanly, then leaning on date/time handling, filtering, sorting, and a few formulas to surface overlaps.

Start by entering your schedule data with separate columns for Date, Name (or resource), Start time, Finish time, and Hours. Calc recognizes dates typed with slashes or hyphens (like 01/01/2008 or 2008-01-15) and times with colons (like 10:43:45), automatically formatting them for you. If Calc isn't interpreting your dates correctly, check **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns** to see which patterns your locale supports.

Once your data is in place, sorting by date and start time makes overlaps visually obvious. Select your range, open **Data > Sort**, and on the *Sort Criteria* tab pick your Date column as the first key and Start as the second, both **Ascending**. Make sure "Range contains column labels" is checked on the *Options* tab so your headers stay put.

The Sort dialog's Options tab shows a list of checkboxes under "Sort Options" including "Case sensitive" (unchecked), "Range contains column labels" (checked), "Include formats" (checked), "Enable natural sort" (unchecked), "Include boundary column(s) containing only comments" (unchecked), "Include boundary column(s) containing only images" (checked), and "Copy sort results to" (unchecked). Below those are a "Custom sort order" checkbox with a day-of-week dropdown, Language and Options dropdowns, and a Direction section with radio buttons for "Top to bottom (sort rows)" (selected) and "Left to right (sort columns)." The dialog has Help, Reset, OK, and Cancel buttons along the bottom.

To zero in on a specific person or resource, AutoFilter is your fastest friend. Click anywhere in your data range and hit **Data > AutoFilter** (or press *Ctrl+Shift+L*). Drop-down arrows appear on each column header — click the one on the Name column, uncheck **All**, and tick just the participant you want to inspect. Rows not matching are hidden instantly, and affected row numbers turn blue so you know filtering is active.

The spreadsheet shows AutoFilter active on a schedule with columns A (Date), B (Name), C (Start), D (Finish), and E (Hours), each header displaying a drop-down arrow. The Name column's drop-down is open, revealing options for Sort Ascending, Sort Descending, Top 10, Empty, Not Empty, Text color, Background color, and Standard Filter, followed by a "Search items…" field. Below that is an "All" checkbox (checked) with check/uncheck-all buttons, and individual name checkboxes for Brigitte (highlighted in blue), Fritz, Hans, Kurt, and Ute — all currently checked. The visible data spans rows 2 through 31 with dates ranging from 01/01/2008 to 08/01/2008, and the dropdown has OK and Cancel buttons at the bottom.

For more complex conflict queries — say, finding all entries where the start time falls before another entry's finish time on the same date — use the Standard Filter. Go to **Data > More Filters > Standard Filter** and build conditions using the Field name, Condition, and Value dropdowns. You can chain up to eight conditions with AND/OR operators, which is enough to compare time windows across multiple criteria. Enable "No duplications" if you only want unique conflicts listed.

The Standard Filter dialog has a "Filter Criteria" section at the top containing four condition rows, each with an Operator dropdown (for AND/OR, blank on the first row), a Field name dropdown (the first row shows "Category," the remaining three show "- none -"), a Condition dropdown (all set to "="), a Value dropdown (all empty), and a red X button to clear that row. The dialog is scrollable for additional rows. Below the criteria is a collapsible "Options" section with checkboxes for "Case sensitive" (unchecked), "Range contains column labels" (checked), "Copy results to" (unchecked) with an "- undefined -" dropdown and text field, "Regular expressions" (unchecked), "No duplications" (unchecked), and "Keep filter criteria" (checked). The bottom of the dialog has Help, Clear, OK, and Cancel buttons.

If your conflict logic gets elaborate, consider the Advanced Filter instead (**Data > More Filters > Advanced Filter**). Write your filter criteria directly into a blank area of the spreadsheet — column headers matching your data, with conditions underneath — then point the dialog at that range. This approach is easier to tweak and reuse than rebuilding Standard Filter conditions each time.

For formula-driven detection, COUNTIFS is particularly handy: it can count how many other entries overlap a given time slot. Calc supports wildcards and regular expressions in functions like COUNTIFS, SUMIFS, and MATCH. You can toggle between wildcards and regex under **Tools > Options > LibreOffice Calc > Calculate** in the *Formulas Wildcards* section. A simple overlap test checks whether any other row's start time is less than the current row's finish time AND its finish time is greater than the current row's start time — if COUNTIFS returns more than 1, you've found a conflict.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > AutoFilter, More Filters (Standard/Advanced Filter), Sort for time overlap queries_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is expanded from the menu bar, showing entries organized into groups: cell/row/column insertion items (Insert Cells, Insert Rows, Insert Columns, Insert Page Break), deletion items (Delete Cells, Delete Rows, Delete Columns, Delete Page Break), sheet insertion items (Insert Sheet, Insert Sheet at End, Insert Sheet from File, External Links), a greyed-out Delete Sheet entry, and further items including Clear Cells, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet, with additional entries partially visible below.

The Data menu is expanded from the menu bar, displaying entries from top to bottom: Sort…, Sort Ascending, Sort Descending, a checkbox for AutoFilter (unchecked), More Filters, Define Range…, Select Range…, a greyed-out Refresh Range, Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… partially visible at the bottom.

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

_Scope: Tools > Options > Calc > Calculate for wildcards/regex in COUNTIFS_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu is expanded from the menu bar, showing from top to bottom: Spelling…, Automatic Spell Checking (checked), Thesaurus… (greyed out), Language, AutoCorrect Options…, AutoInput (checked), ImageMap (greyed out), Redact, Auto-Redact, Goal Seek…, Solver…, Detective, Scenarios… (greyed out), Forms, Share Spreadsheet…, Protect Sheet… (unchecked), and Protect Spreadsheet Structure partially visible at the bottom.

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
