Now I have the full source material. Here's the guide:

# Editing Vector Geometry (QGIS 3.44)

To start editing any vector layer, right-click it in the Layers panel and choose **Toggle Editing**, or click the pencil icon on the digitizing toolbar. Vertex markers appear on all features once you're in edit mode.

**Adding features** is straightforward: activate **Add Point/Line/Polygon Feature**, left-click to place vertices, and right-click to finish. Press `Delete` to undo the last vertex mid-sketching. You can switch between **Digitize with Segment**, **Digitize with Curve** (`Ctrl+Shift+G`), and **Stream Digitizing** (`R`) while drawing a single feature.

**Snapping** keeps things precise — press `S` or click **Enable Snapping** on the Snapping toolbar. Set it to snap to Vertex, Segment, or both, and pick your tolerance (10–12 px works well). For shared boundaries, enable **Topological Editing** so moving a vertex updates all adjoining features. The **Tracing** tool (`T`) auto-follows existing edges between clicks.

The **Vertex Tool** lets you select vertices (click, box-drag, or `Alt`+polygon-select), then move, delete, or add them. Press `O` on a center vertex to toggle between curve and straight segments. Use `Shift+R` for batch selection along the shortest path.

**Reshape Features** redraws part of a line or polygon boundary — just draw a line that crosses the feature twice and right-click to finish. **Split Features** cuts a feature into independent rows by drawing a line across it. **Merge Selected Features** combines multiple geometries (and their attributes) into one multipart feature.

**Move**, **Rotate**, and **Scale Feature** tools work on selections. Hold `Ctrl` while rotating to set a custom pivot point, or `Shift` to snap to 45° increments. **Offset Curve** creates a parallel copy at a specified distance — hold `Ctrl` on the second click to keep the original.

For CAD-like precision, open the **Advanced Digitizing Panel** (`Ctrl+4`) and click the **Enable Advanced Digitizing Tools** button. Lock coordinates with `X`/`Y`, distance with `D`, and angle with `A`. Use `Shift+A` for angles relative to the last segment. **Construction mode** (`C`) lets you click reference points without placing real vertices.

The **Shape Digitizing toolbar** (**View > Toolbars > Shape Digitizing**) offers circles, ellipses, rectangles, and regular polygons as predefined shapes. **Trim/Extend** shortens or lengthens segments to meet a reference line — hold `Shift` on the reference to reuse it across multiple targets.

Save often with **Save Layer Edits** — edits live in memory until you commit. Use `Ctrl+Z` to undo any operation, and check the **Undo/Redo Panel** for full edit history.
