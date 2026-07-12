# Working with the Attribute Table (QGIS 3.44)

Open a layer's attribute table by selecting the layer and hitting `F6`, or right-click it in the Layers panel and choose **Open Attribute Table**. Use `Shift+F6` to open it pre-filtered to selected features, or `Ctrl+F6` for features visible on the current map canvas.

The table has two modes: **Table View** (spreadsheet-style rows and columns) and **Form View** (a feature list on the left, attributes on the right). Switch between them with the icons at the bottom-right of the window.

To select features, click row numbers — hold `Ctrl` for individual picks or `Shift` for a range. For expression-based selection, use **Select features using an Expression** in the toolbar.

Filter what's displayed via the drop-down at the bottom-left: **Show Selected Features**, **Show Features Visible on Map**, **Field Filter** (quick column-value match), or **Advanced filter (Expression)** for full expression power. Filtering only hides rows from view — it doesn't remove features from the layer.

To edit values, click **Toggle Editing** (`Ctrl+E`). You can type directly into cells, or for bulk updates use the **Quick Field Calculation Bar** at the top — pick a field, enter an expression, and hit **Update All** or **Update Selected**.

For calculated fields, open the **Field Calculator** (`Ctrl+I`). Check **Create a new field**, set a name and type, then build an expression (e.g., `$length / 1000` for km). Check **Create virtual field** if you want values to auto-update when underlying data changes — handy for things like `$area` or `now()`.

**Multi Edit mode** lets you change multiple attributes across many features at once — select your features, click **Toggle multi edit mode**, fill in the fields you want to change, and hit **Apply changes**. One undo rolls back the whole batch.

For a quick attribute check without opening the table, use the **Identify Features** tool (`Ctrl+Shift+I`) — just click a feature on the map and its attributes appear in a panel.
