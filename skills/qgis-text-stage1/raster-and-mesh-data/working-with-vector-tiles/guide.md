Now I have the full content. There are no inline image references with `![alt](abs_path)` format in this file — just figure captions. I have enough information to write the guide.

# Working with Vector Tiles (QGIS 3.44)

Vector tiles deliver geographic data as pre-clipped, zoom-level-specific packets — lighter than raster tiles, faster than raw vectors, but they arrive unstyled. QGIS handles the rendering, so you bring your own cartography.

QGIS supports remote XYZ sources (`http://example.com/{z}/{x}/{y}.pbf`), local XYZ tile directories, and local MBTiles databases. To add one, open **Layer > Data Source Manager** and switch to the **Vector Tile** tab, then configure your connection.

If your tile service provides a Style URL, paste it when creating the connection — QGIS will apply the symbology automatically on load. Otherwise, open the layer's **Symbology** tab to build rules manually. Each rule targets a geometry type (Marker, Line, or Fill) and can be scoped to a specific sub-layer, a zoom range (**Min. Zoom** / **Max. Zoom**), and a filter expression.

Add rules with the **Add rule** button, choosing the symbol type that matches your features. Toggle **Visible rules only** to declutter the list at your current zoom, or type in the **Filter rules** box to search by label, layer, or expression.

Global layer rendering options sit at the bottom of the **Symbology** tab: **Opacity** (slider or percentage) and **Blending mode** for compositing effects against layers beneath.

To control when tiles appear on the canvas at all, use **Layer Properties > Rendering** and set **Maximum** and **Minimum** scale thresholds under **Scale dependent visibility**.

Styles can be saved as QML files or imported from MapBox GL JSON configs via the **Styles** menu at the bottom of the properties dialog — handy for sharing looks across projects or migrating from Mapbox-based workflows.
