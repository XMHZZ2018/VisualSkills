# Working with the Attribute Table (QGIS 3.44)

The attribute table is your spreadsheet view into any vector layer's data — each row is a feature, each column a field. Open it by selecting a layer in the Layers panel and hitting `F6`, or right-click the layer and choose **Open Attribute Table**. Use `Shift+F6` to open it pre-filtered to selected features, or `Ctrl+F6` for only features visible on your current map canvas.

See `fig01.png`.

QGIS gives you two ways to browse: **Table view** (the classic grid) and **Form view** (a list of feature identifiers on the left, with a detail form on the right). Switch between them using the icons at the bottom-right of the dialog. Form view is handy when you have many fields and want to focus on one feature at a time.

To select features, click row numbers on the left — hold `Ctrl` for individual picks or `Shift` for a range. Selections sync both ways: pick rows in the table and they highlight on the map, and vice versa. For expression-based selection, use the **Select features using an Expression** button in the toolbar.

Filtering controls what the table *shows* without hiding features from the map. Use the drop-down at the bottom-left to switch between **Show All Features**, **Show Selected Features**, **Show Features Visible on Map**, or **Advanced filter (Expression)**. The field filter option lets you quickly type a value to match against a chosen column. You can save frequently-used filter expressions for reuse via the store button next to the filter bar.

To edit values, toggle the layer into edit mode with `Ctrl+E`. You can then type directly into cells, or for bulk updates open the **Field Calculator** (`Ctrl+I`). The Field Calculator lets you create a new field or update an existing one using any expression — for example, `$length / 1000` to compute line length in kilometres. Check **Create virtual field** if you want values that recalculate automatically whenever underlying data changes.

See `fig02.png`.

For quick existing-field updates without opening the full calculator, use the **Quick Field Calculation Bar** at the top of the table (visible in edit mode). Pick a field, write an expression, and hit **Update All** or **Update Selected**.

When you need to change several fields across many features at once, activate **Toggle multi edit mode**. Select your target features, modify whichever fields you need in the form, and click **Apply changes** — it all happens as a single undoable operation.

Right-click any column header to sort, resize, hide, or reorder columns. Sorting can use expressions like `concat(col0, col1)` for multi-column sorts. To highlight particular rows or cells visually, click the **Conditional formatting** button and define rules based on expressions — useful for flagging empty values, outliers, or features in a specific area.

See `fig03.png`.

Finally, for a quick peek at a single feature's attributes without opening the full table, use the **Identify Features** tool (`Ctrl+Shift+I`) and click a feature on the map. The results panel shows all fields, derived measurements, and even related records if you have relations configured.
