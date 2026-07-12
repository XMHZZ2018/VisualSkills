# Writing Expressions (QGIS 3.44)

The expression engine in QGIS lets you dynamically control labeling, feature selection, field calculations, symbology, and layout content — all from a single builder dialog.

Open the **Expression string builder** anywhere you see the expression button: in **Select By Expression**, the **Field Calculator**, data-defined overrides for symbology/labels, geometry generators, or processing tools. The dialog has two tabs — **Expression** (write and test) and **Function Editor** (create custom Python functions).

As you type, autocompletion suggests field names, variables, and functions — press `Tab` to accept. The editor underlines unknown functions or bad arguments and marks other errors (missing parentheses, stray characters) so you can fix them before applying.

Quoting matters: double-quote field names (`"height"`), single-quote literal strings (`'residential'`), and leave numbers bare (`3.16`). Inside functions that expect a field-name argument as a string, use single quotes — e.g., `attribute(@atlas_feature, 'height')`.

Use `CASE WHEN ... THEN ... ELSE ... END` for conditional labeling or styling, and operators like `and` / `or` to combine filters. Named parameters (`clamp(min:=1, value:=2, max:=9)`) make complex expressions far easier to read later.

The live **Output preview** beneath the editor evaluates your expression against the first feature — switch features via the dropdown to spot-check results. Save frequently-used expressions with **Add current expression to user expressions** so they appear under the **User expressions** group across all your projects.

For anything the built-in functions can't handle, switch to the **Function Editor** tab, hit **New File**, write a Python function decorated with `@qgsfunction(group='Custom', referenced_columns=[])`, then press **Save and Load Functions** — your function immediately appears in the expression tree.
