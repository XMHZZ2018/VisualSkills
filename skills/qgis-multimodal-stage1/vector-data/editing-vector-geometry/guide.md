# Editing Vector Geometry (QGIS 3.44)

To start editing any vector layer, right-click it in the Layers panel and choose **Toggle Editing**, or click the pencil icon on the digitizing toolbar. QGIS loads layers read-only by default, so you always have to opt in. Once in edit mode, vertex markers appear on your features and additional toolbar buttons light up. Save often with **Save Layer Edits** — edits live in memory until you do.

Before digitizing, configure snapping via **Project > Snapping Options...** or press `S` to toggle it on. You can snap to vertices, segments, centroids, or midpoints, and set tolerance in pixels (10–12 is a good default) or map units. Switch to **Advanced Configuration** mode to control snapping per layer, including scale limits. Enable **Topological Editing** on the snapping toolbar so shared boundaries between adjacent polygons move together automatically.

See `fig01.png`.

To add a feature, pick the appropriate tool — **Add Point Feature**, **Add Line Feature**, or **Add Polygon Feature** — then left-click to place vertices and right-click to finish. You can mix drawing methods on the fly: press `R` for freehand streaming, `Ctrl+Shift+G` for curves, or `T` to enable **Tracing**, which follows existing geometry edges between clicks. Press `Delete` to undo the last vertex while drawing. An attribute form pops up after you finish the geometry.

See `fig02.png`.

The **Vertex Tool** (current layer or all layers) lets you select, move, add, and delete individual vertices. Click a vertex to select it (hold `Shift` for multi-select, or drag a box), then drag to reposition. Double-click a segment while holding `Shift` to insert a new vertex, or select vertices and press `Delete` to remove them. Press `O` on a center vertex to convert straight segments to curves and back.

For reshaping existing geometry, the **Reshape Features** tool is your workhorse — draw a new line that crosses the feature boundary at least twice, and QGIS replaces the enclosed portion. **Split Features** works similarly: draw a cutting line across a polygon or line to break it into independent features. To combine features, select them and use **Merge Selected Features** — you'll get a dialog to choose how attribute values are resolved.

See `fig03.png`.

The **Advanced Digitizing Panel** (`Ctrl+4`) brings CAD-like precision. Lock exact coordinates by typing values for `x`, `y`, `d` (distance), or `a` (angle), then pressing `Enter`. Use `Shift+A` for angles relative to the previous segment, or toggle `Shift+X`/`Shift+Y` for coordinates relative to the last vertex. The **Parallel** and **Perpendicular** tools (`P` key) constrain your next segment to match an existing edge's orientation. Construction mode (`C`) lets you click reference points without actually placing vertices, handy for measuring offsets before committing.

Other useful advanced tools: **Add Ring** punches a hole in a polygon, **Add Part** extends a feature to multipart, **Offset Curve** creates a parallel copy at a set distance (hold `Ctrl` on the second click to keep the original), and **Trim/Extend** shortens or lengthens a segment to meet another. The **Shape Digitizing** toolbar provides ready-made circles, ellipses, rectangles, and regular polygons when you need precise geometry without manual vertex placement.

When you're done, click **Toggle Editing** again — QGIS asks whether to save or discard. For bulk geometry operations beyond what the toolbar offers, press **Edit Features In-Place** atop the Processing Toolbox to run algorithms directly on selected features without creating a new layer.
