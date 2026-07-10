# Lending & Borrowing Tracking (LibreOffice Calc 7.3.7)

Calc works surprisingly well as a lightweight lending tracker — think library loans, equipment checkouts, or shared tool inventories. The trick is treating your spreadsheet like a flat database table, then leaning on named ranges, validation, and filters to keep things tidy.

Start by laying out your columns: Item Name, Borrower, Date Loaned, Due Date, Date Returned, Condition, and Overdue Fee. Select the entire table area and give it a named range by typing a name (like `LendingLog`) directly into the Name Box at the left of the Formula bar, then pressing *Enter*. You can also go to **Sheet > Named Ranges and Expressions > Define** to do this through a dialog. Named ranges let your formulas reference the table by name instead of raw cell addresses, and they update automatically if you add rows later.

See `fig01.png`.

To formally treat the range as a database table — which unlocks sorting, filtering, and subtotaling features — open **Data > Define Range**, give it a name, and expand the *Options* section. Tick **Contains column labels** so Calc knows your first row holds headers, and **Contains totals row** if you plan to summarize fees at the bottom.

For the Condition column, you'll want to lock entries to a controlled list (like "Good," "Damaged," "Missing") so nobody types free-form junk. Select the Condition cells, then go to **Data > Validity**. On the *Criteria* tab, set the *Allow* dropdown to **List** and type your allowed values into the *Entries* box. Enable **Show selection list** so borrowers see a dropdown. You can flip to the *Input Help* tab to add a tooltip like "Select the item's return condition," and use the *Error Alert* tab to block invalid entries outright — set the *Action* to **Stop** and write a clear error message.

See `fig02.png`.

Calculating overdue fees is just a formula. Something like `=IF(AND(E2="",TODAY()>D2),(TODAY()-D2)*1.50,0)` checks whether the item is still out past its due date and multiplies the overdue days by a daily rate. For returned items, swap `TODAY()` for the actual return date in column E. Wrap the whole thing in an `IF` so returned-on-time rows show zero.

When your list gets long, filtering is your best friend. Click anywhere in the table and hit **Data > AutoFilter** (or press *Ctrl+Shift+L*) to add dropdown arrows to every column header. From there you can instantly show only overdue items, filter by borrower name, or isolate "Damaged" and "Missing" returns to investigate. The **Top 10** option is handy for spotting the biggest fee balances at a glance. If you need more complex criteria — say, all items overdue by more than 14 days from a specific borrower — use **Data > More Filters > Standard Filter** instead.

See `fig03.png`.

To hunt down suspicious data — maybe someone entered a return date before the loan date, or left a required field blank — run **Tools > Detective > Mark Invalid Data**. Calc highlights any cells that violate your validity rules, making it easy to clean things up. Once you've corrected the entries, clear the marks with **Tools > Detective > Remove All Traces**.

That's really all you need: a named range for structure, validation to keep entries clean, a couple of date-math formulas for fees, and AutoFilter to slice through the noise when you're chasing down missing or damaged items.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > AutoFilter, More Filters > Standard Filter, Validity, Define Range for loan tracking_

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

_Scope: Tools > Detective > Mark Invalid Data for spotting invalid loan entries_

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

