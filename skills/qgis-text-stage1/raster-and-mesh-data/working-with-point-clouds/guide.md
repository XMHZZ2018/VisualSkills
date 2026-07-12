# Working with Point Clouds (QGIS 3.44)

QGIS natively handles LiDAR and other point cloud data in EPT, LAS, and LAZ formats. Just drag a `.las` or `.laz` file into the canvas — QGIS converts it to indexed EPT on first load (stored alongside the original as `ept_<filename>`), so subsequent opens are fast.

To inspect layer details, double-click the layer or go to **Layer > Layer Properties…**. The **Information** tab gives you a quick summary of extent, point count, CRS, and metadata. The **Statistics** tab shows min/max/mean/stddev for every attribute — handy for understanding what you're working with before styling.

For rendering, open the **Symbology** tab. QGIS auto-picks a renderer: **RGB** if red/green/blue attributes exist, **Classification** if there's a `Classification` field, or **Attribute by Ramp** (coloring by Z) as fallback. Switch renderers via the dropdown at the top. Under **Point Symbol**, set size and shape (circle or square). Enable **Render as surface (Triangulate)** to fill gaps with interpolated triangles — use **Skip triangles longer than** to reveal actual holes in coverage.

The **Layer Rendering** section controls draw order (bottom-to-top mimics true ortho), **Maximum error** (point density vs. performance), opacity, and **Eye dome lighting** for better depth perception in 2D views.

For 3D, configure the **3D View** tab with the same renderer options plus a point budget cap. The **Elevation** tab lets you apply a scale factor or offset to Z values, useful when combining datasets at different vertical datums.

To filter points, use **Source > Provider Feature Filter** — build expressions against any attribute (e.g., `Classification = 6` for buildings). Filtered layers show a filter icon in the **Layers** panel.

For large tiled datasets, use a **Virtual Point Cloud** (`.vpc`). Create one via **Processing > Build virtual point cloud (VPC)**, then load the single VPC file instead of dozens of tiles — QGIS handles seamless display and consistent styling across all tiles automatically.
