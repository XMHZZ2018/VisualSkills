# Setting Labels (QGIS 3.44)

Labels let you display text on your map that symbols alone can't communicate — feature names, measurements, categories, whatever your data holds. You configure them through the **Labels** tab in **Layer Properties** (or via the **Layer Labeling Options** button on the Label toolbar).

The **Text** tab is your starting point: pick your font, set size and color, adjust opacity. If you enable **Allow HTML Formatting**, you can embed a subset of HTML/CSS directly in the label expression — bold, italic, colored spans, even inline images via `<img>` tags. The expression builder is where you wire up the field or formula that generates your label text.

Over in the **Formatting** tab you'll control line wrapping, case transforms (title case, all caps, small caps), letter and word spacing, text orientation, and multi-line alignment. Set a wrap character or a max line length and QGIS handles the rest. For line layers, you can also add direction symbols (left/right arrows) alongside curved or parallel labels.

See `fig01.png`.

To make labels pop against busy backgrounds, head to the **Buffer** tab and tick **Draw text buffer**. Set a size, color, and opacity — round join styles look cleanest in most situations. The **Background** tab goes further, letting you place a rectangle, ellipse, SVG, or marker symbol behind each label. The **Shadow** tab adds a drop shadow beneath any label component (text, buffer, or background) with configurable offset angle, blur radius, and opacity.

The **Mask** tab is powerful for dense maps: it carves out a clear zone around labels where specified layers won't draw, giving you separation without bloating a buffer. Enable the mask here, then reference it as a mask source in the overlapping layer's properties.

When labels collide with their features, **Callouts** connect displaced labels back to their origin with a line (straight, Manhattan, curved) or a speech-bubble balloon. Enable them in the **Callouts** tab and style the connector line or balloon fill just like any other symbol.

See `fig02.png`.

**Placement** varies by geometry type. For points, **Cartographic** mode follows best-practice rules (top-right preferred, then top-left, etc.) with configurable distance and maximum offset. For lines, choose **Parallel**, **Curved**, or **Horizontal** — curved labels follow the line's shape and you set a max angle between characters. For polygons, you have options like **Horizontal** or **Free (Angled)** inside the shape, **Offset from Centroid**, or labels along the **Perimeter**. Across all types, you can set label spacing margins, suppress duplicates within a minimum distance, assign priorities, and mark features as obstacles that other labels should avoid.

The **Rendering** tab controls visibility rules: scale-based limits, z-index ordering, and overlap handling. Set **Never overlap** for clean cartography at the cost of missing some labels, or **Allow overlaps if required** to guarantee coverage. Under **Feature options**, suppress labels for features smaller than a threshold, label every part of multi-part geometries, or merge connected lines to avoid repetition.
