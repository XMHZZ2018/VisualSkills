# Using the Processing Toolbox (QGIS 3.44)

Open the toolbox via **Processing > Toolbox** in the menu bar. It lists every available geoprocessing algorithm, organized by provider — QGIS native tools, GDAL, GRASS, and any third-party providers you've enabled in **Settings > Options > Processing**.

At the top of the panel, use the **Search…** box to filter algorithms by name or keyword. As you type, the list narrows in real time. Above the full list you'll see **Recently Used** and **Favorites** sections for quick access — right-click any algorithm and choose **Add to Favorites** to pin it there.

To run an algorithm, double-click its name. The dialog that opens has a **Parameters** tab on the left (where you set inputs and outputs) and a description panel on the right explaining what the tool does. Each parameter auto-populates with available layers from your project; you can also click the **…** button to browse for files on disk or layers from databases and web services.

For output, the **…** dropdown beside the output field lets you choose **Save to File…**, **Save to GeoPackage…**, **Save to Database Table…**, or just leave it blank for a temporary layer that disappears when you close QGIS.

Once parameters are set, hit **Run**. Switch to the **Log** tab to watch progress and click output file paths directly in the log to open them. If something goes wrong with projections, remember: QGIS native algorithms automatically reproject all inputs to match the first input layer's CRS, but third-party tools generally do not — reproject layers beforehand using the **Reproject layer** algorithm if needed.

The **Advanced** dropdown at the bottom gives you **Copy as Python Command** (handy for scripting), **Copy as qgis_process Command** (for CLI automation), and **Algorithm Settings…** to override things like distance units or thread count for just that run. You can also hit **Run as Batch Process…** to execute the same algorithm across multiple inputs in one go.
