# Creating New Layers (QGIS 3.44)

QGIS gives you several ways to spin up a fresh layer: from an empty shell you define yourself, from an existing layer's data, from clipboard contents, or as a live SQL query against other layers.

**GeoPackage layers** are the go-to modern format. Head to **Layer > Create Layer > New GeoPackage Layer…** (or use the toolbar button). In the dialog, browse to an existing `.gpkg` file or type a new filename — QGIS adds the extension for you. Give your table a name, pick a geometry type (point, line, polygon, or none), set the CRS, then define your attribute fields one at a time using **Add to Fields List**. Under Advanced Options you can rename the default `fid` primary key column and opt into a spatial index.

See `fig01.png`.

**Shapefile layers** work almost identically — **Layer > Create Layer > New Shapefile Layer…**. The main differences: you specify a file path instead of a database, choose a file encoding, and the supported field types are more limited (text, integer, decimal, date, boolean). A default integer `id` column is added automatically but you can remove it.

**SpatiaLite layers** mirror the GeoPackage workflow but target a `.sqlite` database file. Open the dialog from the same **Layer > Create Layer** submenu, point at a database, name your layer, define geometry and fields, and hit **OK**.

**Temporary Scratch Layers** live only in memory — perfect for throwaway work or geoprocessing intermediates. Create one via **Layer > Create Layer > New Temporary Scratch Layer…**. These support richer geometry options (compound curves, multi-surfaces) and can even be created with no fields at all. The catch: they vanish when you close QGIS. To keep the data, right-click the layer and choose **Make Permanent**, or use **Export > Save Features As…** to write it to any supported format.

See `fig02.png`.

**Virtual layers** are SQL-driven views over your existing layers. Open the dialog from **Layer > Add Layer > Add/Edit Virtual Layer**. Give it a name, then write a query referencing any loaded layer by name — for instance, `SELECT * FROM airports WHERE USE = "Civilian/Public"`. The engine uses SQLite/SpatiaLite under the hood, so you get spatial functions like `MakePoint()` and `ST_Intersects`. You can also embed layers that aren't on the canvas by adding them in the Embedded Layers section.

See `fig03.png`.

For quick one-offs, you can also paste features directly into a new layer: select features, copy them, then use **Edit > Paste Features as > New Vector Layer…** or **Temporary Scratch Layer…**. This works with WKT geometries from external applications too.
