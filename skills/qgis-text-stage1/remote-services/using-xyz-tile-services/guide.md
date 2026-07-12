The source file contains only text (no inline image references to load). The relevant XYZ Tiles section starts at line 1287. Here's the guide:

# Using XYZ Tile Services (QGIS 3.44)

XYZ tile services deliver pre-rendered raster map tiles — think OpenStreetMap, Google Maps, or terrain hillshades — sliced into a `{z}/{x}/{y}` grid you can drop straight into your project as a basemap.

QGIS ships with two ready-to-use connections out of the box: **OpenStreetMap** (2D street map) and **Mapzen Global Terrain** (DEM tiles). To use one, expand **XYZ Tiles** in the **Browser** panel and double-click the entry.

To add a custom service, right-click **XYZ Tiles** in the **Browser** panel and choose **New Connection**. Give it a **Name**, paste the tile URL (e.g. `https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}`), set **Min. Zoom Level** and **Max. Zoom Level**, and pick a **Tile Resolution** — use *Standard (256×256)* for most providers or *High (512×512)* for retina tiles. If the provider requires a key, configure it under **Authentication**.

The **Interpretation** dropdown is handy for terrain RGB tiles: set it to *MapTiler Terrain RGB* or *Terrarium Terrain RGB* and QGIS decodes the color-encoded elevation into a single-band float raster you can style with hillshade or contour renderers.

Hit **OK**, then double-click the new entry to add it to your map. You can also load tiles without saving a connection — just fill in the **Connection Details** in **Data Source Manager > XYZ** and press **Add**; the layer appears as "XYZ Layer."

To share or back up your connections, right-click the **XYZ Tiles** node and choose **Save Connections** to export an XML file. Import them elsewhere with **Load Connections**.
