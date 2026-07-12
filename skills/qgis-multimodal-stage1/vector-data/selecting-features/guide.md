# Selecting Features (QGIS 3.44)

All selection tools live under **Edit > Select** or on the **Selection Toolbar**, and they always operate on whichever layer is currently active in the Layers panel.

For quick interactive picks, grab **Select Features by area or single click** from the toolbar — click a single feature or drag a rectangle to catch several at once. If you need more control over the shape, switch to **Select Features by Polygon**, **Select Features by Freehand**, or **Select Features by Radius**. With the polygon tool you can even right-click inside an existing polygon from any layer and use it as your selection boundary.

Modifier keys let you refine without starting over. Hold `Shift` to add to your selection, `Ctrl` (or `Cmd`) to subtract, and `Ctrl+Shift` to intersect with what you already have. Hold `Alt` to restrict selection to features entirely within your drawn shape. If you accidentally clear a careful selection, **Edit > Select > Reselect Features** brings it right back.

For attribute-driven selection, open **Select Features By Expression** (`Ctrl+F3`). Build a query like `"TYPE_2" = 'Borough'` using the field list and unique-values helper, then hit **Select Features**. The dialog remembers your last 20 expressions under Recent (Selection).

**Select Features By Value** (`F3`) is a friendlier alternative — it presents the layer's attribute form with per-field operators (equals, contains, between, starts with, etc.) and autocomplete suggestions as you type. Once you've filled in your criteria, choose whether to select, add to selection, remove from selection, or filter the current selection. You can also **Zoom to features** or **Flash features** without committing to a selection at all.

See `fig01.png`.

For spatial queries, use **Select by Location** to grab features based on their relationship to another layer's geometry, or **Select within Distance** to catch everything within a specified radius of reference features.

Rounding out the toolbox: **Select All Features** (`Ctrl+A`), **Invert Feature Selection**, **Deselect Features from All Layers** (`Ctrl+Alt+A`), and **Deselect Features from the Current Active Layer** (`Ctrl+Shift+A`) handle the common housekeeping. To save selected features out, copy them with **Edit > Copy Features** and paste into a new layer with **Edit > Paste Features as** in your preferred format.
