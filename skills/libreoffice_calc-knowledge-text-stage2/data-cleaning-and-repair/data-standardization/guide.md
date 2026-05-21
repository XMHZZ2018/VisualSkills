# Data Standardization (LibreOffice Calc 7.3.7)

Messy data comes in all shapes — dates in three different formats, inconsistent capitalization, rogue spaces. Calc gives you a solid toolkit to whip things into shape without retyping everything by hand.

**Enforcing consistent input with validation.** The best way to standardize data is to prevent bad entries in the first place. Select the target cells, then head to **Data > Validity** to open the Validity dialog. On the Criteria tab, set the *Allow* dropdown to the type you need — *Date* forces date formatting, *Whole Numbers* restricts to integers, and *List* lets you define an explicit set of acceptable values. Check **Show selection list** to give users a dropdown right in the cell, which is perfect for standardizing category fields like status codes or department names.

The Validity dialog is shown with the Criteria tab active. The Allow dropdown is set to "Cell range" and is highlighted in blue. Below it are checkboxes for "Allow empty cells" (checked) and "Show selection list" (checked), with an indented unchecked "Sort entries ascending" option beneath. A Source text field with a shrink button sits below, accompanied by a note explaining that a valid source must be a contiguous selection of rows and columns or a formula resulting in an area or array. The dialog has three tabs along the top — Criteria, Input Help, and Error Alert — and four buttons at the bottom: Help, Reset, OK (highlighted), and Cancel.

You can also guide people toward correct input. Flip to the **Input Help** tab and write a short message explaining the expected format — it'll pop up whenever someone clicks the cell. On the **Error Alert** tab, choose *Stop* to flat-out reject invalid entries, or *Warning* to let them through with a nudge. A custom error message here ("Please use YYYY-MM-DD format") goes a long way.

**Spotting existing bad data.** Already have a sheet full of inconsistencies? After setting up your validity rules, go to **Tools > Detective > Mark Invalid Data** to highlight every cell that breaks the rules. Fix them up, then clear the markers with **Tools > Detective > Remove All Traces**.

**Bulk-replacing inconsistent values.** For standardizing text that's already in the sheet — say, replacing every "USA", "U.S.A.", and "United States" with a single canonical value — open **Edit > Find and Replace** (or just hit *Ctrl+H*). Type the variant in the *Find* box, the standard form in *Replace*, and click **Replace All**. Enable **Regular expressions** under *Other options* if you need pattern matching, like catching "St." and "Street" in one pass. Wildcards work too: `?` matches any single character and `*` matches any sequence.

The Find and Replace dialog is displayed with a Find text field and a Replace text field at the top, each with a dropdown arrow. Below the Find field are checkboxes for "Match case", "Formatted display" (checked), "Entire cells", and "All sheets". A row of five buttons spans the middle: Find All, Find Previous, Find Next, Replace, and Replace All. An expanded "Other options" section below shows checkboxes in two columns — on the left: "Current selection only" (checked), "Wildcards" (greyed out), "Regular expressions" (greyed out), "Similarity search" (checked) with a "Similarities…" button, and "Diacritic-sensitive"; on the right: "Replace backwards", "Cell Styles" (greyed out), "Match character width", "Sounds like (Japanese)" with a "Sounds…" button, and "Kashida-sensitive". At the bottom, Direction radio buttons offer "Rows" (selected) and "Columns", and a "Search in" dropdown is set to "Formulas". Help and Close buttons appear in the bottom corners.

Be careful with **Replace All** — a sloppy pattern can do real damage across an entire sheet. When in doubt, use **Find Next** and **Replace** one at a time to verify each match before committing.

**Normalizing date formats.** Dates that Calc already recognizes internally can be reformatted in one move: select the column, open **Format > Cells**, and pick the date pattern you want. The tricky part is dates stored as plain text. Use Find and Replace with regular expressions to restructure them — for instance, converting "12/31/2023" to "2023-12-31" — or use helper columns with `DATEVALUE()`, `TEXT()`, and date-part functions like `YEAR()`, `MONTH()`, and `DAY()` to parse and reassemble.

**Using regular expressions in functions.** Calc's functions like COUNTIF, SUMIF, MATCH, SEARCH, and VLOOKUP all support regex when you enable it under **Tools > Options > LibreOffice Calc > Calculate** by selecting **Enable regular expressions in formulas**. This is powerful for counting or summing across messy categories — `=COUNTIF(A1:A100,".*blue.*")` would catch "Blue", "light blue", "BLUE", since regex searches in Calc are case-insensitive by default.

The Options dialog is open at the "LibreOffice Calc – Calculate" page. The left-hand navigation tree shows collapsible categories (LibreOffice, Load/Save, Language Settings, and the expanded LibreOffice Calc section with sub-items General, Defaults, View, Calculate (highlighted in blue), Formula, Sort Lists, Changes, Compatibility, Grid, and Print), plus collapsed LibreOffice Base, Charts, and Internet nodes. The right-hand pane has four sections: "Formulas Wildcards" with three radio buttons — "Enable wildcards in formulas" (selected), "Enable regular expressions in formulas", and "No wildcards or regular expressions in formulas"; a "Date" group with radio buttons for the date base (12/30/1899 selected as default, plus 01/01/1900 and 01/01/1904); "General Calculations" with checkboxes for "Case sensitive" (checked), "Precision as shown", "Search criteria = and <> must apply to whole cells" (checked), "Automatically find column and row labels", and "Limit decimals for general number format" with a Decimal places spinner set to 0; "Iterative References" with an "Iterations" checkbox (unchecked), Steps spinner (100), and Minimum change field (0.001); and "CPU Threading Settings" with "Enable multi-threaded calculation" checked. Buttons at the bottom include Help, Reset, Apply, OK (highlighted), and Cancel.

**Sorting to surface outliers.** Once you've cleaned things up, a quick sort via **Data > Sort Ascending** helps you visually scan for remaining oddities that slipped through — misspellings cluster near their correct versions, making them easy to spot and fix.

---

## UI Reference  —  Edit and View Menus

_Scope: Edit > Find and Replace (Ctrl+H) for bulk-replacing inconsistent values with regex/wildcards_

The Edit menu handles clipboard operations, find/replace, selection modes, track changes, and cell editing controls. The View menu manages display modes, UI element visibility, freeze/split panes, sidebar panels, and zoom.

## Screenshots

The Edit menu is shown expanded from the menu bar. It lists items vertically: Undo, Redo, and Repeat (all greyed out), followed by a separator, then Cut, Copy, and Paste (greyed out), Paste Special, a separator, Select All (with the shortcut Shi… partially visible), Select, a separator, Find… and Find and Replace… (with a checkbox icon beside it), and Track Changes at the bottom. The menu appears over a mostly empty spreadsheet with cell A1 selected.

The View menu is shown expanded from the menu bar. At the top are two radio-button items: Normal (selected) and Page Break. Below a separator are User Interface… and Toolbars, then checkboxes for Formula Bar (checked), Status Bar (checked), View Headers (checked), and View Grid Lines (checked). Next is Grid and Helplines, followed by unchecked toggles for Value Highlighting, Column/Row Highlighting, Hidden Row/Column Indicator, and Show Formula. Comments appears greyed out. After a separator come unchecked checkboxes for Split Window, Freeze Rows and Columns, and Freeze Cells, then a checked Sidebar item. The menu is displayed over a spreadsheet with a yellow information bar visible behind it.

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

## UI Reference  —  Format Menu

_Scope: Cells (Ctrl+1) for reformatting date columns to a standard pattern_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

The Format menu is shown expanded from the menu bar. Items listed from top to bottom are: Text, Align Text, and Number Format (each with submenu arrows), a separator, Clone Formatting (with an unchecked checkbox icon), Clear Direct Formatting, a separator, Cells…, Rows, Columns, Merge and Unmerge C… (label truncated), a separator, Character… and Paragraph… (both greyed out), a separator, Page Style…, Print Ranges, Conditional (with a submenu arrow), AutoFormat Styles… (greyed out), a separator, Spreadsheet Theme, Theme…, a separator, Image, and Chart. The menu overlaps a spreadsheet showing a cell containing the text "ning versi" (partially visible) and a cell with "B" in it.

## Elements

- **Text** — submenu: Bold (Ctrl+B), Italic (Ctrl+I), Single/Double Underline, Strikethrough, Overline, Superscript (Shift+Ctrl+P), Subscript (Shift+Ctrl+B), Shadow, Outline, Wrap Text, case conversions (UPPERCASE, lowercase, Cycle Case Shift+F3, Sentence case, Capitalize Every Word, tOGGLE cASE)
- **Align Text** — horizontal/vertical alignment options
- **Number Format** — quick presets: General (Shift+Ctrl+6), Number (Shift+Ctrl+1), Percent (Shift+Ctrl+5), Currency (Shift+Ctrl+4), Date (Shift+Ctrl+3), Time, Scientific (Shift+Ctrl+2), Thousands Separator
- **Clone Formatting** — toggle paint-bucket mode
- **Clear Direct Formatting** (Ctrl+M) — reverts to style defaults
- **Cells…** (Ctrl+1) — opens the Format Cells dialog (see [format-cells-dialog](format-cells-dialog.md))
- **Rows** — submenu: Height…, Optimal Height…, Hide, Show
- **Columns** — submenu: Width…, Optimal Width…, Hide, Show
- **Merge and Unmerge Cells** — submenu: Merge and Center Cells, Merge Cells, Unmerge Cells (all require multi-cell selection)
- **Character…**, **Paragraph…** — greyed when not in text-edit mode
- **Page Style…** — opens Page Style dialog (7 tabs: Organizer, Page, Borders, Background, Header, Footer, Sheet)
- **Print Ranges** — submenu: Define, Add, Edit…, Clear
- **Conditional** — submenu: Condition…, Color Scale…, Data Bar…, Icon Set…, Date…, Manage…
- **AutoFormat Styles…** — greyed without data range selected
- **Spreadsheet Theme**, **Theme…**
- **Image**, **Chart**, **Sparklines**, **Text Box and Shape**, **Anchor**, **Arrange**, **Flip**, **Group** — object-specific (greyed when no object selected)
- **Name…**, **Alt Text…** — object naming/accessibility (greyed when no object selected)

---

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Validity dialog for enforcing input rules and Mark Invalid Data_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar. It lists items from top to bottom: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break (each with submenu arrows where applicable), a separator, Delete Cells…, Delete Rows, Delete Columns, Delete Page Break, a separator, Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet… (greyed out), a separator, Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions (truncated), Cell Comments, and Rename Sheet… at the bottom. The menu appears over a spreadsheet showing "4.2 of LibreO…" in a cell and column C visible.

The Data menu is shown expanded from the menu bar. Items listed from top to bottom are: Sort… (with a submenu arrow), Sort Ascending, Sort Descending (labels partially truncated), a separator, AutoFilter (with an unchecked checkbox icon), More Filters, a separator, Define Range…, Select Range…, Refresh Range (greyed out), a separator, Pivot Table, Calculate, Validity…, Subtotals…, Form…, Streams…. The menu appears over a spreadsheet with a cell displaying "LibreOffice for" and column D visible.

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

_Scope: Tools > Detective > Mark Invalid Data, Remove All Traces after validation cleanup_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu is shown expanded from the menu bar. Items listed from top to bottom are: Spelling…, Automatic Spell C… (checked, label truncated), Thesaurus… (greyed out), Language, AutoCorrect Options (truncated), a separator, AutoInput (checked), ImageMap (greyed out), Redact, Auto-Redact, a separator, Goal Seek…, Solver…, Detective, Scenarios… (greyed out), a separator, Forms, Share Spreadsheet (truncated), a separator, Protect Sheet… (with an unchecked checkbox), and Protect Spreadsh… (truncated, with an unchecked checkbox). The menu appears over a spreadsheet showing "Office for the firs" (truncated) in a cell with columns D and E visible.

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
