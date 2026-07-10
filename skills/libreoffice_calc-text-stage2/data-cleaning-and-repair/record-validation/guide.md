# Record Validation & Verification (LibreOffice Calc 7.3.7)

When you're building spreadsheets that others will use — or just want to keep your own data clean — Calc's validation and detective tools are your best friends. They let you define exactly what's allowed in each cell, flag anything that doesn't fit, and trace formulas back to their sources to verify calculations.

To set up validation, select a cell or range and head to **Data > Validity** on the menu bar. The Criteria tab is where you pick what kind of data the cell accepts: whole numbers, decimals, dates, text of a certain length, or values from a cell range or list. You can even write a custom formula — for instance, `ISEVEN(A4)` to allow only even numbers. If you need to restrict input to a predefined set of choices, tick **Show selection list** and the cell gets a handy drop-down.

The Validity dialog is shown with the Criteria tab active and three tabs across the top: Criteria, Input Help, and Error Alert. The "Allow" dropdown is set to "Cell range" (highlighted in blue), with "Allow empty cells" and "Show selection list" both checked, and an unchecked "Sort entries ascending" sub-option beneath. Below these options is a "Source" text field with a shrink-to-sheet button, accompanied by a note explaining that a valid source must be a contiguous selection of rows and columns or a formula that results in an area or array. The bottom of the dialog has Help, Reset, OK, and Cancel buttons.

Over on the **Input Help** tab, you can write a short message that pops up whenever someone clicks the cell — great for explaining what's expected without cluttering the sheet. The **Error Alert** tab controls what happens when bad data sneaks in: set the action to *Stop* to outright reject it, or choose *Warning* or *Information* if you'd rather let users decide. You can customize the error title and message so it's actually helpful rather than cryptic.

Once validation rules are in place, you can audit your sheet after the fact. Go to **Tools > Detective > Mark Invalid Data** and Calc will circle every cell that currently violates its validation rule. Fix the offending entries, then clear the marks with **Tools > Detective > Remove All Traces**.

When a formula gives you something unexpected — `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?` — those error codes are your first clue. A `#DIV/0!` usually means a blank or zero snuck into a divisor; wrapping the formula in an IF check like `=IF(C3>0, B3/C3, "No Report")` handles it gracefully. A `#VALUE!` often means text landed in a numeric field, and `#REF!` points to a deleted sheet or shifted range.

The spreadsheet displays a table with columns Date (A), Patients (B), Nursing Staff (C), and Patients per Nurse (D), containing daily records from 01/05/2007 through 11/05/2007 in rows 3–13. Most rows show valid ratios in column D (e.g., 4.8, 3.2, 7), but row 6 has a Nursing Staff value of 0 and row 8 has an empty Nursing Staff cell — both producing a #DIV/0! error in the Patients per Nurse column, clearly illustrating how zero and blank divisors trigger this error.

To verify calculations against their source data, use the Detective. Select a formula cell and choose **Tools > Detective > Trace Precedents** (or press *Shift+F9*). Calc draws arrows from every cell that feeds into your formula, so you can visually confirm it's pulling from the right places. If you also enable **View > Value Highlighting** (*Ctrl+F8*), text shows in black and numbers in blue — an instant way to spot a "number" that's actually stored as text and silently breaking your math.

The spreadsheet shows row 3 of the same table with Value Highlighting and Trace Precedents both active. The formula bar at the top displays `=IF(C3>0,B3/C3,"No Report")` with "IF" shown in the Name Box. Cells B3 (24) and C3 (5) are outlined with colored borders — red for numeric values — and magenta/pink Trace Precedent arrows run from both B3 and C3 into the formula cell D3, visually confirming which cells feed the calculation.

Between validation rules on the front end, the Detective for tracing formula logic, and value highlighting for catching type mismatches, you have a solid toolkit for keeping records consistent and calculations trustworthy.

---

## UI Reference  —  Edit and View Menus

_Scope: View > Value Highlighting for spotting text stored as numbers_

The Edit menu handles clipboard operations, find/replace, selection modes, track changes, and cell editing controls. The View menu manages display modes, UI element visibility, freeze/split panes, sidebar panels, and zoom.

## Screenshots

The Edit menu is expanded from the menu bar, showing a vertical list of items: Undo, Redo, Repeat, then a separator, followed by Cut, Copy, Paste, Paste Special, then Select All, Select, then Find… and Find and Replace… (with a checkbox icon), and Track Changes at the bottom. Several items such as Undo, Redo, and Repeat appear greyed out, indicating no actions are available to undo or repeat.

The View menu is expanded, showing radio buttons for Normal (selected) and Page Break at the top, followed by User Interface… and Toolbars. Below that are checked toggle items: Formula Bar, Status Bar, View Headers, and View Grid Lines. Then Grid and Helplines, followed by unchecked toggles for Value Highlighting, Column/Row Highlighting, Hidden Row/Column Indicator, and Show Formula. Further down are Comments (greyed), Split Window, Freeze Rows and Columns, Freeze Cells, and Sidebar (checked).

## Edit Menu Elements

- **Undo** (Ctrl+Z), **Redo** (Ctrl+Y), **Repeat** (Shift+Ctrl+Y)
- **Cut** (Ctrl+X), **Copy** (Ctrl+C), **Paste** (Ctrl+V) — standard clipboard ops
- **Paste Special** — submenu: Paste Unformatted Text (Shift+Ctrl+Alt+V), Paste Only Text/Numbers/Formula, Paste Transposed, Paste Special… (Shift+Ctrl+V)
- **Select All** (Shift+Ctrl+Space)
- **Select** — submenu: Select All Sheets, Select Sheets…, Select to Next/Previous Sheet, Select Row (Shift+Space), Select Column (Ctrl+Space), Select Data Area (Ctrl+\*), Select Unprotected Cells, Select Visible Rows/Columns Only
- **Find…** (Ctrl+F) — opens the Find toolbar docked at the bottom
- **Find and Replace…** (Ctrl+H) — opens the Find and Replace dialog with match case, entire cells, all sheets, regex, wildcards, and direction options
- **Track Changes** — submenu: Record (toggle), Show, Manage, Comment, Protect, Compare Document, Merge Document
- **Cell Edit Mode** (F2) — enters inline cell editing
- **Cell Protection** — toggle (checked by default)
- **Links to External Files…** — manage external links (greyed when none exist)
- **Edit Mode** (Shift+Ctrl+M) — toggle for read-only documents

## View Menu Elements

- **Normal** / **Page Break** — radio toggle for view mode
- **User Interface…** — choose UI layout (Standard Toolbar, Tabbed, Groupedbar, etc.)
- **Toolbars** — submenu listing 20 available toolbars; Formatting and Standard enabled by default
- **Formula Bar** ✓, **Status Bar** ✓, **View Headers** ✓, **View Grid Lines** ✓ — visibility toggles (all on by default)
- **Grid and Helplines** — submenu: Display Grid, Snap to Grid, Helplines While Moving
- **Value Highlighting** (Ctrl+F8) — colours cells by data type (text=black, numbers=blue, formulas=green)
- **Column/Row Highlighting**, **Hidden Row/Column Indicator**, **Show Formula** (Ctrl+\`)
- **Split Window**, **Freeze Rows and Columns**, **Freeze Cells** (submenu: Freeze First Column/Row)
- **Sidebar** (Ctrl+F5), **Styles** (F11), **Gallery**, **Navigator** (F5), **Function List**, **Data Sources** (Shift+Ctrl+F4)
- **Full Screen** (Shift+Ctrl+J)
- **Zoom** — submenu: Entire Page, Page Width, Optimal View, 50%/75%/100%/150%/200%, Zoom…

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Validity for criteria, input help, error alerts; Detective > Mark Invalid Data_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is expanded from the menu bar, displaying a long vertical list organized in groups: Insert Cells…, Insert Rows, Insert Columns, and Insert Page Break at the top, followed by Delete Cells…, Delete Rows, Delete Columns, and Delete Page Break. A separator precedes sheet management items: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, and Delete Sheet… (greyed out). Below another separator are Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet…, with the list continuing below the visible area.

The Data menu is expanded, showing Sort…, Sort Ascending, and Sort Descending at the top, followed by AutoFilter (unchecked checkbox) and More Filters. Below a separator are Define Range…, Select Range…, and Refresh Range (greyed out). Then Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… appear in the lower portion of the menu.

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

_Scope: Tools > Detective > Mark Invalid Data and Trace Precedents for validation auditing_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu is expanded from the menu bar, showing Spelling… at the top, followed by Automatic Spell Checking (checked), Thesaurus… (greyed out), Language, and AutoCorrect Options…. Below is AutoInput (checked), then ImageMap (greyed), Redact, and Auto-Redact. The next group contains Goal Seek… and Solver…, followed by Detective (which leads to the formula auditing submenu) and Scenarios… (greyed). Further down are Forms, Share Spreadsheet…, Protect Sheet… (unchecked checkbox), and the beginning of Protect Spreadsheet Structure… visible at the bottom edge.

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
