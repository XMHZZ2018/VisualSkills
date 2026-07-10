# Billing, Invoicing & Pricing (LibreOffice Calc 7.3.7)

If you're building invoices or billing sheets from scratch, don't start with a blank file — Calc ships with ready-made templates. Head to **File > New > Templates** (or press *Ctrl+Shift+N*), filter by **Spreadsheets**, and browse the **Other Business Documents** category. You'll find a **Company Invoice** and an **Expense Claim** template waiting for you. Double-click one to open a fresh spreadsheet pre-loaded with the layout, and customize it from there.

The Templates dialog is shown with the Filter set to "Spreadsheets" and the category dropdown set to "Other Business Documents." Two template thumbnails appear in the main area: "Company Invoice" (currently selected, highlighted in blue) and "Expense Claim." Along the bottom of the dialog are Move, Export, Import, and Extensions buttons, with Help, Close, and Open buttons in the lower corners.

Once you've got your layout, the real work is in the formulas. Every billable amount starts with a simple cell reference: put your unit price in one cell, your quantity in another, and multiply them with something like `=B3*C3`. For subtotals across a column of line items, `=SUM(B3:B20)` does the job. If you need to apply a tax rate or discount percentage, `=A1*16%` calculates 16% of a cell's value directly. Rounding to the nearest cent is as easy as wrapping your formula in `=ROUND(B3*C3, 2)`.

For reconciling invoices against statements, the IF function is your best friend. A formula like `=IF(C31>140, "HIGH", "OK")` flags any line item exceeding a threshold — swap in your own values to highlight overcharges or discrepancies. You can compare invoice totals to expected amounts with the `<>` (inequality) operator: if two cells should match but don't, a simple `=A1<>B1` returns TRUE and tells you something's off.

When building pricing models, you'll want clean number formatting. Select your currency cells and use the dollar/currency icon on the Formatting toolbar, or open **Format > Cells** (*Ctrl+1*) and pick a currency format from the *Numbers* tab. You can control decimal places and leading zeroes here too — handy for keeping price lists consistent.

To catch errors before they reach a client, set up a cross-check row. Sum your line items independently across rows and columns, then compare the two totals. If they disagree, you'll spot it immediately. For deeper debugging, **Tools > Detective > Trace Error** will visually trace which cells are feeding a bad result.

A spreadsheet titled "Error Checking Demonstration" is shown with columns A, B, and C containing decimal values, a "Row Sums" column on the right summing each row, and a "Column Sums" row at the bottom summing each column. One of the Column Sums cells is in edit mode, displaying the formula `=SUM(B22:B29)` with a blue cell-range highlight around the referenced range. At the bottom, a TOTAL row shows 11.37 (circled in red) as the column-based total and 12.03 (also circled in red) as the row-based total, with a bold "ERROR!!!" label below indicating the two cross-check totals do not match.

If your billing spreadsheet is one you'll reuse monthly, save it as a template. Go to **File > Templates > Save as Template** (or press *Shift+F11*), give it a name like "Monthly Sales," pick a category, and hit **Save**. Every new invoice you create from that template will carry your logo, formulas, and formatting — no copy-pasting from last month's file. The link between template and spreadsheet is tracked under **File > Properties > General**, so you'll always know which template a given invoice came from.

For pricing analysis across larger datasets, lean on statistical functions: `=AVERAGE(B3:B50)` gives you a mean price, `=MEDIAN(B3:B50)` finds the midpoint, and `=MIN()` / `=MAX()` quickly surface your cheapest and most expensive line items. Use `=COUNT()` to confirm you haven't missed any entries, and `=QUARTILE()` if you want to segment pricing into tiers.

---

## UI Reference  —  File Menu

_Scope: File > New > Templates for invoice templates, Templates > Save as Template, Properties > General_

The File menu provides document lifecycle operations: creating, opening, saving, exporting, printing, and managing document properties.

The File menu is shown expanded in the menu bar. The "New" item is highlighted and its submenu is open to the right, listing document types: Text Document, Spreadsheet, Presentation, Drawing, Formula, Database, HTML Document, XML Form Document, Labels, Business Cards, Master Document, and Templates. Below "New" in the main File menu, entries are visible in order: Open (Ctrl+O), Open Remote, Recent Documents, Close, Wizards, Templates, Reload, Versions, Save (Ctrl+S), Save As (Shift+Ctrl+S), Save Remote, Save a Copy, Save All, Export, Export as PDF, and Send.

## Elements

- **New** (Ctrl+N) — submenu listing document types: Spreadsheet, Text Document, Presentation, Drawing, Formula, Database, HTML Document, XML Form Document, Labels, Business Cards, Master Document, Templates
- **Open…** (Ctrl+O) — file picker to open an existing document
- **Open Remote…** — connect to and open a file from a remote server
- **Recent Documents** — submenu of recently opened files
- **Close** — closes the current document
- **Wizards** — submenu: Letter, Fax, Agenda, Document Converter, Address Data Source
- **Templates** — submenu: Edit Template, Save as Template (Shift+F11), Manage Templates (Shift+Ctrl+N)
- **Reload** — reloads from disk (greyed on unsaved documents)
- **Versions…** — document version manager (greyed on unsaved documents)
- **Save** (Ctrl+S), **Save As…** (Shift+Ctrl+S), **Save Remote…**, **Save a Copy…**, **Save All**
- **Export…** — export in various formats via file picker
- **Export as PDF…** — opens the PDF Options dialog (see [export-pdf-dialog](export-pdf-dialog.md))
- **Send** — submenu: Email Document, Email as ODS/Excel/PDF, Send via Bluetooth
- **Preview in Web Browser** — exports to temporary HTML and opens in browser
- **Print Preview** (Shift+Ctrl+O) — toggles print preview mode
- **Print…** (Ctrl+P) — opens Print dialog (General + LibreOffice Calc tabs)
- **Printer Settings…** — printer selection and configuration
- **Properties…** — document metadata dialog (6 tabs: General, Description, Custom Properties, Security, Font, Statistics)
- **Digital Signatures** — submenu: Digital Signatures…, Sign Existing PDF…
- **Exit LibreOffice** (Ctrl+Q)

### Save As Format Options

The Save As dialog supports 16 file formats:
ODS, OTS, FODS, UOS, XLSX, XLTX, XLS, XLT, DIF, DBF, HTML, SLK, CSV, Office Open XML (.xlsx), XLSM.

---

## UI Reference  —  Format Cells Dialog

_Scope: Numbers tab > Currency for invoice line items and price formatting_

The Format Cells dialog (Ctrl+1 or Format > Cells…) is the central dialog for detailed cell formatting. It has 7 tabs covering number format, font, alignment, borders, background, and protection.

The Format Cells dialog is shown with the Numbers tab active (other visible tabs are Font, Alignment, and Borders). On the left is a Category list containing All, User-defined, Number (currently selected and highlighted in blue), Percent, Currency, Date, Time, Scientific, Fraction, and Boolean Value. On the right is a Format list showing preview examples such as General, -1235, -1234.57, -1,235, -1,234.57, (1,235), (1,234.57), "one hundred," and "One hundred." Below the lists is an Options section with a "Decimal places" spinner and a "Negative numbers red" checkbox partially visible.

## Tabs

### Numbers
- **Category** list: All, User-defined, Number, Percent, Currency, Date, Time, Scientific, Fraction, Boolean Value
- **Format** list showing preview examples (General, -1235, -1234.57, -1,235, etc.)
- **Language** dropdown (Default - English USA)
- **Preview** box showing the formatted sample
- **Options**: Decimal places spinner, Negative numbers red checkbox, Leading zeroes spinner, Thousands separator checkbox
- **Format Code** field with validate (✓), copy, and delete buttons

### Font
- **Family** field + scrollable font list
- **Style** dropdown: Regular, Italic, Bold, Bold Italic
- **Size** dropdown (default 10pt)
- **Language** dropdown
- **Features…** button for OpenType features
- Preview panel

### Font Effects
- Accessible from the Font Effects tab for underline style, colour, strikethrough, relief, etc.

### Alignment
- **Horizontal**: Default, Left, Center, Right, Justified, Filled, Distributed (with Indent spinner)
- **Vertical**: Default, Top, Middle, Bottom, Justified, Distributed
- **Text Orientation**: Vertically stacked checkbox, Degrees spinner, Reference edge buttons, rotation dial
- **Properties**: Wrap text automatically, Hyphenation active, Shrink to fit cell size
- **Text direction** dropdown

### Borders
- **Line Arrangement Presets**: 5 icons (no border, box, thick box, inner lines, diagonal)
- **User-defined** border editor (click edges to toggle)
- **Adjacent Cells**: Remove border checkbox
- **Line**: Style, Color (Black), Thickness (0.75pt) dropdowns
- **Padding**: Left/Right/Top/Bottom spinners (1.0pt), Synchronize checkbox
- **Shadow Style**: Position icons, Color (Gray), Distance (5pt)

### Background
- **None / Color** sub-buttons
- Palette dropdown, ~120-swatch colour grid
- Recent Colors, Custom Palette (Add/Delete), R/G/B spinners, Hex field, Pick button

### Cell Protection
- **Protection**: Hide all, Protected (checked by default), Hide formula
- **Print**: Hide when printing
- Note: protection only takes effect after Tools > Protect Sheet is enabled

---

## UI Reference  —  Formatting Toolbar

_Scope: Format as Currency button for invoice price columns_

The Formatting toolbar is the second icon row, providing direct cell styling controls for font, alignment, number format, merge, borders, and conditional formatting.

The Formatting toolbar is displayed as a single horizontal row of controls. From left to right it contains: a Font Name dropdown (showing "Liberation Sans"), a Font Size dropdown (showing "10 pt"), Bold/Italic/Underline toggle buttons, a Font Color split-button (with a colored underline indicator), a Background Color split-button, horizontal alignment buttons (Align Left, Center, Right), vertical alignment buttons (Top, Center Vertically, Bottom), a Wrap Text toggle, merge cell buttons, and number format buttons including Format as Currency, Format as Percent, and decimal place adjustment buttons. A Borders split-button appears at the far right.

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
