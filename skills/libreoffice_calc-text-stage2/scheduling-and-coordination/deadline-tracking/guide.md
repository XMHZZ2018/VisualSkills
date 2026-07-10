# Deadline & Renewal Tracking (LibreOffice Calc 7.3.7)

The backbone of any deadline tracker is a simple "days remaining" calculation. Since Calc stores dates as serial numbers internally, you can just subtract today from a future date. Put your deadline in one column (say B2), then in the next column type `=B2-TODAY()`. That gives you the number of days left. The `TODAY()` function is volatile, meaning it recalculates every time you open the file or press *F9*, so your countdown stays current automatically.

To label urgency, wrap that days-remaining value in a nested `IF`. Something like `=IF(B2-TODAY()<0,"OVERDUE",IF(B2-TODAY()<=7,"URGENT",IF(B2-TODAY()<=30,"UPCOMING","OK")))` works nicely. This gives you a text-based priority column you can sort or filter on. You can enter dates using a slash or hyphen separator (e.g. 10/15/2024 or 2024-10-15) — Calc recognizes both and converts to your locale's format. If you need to verify accepted date patterns, check **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns**.

Now the real magic: making those deadlines visually jump off the screen with conditional formatting. Select the cells containing your days-remaining values, then go to **Format > Conditional > Condition**. Set up rules like "Cell value is less than 0" and assign a style with a red background, "Cell value is between 1 and 7" with orange, and so on. Hit **Add** to stack multiple conditions in the same dialog, and Calc evaluates them top to bottom. Make sure **Data > Calculate > AutoCalculate** is enabled or the formatting won't update live.

The spreadsheet shows a deadline-tracking table with columns for task name, deadline date, days remaining, and status. The days-remaining cells are highlighted using conditional formatting: cells with negative values (overdue items) appear with a red background, cells with values between 1 and 7 (urgent items) have an orange background, cells in the 8–30 range show a yellow background, and cells above 30 display a green background. The status column contains the corresponding text labels produced by the nested IF formula — OVERDUE, URGENT, UPCOMING, and OK.

For a quick heat-map effect without manually defining breakpoints, try **Format > Conditional > Color Scale**. Choose a three-color scale — red for low values (imminent deadlines), yellow in the middle, green for plenty of time — and Calc handles the gradient automatically across your range.

The Color Scale dialog is open, showing the three-color-scale configuration. It has three rows — Minimum, Midpoint, and Maximum — each with a drop-down for the type (e.g., Min, Percentile, Max) and a color selector. The colors are set to red for the minimum value, yellow for the midpoint, and green for the maximum value. A preview strip at the bottom of the dialog displays the resulting smooth gradient from red through yellow to green.

If you prefer icons over colors, go to **Format > Conditional > Icon Set** and pick something like "3 Arrows." Calc places a colored arrow icon right in the cell based on percentage thresholds you define — a red down-arrow for overdue, yellow sideways for soon, green up for safe. There's also a **Date** option under **Format > Conditional > Date** that lets you apply styles based on built-in ranges like *Tomorrow*, *Next week*, or *Last 7 days*, which is perfect for highlighting renewal windows without writing any formulas at all.

The Icon Set dialog is displayed, showing a "3 Arrows" icon set selected from the drop-down at the top. Below it, a conditions table lists three threshold rows, each with a colored arrow preview (green up-arrow, yellow right-arrow, red down-arrow), a comparison operator (e.g., >= with a percentage or value), and a threshold value field. The dialog also includes an "Icons Only" checkbox to hide the cell value and show just the arrow, along with OK, Cancel, and Help buttons at the bottom.

To review or clean up all your rules later, go to **Format > Conditional > Manage**. This opens a summary of every conditional format in the spreadsheet, showing the range and first condition for each. You can **Edit**, **Remove**, or **Add** new rules from this single dialog. If you want to create a custom look — say bold white text on a dark red cell — click **New Style** in the condition dialog to open the Cell Style editor, where you can define exactly the appearance you need and reuse it across multiple rules.

---

## UI Reference  —  Format Menu

_Scope: Conditional > Condition, Color Scale, Icon Set, Date, and Manage for deadline urgency formatting_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

The Format menu is fully expanded in the menu bar, showing a long vertical list of entries. Near the top are Text, Align Text, Number Format, Clone Formatting, and Clear Direct Formatting (Ctrl+M). The middle section includes Cells… (Ctrl+1), Rows, Columns, and Merge and Unmerge Cells submenus. Further down, the Conditional submenu is visible with its flyout listing Condition…, Color Scale…, Data Bar…, Icon Set…, Date…, and Manage…. The bottom portion contains entries for AutoFormat Styles…, Spreadsheet Theme, and object-specific options such as Image, Chart, Sparklines, Anchor, Arrange, Flip, and Group, many of which appear greyed out when no object is selected.

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

_Scope: Data > Calculate > AutoCalculate for live conditional formatting updates_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is fully expanded, displaying its entries in a single vertical drop-down. The top section contains cell and row/column operations: Insert Cells… (Ctrl++), Insert Rows (with a submenu arrow), Insert Columns, Insert Page Break, and their corresponding Delete counterparts. Below that are Clear Cells… (Backspace), Cycle Cell Reference Types (F4), and the Fill Cells submenu. The middle section lists Named Ranges and Expressions and Cell Comments submenus. The lower section covers sheet management entries: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet…, Rename Sheet…, Hide Sheet, Show Sheet…, Move or Copy Sheet…, Duplicate Sheet, Navigate, Sheet Tab Color…, Sheet Events…, and Right-To-Left.

The Data menu is fully expanded, showing its entries top to bottom. At the top are Sort…, Sort Ascending, and Sort Descending. Next are AutoFilter (Shift+Ctrl+L) and the More Filters submenu. The middle section includes Define Range…, Select Range…, Refresh Range, and the Pivot Table submenu. The Calculate submenu is visible with its flyout showing Recalculate (F9), Recalculate Hard (Shift+Ctrl+F9), Formula to Value, and AutoCalculate with a checkmark indicating it is currently enabled. Below Calculate are Validity…, Subtotals…, Form…, Streams…, XML Source…, Multiple Operations…, Text to Columns…, Consolidate…, the Group and Outline submenu, and finally the Statistics submenu at the bottom.

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
