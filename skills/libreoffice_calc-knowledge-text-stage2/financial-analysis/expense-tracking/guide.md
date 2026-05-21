# Expense Tracking & Budget Variance (LibreOffice Calc 7.3.7)

Managing expenses in Calc starts with a solid layout. Set up columns for date, category, description, budgeted amount, actual amount, and variance. Keep each transaction on its own row — this flat structure makes formulas and charting much easier down the road.

For totaling spend by category, `=SUM()` is your workhorse, but don't overlook `=SUMIF()` when you need to pull totals for just one category out of a mixed list. You can also use simple arithmetic operators directly — typing `=B2-C2` for a variance column is perfectly readable and often preferable to nesting functions. As the guide notes, writing `=A1*(A2+A3)` is briefer and easier to read than `=PRODUCT(A1,SUM(A2:A3))`, so lean on operators for straightforward expense math.

To figure out cost-per-use, just divide total spend by usage count: `=B2/C2`. If there's any chance the divisor could be zero, wrap it in `=IF(C2=0,"N/A",B2/C2)` so you don't litter the sheet with `#DIV/0!` errors. For rounding dollar amounts, `=ROUND(SUM(B2:B10),2)` keeps things tidy on invoices and reports. You can nest the rounding around any calculation, or keep the raw number in one cell and round it in another for auditing purposes.

Reconciling receipts against a budget is where statistics functions shine. Use `=COUNT()` to verify you have the right number of entries, `=MIN()` and `=MAX()` to spot outliers, and `=AVERAGE()` to sanity-check your typical spend. If you want the middle-of-the-road figure instead, `=MEDIAN()` ignores extreme outliers better than a simple average.

Conditional formatting is the fastest way to flag budget overruns visually. Select your variance column, then go to **Format > Conditional > Condition**. Set a rule like "Cell value is less than 0" and assign a red cell style — now every overspend jumps off the screen. You can layer on a **Color Scale** (choose **All Cells** in the condition type) to shade cells from green to red across the whole range, giving you an instant heat map of where money is going. To manage all your rules later, open **Format > Conditional > Manage** and edit or remove them from one place.

Once your data is clean, visualize the variance with a chart. Click anywhere in your expense table and go to **Insert > Chart**. The Chart Wizard opens — pick a **Column** chart to compare budgeted vs. actual side by side. On the Data Range page, confirm that your series are in columns and that the first row is used as a label. On the Data Series page, make sure both "Budget" and "Actual" appear as separate series so they render as paired bars.

The Chart Wizard dialog is shown on Step 1 ("Chart Type"), with a left-hand sidebar listing all four steps: Chart Type, Data Range, Data Series, and Chart Elements. The main area is titled "Choose a Chart Type" and presents a vertical list of chart types — Column (currently highlighted in blue), Bar, Pie, Area, Line, XY (Scatter), Bubble, Net, Stock, and Column and Line. To the right, three thumbnail previews show column chart variants (Normal is selected, along with stacked and percentage-stacked options). Below the previews, a "3D Look" checkbox and a "Realistic" dropdown are available, and a "Shape" list offers Bar, Cylinder, Cone, and Pyramid options. Navigation buttons at the bottom include Help, < Back, Next >, Finish (highlighted in blue), and Cancel.

Give the chart a clear title on the Chart Elements page — something like "Q2 Budget vs. Actual" — and add axis labels so the numbers speak for themselves. If the chart's data lives in the same document, any receipt you add or correct will automatically update the chart, keeping your visual always in sync with the raw numbers.

For ongoing tracking, consider linking to external data sources (CSV exports from your bank, for instance) via **Insert > Chart** data linking options, so the chart refreshes whenever the source file changes. That way, reconciliation becomes a matter of reviewing the visual rather than hunting through rows.

---

## UI Reference  —  Format Menu

_Scope: Conditional > Condition for budget overruns, Conditional > Color Scale heat map, Conditional > Manage_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

The Format menu is shown expanded as a dropdown from the menu bar (which also displays Insert, Styles, and Sheet). The menu items listed from top to bottom are: Text, Align Text, Number Format, Clone Formatting, Clear Direct Formatting, Cells…, Rows, Columns, Merge and Unmerge C… (truncated), Character… (greyed out), Paragraph… (greyed out), Page Style…, Print Ranges, Conditional, AutoFormat Styles… (greyed out), Spreadsheet Theme, Theme…, Image, and Chart. The menu appears against a spreadsheet background with partial cell content visible behind it.

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

## UI Reference  —  Formatting Toolbar

_Scope: Conditional Formatting dropdown for quick access to budget variance rules_

The Formatting toolbar is the second icon row, providing direct cell styling controls for font, alignment, number format, merge, borders, and conditional formatting.

The Formatting toolbar is displayed as a single horizontal strip beneath the menu bar. On the far left, a Font Name dropdown shows "Liberation Sans" highlighted in blue, followed by a Font Size dropdown set to "10 pt". Next are Bold (B), Italic (I), and Underline (U) icon buttons. Following those are a Font Color button (shown as an "A" with a colored underline) and a Background Color button (paint bucket icon). The middle section contains horizontal alignment buttons (Align Left, Align Center, Align Right) and vertical alignment buttons (Align Top, Center Vertically, Align Bottom). Further right are Merge Cells buttons, then number format icons including Percent (%) and decimal place controls (0.0). The toolbar ends with additional formatting icons on the far right.

## Elements (left to right)

### Font Controls
- **Font Name** dropdown — scrollable list of installed fonts, rendered in their own typeface; typing filters the list
- **Font Size** dropdown — common sizes; also accepts typed values
- **Bold** (Ctrl+B), **Italic** (Ctrl+I) — toggles
- **Underline** (Ctrl+U) — split-button; dropdown palette: (Without), Single, Double, Fine Dotting, Bold Dotting, Fine/Bold Dashing, Dash-dot, Dash-dot-dot, Wavy, More Options…

### Color Controls
- **Font Color** — split-button; dropdown opens ~120-swatch colour picker with Automatic, Recent, and Custom Color… options
- **Background Color** — split-button; dropdown opens colour picker with No Fill, Recent, and Custom Color…

### Alignment
- **Align Left** (Ctrl+L), **Align Center** (Ctrl+E), **Align Right** (Ctrl+R) — horizontal
- **Align Top**, **Center Vertically**, **Align Bottom** — vertical
- **Wrap Text** — toggle; auto-expands row height

### Merge
- **Merge and Center** — toggle (merges + centers / unmerges)
- **Merge Cells** — merges without centering

### Number Format
- **Format as Currency** (Shift+Ctrl+4)
- **Format as Percent** (Shift+Ctrl+5)
- **Format as Number** (Shift+Ctrl+1)
- **Format as Date** (Shift+Ctrl+3)
- **Add Decimal Place**, **Delete Decimal Place**

### Indent & Borders
- **Increase Indent**, **Decrease Indent**
- **Borders** — split-button; dropdown shows 18-preset border palette (no borders, box, thick box, inner lines, diagonal, etc.)
- **Border Style** dropdown — line style options (thin, thick, dashed, etc.)
- **Border Color** — split-button with colour picker

### Conditional
- **Conditional Formatting** dropdown — Condition…, Color Scale…, Data Bar…, Icon Set…, Date…, Manage…

---

## UI Reference  —  Insert Menu

_Scope: Chart for budget vs actual column chart creation_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

The Insert menu is shown expanded as a dropdown from the menu bar (with View, Format, Styles, and Sheet also visible). The menu items listed from top to bottom are: Image…, Chart…, Sparkline…, Pivot Table…, Media, OLE Object, Shape, Function…, Named Range or Expression…, Text Box (with a checkbox), Comment, Fontwork…, Hyperlink…, Special Character…, and Formatting Mark. The menu appears over a spreadsheet background where partial cell content including "re runn" and a blue-highlighted cell labeled "A" are visible behind the dropdown.

## Elements

- **Image…** — file browser to insert an image
- **Chart…** — inserts a chart object from selected data
- **Sparkline…** — inserts a mini-chart within a cell
- **Pivot Table…** — inserts or edits a pivot table
- **Media** — submenu: Gallery, Scan (Select Source, Request), Audio or Video…
- **OLE Object** — submenu: Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** — submenu with 7 categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart
- **Function…** (Ctrl+F2) — opens Function Wizard dialog with search, category filter, and full function library
- **Named Range or Expression…** — opens Paste Names dialog showing defined named ranges
- **Text Box** — checkbox toggle to insert a text box
- **Comment** (Ctrl+Alt+C) — inserts a cell comment
- **Fontwork…** — decorative text effects
- **Hyperlink…** (Ctrl+K) — opens Hyperlink dialog (4 tabs: Internet, Mail, Document, New Document)
- **Special Character…** — Unicode character picker
- **Formatting Mark** — submenu: No-break Space, Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner (all greyed in normal cell mode)
- **Date** (Ctrl+;), **Time** (Shift+Ctrl+;) — insert current date/time
- **Field** — submenu: Date, Sheet Name, Document Title
- **Headers and Footers…** — opens headers/footers editor dialog
- **Form Control** — submenu with 21 form controls: Label, Text Box, Check Box, Option Button, List Box, Combo Box, Push Button, Image Button, Formatted Field, Date/Time/Numerical/Currency/Pattern Field, Group Box, Image Control, File Selection, Table Control, Navigation Bar, Spin Button, Scrollbar
- **Signature Line…**
