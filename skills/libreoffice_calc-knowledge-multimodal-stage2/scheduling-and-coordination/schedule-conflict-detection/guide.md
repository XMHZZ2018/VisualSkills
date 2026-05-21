# Schedule Conflict Detection (LibreOffice Calc 7.3.7)

When you're juggling rooms, people, or equipment across overlapping time slots, Calc can help you spot conflicts before they become problems. The trick is setting up your schedule data cleanly, then leaning on date/time handling, filtering, sorting, and a few formulas to surface overlaps.

Start by entering your schedule data with separate columns for Date, Name (or resource), Start time, Finish time, and Hours. Calc recognizes dates typed with slashes or hyphens (like 01/01/2008 or 2008-01-15) and times with colons (like 10:43:45), automatically formatting them for you. If Calc isn't interpreting your dates correctly, check **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns** to see which patterns your locale supports.

Once your data is in place, sorting by date and start time makes overlaps visually obvious. Select your range, open **Data > Sort**, and on the *Sort Criteria* tab pick your Date column as the first key and Start as the second, both **Ascending**. Make sure "Range contains column labels" is checked on the *Options* tab so your headers stay put.

See `fig01.png`.

To zero in on a specific person or resource, AutoFilter is your fastest friend. Click anywhere in your data range and hit **Data > AutoFilter** (or press *Ctrl+Shift+L*). Drop-down arrows appear on each column header — click the one on the Name column, uncheck **All**, and tick just the participant you want to inspect. Rows not matching are hidden instantly, and affected row numbers turn blue so you know filtering is active.

See `fig02.png`.

For more complex conflict queries — say, finding all entries where the start time falls before another entry's finish time on the same date — use the Standard Filter. Go to **Data > More Filters > Standard Filter** and build conditions using the Field name, Condition, and Value dropdowns. You can chain up to eight conditions with AND/OR operators, which is enough to compare time windows across multiple criteria. Enable "No duplications" if you only want unique conflicts listed.

See `fig03.png`.

If your conflict logic gets elaborate, consider the Advanced Filter instead (**Data > More Filters > Advanced Filter**). Write your filter criteria directly into a blank area of the spreadsheet — column headers matching your data, with conditions underneath — then point the dialog at that range. This approach is easier to tweak and reuse than rebuilding Standard Filter conditions each time.

For formula-driven detection, COUNTIFS is particularly handy: it can count how many other entries overlap a given time slot. Calc supports wildcards and regular expressions in functions like COUNTIFS, SUMIFS, and MATCH. You can toggle between wildcards and regex under **Tools > Options > LibreOffice Calc > Calculate** in the *Formulas Wildcards* section. A simple overlap test checks whether any other row's start time is less than the current row's finish time AND its finish time is greater than the current row's start time — if COUNTIFS returns more than 1, you've found a conflict.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > AutoFilter, More Filters (Standard/Advanced Filter), Sort for time overlap queries_

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

---

## UI Reference  —  Tools, Window, and Help Menus

_Scope: Tools > Options > Calc > Calculate for wildcards/regex in COUNTIFS_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

Read the screenshot `ui-tools-menu-expanded.png` in this directory.

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

