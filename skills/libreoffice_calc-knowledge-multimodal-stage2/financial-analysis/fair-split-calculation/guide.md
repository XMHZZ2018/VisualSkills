# Fair Split & Settlement Calculation (LibreOffice Calc 7.3.7)

Splitting a dinner bill, dividing rent, or settling shared expenses doesn't need to be messy — a quick Calc spreadsheet handles the math and keeps everyone honest. The key ingredients are basic arithmetic formulas, a couple of handy functions, and one important trick with absolute references.

Start by laying out your data clearly. Put participant names down column A and the amounts each person paid (or owes) in column B. In a separate cell — say D1 — enter the total shared cost. You could type it manually, but it's better to use `=SUM(B2:B10)` so the total updates automatically whenever you adjust an entry. For a simple equal split, just divide that total by the number of people using something like `=D1/COUNT(B2:B10)` in another cell. COUNT tallies how many entries exist, so you won't have to update the divisor when someone joins or drops out.

See `fig01.png`.

Now, say the split isn't equal — maybe it's proportional to income or usage. Put each person's weight or share percentage in column C. To calculate what each person owes, multiply the total cost by their proportion: `=D1*C2`. Here's where absolute references matter. If you write `=$D$1*C2` instead, you can drag that formula down the entire column and the D1 reference stays locked while C2 shifts to C3, C4, and so on. The `$` signs anchor the reference so it doesn't slide when you copy the formula — without them, Calc adjusts both references relative to the new cell, and you'll get wrong numbers.

See `fig02.png`.

To figure out who's owed money and who still needs to pay, subtract each person's actual contribution from their fair share. A formula like `=E2-B2` in column F gives a positive number if they underpaid and a negative one if they overpaid. You can use an IF function to make this friendlier: `=IF(F2>0,"Owes "&F2,"Gets back "&ABS(F2))` labels each person's status in plain language.

For a quick sanity check, use `=SUM(F2:F10)` at the bottom of the settlement column — it should be zero (or very close to it). If it's not, something's off in your data. You can also lean on ROUND to keep currency values tidy: wrap your division formulas with `=ROUND(D1/COUNT(B2:B10),2)` to pin results to two decimal places and avoid penny-rounding arguments.

Finally, format the money columns so they look right. Select the cells, go to **Format > Cells...**, pick the **Numbers** tab, and choose **Currency**. This doesn't change the underlying values — just makes everything easier to read at a glance. If you want to highlight who still owes money, a quick conditional trick with `=IF` or even just sorting by column F gets you there fast.

---

## UI Reference  —  Format Cells Dialog

_Scope: Numbers tab > Currency category for formatting money columns_

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

## UI Reference  —  Formatting Toolbar

_Scope: Format as Currency button for money columns_

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

