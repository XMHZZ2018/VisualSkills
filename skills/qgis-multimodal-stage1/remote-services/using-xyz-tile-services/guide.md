# Using XYZ Tile Services (QGIS 3.44)

XYZ Tile services let you pull in raster basemaps — things like OpenStreetMap, Google Maps, or terrain tiles — as backdrop layers in your project. QGIS 3.44 ships with a couple already configured: **OpenStreetMap** for general-purpose mapping and **Mapzen Global Terrain** for elevation data. You can start using them immediately from the Browser panel.

To add a new XYZ tile source, open **Data Source Manager** (`Ctrl+L`) and switch to the **XYZ** tab, or right-click **XYZ Tiles** in the **Browser** panel and choose **New Connection**. Give it a **Name**, then paste the tile URL using the `{z}/{x}/{y}` placeholder pattern — for example, `https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}` for Google Maps. Local tile caches work too with `file:///local_path/{z}/{x}/{y}.png`.

See `fig01.png`.

Set the **Min. Zoom Level** and **Max. Zoom Level** to match what the provider supports (typically 0–19). If the provider requires credentials, expand the **Authentication** section and configure them. The **Tile Resolution** dropdown handles HiDPI displays — choose **High (512x512 / 192DPI)** if the service offers retina tiles, otherwise leave it at **Standard**.

For terrain-style tiles that encode elevation in RGB values, use the **Interpretation** dropdown. Select **MapTiler Terrain RGB** or **Terrarium Terrain RGB** and QGIS will decode the color channels into a single-band float raster you can style with standard raster renderers — hillshade, pseudocolor, whatever you need.

You don't always need to save a connection permanently. In the **XYZ** tab, just edit the **Connection Details** fields directly — the **Name** switches to `Custom` — and hit **Add**. The layer loads as "XYZ Layer" without cluttering your saved connections.

Once a connection exists, double-click it in the Browser panel (or select it and press **Add**) to drop it into your project. Right-clicking the entry also lets you **Export layer… > To File** to save tiles as a local raster, or view **Layer Properties** for metadata and a preview.

To share your tile configurations with colleagues, use **Save Connections** from the XYZ section of Data Source Manager — this exports an `.XML` file they can import via **Load Connections**.
