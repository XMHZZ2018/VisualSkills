# Exploring Data Formats and Fields (QGIS 3.44)

QGIS supports a wide range of data formats through GDAL drivers. Here's a practical overview of what you can work with and how fields behave across formats.

**Raster data** consists of cell grids — each cell holds one value (elevation, temperature, reflectance). Rasters don't carry per-cell attribute tables; they're positioned via georeferencing embedded in the file (GeoTIFF) or a sidecar world file. GeoPackage and GeoTIFF are your best bets for raster storage.

**Vector data** is where format differences matter most. GeoPackage (`.gpkg`) is the default and preferred format — it's a single SQLite file that can hold vectors, rasters, styles, and even entire QGIS projects. Shapefiles still work but come as a bundle of files (`.shp`, `.dbf`, `.shx`, and optionally `.prj`). To speed up shapefile rendering, open **Layer Properties > Source** and click **Create Spatial Index**.

**Delimited text** (CSV) files load as layers if they have a header row and coordinate columns (X/Y) or a WKT geometry column. GDAL treats all CSV columns as strings unless you place a `.csvt` file alongside it — a single-line file like `"Integer","Real","String"` that declares column types. QGIS can also auto-detect field types during import.

**PostgreSQL/PostGIS** layers need a unique integer column (primary key or `ctid`) for QGIS to identify features. Enable server-side filtering via **Settings > Options > Data Sources > Execute expressions on server-side if possible**. Import data using **DB Manager**, `shp2pgsql`, or `ogr2ogr`, and always create a GiST spatial index afterward for performance.

**SpatiaLite** layers work similarly — save as SpatiaLite format or use SQLite with the `SPATIALITE=YES` custom option. Editable views are supported.

**GeoJSON** export offers useful layer options: set `RFC7946=YES` for the modern standard (forces EPSG:4326, right-hand polygon winding), and `COORDINATE_PRECISION` to control decimal digits. Newline-delimited GeoJSON streams features one per line for large datasets.

**Field domains** (available in GeoPackage and File Geodatabase) enforce value constraints at the database level. Right-click a field in the Browser panel to create Range, Coded Values, or Glob (pattern-matching) domains. These constraints persist across applications, not just QGIS.

For layers crossing the 180° longitude line that appear split on the canvas, import into PostGIS and run `UPDATE table SET geom = ST_ShiftLongitude(geom);` to wrap coordinates into a continuous range.
