# Setting Labels (QGIS 3.44)

Open labeling from the **Labels** tab in **Layer Properties**, the **Layer Styling** panel, or the **Layer Labeling Options** button on the Label toolbar. Pick the field or expression that supplies your label text.

In the **Text** tab, set font, size, color, and opacity. Enable **Allow HTML Formatting** to use inline HTML/CSS — bold, italic, colored spans, even embedded images via `<img src="...">` tags. The **Formatting** tab handles capitalization (type case), letter/word spacing, line wrapping characters, line height, and multi-line alignment. Set orientation to horizontal, vertical, or rotation-based for line-following labels.

Add a **Buffer** to halo text against busy backgrounds — configure size, color, opacity, and join style. The **Background** tab places a shape (rectangle, ellipse, SVG, or marker symbol) behind each label with configurable size, offset, rotation, and corner radius. **Shadow** adds a drop shadow beneath any label component with angle, distance, blur, and blend mode controls.

For placement, point layers offer **Cartographic** (rule-based offsets with position priority), **Around Point**, or **Offset from Point**. Line layers support **Parallel**, **Curved**, or **Horizontal**, with repeating-label distance and anchor position settings. Polygon layers get options like **Offset from Centroid**, **Horizontal**, **Free (Angled)**, and **Using Perimeter** (including curved). Set **Priority** to rank which labels win contested space, and mark features as **Obstacles** to repel labels from important geometry.

Use **Callouts** when labels must be displaced — choose simple lines, Manhattan, curved, or balloon connectors linking the label back to its feature. The **Mask** tab carves out an area around labels where specified layers won't draw, improving legibility without buffers.

In the **Rendering** tab, control scale-based visibility, z-index stacking, and overlap behavior (never overlap, allow if required, or allow without penalty). Under feature options, suppress labels on features smaller than a threshold, label every part of multi-part geometries, or merge connected lines to deduplicate.
