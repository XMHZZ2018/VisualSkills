# Loan & Mortgage Analysis (LibreOffice Calc 7.3.7)

Calc's Financial function category (63 functions strong) gives you everything you need to model loans, compare payoff strategies, and figure out when a refinance actually saves you money. The key is knowing which tools to reach for — and Calc has a few "what-if" analysis features beyond plain formulas that make mortgage math surprisingly painless.

Start with the basics: the `PMT` function calculates a fixed loan payment. Feed it the periodic interest rate, the number of periods, and the present value (loan amount), and it returns your monthly payment as a negative number (cash flowing out). For a $250,000 mortgage at 6% over 30 years, that's `=PMT(0.06/12, 360, 250000)`. If you're unsure about the arguments, open the Function Wizard with **Insert > Function** (or press *Ctrl+F2*), pick the Financial category, and select PMT — the dialog shows each argument with a live preview of the result as you fill things in.

The Function Wizard dialog has two tabs — Functions and Structure — at the top left. The left panel contains a Search field, a Category dropdown (here set to "Mathematical"), and a scrollable alphabetical Function list with the currently selected function highlighted in blue. The right panel displays the selected function's name and description at the top, followed by labeled argument input fields (Number 1, Number 2, etc.) each with an fx button and a shrink/expand cell-reference picker. Below the arguments, a Formula preview box shows the formula being built (e.g., "=SUM()") alongside a Result field. The bottom of the dialog has an Array checkbox, Help button, Back/Next navigation buttons, and OK/Cancel buttons.

Related functions round out the picture. `IPMT` and `PPMT` break a single payment into its interest and principal portions for any given period — handy for building an amortization table row by row. `CUMIPMT` and `CUMPRINC` sum those components over a range of periods, so you can instantly see how much interest you'll pay in, say, years 5 through 10 without building the full schedule.

For payoff strategies, model extra payments by adjusting the payment or term. Want to know how many months early you'd finish by paying an extra $200/month? Use `NPER` with the larger payment to get the new term, then compare. For a side-by-side view of different extra-payment amounts and their effect on total interest, set up a column of scenarios and use Calc's **Sheet > Named Ranges and Expressions** to keep your formulas readable.

Goal Seek is where things get really useful for mortgage questions. Say you know you can afford $1,800/month and want to find the maximum loan amount — set up your PMT formula, then go to **Tools > Goal Seek**. Point the *Formula cell* at your PMT result, set the *Target value* to -1800, and pick the loan amount cell as the *Variable cell*. Calc iterates backward and hands you the answer.

The Goal Seek dialog is a compact window titled "Goal Seek" with a "Default Settings" heading. It contains three vertically stacked input fields: "Formula cell" (with a shrink/expand cell-reference picker button to its right), "Target value" (a plain text entry field), and "Variable cell" (also with a cell-reference picker button). To the right of these fields are three buttons arranged vertically: OK (highlighted with a bold blue border as the default action), Cancel, and Help.

When you click **OK**, a result dialog tells you whether it succeeded and offers to insert the value into your variable cell. Hit **Yes** and your spreadsheet updates instantly. This same approach works for finding break-even interest rates on a refinance: set up the total cost of the new loan (closing costs plus cumulative interest) minus the old loan's remaining interest, target zero, and let Goal Seek find the month where you break even.

For more complex optimization — like allocating payments across multiple loans to minimize total interest subject to a fixed monthly budget — reach for the Solver via **Tools > Solver**. It's a step up from Goal Seek: you define a target cell to minimize or maximize, specify which cells Calc can change, and add constraints (like each payment being at least the minimum). The Solver dialog lets you pick from several engines, including the CoinMP Linear Solver for straightforward problems or the DEPS Evolutionary Algorithm for nonlinear ones.

The Solver dialog has two sections. The top section contains a "Target cell" field (showing "$B$4"), an "Optimize result to" area with three radio buttons — Maximum, Minimum, and "Value of" (selected, with "1000" entered) — and a "By changing cells" field (showing "$C$2"); both cell-reference fields have shrink/expand picker buttons. The bottom section, labeled "Limiting Conditions," displays a scrollable list of constraints, each row consisting of a Cell reference field, an Operator dropdown (options like "<=", "=>", "Integer"), and a Value field, with each row having its own cell-picker buttons and a red delete button. In this example, three constraints are defined on $C$2. The dialog footer has Help, Reset All, Options…, Close, and a highlighted blue Solve button.

Set your constraints using operators like `<=`, `>=`, or **Integer** (useful for forcing whole-dollar payments), then click **Solve**. When it finishes, a Solving Result dialog lets you **Keep Result** or **Restore Previous** values — so you can safely experiment without fear of losing your original numbers. For risk scoring, combine `IF` and nested functions to flag loans by debt-to-income ratio or rate thresholds, and use conditional formatting via **Format > Cells > Background Color** to visually highlight high-risk entries.

One last tip: the Functions deck in the Sidebar (**View > Function List**) is a quick way to browse and insert financial functions without opening the full wizard. Just double-click a function name and it drops into your cell with argument placeholders ready to fill.

---

## UI Reference  —  Formula Bar

_Scope: Function Wizard for PMT/IPMT/PPMT financial functions, Functions deck via Sidebar_

The Formula bar sits below the Formatting toolbar and provides cell navigation, function insertion, and formula editing.

The Formula Bar is a narrow horizontal strip. On the far left is the Name Box displaying "A1" with a text cursor and a dropdown arrow (▼) to its right. Next is the Function Wizard button labeled "fx", followed by the AutoSum button showing the sigma symbol (Σ) with its own dropdown arrow. Then comes the equals sign (=) button for entering formula mode. The remainder of the bar to the right is the wide, empty Input Line where cell contents and formulas are typed and displayed.

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

## UI Reference  —  Tools, Window, and Help Menus

_Scope: Tools > Goal Seek for back-solving loan amounts; Tools > Solver for multi-loan optimization_

The Tools menu provides spelling, analysis tools, formula auditing, macros, protection, and global options. Window and Help are small utility menus.

The screenshot shows the Tools menu expanded from the menu bar, with partial views of the neighboring Sheet, Data, Window, and Help menus on either side. The menu items listed from top to bottom are: Spelling… (with a checkmark-style icon), Automatic Spell Checking (checked, enabled), Thesaurus… (greyed out), Language, AutoCorrect Options…, AutoInput (checked, enabled), ImageMap (greyed out), Redact, Auto-Redact, Goal Seek…, Solver…, Detective, Scenarios… (greyed out), Forms, Share Spreadsheet…, Protect Sheet… (unchecked), and Protect Spreadsheet Structure (partially visible, unchecked). The menu appears over a spreadsheet with a blue-highlighted cell area visible in the background.

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
