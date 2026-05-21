# Blood Donation Eligibility Tracking (LibreOffice Calc 7.3.7)

Tracking when donors become eligible again is really just date math — you log the last donation date, add the required waiting period, and let Calc tell you who's ready. Here's how to set it up cleanly.

Start by laying out your columns: donor name in A, donation type in B (whole blood, platelets, plasma, etc.), last donation date in C, waiting period in days in D, and next eligible date in E. When you type a date into column C, Calc recognizes common formats like `10/15/2024` or `2024-10-15` and converts it automatically. If Calc misreads your date, select the cell, open **Format > Cells**, go to the **Numbers** tab, pick **Date** from the *Category* list, and choose the format you want.

For column D, enter the waiting period in whole days — 56 for whole blood, 7 for platelets, 112 for double red cells, and so on. The formula in E is simply `=C2+D2`. Calc handles date arithmetic natively, so adding an integer to a date gives you a future date. To flag whether someone is eligible *right now*, add a column F with something like `=IF(TODAY()>=E2,"Eligible","Wait")`. Note that `TODAY()` is a volatile function — it recalculates every time you open the file or press *F9*, so your eligibility status stays current.

To keep data entry clean, use validation on the donation type column. Select the cells in column B, then go to **Data > Validity**. On the *Criteria* tab, set *Allow* to **List** and type your accepted donation types in the *Entries* field (e.g., Whole Blood, Platelets, Plasma, Double Red). Check **Show selection list** so users get a dropdown instead of free-typing.

The Validity dialog is shown open to the Criteria tab. The *Allow* dropdown is set to "Cell range" (which you would change to "List" for this use case), and below it are checkboxes for "Allow empty cells," "Show selection list," and "Sort entries ascending." A *Source* text field with a shrink button appears at the bottom, along with a note that a valid source must be a contiguous range or a formula resulting in an area or array. The dialog has three tabs — Criteria, Input Help, and Error Alert — and four buttons at the bottom: Help, Reset, OK, and Cancel.

You can also validate the date column to prevent nonsense entries. Select column C, open **Data > Validity** again, set *Allow* to **Date**, and configure the *Data* operator to reject future dates (e.g., "less than or equal to" with a value of `TODAY()`). Switch to the *Input Help* tab and add a short message like "Enter the date of the most recent donation" — it'll pop up whenever someone clicks into that cell.

The Validity dialog is shown open to the Input Help tab. At the top is a checked checkbox labeled "Show input help when cell is selected." Below that, a Contents section provides a *Title* text field and a larger *Input help* text area where you can type the tooltip message that will appear when a user selects the validated cell. The same three tabs (Criteria, Input Help, Error Alert) are visible at the top, and Help, Reset, OK, and Cancel buttons appear at the bottom.

On the *Error Alert* tab, set the *Action* to **Stop** if you want to hard-block bad entries, or **Warning** if you'd rather just nudge people. Either way, type a clear message explaining what went wrong so nobody's left guessing.

If you want to get fancier, use COUNTIF to summarize how many donors are currently eligible: `=COUNTIF(F2:F100,"Eligible")`. For lookups that pull waiting periods from a reference table instead of hardcoding them, VLOOKUP or HLOOKUP work well and support wildcards by default under **Tools > Options > LibreOffice Calc > Calculate**.

That's really all there is to it — dates in, simple addition for the next eligible date, TODAY() for live status checks, and validation to keep the data honest.

---

## UI Reference  —  Format Cells Dialog

_Scope: Numbers tab > Date category for consistent donation date display_

The Format Cells dialog (Ctrl+1 or Format > Cells…) is the central dialog for detailed cell formatting. It has 7 tabs covering number format, font, alignment, borders, background, and protection.

The Format Cells dialog is displayed with the Numbers tab active and selected. On the left is the Category list showing entries including All, User-defined, Number (currently highlighted in blue), Percent, Currency, Date, Time, Scientific, Fraction, and Boolean Value. On the right is the Format list previewing example formats such as General, -1235, -1234.57, -1,235, -1,234.57, (1,235), (1,234.57), "one hundred," and "One hundred." Above the dialog, the Alignment, Borders, Font, and Numbers tabs are visible. At the bottom, an Options section is partially visible with a "Decimal places" spinner and a "Negative" checkbox beginning to appear.

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

## UI Reference  —  Sheet and Data Menus

_Scope: Data > Validity for date and list validation on donation type and date columns_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is shown expanded from the menu bar. It lists items in order from top to bottom: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break, then a separator followed by Delete Cells…, Delete Rows, Delete Columns, Delete Page Break. After another separator: Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, and Delete Sheet… (greyed out). Then: Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, and Rename Sheet… with additional items continuing below the visible area.

The Data menu is shown expanded from the menu bar. It lists items from top to bottom: Sort…, Sort Ascending, Sort Descending, then a checkbox for AutoFilter, followed by More Filters. After a separator: Define Range…, Select Range…, Refresh Range (greyed out). Then: Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… continuing below the visible area.

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
