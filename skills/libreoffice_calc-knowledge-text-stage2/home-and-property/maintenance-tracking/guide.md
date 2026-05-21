# Maintenance & Service Tracking (LibreOffice Calc 7.3.7)

A maintenance tracker lives or dies by clean data entry and clear visual warnings. Here's how to set one up in Calc that handles service intervals, cumulative mileage, and overdue flags for vehicles, bikes, pools, or any asset you need to keep running.

Start by laying out your columns: asset name, last service date, service interval (in days or miles), current mileage or reading, and a calculated "next due" column. For dates, just click a cell and type the date using slashes or hyphens — something like 10/03/2024 or 2024-10-03. Calc auto-detects date formats based on your locale. If it's not behaving, check **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns** to see which patterns your locale recognizes.

For the mileage and interval columns, keep things numeric so formulas work cleanly. If someone might accidentally type text into a mileage cell, lock it down with validation: select the cell range, open **Data > Validity**, and on the *Criteria* tab set **Allow** to *Whole Numbers* with a minimum of 0. You can also tick **Show selection list** if you want to restrict entries to a predefined set of service types (like "Oil Change", "Filter", "Inspection") by choosing *List* from the **Allow** dropdown and entering your values.

The Validity dialog is shown with the Criteria tab selected. At the top is an **Allow** dropdown (currently set to "Cell range"), followed by checkboxes for "Allow empty cells" (checked) and "Show selection list" (checked), with a nested unchecked "Sort entries ascending" option. Below is a **Source** field with a cell-range picker button beside it, and a note explaining that a valid source must be a contiguous selection of rows and columns or a formula resulting in an area or array. The dialog has three tabs across the top — Criteria, Input Help, and Error Alert — and four buttons along the bottom: Help, Reset, OK (highlighted in blue), and Cancel.

The *Input Help* tab is handy for guiding whoever fills in the sheet — enable **Show input help when cell is selected**, give it a title like "Mileage Entry", and add a short note such as "Enter current odometer reading." On the *Error Alert* tab, set the **Action** to *Stop* if you want to hard-block bad data, or *Warning* if you'd rather just nudge the user. Either way, fill in a clear error message so people know what went wrong.

The Validity dialog is shown with the Input Help tab selected. At the top of the tab is a checkbox labeled "Show input help when cell is selected" (checked). Below that is a **Contents** section containing two fields: a single-line **Title** text field and a larger multi-line **Input help** text area where you can type the guidance message that will appear as a tooltip when the cell is selected. The bottom of the dialog has Help, Reset, OK (blue-highlighted), and Cancel buttons.

Now for the real power: conditional formatting to flag overdue maintenance at a glance. Select your "next due" column and go to **Format > Conditional > Condition**. Set it so that when a cell value is less than today's date, it applies a red-background style — overdue items will scream for attention. You can add a second condition for "due within 7 days" using a yellow style, giving you an early warning band. Click **Add** in the dialog to stack multiple conditions, then hit **OK**.

The Conditional Formatting dialog is shown, titled "Conditional Formatting for A1:F8." Under a **Conditions** heading is a "Condition 1" block with three dropdowns in a row: the first set to "Cell value," the second to "is equal to," and a third empty value field. Below that is an **Apply Style** dropdown set to "Accent" with a "Lorem ipsum" preview showing the style appearance to its right. An **Enter a value** label sits above a large empty text area for formula or value input. Below the condition block are four buttons: Add, Delete, Up (greyed out), and Down (greyed out). At the bottom, a **Cell Range** section shows a **Range** field containing "A1:F8" with a cell-range picker button, followed by Help, OK (blue-highlighted), and Cancel buttons.

For a more visual approach, try **Format > Conditional > Color Scale** on a "days until due" column. A three-color scale running from red (min) through yellow (midpoint) to green (max) gives you an instant heat map of your maintenance urgency across every asset. Icon sets work well too — pick **3 Arrows** under **Format > Conditional > Icon Set** so each row gets an up, sideways, or down arrow based on how close the next service is.

To review or clean up all your conditional rules later, open **Format > Conditional > Manage**. The Manage Conditional Formatting dialog lists every rule by cell range and condition, and you can **Edit** or **Remove** them from there.

One last trick: turn on **View > Value Highlighting** (or press *Ctrl+F8*) while building the sheet. Dates and numbers show in blue, text in black, and formulas in green — it's an easy way to spot a mileage cell that accidentally got text typed into it before your validation rules catch it.

---

## UI Reference  —  Edit and View Menus

_Scope: View > Value Highlighting (Ctrl+F8) to spot text in numeric cells_

The Edit menu handles clipboard operations, find/replace, selection modes, track changes, and cell editing controls. The View menu manages display modes, UI element visibility, freeze/split panes, sidebar panels, and zoom.

## Screenshots

The Edit menu is shown expanded from the menu bar. Visible items from top to bottom are: Undo, Redo, and Repeat (all greyed out); a separator; Cut, Copy, and Paste (greyed out); Paste Special (with a submenu arrow); a separator; Select All (with the shortcut "Shi…" partially visible); Select (with a submenu arrow); a separator; Find… and Find and Replace… (with a checkbox icon); and Track Changes at the bottom, also with a submenu arrow. The menu bar behind it shows File, Edit (selected/highlighted), View, Insert, Format, and partial other entries.

The View menu is shown expanded from the menu bar. At the top are two radio-button options: Normal (selected) and Page Break. Below a separator are User Interface… and Toolbars (submenu arrow). Then four checked items with blue checkboxes: Formula Bar, Status Bar, View Headers, and View Grid Lines. Next is Grid and Helplines (submenu arrow). Below another separator are unchecked toggle items: Value Highlighting, Column/Row Highlighting, Hidden Row/Column Indicator, and Show Formula, followed by a greyed-out Comments entry. Further down are unchecked items: Split Window, Freeze Rows and Columns, and Freeze Cells. At the bottom, Sidebar is shown checked. The menu bar shows Edit, View (selected/highlighted), Insert, Format, Styles, and partial other entries.

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

_Scope: Conditional > Condition, Color Scale, Icon Set for overdue service flags, Conditional > Manage_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

The Format menu is shown expanded from the menu bar. From top to bottom the entries are: Text and Align Text (both with submenu arrows), Number Format (submenu arrow), a separator, Clone Formatting (with an unchecked checkbox), Clear Direct Formatting, a separator, Cells…, a separator, Rows, Columns, Merge and Unmerge C… (truncated, with submenu arrow), a separator, Character… and Paragraph… (both greyed out), a separator, Page Style…, Print Ranges (submenu arrow), Conditional (submenu arrow), AutoFormat Styles… (greyed out), Spreadsheet Theme, Theme…, a separator, Image, Chart, and the list continues below the visible area. The menu bar shows Insert, Format (selected/highlighted), Styles, and Sheet.

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

_Scope: Data > Validity for mileage and service-type input constraints_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar. From top to bottom the entries are: Insert Cells…, Insert Rows (submenu arrow), Insert Columns (submenu arrow), Insert Page Break (submenu arrow), a separator, Delete Cells…, Delete Rows, Delete Columns, Delete Page Break, a separator, Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet… (greyed out), a separator, Clear Cells…, Cycle Cell Reference Types (partially truncated), Fill Cells (submenu arrow), Named Ranges and Expres… (truncated, submenu arrow), Cell Comments (submenu arrow), a separator, and Rename Sheet… with further items continuing below the visible area. The menu bar shows Format, Styles, Sheet (selected/highlighted), Data, Tools, and Window.

The Data menu is shown expanded from the menu bar. From top to bottom the entries are: Sort… , Sort Ascending (partially truncated), Sort Descending (partially truncated), a separator, AutoFilter (with an unchecked checkbox), More Filters (submenu arrow), a separator, Define Range… (partially truncated), Select Range…, Refresh Range (greyed out), a separator, Pivot Table (submenu arrow), Calculate (submenu arrow), Validity…, Subtotals…, a separator, Form…, a separator, and Streams… continuing below. The menu bar shows Styles, Sheet, Data (selected/highlighted), Tools, and Wi… (truncated Window).

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
