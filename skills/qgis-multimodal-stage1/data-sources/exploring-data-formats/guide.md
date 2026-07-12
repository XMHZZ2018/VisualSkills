# Exploring Data Formats and Fields (QGIS 3.44)

QGIS reads a wide range of spatial data through GDAL drivers. Knowing how each format behaves — and where its quirks hide — saves you from mysterious blank layers and broken projections.

**Raster data** lives in grids of uniform cells (think satellite imagery or DEMs). Each cell has a value but no attribute table. QGIS positions rasters using embedded georeference info or a sidecar world file. GeoPackage and GeoTIFF are the go-to formats here.

**Vector data** is where variety explodes. GeoPackage (GPKG) is the default vector format in QGIS — it's a single SQLite file that can hold vectors, rasters, styles, and even entire QGIS projects. ESRI Shapefiles still appear everywhere, but remember they're actually a bundle of files (`.shp`, `.dbf`, `.shx`, and ideally `.prj`). To speed up Shapefile rendering, open **Layer Properties > Source** and hit **Create Spatial Index** to generate a `.qix` file.

For delimited text (CSV and friends), your file needs a header row and — if spatial — columns for coordinates or a WKT geometry field. QGIS will auto-detect delimiters, but by default GDAL treats every column as text. Drop a `.csvt` file alongside your CSV (same name, one line of quoted type declarations like `"Integer","Real","String"`) to enforce proper typing.

**PostgreSQL/PostGIS** layers need a column usable as a unique integer key — typically the primary key. For views lacking one, you'll need to define a key field in QGIS before loading. Enable server-side filtering via **Settings > Options > Data Sources > Execute expressions on server-side if possible**. Import data with the **DB Manager** plugin, `shp2pgsql`, or `ogr2ogr`, and always create a GiST spatial index afterward (`CREATE INDEX ... USING GIST(geom)`) followed by `VACUUM ANALYZE`.

**SpatiaLite** works like a lightweight, file-based PostGIS. Save to it by choosing `SpatiaLite` as the format when exporting, or select `SQLite` and add `SPATIALITE=YES` under custom data source options.

When exporting to **GeoJSON**, note the RFC7946 option — setting it to YES forces EPSG:4326, right-hand-rule polygon winding, and 7-digit coordinate precision. For streaming large datasets, use the "GeoJSON - Newline Delimited" variant instead.

**Field domains** (available in GeoPackage and File Geodatabases) let you constrain field values at the database level. Right-click a field in the Browser panel to create Range, Coded Values, or Glob (pattern-match) domains. These constraints travel with the data and are enforced across applications.

If your layer crosses the **180° longitude line** and features appear split across the canvas, import into PostGIS and run `UPDATE table SET geom = ST_ShiftLongitude(geom);` to shift coordinates into a continuous range. See `fig01.png` for the split-layer appearance before applying the fix.
