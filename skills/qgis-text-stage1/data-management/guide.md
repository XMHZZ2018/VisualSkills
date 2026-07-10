Manage data sources in QGIS through the unified Data Source Manager or Browser Panel — both lead to the same capabilities.

## Opening the Data Source Manager

**Shortcut:** `Ctrl+L` — opens the Data Source Manager dialog with tabs for every data type.

Alternatively, use **Layer → Add Layer →** submenu, or enable the **Manage Layers toolbar** via **View → Toolbars**.

The Data Source Manager dialog has a left-side tab list: Browser, Vector, Raster, Mesh, Point Cloud, Delimited Text, GeoPackage, SpatiaLite, PostgreSQL, etc. Each tab has format-specific options.

## The Browser Panel

Open with `Ctrl+2` or **View → Panels → Browser**.

The Browser panel shows a tree hierarchy:
- **Favorites** — pinned shortcuts
- **Project Home** — folder containing your .qgz file
- **Home / filesystem root** — full file system
- Database entries (GeoPackage, SpatiaLite, PostgreSQL, etc.)
- Web services (WMS/WMTS, WFS, XYZ Tiles, ArcGIS REST)

### Adding a layer from the Browser
1. Navigate the tree to your file
2. **Double-click** to add it directly, or
3. **Drag and drop** onto the map canvas or Layers panel, or
4. **Right-click → Add Layer to Project**

Use the filter button (funnel icon) at the top of the Browser to search by filename, folder, or DB table. Supports Normal, Wildcard (`*`, `?`), and Regular Expression modes.

**Tip:** Right-click any folder → **Add as a Favorite** to pin it for fast access.

## Loading Specific Data Types

### Vector files (Shapefile, GeoJSON, GeoPackage, etc.)
**Layer → Add Layer → Add Vector Layer** (`Ctrl+Shift+V`)
- Source type: File, Directory, Database, or Protocol
- Click **...** to browse to the file
- Click **Add**

### Raster files (GeoTIFF, JPEG, etc.)
**Layer → Add Layer → Add Raster Layer** (`Ctrl+Shift+R`)
- Browse to file, click **Add**

### Delimited text (CSV with coordinates)
**Layer → Add Layer → Add Delimited Text Layer** (`Ctrl+Shift+T`)
- Specify X/Y field columns for point geometry, or "No geometry" for attribute-only table
- Set the CRS before clicking **Add**

### PostGIS / PostgreSQL
**Layer → Add Layer → Add PostGIS Layers** (`Ctrl+Shift+D`)
- Requires a saved connection — click **New** to configure host, port, database, credentials
- After connecting, select tables from the list

### Web services (WMS, WFS, XYZ Tiles)
**Layer → Add Layer → Add WMS/WMTS Layer** (or WFS, WCS)
- Click **New** to add a service URL
- Connect, then select layers from the list

## Creating New Layers

All creation dialogs are at **Layer → Create Layer →**.

### New GeoPackage Layer
1. **Layer → Create Layer → New GeoPackage Layer**
2. Click **...** next to Database — select existing `.gpkg` or type a new filename
3. Set **Table name**, **Geometry type**, and **CRS**
4. Add fields: enter Name, select Type (Text, Whole number, Decimal, Date, Boolean), click **Add to Fields List**
5. Click **OK** — layer appears in the Layers panel ready to edit

**Note:** A `fid` primary key column is auto-generated. A spatial index is created by default.

### New Shapefile Layer
1. **Layer → Create Layer → New Shapefile Layer**
2. Set file path via **...**, choose **File encoding**
3. Choose **Geometry type** (Point, Line, Polygon, No Geometry)
4. Set CRS, add fields (limited types: Decimal, Integer, Text, Date, Boolean)
5. Click **OK**

**Pitfall:** Shapefile field names are limited to 10 characters — longer names will be silently truncated.

### New SpatiaLite Layer
Same workflow as GeoPackage but via **Layer → Create Layer → New SpatiaLite Layer**. Stores in a `.sqlite` file. Supports autoincrementing primary key under **Advanced Options**.

### New Temporary Scratch Layer (Memory Layer)
**Layer → Create Layer → New Temporary Scratch Layer**
- Fast to create, no file location needed
- **Lost when QGIS closes** — use **Layer → Make Permanent** to save to disk before closing
- Useful for intermediate processing or temporary digitizing

### New GPX Layer
**Layer → Create Layer → New GPX Layer**
- Creates three linked layers at once: **waypoints** (points), **routes** (lines), **tracks** (lines)
- All three are added to the Layers panel simultaneously

## Common Pitfalls

- **CRS mismatch:** Always verify the CRS when loading data. If a layer appears in the wrong location, right-click the layer → **Set CRS → Set Layer CRS** and check for on-the-fly reprojection conflicts.
- **Temporary layers lost on exit:** Memory/scratch layers show a warning icon in the Layers panel. Save them via right-click → **Export → Save Features As** or **Make Permanent**.
- **Format not available:** Run `ogrinfo --formats` (vector) or `gdalinfo --formats` (raster) in a terminal, or check **Settings → Options → GDAL** to confirm your GDAL build supports a given format.
- **Browser not showing new files:** Click the **Refresh** button (circular arrow) at the top of the Browser panel.
- **Database/service entries missing:** Expand the relevant entry in the Browser and right-click → **New Connection** to configure credentials before data appears.