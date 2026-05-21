# Transaction & Rewards Analysis (LibreOffice Calc 7.3.7)

When you're staring at a big spreadsheet of transactions — purchases, dates, amounts, reward categories — the first thing you want is to narrow it down. Calc gives you three flavors of filtering, plus sorting and search, that make transaction analysis straightforward.

**AutoFilter** is the fastest way to slice your data. Click anywhere in your transaction table, then hit **Data > AutoFilter** (or press *Ctrl+Shift+L*). Drop-down arrows appear on every column header. Click one to filter by specific merchants, date ranges, or reward categories — just tick the values you want and hit **OK**. The **Top 10** option in that dropdown is great for spotting your highest-spending transactions quickly, and you can use **Background color** filtering if you've color-coded reward tiers.

The AutoFilter combo box dropdown is shown open on a column header labeled "Student" in a spreadsheet with columns A, B, and C. The dropdown menu lists sorting options (Sort Ascending, Sort Descending), special filters (Top 10, Empty, Not Empty), color-based filters (Text color, Background color — the latter highlighted in blue — with green, red, and yellow color swatches shown to the right), a Standard Filter link, and a "Search items…" text field. Below that is a scrollable checklist with an "All" checkbox and individual value checkboxes (Andrew, Bethany, Charles, David, Emily, Ferdinand, Georgia, Haley), with OK and Cancel buttons at the bottom.

For more targeted anomaly detection, open **Data > More Filters > Standard Filter**. This dialog lets you stack up to eight conditions with AND/OR logic — for example, filtering transactions where the amount is above a threshold AND the category is unexpected. Pick your **Field name**, set a **Condition** like "greater than," type a **Value**, and chain rows together. Tick **No duplications** if you want to eliminate repeated entries, or enable **Regular expressions** to match patterns in merchant names.

The Standard Filter dialog is displayed with a title bar reading "Standard Filter." The upper section, labeled "Filter Criteria," contains four condition rows, each with dropdown columns for Operator (AND/OR, blank on the first row), Field name, Condition, and Value, plus a red X button to clear each row. The first row has "Category" selected in the Field name dropdown and "=" as the Condition; the remaining three rows are set to "- none -." Below the criteria rows is a collapsible "Options" section with checkboxes for Case sensitive, Range contains column labels (checked), Copy results to (with an "- undefined -" dropdown and an empty text field), Regular expressions, No duplications, and Keep filter criteria (checked). The bottom of the dialog has Help, Clear, OK (highlighted in blue), and Cancel buttons.

If your anomaly-detection rules are complex or reusable, try an **Advanced Filter** instead. Write your filter criteria directly into a blank area of a sheet — copy your column headers, then put conditions beneath them. Criteria on the same row are joined with AND; separate rows act as OR. Then select your data, go to **Data > More Filters > Advanced Filter**, point the **Read Filter Criteria From** field to your criteria range, and click **OK**. This approach is especially handy when you want to keep a persistent "anomaly rules" block alongside your transaction data.

Once you've filtered, sorting helps you prioritize. Select your range and go to **Data > Sort** to open the Sort dialog. Under the *Sort Criteria* tab, set up to three sort keys — say, date descending as the primary key and amount descending as secondary. On the *Options* tab, check **Range contains column labels** so your headers stay put, and consider **Enable natural sort** if your transaction IDs mix letters and numbers (like TXN1, TXN2, ... TXN19) so they sort in human-friendly order. For a quick one-click sort, just use **Data > Sort Ascending** or **Data > Sort Descending**.

To hunt for a specific merchant or transaction ID, press *Ctrl+F* to pop open the **Find** toolbar. Type your search term, toggle **Match Case** if needed, and click **Find All** to highlight every occurrence at once — useful for auditing all charges from a single vendor.

When grouping transactions by period for rewards analysis, **Data > Group and Outline > AutoOutline** can automatically collapse columns that feed into quarterly or monthly subtotals, giving you a clean summary view without hiding the detail. Remove groupings later with **Data > Group and Outline > Remove Outline**.

---

## UI Reference  —  Edit and View Menus

_Scope: Edit > Find (Ctrl+F) toolbar and Find All for merchant lookup_

The Edit menu handles clipboard operations, find/replace, selection modes, track changes, and cell editing controls. The View menu manages display modes, UI element visibility, freeze/split panes, sidebar panels, and zoom.

## Screenshots

The Edit menu is shown expanded from the LibreOffice Calc menu bar, displaying its entries in order from top to bottom: Undo, Redo, Repeat (separated by a divider), Cut, Copy, Paste, Paste Special (with a submenu arrow), Select All, Select (with a submenu arrow), then a divider followed by Find…, Find and Replace… (with a checkbox icon), and Track Changes (with a submenu arrow). Several items appear greyed out, indicating they are currently unavailable.

The View menu is shown expanded from the menu bar, listing radio-button options for Normal (selected) and Page Break view modes at the top, followed by User Interface… and Toolbars (submenu). Below that are checkboxes for Formula Bar, Status Bar, View Headers, and View Grid Lines — all four checked — then Grid and Helplines (submenu). Further down are unchecked checkboxes for Value Highlighting, Column/Row Highlighting, Hidden Row/Column Indicator, and Show Formula, followed by a greyed-out Comments entry. The lower section shows unchecked checkboxes for Split Window, Freeze Rows and Columns, and Freeze Cells, then a checked Sidebar checkbox, with additional entries continuing below.

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

_Scope: Data > AutoFilter, More Filters (Standard/Advanced), Sort dialog, Group and Outline_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar, listing from top to bottom: Insert Cells…, Insert Rows (submenu), Insert Columns (submenu), Insert Page Break (submenu), then a divider followed by Delete Cells…, Delete Rows, Delete Columns, Delete Page Break. After another divider appear sheet-management entries: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, and Delete Sheet… (greyed out). Below another divider are Clear Cells…, Cycle Cell Reference Types, Fill Cells (submenu), Named Ranges and Expressions (submenu), Cell Comments (submenu), and Rename Sheet…, with additional entries continuing below the visible area.

The Data menu is shown expanded from the menu bar, listing from top to bottom: Sort… (with a submenu arrow), Sort Ascending, Sort Descending, then a divider followed by AutoFilter (with an unchecked checkbox icon) and More Filters (submenu). After a divider are Define Range…, Select Range…, and Refresh Range (greyed out). Below that are Pivot Table (submenu), Calculate (submenu), Validity…, Subtotals…, Form…, and Streams…, with additional entries continuing below the visible area.

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
