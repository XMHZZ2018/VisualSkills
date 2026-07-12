# Using the Processing Toolbox (QGIS 3.44)

The Processing Toolbox is your daily driver for geoprocessing in QGIS. Open it from **Processing > Toolbox** (or the toolbar shortcut), and you'll see every available algorithm organized by provider — QGIS native tools, GDAL, GRASS, and any third-party providers you've enabled. Custom models and scripts you create show up here too.

See `fig01.png`.

At the top of the toolbox there's a search box. Just start typing — the list filters in real time to show only algorithms whose names or keywords match what you've entered. Below the search bar you'll find your **Recently Used** and **Favorites** lists for quick re-runs. Right-click any algorithm to add it to Favorites, execute it directly, or launch it in batch mode.

To run an algorithm, double-click its name. This opens the algorithm dialog with two tabs: **Parameters** (where you set inputs and outputs) and **Log** (which streams progress info while the tool runs). A description panel on the right side gives you a quick summary of what the algorithm does.

See `fig02.png`.

For input layers, you can pick from loaded layers in the dropdown, browse for files on disk, or just drag a layer straight from the **Layers** panel onto the input widget. The iterator button next to vector inputs lets you run the algorithm once per feature — handy when you need to process features individually without scripting a loop.

Output parameters give you several choices: save to a file, write into a GeoPackage or database table, create a temporary layer, or append to an existing layer. If you leave the output blank, QGIS writes a temporary file that disappears when you close the session.

When working with multiple input layers, be aware that native QGIS algorithms will reproject everything to match the CRS of the first input layer. External provider algorithms (GRASS, SAGA) typically won't — so make sure your layers share a CRS before feeding them in, or run **Reproject layer** first.

The **Advanced** dropdown at the bottom of the dialog is worth knowing about. From there you can copy the equivalent PyQGIS command or qgis_process CLI command for the current parameter setup — great for scripting or reproducibility. You can also override settings like distance units and thread count on a per-run basis via **Algorithm Settings…**.
