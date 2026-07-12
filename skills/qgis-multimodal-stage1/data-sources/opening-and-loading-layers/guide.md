# Opening and Loading Layers (QGIS 3.44)

The central hub for getting data into QGIS is the **Data Source Manager**. Open it with `Ctrl+L` or click the **Open Data Source Manager** button on the Data Source Manager toolbar. The left sidebar lists every supported source type — Vector, Raster, Mesh, Delimited Text, databases, web services — so you pick a tab and go.

See `fig01.png`.

For the quickest workflow, just use the **Browser panel** (toggle it with `Ctrl+2` or **View > Panels**). It shows your filesystem, databases, and remote services as a navigable tree. Find your file, then double-click or drag it straight onto the map canvas — done. You can also right-click any item and choose **Add Layer to Project**.

To load a **vector layer** from file (Shapefile, GeoPackage, GeoJSON, etc.), open the Data Source Manager, switch to the **Vector** tab, make sure the **File** source type is selected, click the **...** browse button, pick your file, and hit **Add**. The shortcut is `Ctrl+Shift+V`. For multi-layer files you'll get a dialog to choose which sublayers to import.

**Raster layers** (GeoTIFF, MBTiles, JPEG, etc.) work the same way — use the **Raster** tab or `Ctrl+Shift+R`, browse to the file, and press **Add**.

For **mesh data** (unstructured grids with temporal components), switch to the **Mesh** tab in the Data Source Manager, browse to your file, and press **Add**. If the file contains multiple mesh layers, you'll be prompted to select which ones to load.

**Delimited text files** like CSVs with coordinate columns deserve their own tab — **Delimited Text**. Browse to your file, then configure the delimiter (CSV, regex, or custom), confirm that field names come from the first row, and set the geometry definition: pick **Point coordinates** and assign X/Y fields, choose **Well known text (WKT)** if the file has a geometry column, or select **No geometry** for attribute-only tables. Set the CRS, then hit **Add**.

See `fig02.png`.

Don't forget the drag-and-drop shortcut: you can drag files directly from your OS file manager onto the map canvas or the Layers panel, and QGIS will load them with sensible defaults.
