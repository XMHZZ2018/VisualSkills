# Creating New Layers (QGIS 3.44)

All new layer types live under **Layer › Create Layer**. Pick the format that fits your workflow.

**GeoPackage** is the go-to for new projects. Hit **New GeoPackage Layer…**, browse to an existing `.gpkg` or type a new filename, set a table name, choose your geometry type, and assign a CRS. Add fields in the New Field section — give each a name and type (Text, Integer, Real, Date, etc.), then click **Add to Fields List**. Under Advanced Options you can rename the `fid` primary key and toggle the spatial index.

**Shapefile** works similarly via **New Shapefile Layer…**. You'll set a file path, file encoding, geometry type, and optional Z/M dimensions. Field types are more limited here — just Decimal, Integer, Text, Date, and Boolean. A default `id` column is created but you can remove it.

**SpatiaLite** mirrors the GeoPackage flow — point it at a `.sqlite` database, name the layer, pick geometry and CRS, then define your fields. Enable the autoincrementing primary key in Advanced Options if you want one.

**Temporary Scratch Layers** are pure in-memory — great for quick experiments or geoprocessing intermediates, but gone when you close QGIS. Create one via **New Temporary Scratch Layer…**, choose geometry (including curved types like CompoundCurve), and optionally add fields. To persist a scratch layer later, click the memory-indicator icon beside it or right-click and choose **Make permanent**.

**Virtual Layers** let you define a layer as a live SQL query over other loaded layers. Open it from **Layer › Add Layer › Add/Edit Virtual Layer**. Give it a name, write a query referencing layer names as tables (e.g., `SELECT * FROM airports WHERE USE = 'Civilian/Public'`), and QGIS handles the rest regardless of the underlying provider. Joins across layers work too. The engine is SQLite/SpatiaLite, so all spatial functions are available.

You can also create layers by pasting clipboard features via **Edit › Paste Features as › New Vector Layer…** or **Temporary Scratch Layer…** — handy for splitting data on the fly.
