# Spreadsheet Formatting & Layout (LibreOffice Calc 7.3.7)

When you need a spreadsheet to look polished — whether for printing, sharing, or just your own sanity — Calc gives you a solid set of formatting and layout tools. Here's what matters most.

**Merging cells** is the quickest way to create clean headers that span multiple columns. Select the cells you want to combine, then go to **Format > Merge Cells > Merge and Center Cells**. If any of the selected cells already have data, a dialog pops up asking whether to move, keep, or empty the contents of the hidden cells. To undo a merge later, select the merged cell and use **Format > Merge Cells > Split Cells**. One word of caution: merged cells can break formula references, so use them for labels and titles rather than in the middle of calculated ranges.

See `fig01.png`.

For **text wrapping and alignment**, open the Format Cells dialog with *Ctrl+1* and head to the **Alignment** tab. Check **Wrap text automatically** under *Properties* to keep long text visible without widening the column. You can also tweak text orientation here by entering a rotation angle in the **Degrees** box, or tick **Shrink to fit cell size** if you'd rather the font scale down instead. Need a manual line break inside a cell? Press *Ctrl+Enter* while typing.

**Fonts and number formats** live on the Formatting toolbar — pick a font from the **Font Name** box, adjust the size, and hit the **Bold**, **Italic**, or **Underline** icons. For numbers, the toolbar offers quick icons for currency, percent, and decimal adjustments, but for full control use the *Numbers* tab in the Format Cells dialog where you can set custom format codes.

**Cell borders** bring structure to any table. Select your range, open **Format > Cells**, and switch to the **Borders** tab. Choose a preset line arrangement, set the style and color under *Line*, and adjust padding under *Padding*. For quick work, the **Borders** icon on the Formatting toolbar lets you apply common border layouts in one click — hold *Shift* while clicking to add to existing borders rather than replacing them.

See `fig02.png`.

**Background colors** are just as straightforward: on the *Background* tab of the Format Cells dialog, pick a color and click **OK**. Or use the **Background Color** icon on the toolbar for the fast route. If you want a consistent look across an entire table, try **Format > AutoFormat Styles** — select at least a 3-column-by-3-row range and Calc will offer preset themes covering fonts, borders, colors, and alignment all at once.

When it's time to **print**, hit *Ctrl+P* to open the Print dialog. The *General* tab lets you choose your printer, page range, orientation, and paper size. You can print multiple spreadsheet pages per sheet of paper using the **Pages per sheet** dropdown, and tick **Draw a border around each page** so they're easy to distinguish. On the *LibreOffice Calc* tab, enable **Suppress output of empty pages** to skip blanks.

See `fig03.png`.

To control exactly what prints, define a **print range** by selecting your data and going to **Format > Print Ranges > Define**. Edit it later through **Format > Print Ranges > Edit**, where you can also set rows or columns to repeat on every printed page — perfect for keeping headers visible across a long report. Before committing to paper, preview with **File > Print Preview** (*Ctrl+Shift+O*) to catch layout issues early.

For **headers and footers** on printed pages, open **Format > Page Style** and select the *Header* or *Footer* tab. Check **Header on** (or **Footer on**), set your margins and spacing, then click **Edit** to place page numbers, dates, sheet names, or custom text in the left, center, or right areas. Uncheck **Same content on left and right pages** if you want different headers for facing pages.

Finally, under the *Sheet* tab of the Page Style dialog, you'll find options to control **page order** (top-to-bottom or left-to-right), choose whether to print column/row headers, gridlines, comments, or formulas, and set a **scaling mode** — either a percentage, fit to a specific width/height, or fit to a total number of pages. These small tweaks make the difference between a printout that looks thrown together and one that looks intentional.

---

## UI Reference  —  File Menu

_Scope: File > Print (Ctrl+P), Print Preview (Ctrl+Shift+O) for print layout workflow_

The File menu provides document lifecycle operations: creating, opening, saving, exporting, printing, and managing document properties.

Read the screenshot `ui-file-menu-expanded.png` in this directory.

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

_Scope: Alignment tab (wrap text, orientation), Borders tab (line style, padding), Background tab (colour)_

The Format Cells dialog (Ctrl+1 or Format > Cells…) is the central dialog for detailed cell formatting. It has 7 tabs covering number format, font, alignment, borders, background, and protection.

Read the screenshot `ui-format-cells-dialog.png` in this directory.

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

## UI Reference  —  Format Menu

_Scope: Merge and Unmerge Cells, Page Style dialog, Print Ranges submenu, AutoFormat Styles, Cells (Ctrl+1)_

The Format menu controls cell appearance, row/column sizing, merge operations, conditional formatting, page style, and print ranges.

Read the screenshot `ui-format-menu-expanded.png` in this directory.

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

_Scope: Font Name/Size, Bold/Italic, Borders icon, Background Color, Merge and Center, alignment buttons_

The Formatting toolbar is the second icon row, providing direct cell styling controls for font, alignment, number format, merge, borders, and conditional formatting.

Read the screenshot `ui-formatting-toolbar.png` in this directory.

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

