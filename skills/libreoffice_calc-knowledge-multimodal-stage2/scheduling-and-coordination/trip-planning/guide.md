# Trip & Route Planning (LibreOffice Calc 7.3.7)

A spreadsheet is a natural fit for planning road trips or hikes — you've got columns of waypoints, distances, fuel stops, and elevation gains just waiting to be crunched. Start by laying out your itinerary with columns for each leg's location name, distance (km or mi), estimated speed, fuel consumption rate, and elevation. Put your raw data in individual cells so every formula works by reference rather than hard-coded numbers — if plans change (and they always do), one edit ripples through automatically.

For distance and time, simple arithmetic operators do the heavy lifting. To get drive time for a leg, divide the distance cell by average speed: something like `=B3/C3`. Multiply by 60 if you want the result in minutes instead of hours. You can total the full trip distance with `=SUM(B2:B15)` and get overall drive time the same way. If fuel economy matters, calculate litres or gallons per leg with `=B3/D3` (distance divided by your vehicle's km-per-litre rating), then `=SUM` that column for the total fuel needed.

See `fig01.png`.

Comparative operators come in handy for flagging trouble spots. Wrap your elevation or distance values in an IF formula — for example, `=IF(C31>140, "HIGH", "OK")` — to automatically warn you when a hiking segment exceeds a comfortable threshold. You can use the same pattern to flag legs where estimated drive time is unreasonably long or fuel stops are too far apart.

For series of waypoint numbers or date-based itineraries, the Fill tool saves a lot of typing. Enter your first date or waypoint number, select the range you want to fill, then head to **Sheet > Fill Cells > Fill Series**. In the Fill Series dialog, pick *Date* as the series type and set the increment to 1 day (or whatever interval your trip uses). For a linear sequence of waypoint IDs, choose *Linear* and set your start value and increment. You can also just grab the small selection handle at the bottom-right corner of a cell and drag — Calc will auto-detect the pattern.

See `fig02.png`.

If you're reusing a set of route names or campsite labels across multiple trips, define a custom fill series. Go to **Tools > Options > LibreOffice Calc > Sort Lists**, click **New**, type each entry on its own line, then hit **Add**. Now you can type the first entry in a cell and drag to auto-fill the rest of your custom list — great for a recurring loop of trailheads or a fixed rotation of driver names.

See `fig03.png`.

For statistics across your route, use `=MAX(E2:E20)` and `=MIN(E2:E20)` to find your highest and lowest elevation points, `=AVERAGE(B2:B20)` for average leg distance, and `=COUNT(B2:B20)` to confirm you haven't missed any entries. Named ranges can make these formulas much more readable — define one via **Sheet > Named Ranges and Expressions > Define**, call it something like *ElevationData*, and your formulas become `=MAX(ElevationData)` instead of cryptic cell addresses.

If you want a running total column — cumulative distance as you progress through each waypoint — put `=B2` in the first row and `=F2+B3` in the next, then fill down. At a glance you'll see exactly how far along you are at any point in the trip, which is invaluable for planning rest stops and overnight stays.

---

## UI Reference  —  Sheet and Data Menus

_Scope: Sheet > Fill Cells > Fill Series for date itineraries, Sheet > Named Ranges for route data_

The Sheet menu manages sheet-level and cell/row/column structural operations. The Data menu handles sorting, filtering, pivot tables, grouping, statistical analysis, and data validation.

## Screenshots

(see screenshot `ui-sheet-menu-expanded.png`)

(see screenshot `ui-data-menu-expanded.png`)

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

_Scope: Tools > Options > LibreOffice Calc > Sort Lists for custom fill series_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

Read the screenshot `ui-tools-menu-expanded.png` in this directory.

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

