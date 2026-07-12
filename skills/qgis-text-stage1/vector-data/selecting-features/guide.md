# Selecting Features (QGIS 3.44)

All selection tools live under **Edit > Select** or on the **Selection Toolbar**, and they always operate on the currently active layer.

For interactive picking, grab **Select Features by area or single click** — click a feature or drag a rectangle. Alternatively, switch to **Select Features by Polygon**, **by Freehand**, or **by Radius** for irregular shapes. Hold `Shift` to add to your selection, `Ctrl` to subtract, `Ctrl+Shift` to intersect with the existing selection, or `Alt` to require features fall entirely within your drawn shape.

To select by attribute, open **Select Features By Expression** (`Ctrl+F3`) and write a filter like `"TYPE_2" = 'Borough'`. The expression builder remembers your last 20 queries under **Recent (Selection)**. For simpler lookups, **Select Features By Value** (`F3`) gives you a form with per-field operators (equals, contains, between, etc.) and autocomplete — just fill in what you need and hit **Select features**.

Spatial selection is handled by **Select by Location** (picks features that intersect, overlap, or touch features in another layer) and **Select within Distance** (picks everything within a specified radius of reference features).

Handy extras: **Select All Features** (`Ctrl+A`), **Invert Feature Selection**, **Deselect Features from All Layers** (`Ctrl+Alt+A`), and **Reselect Features** under **Edit > Select** if you accidentally clear a painstaking selection.

Once you have a selection, you can save it out via **Edit > Copy Features** then **Edit > Paste Features as** into a new layer or scratch layer.
