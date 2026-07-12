# Handling Broken File Paths (QGIS 3.44)

When you open a project and QGIS can't find a data source — maybe the file moved, a database went offline, or someone renamed a folder — it pops up the **Handle Unavailable Layers** dialog listing every layer it couldn't reach.

From here you have a few options. You can double-click the **Datasource** field directly in the dialog, fix the path by hand, and hit **Apply changes**. If you'd rather browse to the correct location, select the row, press **Browse**, point it to the right file, then **Apply changes**.

For bulk fixes, try **Auto-Find** — QGIS will crawl your folders looking for matches. This can take a while on large directory trees, but it's great when an entire parent folder was renamed or moved. Once it finishes, confirm with **Apply changes**.

If you'd rather deal with it later, click **Keep Unavailable Layers**. The layers still appear in the **Layers** panel but show no data. You'll see a warning icon next to each broken layer — click it, or right-click the layer and choose **Repair Data Source…** to fix the path. A nice bonus: once you repair one layer this way, QGIS automatically attempts to fix other layers that share the same broken base path.

To permanently drop layers you no longer need, hit the **Remove Unavailable Layers** button (the red trash icon) in the dialog.

If you want to skip the dialog entirely at launch — say, in a scripting or automation context — start QGIS from the command line with the `--skipbadlayers` flag.
