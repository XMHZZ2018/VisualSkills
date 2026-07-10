# Formula Debugging & Auditing (LibreOffice Calc 7.3.7)

When a formula misbehaves, Calc gives you three main investigation tools: error messages, color coding for input, and the Detective. Knowing how to read and use each one will save you hours of guesswork.

Error codes show up directly in the cell and on the right side of the Status Bar. The most common ones are **#NAME?** (Err:525 — the function or named range doesn't exist, usually a typo), **#REF!** (Err:524 — a referenced column, row, or entire sheet has been deleted), and **#VALUE!** (Err:519 — an argument is the wrong type, like text where a number is expected). You'll also see **#DIV/0!** when something divides by zero or a blank cell. For a full list, search "error codes" in the Help or check Appendix B.

A quick fix for **#DIV/0!** is to wrap your formula in an IF check. For instance, `=IF(C3>0, B3/C3, "No Report")` gracefully handles zeros and blanks instead of showing an ugly error. The **#VALUE!** error often sneaks in when a cell that looks numeric actually contains text — someone typed "None" where a number belongs, and now your downstream formula breaks. The **#REF!** error typically appears after you delete a sheet or column that another formula pointed to; undo the deletion or manually fix the reference.

The spreadsheet shows a small table where column B contains numerator values and column C contains divisor values, with column D holding the result formula. Where C3 is zero or blank, a plain `=B3/C3` formula produces the #DIV/0! error, while the guarded version `=IF(C3>0, B3/C3, "No Report")` displays the text "No Report" instead, demonstrating how the IF wrapper prevents the error from appearing. The formula bar at the top shows the active cell's IF formula, and the contrast between the error cell and the gracefully handled cell is clearly visible.

When you click into a cell with a formula, Calc color-codes the referenced ranges right on the sheet — each argument gets its own colored outline (blue, magenta, green, dark blue, brown, purple, yellow, cycling through eight colors). This is the fastest way to visually confirm that a formula is pointing at the right data, especially for ranges that span multiple columns.

If color coding isn't enough — say you're dealing with a complex, multi-sheet workbook — turn to the Detective. Open **Tools > Detective** and pick the operation you need. **Trace Precedents** (also *Shift+F9*) draws lines with dots pointing back to every cell that feeds into your selected formula. **Trace Dependents** shows the reverse: which formulas rely on the current cell. These arrows make it straightforward to follow data flow across sheets and catch broken links or unexpected inputs. You can also use **Trace Error** to jump straight to the source of a problem, and **Remove All Traces** when you're done to clean up the arrows.

For spotting subtle type mismatches, enable **View > Value Highlighting** (or *Ctrl+F8*). This colors text in black and numbers in blue, so a "number" that's actually stored as text will immediately stand out. It's a lifesaver when SUM or AVERAGE silently ignores cells that look numeric but aren't.

When auditing formulas across sheets — like a Combined sheet that pulls from Branch1, Branch2, and Branch3 — keep in mind that references use the `Sheet.Cell` syntax (e.g., `=Branch1.K7+Branch2.K7+Branch3.K7`). If someone renames or deletes a sheet tab, every formula pointing at it will flip to **#REF!**. Use the Detective's trace precedents on your summary sheet to verify all cross-sheet links are intact. And remember: relative references shift when you copy formulas, so if a SUM range looks wrong after a paste, check whether you need absolute references (`$A$1`) to lock the range in place.

---

## UI Reference  —  Edit and View Menus

_Scope: View > Value Highlighting (Ctrl+F8) to colour-code text vs numbers vs formulas_

The Edit menu handles clipboard operations, find/replace, selection modes, track changes, and cell editing controls. The View menu manages display modes, UI element visibility, freeze/split panes, sidebar panels, and zoom.

## Screenshots

The Edit menu is shown fully expanded in the LibreOffice Calc menu bar, displaying a vertical list of commands organized into logical groups separated by dividers. At the top are Undo, Redo, and Repeat, followed by the clipboard operations (Cut, Copy, Paste, Paste Special with its flyout submenu arrow), then Select All and a Select submenu, Find and Find and Replace, the Track Changes submenu, and at the bottom Cell Edit Mode, Cell Protection, Links to External Files, and Edit Mode — each entry showing its keyboard shortcut on the right side where applicable.

The View menu is shown fully expanded, revealing its full list of entries from top to bottom: the Normal and Page Break radio-toggle view modes, User Interface, a Toolbars submenu, visibility checkboxes for Formula Bar, Status Bar, View Headers, and View Grid Lines (all checked by default), then Grid and Helplines, Value Highlighting (with its Ctrl+F8 shortcut), Column/Row Highlighting, Hidden Row/Column Indicator, Show Formula, Split Window, Freeze Rows and Columns, Freeze Cells, and the lower section with Sidebar, Styles, Gallery, Navigator, Function List, Data Sources, Full Screen, and the Zoom submenu.

## Edit Menu Elements

- **Undo** (Ctrl+Z), **Redo** (Ctrl+Y), **Repeat** (Shift+Ctrl+Y)
- **Cut** (Ctrl+X), **Copy** (Ctrl+C), **Paste** (Ctrl+V) — standard clipboard ops
- **Paste Special** — submenu: Paste Unformatted Text (Shift+Ctrl+Alt+V), Paste Only Text/Numbers/Formula, Paste Transposed, Paste Special… (Shift+Ctrl+V)
- **Select All** (Shift+Ctrl+Space)
- **Select** — submenu: Select All Sheets, Select Sheets…, Select to Next/Previous Sheet, Select Row (Shift+Space), Select Column (Ctrl+Space), Select Data Area (Ctrl+\*), Select Unprotected Cells, Select Visible Rows/Columns Only
- **Find…** (Ctrl+F) — opens the Find toolbar docked at the bottom
- **Find and Replace…** (Ctrl+H) — opens the Find and Replace dialog with match case, entire cells, all sheets, regex, wildcards, and direction options
- **Track Changes** — submenu: Record (toggle), Show, Manage, Comment, Protect, Compare Document, Merge Document
- **Cell Edit Mode** (F2) — enters inline cell editing
- **Cell Protection** — toggle (checked by default)
- **Links to External Files…** — manage external links (greyed when none exist)
- **Edit Mode** (Shift+Ctrl+M) — toggle for read-only documents

## View Menu Elements

- **Normal** / **Page Break** — radio toggle for view mode
- **User Interface…** — choose UI layout (Standard Toolbar, Tabbed, Groupedbar, etc.)
- **Toolbars** — submenu listing 20 available toolbars; Formatting and Standard enabled by default
- **Formula Bar** ✓, **Status Bar** ✓, **View Headers** ✓, **View Grid Lines** ✓ — visibility toggles (all on by default)
- **Grid and Helplines** — submenu: Display Grid, Snap to Grid, Helplines While Moving
- **Value Highlighting** (Ctrl+F8) — colours cells by data type (text=black, numbers=blue, formulas=green)
- **Column/Row Highlighting**, **Hidden Row/Column Indicator**, **Show Formula** (Ctrl+\`)
- **Split Window**, **Freeze Rows and Columns**, **Freeze Cells** (submenu: Freeze First Column/Row)
- **Sidebar** (Ctrl+F5), **Styles** (F11), **Gallery**, **Navigator** (F5), **Function List**, **Data Sources** (Shift+Ctrl+F4)
- **Full Screen** (Shift+Ctrl+J)
- **Zoom** — submenu: Entire Page, Page Width, Optimal View, 50%/75%/100%/150%/200%, Zoom…

---

## UI Reference  —  Tools, Window, and Help Menus

_Scope: Tools > Detective submenu: Trace Precedents, Trace Dependents, Trace Error, Remove All Traces_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The Tools menu is shown fully expanded in the menu bar, listing its entries from top to bottom: Spelling and Automatic Spell Checking at the top, then Thesaurus, Language, AutoCorrect Options, and AutoInput, followed by greyed-out ImageMap, Redact, and Auto-Redact entries. Below a divider appear Goal Seek and Solver, then the Detective submenu (which provides Trace Precedents, Trace Dependents, Remove All Traces and individual remove options, Trace Error, Refresh Traces, Fill Mode, AutoRefresh, and Mark Invalid Data). The lower portion of the menu shows Scenarios, Forms, Share Spreadsheet, Protect Sheet, Protect Spreadsheet Structure, the Macros submenu, Development Tools, XML Filter Settings, Extensions, Customize, and Options at the very bottom — each with its associated shortcut key displayed to the right.

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
