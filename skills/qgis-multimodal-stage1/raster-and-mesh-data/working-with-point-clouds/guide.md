# Working with Point Clouds (QGIS 3.44)

Point clouds are massive 3D datasets — sometimes billions of points — captured by LiDAR or photogrammetry. Each point carries x/y/z coordinates plus attributes like intensity or color. QGIS handles EPT, LAS, and LAZ formats natively. When you first load a LAS/LAZ file, QGIS converts it to EPT in a subfolder (`ept_<filename>`) beside the original; subsequent loads skip this step entirely.

To bring in a point cloud, just drag the file into the canvas or use **Layer > Add Layer > Add Point Cloud Layer**. QGIS auto-selects a renderer based on what's in the data: RGB if color attributes exist, Classification if a `Classification` field is present, or a Z-based color ramp as a fallback.

Open the layer's properties (double-click it in the **Layers** panel) and head to the **Symbology** tab to change renderers. **Attribute by Ramp** maps a numeric attribute (Z, intensity, etc.) to a color gradient — set your min/max, pick an interpolation mode (Linear is usually what you want), and choose a color ramp. **RGB** assigns red/green/blue channels from matching attributes automatically. **Classification** colors points by category using ASPRS standard classes (ground, vegetation, buildings, etc.), and you can tweak each class's color, size, or visibility individually.

See `fig01.png`.

Under **Point Symbol**, control how big each dot renders (in pixels, mm, or map units) and whether it draws as a circle or square. Enable **Render as surface (Triangulate)** to fill gaps between points with interpolated triangles — handy for a continuous terrain look. Use **Skip triangles longer than** to punch holes where data is genuinely sparse.

The **Layer Rendering** section offers draw-order control (bottom-to-top gives you a true ortho look), a **Maximum error** slider that balances density against performance, and **Eye dome lighting** for quick depth shading without a full 3D view.

See `fig02.png`.

For 3D, switch to the **3D View** tab. Pick a rendering mode (or just **Follow 2D Symbology** to reuse your existing style), set a point budget so your GPU doesn't melt, and optionally triangulate in 3D as well. Bounding boxes can be toggled on for debugging tile hierarchies.

In the **Elevation** tab, apply a scale factor or offset to Z values — useful when combining datasets at different vertical datums. The **Profile Chart** settings here control how the layer appears in QGIS's elevation profile tool.

You can't edit point clouds directly in QGIS yet, but you can inspect any point with the **Identify** tool (since there's no attribute table for point clouds). For editing, reach for CloudCompare or PDAL on the command line.

For large tiled surveys, use a **Virtual Point Cloud (VPC)** — a lightweight JSON file (`.vpc`) that references your individual tiles and lets QGIS treat them as one seamless layer. Generate one with the **Processing > Build virtual point cloud (VPC)** algorithm. This eliminates the edge artefacts and per-tile styling headaches you'd otherwise fight.

The **Source** tab also exposes a **Provider Feature Filter** where you can write PDAL-style expressions to load only a subset (say, `Classification == 6` for buildings above a certain altitude) — filtered layers show a funnel icon in the Layers panel.

See `fig03.png`.

Finally, the **Statistics** tab gives a quick attribute summary — min, max, mean, standard deviation — plus a classification breakdown showing what percentage of points fall into each category. Great for sanity-checking unfamiliar datasets before you style them.
