Open, import, and create vector/raster layers in QGIS 3.44 using the Data Source Manager, Browser Panel, and layer creation dialogs.

---

## Opening Data

### Data Source Manager

The **Data Source Manager** is the primary entry point for loading any data into QGIS. It provides a unified interface for files, databases, and web services.

Open it via:
- **Toolbar**: Click the Open Data Source Manager button (Read the screenshot `fig01.png` in this directory — it shows the Data Source Manager toolbar button)
- **Menu**: `Layer › Add Layer ›` (each submenu item opens the relevant tab)
- **Keyboard**: `Ctrl+L`

Read the screenshot `fig03.png` in this directory — it shows the full Data Source Manager dialog with its left-side tab list (Vector, Raster, Mesh, Point Cloud, WMS/WMTS, WFS, WCS, PostGIS, etc.)

Each tab corresponds to a data type. Select the appropriate tab, configure the source path or connection, then click **Add**.

### DB Manager

For advanced database operations, use the **DB Manager** plugin (`Database › DB Manager`).

Read the screenshot `fig05.png` in this directory — it shows the DB Manager interface for querying and managing connected spatial databases.

---

## Browser Panel

The Browser Panel provides a file-system tree for drag-and-drop layer loading.

Open it via:
- `View › Panels › Browser` or `Settings › Panels` (Read the screenshot `fig09.png` in this directory — it shows the Settings/Panels menu icon)
- **Keyboard**: `Ctrl+2`
- Or as a tab inside the Data Source Manager (`Ctrl+L`)

### Browser Toolbar Buttons

At the top of the Browser panel:

- **Add Selected Layers** — Read the screenshot `fig11.png` in this directory — it shows the Add Layer button used to load selected items into the project
- **Refresh** — Read the screenshot `fig13.png` in this directory — it shows the Refresh button to update the browser tree
- **Filter Browser** — Read the screenshot `fig15.png` in this directory — it shows the Filter/search box; supports Normal, Wildcard (`?`, `*`), and Regular Expression modes

### Browser Tree Structure

The tree is organized as:
- **Favorites** — pinned shortcuts to frequent folders
- **Spatial Bookmarks** — stored map extents
- **Project Home** — folder containing current project files
- **Home / filesystem root** — local drives
- **Database/service entries**: GeoPackage, SpatiaLite, PostgreSQL, SAP HANA, MS SQL Server, Oracle, WMS/WMTS, WFS, WCS, XYZ Tiles, ArcGIS REST Server

### Adding a Layer from the Browser

1. Open the Browser panel (`Ctrl+2`)
2. Navigate the tree to your file or database table
3. **Double-click** the layer name, or **drag it** onto the map canvas, or right-click › **Add Layer to Project**
4. The layer appears in the Layers panel and is rendered on the canvas

> **Tip**: Right-click any entry for context options including Export, Rename, Delete, and Layer Properties (with metadata, preview, and attribute table).

---

## Creating New Layers

Access all creation tools via `Layer › Create Layer ›` or the **Data Source Manager toolbar**.

### New GeoPackage Layer

GeoPackage (`.gpkg`) is the recommended format — a single file supporting multiple layers.

Read the screenshot `fig02.png` in this directory — it shows the New GeoPackage Layer toolbar button

1. Go to `Layer › Create Layer › New GeoPackage Layer…` or click the button shown in `fig02.png`
2. The **New GeoPackage Layer** dialog opens — Read the screenshot `fig04.png` in this directory — it shows the full dialog with Database path, Table name, Geometry type, CRS, and Fields list sections
3. Click **`…`** next to **Database** to select an existing `.gpkg` file or create a new one
4. Enter a **Table name**
5. Set **Geometry type** (Point, Line, Polygon, or No Geometry); optionally enable Z/M dimensions
6. Set the **CRS** using the projection button — Read the screenshot `fig06.png` in this directory — it shows the CRS selector button
7. **Add fields**:
   - Enter field **Name**
   - Select **Type**: Text, Whole number, Decimal number, Date, Date and time, Binary (BLOB), Boolean
   - Set **Maximum length** if applicable
   - Click **Add to Fields List** — Read the screenshot `fig08.png` in this directory — it shows the Add to Fields List (newAttribute) button
   - Reorder fields with Move Up / Move Down — Read the screenshot `fig10.png` and `fig12.png` in this directory — they show the arrowUp and arrowDown reorder buttons
8. Click **OK** — the layer is added to the Layers panel ready for editing

> By default, a `fid` primary key column and a `geometry` column (with optional spatial index) are created. These can be renamed under **Advanced Options**.

### New Shapefile Layer

1. Go to `Layer › Create Layer › New Shapefile Layer…` — Read the screenshot `fig14.png` in this directory — it shows the New Shapefile Layer toolbar button
2. Click **`…`** next to **File name** to set the save path
3. Set **File encoding**, **Geometry type** (No Geometry, Point, Multipoint, Line, Polygon), and optional Z/M dimensions
4. Set the **CRS** using the projection button (same selector as fig06)
5. Add fields the same way as GeoPackage (Name → Type → Length/Precision → Add to Fields List)
6. Click **OK**

> Shapefile field types are limited to: Decimal number, Whole number, Text data, Date, Boolean.

### New SpatiaLite Layer

1. Go to `Layer › Create Layer › New SpatiaLite Layer…`
2. Select or create a `.sqlite` database file
3. Provide a **Layer name**, set **Geometry type** and **CRS**
4. Add fields (supported: Text, Whole number, Decimal number, Date, Date time)
5. Under **Advanced Options**, optionally enable an autoincrementing primary key
6. Click **OK**

### New GPX Layer

1. `Layer › Create Layer › New GPX Layer…`
2. Choose a save location and file name, then click **Save**
3. Three layers are created automatically:
   - **waypoints** (point layer — name, elevation, description, URL)
   - **routes** (line layer — planned navigation sequences)
   - **tracks** (line layer — recorded movement over time)

### New Temporary Scratch Layer

In-memory layers — fast for intermediate geoprocessing but **not saved to disk** and lost when QGIS closes.

1. `Layer › Create Layer › New Temporary Scratch Layer…`
2. Set geometry type and add fields as needed
3. To make permanent: right-click the layer in Layers panel › **Make Permanent…** and save to a file format

---

## Quick Reference

| Action | Shortcut / Location |
|---|---|
| Open Data Source Manager | `Ctrl+L` |
| Open Browser Panel | `Ctrl+2` |
| Add layer from Browser | Double-click or drag to canvas |
| New GeoPackage layer | `Layer › Create Layer › New GeoPackage Layer…` |
| New Shapefile layer | `Layer › Create Layer › New Shapefile Layer…` |
| New Temporary layer | `Layer › Create Layer › New Temporary Scratch Layer…` |