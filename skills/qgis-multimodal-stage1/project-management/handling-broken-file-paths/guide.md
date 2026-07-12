# Handling Broken File Paths (QGIS 3.44)

When you open a project and QGIS can't locate one or more data sources — maybe a file got moved, a drive was renamed, or a database connection dropped — it pops up the **Handle Unavailable Layers** dialog listing every layer it couldn't reach.

From here you have a few ways to fix things. You can double-click directly in the **Datasource** field for any layer, correct the path by hand, and then hit **Apply changes**. If you'd rather browse to the file visually, select the row, press **Browse**, point it to the right location, and click **Apply changes**.

For bulk repairs, **Auto-Find** is your friend. It scans folders looking for files that match the broken layer names and attempts to reconnect them automatically. This can take a while on large directory trees, but it beats fixing dozens of paths one by one. Once it finishes, confirm with **Apply changes**.

If you'd rather deal with it later, click **Keep Unavailable Layers**. The layers still appear in the **Layers** panel but show no data — you'll see a warning icon next to each broken one. To fix them after the fact, right-click the layer and choose **Repair Data Source…** from the context menu. A nice touch: once you repair one layer this way, QGIS automatically tries to fix any other layers that share the same broken base path.

If a layer is simply no longer needed, select it and click the **Remove Unavailable Layers** button (the red trash icon) to drop it from the project entirely.

One more trick: if you're launching QGIS from the command line and want to skip this dialog altogether, pass the `--skipbadlayers` flag. The project opens immediately and any broken layers just show up as unavailable in the panel, ready for you to repair at your leisure.
