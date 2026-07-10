# Plant & Garden Care Tracking (LibreOffice Calc 7.3.7)

Keeping tabs on watering schedules, propagation attempts, and seed viability is the kind of repetitive-but-important work that Calc handles beautifully. Here's how to set up a tracker that actually makes your life easier.

Start by entering your plant names in column A and your care dates across the top row. When typing dates, Calc recognizes formats like 10 Oct 2020 or 2020-10-07 and automatically converts them to the date format your locale expects. If Calc isn't picking up your preferred pattern, check **Tools > Options > Language Settings > Languages > Formats > Date acceptance patterns** to see which formats are recognized.

For watering schedules, you'll want a sequence of dates down a column. Type the first date, select the cell, then drag the small fill handle at the bottom-right corner of the cell downward — Calc will auto-generate a date series. For more control, select your range and go to **Sheet > Fill Cells > Fill Series**. In the Fill Series dialog, choose *Date* as the Series Type, pick your Time Unit (Day, Weekday, or Month), and set the increment to match your watering interval — say, every 3 days.

The Fill Series dialog is divided into three groups of radio buttons across the top: Direction (Down, Right, Up, Left), Series Type (Linear, Growth, Date, AutoFill), and Time Unit (Day, Weekday, Month, Year). Below these are three text fields — Start value, End value, and Increment — where you enter the numeric parameters for the series. The dialog's bottom row has Help, OK, and Cancel buttons, with OK highlighted by a blue border.

To track propagation success rates, you might keep columns for "Cuttings Taken" and "Cuttings Rooted," then calculate the rate with a simple formula. Functions like COUNTIF are handy here — for instance, `=COUNTIF(C2:C50,"rooted")` counts how many entries say "rooted." If you enable wildcards under **Tools > Options > LibreOffice Calc > Calculate**, you can use patterns like `=COUNTIF(C2:C50,"root*")` to match "rooted," "rooting," and so on.

The Options dialog is open to the "LibreOffice Calc > Calculate" page, shown by the highlighted "Calculate" entry in the left-hand navigation tree (which also lists General, Defaults, View, Formula, Sort Lists, Changes, Compatibility, Grid, and Print under LibreOffice Calc). The right-hand pane contains several sections: "Formulas Wildcards" with three radio buttons — "Enable wildcards in formulas" (selected), "Enable regular expressions in formulas," and "No wildcards or regular expressions in formulas"; a "Date" group with base-date options; "General Calculations" with checkboxes for Case sensitive, Precision as shown, Search criteria options, and others; "Iterative References" with an Iterations checkbox and Steps/Minimum change fields; and "CPU Threading Settings" with an "Enable multi-threaded calculation" checkbox. The bottom of the dialog has Help, Reset, Apply, OK, and Cancel buttons.

For seed viability tracking, you'll want consistent data entry — no one typing "Yes" when someone else types "viable." Open **Data > Validity** on any input cell, set the *Allow* dropdown to *List*, and enter your accepted values (e.g., Viable, Expired, Unknown). Check **Show selection list** so a dropdown arrow appears on the cell, and anyone entering data just picks from the list. You can even flip to the *Input Help* tab to add a tooltip like "Select seed status" that appears when the cell is selected.

The Validity dialog is shown on its Criteria tab, with two additional tabs — Input Help and Error Alert — visible along the top. The "Allow" dropdown is set to "Cell range" (highlighted in blue), and below it are two checked checkboxes: "Allow empty cells" and "Show selection list," with an unchecked "Sort entries ascending" checkbox nested beneath the latter. A "Source" text field with a shrink/expand button sits below, accompanied by a note explaining that a valid source must be a contiguous selection of rows and columns or a formula resulting in an area or array. The bottom of the dialog provides Help, Reset, OK (blue-bordered), and Cancel buttons.

If you find yourself retyping the same plant categories or care actions, create a custom sort list. Head to **Tools > Options > LibreOffice Calc > Sort Lists**, click **New**, and type your entries one per line — things like "Succulent, Tropical, Herb, Fern." Once saved, Calc's AutoFill will recognize and extend your custom sequence when you drag the fill handle, just like it does with days of the week.

Finally, a small quality-of-life tip: for long plant notes or care instructions, press *Ctrl+Enter* inside a cell to start a new paragraph, or click the **Expand / Collapse Formula Bar** icon to give yourself a multi-line input area. It keeps your notes readable without widening every column.

---

## UI Reference  —  Formula Bar

_Scope: Expand/Collapse Formula Bar for multi-line plant care notes_

The Formula bar sits below the Formatting toolbar and provides cell navigation, function insertion, and formula editing.

The Formula Bar is a narrow horizontal strip showing, from left to right: the Name Box displaying "A1" with a text cursor and a dropdown arrow (▼), followed by the Function Wizard button (fx), the Select Function button (Σ with a small dropdown arrow), the Formula button (=), and a wide empty Input Line stretching to the right edge of the bar.

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

## UI Reference  —  Sheet and Data Menus

_Scope: Sheet > Fill Cells > Fill Series for watering date sequences, Data > Validity for seed status list_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

The Sheet menu is expanded from the menu bar, showing a vertical list of items in order: Insert Cells…, Insert Rows, Insert Columns, Insert Page Break, then a separator, followed by Delete Cells…, Delete Rows, Delete Columns, Delete Page Break, another separator, then Insert Sheet…, Insert Sheet at End…, Insert Sheet from File…, External Links…, Delete Sheet… (greyed out), then another separator with Clear Cells…, Cycle Cell Reference Types, Fill Cells, Named Ranges and Expressions, Cell Comments, Rename Sheet…, and the list continues below the visible area toward Hide Sheet.

The Data menu is expanded from the menu bar, displaying items from top to bottom: Sort…, Sort Ascending, Sort Descending, then a checkbox for AutoFilter, followed by More Filters, a separator, Define Range…, Select Range…, Refresh Range (greyed out), then a separator, Pivot Table, Calculate, Validity…, Subtotals…, Form…, and Streams… at the bottom of the visible portion.

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

---

## UI Reference  —  Tools, Window, and Help Menus

_Scope: Tools > Options > Calc > Calculate for wildcards; Tools > Options > Sort Lists_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu is expanded from the menu bar, listing items from top to bottom: Spelling…, Automatic Spell Checking (shown with a checked checkbox), Thesaurus… (greyed out), Language, AutoCorrect Options…, AutoInput (shown with a checked checkbox), ImageMap (greyed out), Redact, Auto-Redact, then a separator, Goal Seek…, Solver…, Detective, Scenarios… (greyed out), then another separator, Forms, Share Spreadsheet…, Protect Sheet… (with an unchecked checkbox), and Protect Spreadsheet Structure… partially visible at the bottom.

## Tools Menu Elements

- **Spelling…** (F7) — spell-check dialog
- **Automatic Spell Checking** (Shift+F7) — toggle, enabled by default
- **Thesaurus…** (Ctrl+F7)
- **Language** — submenu for language settings
- **AutoCorrect Options…**
- **AutoInput** — toggle auto-completion from existing column values (on by default)
- **ImageMap** (greyed), **Redact**, **Auto-Redact**
- **Goal Seek…** — set a formula cell to a target by changing an input cell
- **Solver…** — optimisation with multiple constraints
- **Detective** — formula auditing submenu: Trace Precedents (Shift+F9), Trace Dependents (Shift+F5), Remove All/Precedents/Dependents Traces, Trace Error, Refresh Traces, Fill Mode (toggle), AutoRefresh (toggle, on), Mark Invalid Data
- **Scenarios…** (greyed)
- **Forms** — submenu: Design Mode, Control Wizards, Control/Form Properties, Form Navigator, Activation Order, Add Field, Open in Design Mode, Automatic Control Focus
- **Share Spreadsheet…**
- **Protect Sheet…** — password-protect the active sheet
- **Protect Spreadsheet Structure…** — prevent sheet add/delete/rename
- **Macros** — submenu: Run Macro…, Edit Macros…, Organize Macros, Digital Signature…, Organize Dialogs…
- **Development Tools** (toggle)
- **XML Filter Settings…**
- **Extensions…** (Ctrl+Alt+E) — Extension Manager
- **Customize…** — customise menus, toolbars, keyboard, events
- **Options…** (Alt+F12) — global LibreOffice settings

## Window Menu

- **New Window** — opens a second view of the current document
- **Close Window** (Ctrl+W)
- Document list — radio-button list of open document windows; click to switch

## Help Menu

- **LibreOffice Help** (F1), **What's This?**, **User Guides**
- **Show Tip of the Day**
- **Search Commands** (Shift+Escape) — command search bar
- **Get Help Online**, **Send Feedback**, **Restart in Safe Mode…**
- **Get Involved**, **Donate to LibreOffice**, **License Information**
- **About LibreOffice** — version 24.2 Community
