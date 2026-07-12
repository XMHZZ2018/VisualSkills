# Writing Expressions (QGIS 3.44)

Expressions in QGIS let you dynamically control labels, styles, selections, field values, and geometry — all from a single formula language. You'll find the Expression string builder everywhere: behind the little expression button next to most inputs, in **Select By Expression…**, in the **Field Calculator**, and inside data-defined overrides for symbology and layouts.

The builder has two main tabs. The **Expression** tab is where you write and test formulas. On the left you get an editor with autocomplete (arrow keys to browse suggestions, `Tab` to insert), a live output preview at the bottom, and a function/field browser on the right. Double-click any function or field name to drop it into your expression. The **Function Editor** tab lets you write custom Python functions when the built-ins aren't enough.

See `fig01.png`.

A key thing to internalize: the dialog you opened already supplies context. If you launched **Select By Expression…** on a layer, you only need the *condition* — the "select from layer where…" part is implied. If you're in the Field Calculator updating an existing field, you only supply the *new value*. The surrounding tool handles the rest.

Watch your quotes. Double quotes reference field names (`"height"`), single quotes are string literals (`'residential'`), and numbers stand alone (`3.16`). Inside functions that expect a field name as a string argument, use single quotes: `attribute(@atlas_feature, 'height')`.

For readability, use named parameters: `clamp(min:=1, value:=2, max:=9)` beats `clamp(1, 2, 9)` when you revisit it later. You can also reorder arguments when using named syntax. Add comments with `--` for inline or `/* */` for blocks — future-you will appreciate it on complex aggregates.

Common patterns worth memorizing: `"total_pop" / "area_km2"` for field math, `CASE WHEN ... THEN ... ELSE ... END` for categorization, `overlay_intersects(layer:='lands', filter:="zone_type"='Natural')` for spatial queries, and `point_on_surface(@geometry)` inside geometry generators.

Once you've built an expression you'll reuse, hit **Add current expression to user expressions** above the editor. Saved expressions live in your user profile and appear under the **User expressions** group in every project. You can also import/export them as `.json` files to share with teammates.

See `fig02.png`.

For truly custom logic, switch to the **Function Editor** tab, click **New File**, and write a Python function decorated with `@qgsfunction`. Set `group='Custom'` to control where it appears in the function list, and declare `referenced_columns=[]` if your function doesn't need attribute access (speeds things up). Hit **Save and Load Functions** and your function is immediately available in the Expression tab. You can store custom functions either as standalone `.py` files in your profile (available across projects) or embedded in the project file itself (portable but requires the recipient to trust embedded Python).
