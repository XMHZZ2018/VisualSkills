# Basic Formulas & Operations (LibreOffice Calc 7.3.7)

Every formula in Calc starts with an equals sign. Type `=` into a cell and you're telling Calc "this is a calculation, not plain text." If your formula happens to begin with `+` or `-` (like `-2*A1`), Calc adds the `=` for you automatically. You can type formulas directly into a cell or into the Input Line above the sheet.

The simplest formulas use arithmetic operators you already know: `+` for addition, `-` for subtraction, `*` for multiplication, `/` for division, and `^` for exponentiation. So `=A1*B1` multiplies two cells together, and `=A1^3` cubes the value in A1. Percentage works too — `=A1*16%` gives you 16% of whatever sits in A1.

Rather than typing raw numbers, you'll almost always want to reference cells. A formula like `=B3+B4` pulls live values from those cells, and the result updates whenever the source data changes. This is the whole point of a spreadsheet — change one number and everything downstream recalculates.

When you copy a formula, Calc adjusts its references relative to the new location. Copy `=B3+B4` one column to the right and it becomes `=C3+C4`. This is called relative referencing, and it's the default. If you need a reference to stay fixed — say, pointing at a single exchange rate in cell D1 — lock it with dollar signs: `=$D$1`. Mix and match as needed; `=D2*$D$1` lets the row shift but keeps the column and row of D1 anchored.

For summing a range of cells, reach for `=SUM(B1:B14)` instead of chaining plus signs. SUM accepts ranges (B1:B14), individual cells separated by commas, or even nested functions. PRODUCT does the same thing for multiplication, and QUOTIENT handles division. That said, for quick one-off math like `=A1+A2`, plain operators are perfectly readable — use whichever feels clearer.

Statistical functions pull useful information from lists without manual scanning. `=AVERAGE(B1:B10)` gives you the arithmetic mean. COUNT tells you how many entries exist in a range. MIN and MAX find the extremes. For more nuance, MEDIAN returns the middle value of a sorted set, MODE finds the most frequent entry, and RANK tells you where a particular value falls in the list.

Conditional logic lives in the IF function. The pattern is `=IF(test, value_if_true, value_if_false)`. For example, `=IF(C31>140, "HIGH", "OK")` checks whether C31 exceeds 140 and labels it accordingly. You can nest these — wrapping an AVERAGE inside an IF lets you give different feedback depending on a calculated score.

To concatenate text from multiple cells, use the `&` operator: `=B2 & " " & C2 & ", " & D2` stitches pieces together with spaces and punctuation. Calc also has a CONCATENATE function that does the same thing if you prefer a named approach.

When you need help building a formula, open the Function Wizard via **Insert > Function** (or press *Ctrl+F2*). It lists all 500+ available functions organized by category — Mathematical, Statistical, Date&Time, Logical, and more. Pick a function and you'll see a description plus input fields for each argument, along with a live preview of the result. See `fig01.png` for the Function Wizard dialog.

Alternatively, open the Functions deck in the Sidebar with **View > Function List**. It works like a quick-reference catalog — highlight any function to read its description at the bottom of the pane, then double-click to insert it into the current cell with placeholder arguments ready to fill in.

Rounding deserves a quick mention: `=ROUND(SUM(A1,A2))` sums two cells and rounds to the nearest whole number. You can nest the rounding around any calculation, or keep the raw result in one cell and round it in another for clarity. Calc supports several rounding variants — check the Help for ROUNDUP, ROUNDDOWN, and others.

One thing to watch for: volatile functions like `=RAND()` recalculate every time *any* cell in the spreadsheet changes, not just their own inputs. This is by design, but in large sheets it can slow things down. You can manually trigger recalculation with **Data > Calculate > Recalculate** or by pressing *F9*.

---

## UI Reference  —  Formula Bar

_Scope: Function Wizard (fx), Select Function (Sigma), Formula Button (=), Input Line for formula editing_

The Formula bar sits below the Formatting toolbar and provides cell navigation, function insertion, and formula editing.

Read the screenshot `ui-formula-bar.png` in this directory.

## Elements (left to right)

- **Name Box** — displays current cell reference (e.g. "A1"). Click to edit, type an address and press Enter to navigate. Dropdown (▼) lists defined named ranges and "Manage Names…". During formula entry, switches to a function-name selector.

- **Function Wizard** (fx button) — opens the Function Wizard dialog with:
  - Search field to filter functions by name
  - Category dropdown (All, plus 13 categories: Math, Statistical, Text, etc.)
  - Full alphabetical function list (ABS, ACCRINT, ACOS, ADDRESS, AGGREGATE, …)
  - Formula and Result preview panels
  - Array checkbox, Back/Next navigation, Help/Cancel/OK

- **Select Function** (Σ button) — main click inserts SUM. Dropdown (▼) shows 11 common functions: Sum, Average, Min, Max, Count, CountA, Product, Stdev, StdevP, Var, VarP

- **Formula Button** (= button) — activates formula entry mode:
  - Inserts "=" in the active cell
  - Name Box changes to function-name selector (shows "SUM")
  - Σ button is replaced by **Cancel** (×, red) and **Accept** (✓, green)
  - Press Escape to cancel, Enter to accept

- **Input Line** — wide text area showing raw cell content (formula or value). Click to enter edit mode. Supports multi-line expansion.

- **Expand/Collapse Formula Bar** (▼/▲ chevron, far right) — toggles the input line between single-line and multi-line height for editing long formulas

---

## UI Reference  —  Insert Menu

_Scope: Function (Ctrl+F2) for opening Function Wizard_

The Insert menu adds objects, media, functions, and content into the spreadsheet. Structural operations (cells, rows, columns, page breaks) are in the Sheet menu, not here.

Read the screenshot `ui-insert-menu-expanded.png` in this directory.

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

