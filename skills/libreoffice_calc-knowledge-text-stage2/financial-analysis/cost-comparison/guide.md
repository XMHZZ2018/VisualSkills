# Cost Comparison & Best-Value Analysis (LibreOffice Calc 7.3.7)

When you're staring down a handful of competing quotes or subscription plans, a well-structured Calc spreadsheet turns the decision from gut-feel into something defensible. Start by laying out your options in columns — one column per vendor or plan — with rows for each cost component (base price, fees, taxes, etc.). Keep your raw numbers in their own cells rather than hard-coding sums; that way everything updates automatically when a quote changes.

To total each option, click the cell where you want the result and type a formula like `=SUM(B2:B10)`. You can reference cells across the sheet or even from other sheets using the syntax `=$Sheet2.B12+$Sheet3.B12`, which is handy if you keep each vendor's detailed breakdown on its own tab. For quick arithmetic — say, calculating a percentage markup — just use operators directly: `=B2*1.08` adds 8% tax, and `=B2-C2` shows you the price difference between two options.

Comparative operators are your best friend for flagging the winner. The `IF` function lets you tag results automatically: `=IF(B11<C11,"Plan B cheaper","Plan A cheaper")` drops a plain-English verdict right into your sheet. You can nest these or chain them with `MIN` to find the lowest total across several columns — something like `=MIN(B11,C11,D11)` instantly surfaces the cheapest option regardless of how many you're comparing.

Beyond totals, use `AVERAGE` to see the mean cost across options, `MAX` to spot the priciest outlier, and `RANK` to order every option from cheapest to most expensive without manually sorting. Named ranges (defined via **Sheet > Named Ranges and Expressions > Define**) make complex formulas readable — instead of `=SUM(B2:B10)`, you can write `=SUM(VendorA_Costs)`.

To make the best value pop visually, conditional formatting is a game-changer. Select your totals row and go to **Format > Conditional > Condition**. Set a condition like "Cell value is less than" and point it at your target threshold, then assign a green cell style. Add a second condition for values above the threshold with a red style. Now the cheapest option literally lights up green the moment you update any number.

Color scales offer an even quicker overview when you have many options. Select the full range of costs, then choose **Format > Conditional > Color Scale**. Calc paints a gradient from green (low) to red (high) across every cell, so you can scan dozens of line items at a glance without reading a single number.

You can manage all your conditional rules in one place via **Format > Conditional > Manage**, which lists every rule and the range it applies to. From there, **Edit** tweaks an existing rule and **Remove** deletes one outright — no hunting through menus. The Manage Conditional Formatting dialog presents a scrollable list area where each entry shows the conditional rule's description alongside the cell range it applies to. Below the list, "Add," "Edit," and "Remove" buttons let you create, modify, or delete rules directly, and a "Close" button at the bottom right dismisses the dialog.

If you want to share the comparison but keep the raw data tidy, hide helper columns (right-click the column header, then **Hide Columns**) so stakeholders see only the summary. The hidden data still feeds your formulas — nothing breaks. When you need it back, select the surrounding columns and choose **Show Columns** from the same context menu. With formulas doing the math and conditional formatting doing the storytelling, your cost comparison practically reads itself.

---

## UI Reference  —  Format Menu

_Scope: Conditional > Condition, Conditional > Color Scale, Conditional > Manage for best-value highlighting_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

The Format menu dropdown is organized into logical groups separated by thin dividers. At the top are text-level entries — Text (with a submenu arrow), Align Text, and Number Format — followed by Clone Formatting and Clear Direct Formatting. The middle section contains structural items: Cells… (Ctrl+1), Rows, Columns, and Merge and Unmerge Cells, each with submenu arrows. Below that sit Character…, Paragraph…, and Page Style…, then Print Ranges and the Conditional submenu (whose flyout lists Condition…, Color Scale…, Data Bar…, Icon Set…, Date…, and Manage…). The bottom portion holds AutoFormat Styles…, Spreadsheet Theme, Theme…, and a set of object-specific entries (Image, Chart, Sparklines, Text Box and Shape, Anchor, Arrange, Flip, Group, Name…, Alt Text…), most of which appear greyed out when no drawing object is selected.

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

_Scope: Sheet > Named Ranges for readable formula references_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu dropdown begins with cell and row/column insertion entries — Insert Cells… (Ctrl++), Insert Rows (with submenu arrows for Rows Above and Rows Below), Insert Columns (Columns Before and Columns After), and Insert Page Break — followed by their matching delete counterparts (Delete Cells…, Delete Rows, Delete Columns, Delete Page Break) and Clear Cells…. A divider separates these from Cycle Cell Reference Types (F4), then Fill Cells and Named Ranges and Expressions (each with submenu arrows), and Cell Comments. The lower portion of the menu lists sheet-management items: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet… (greyed out when only one sheet exists), Rename Sheet…, Hide Sheet, Show Sheet…, Move or Copy Sheet…, Duplicate Sheet, Navigate, Sheet Tab Color…, Sheet Events…, and Right-To-Left.

The Data menu dropdown lists sorting options at the top — Sort…, Sort Ascending, and Sort Descending — followed by AutoFilter (Shift+Ctrl+L) and a More Filters submenu. Below a divider are Define Range…, Select Range…, and Refresh Range. The middle section contains Pivot Table (with a submenu arrow) and Calculate (also with a submenu). Further down are Validity…, Subtotals…, Form…, Streams…, XML Source…, Multiple Operations…, and Text to Columns…. Near the bottom sit Consolidate…, Group and Outline (with a submenu for grouping, ungrouping, and outline controls), and finally a Statistics submenu that provides access to 13 statistical analysis tools.

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
