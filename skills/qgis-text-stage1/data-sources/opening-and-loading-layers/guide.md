# Opening and Loading Layers (QGIS 3.44)

The central hub for loading data is the **Data Source Manager** dialog. Open it with `Ctrl+L` or click the **Open Data Source Manager** button on the toolbar. The left sidebar has tabs for each data type: Vector, Raster, Mesh, Delimited Text, and more.

**Vector layers** (Shapefile, GeoPackage, GeoJSON, etc.): switch to the **Vector** tab or press `Ctrl+Shift+V`. Keep the source type set to **File**, click the **…** browse button, pick your file, then hit **Add**. Hold `Ctrl` or `Shift` to select multiple files at once.

**Raster layers** (GeoTIFF, MBTiles, etc.): switch to the **Raster** tab or press `Ctrl+Shift+R`. Same workflow — browse, select, **Add**.

**Mesh layers**: open the **Mesh** tab, browse to your file (NetCDF, GRIB, etc.), and press **Add**. If it contains sublayers, you'll be prompted to choose which ones to load.

**Delimited text files** (CSV, TSV, TXT with coordinates): use the **Delimited Text** tab. After selecting the file, set the delimiter format and configure the **Geometry Definition** section — pick **Point coordinates** and assign the X/Y fields, or choose **Well known text (WKT)** if your geometry lives in a single column. Set the CRS, then hit **Add**.

For the fastest workflow, skip the dialog entirely — just drag files from the **Browser** panel (open it with `Ctrl+2`) or from your OS file manager directly onto the map canvas. Double-clicking a layer in the Browser works too.

The Browser panel also connects to databases (PostgreSQL, GeoPackage, SpatiaLite) and web services (WMS, WFS, XYZ Tiles). Right-click a database entry and choose **New Connection…** to set one up, then expand it and drag tables straight into your project.
