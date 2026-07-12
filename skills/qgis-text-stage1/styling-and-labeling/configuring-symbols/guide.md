# Configuring Symbols (QGIS 3.44)

The Symbol Selector is where you build marker, line, and fill symbols. Open it from a layer's symbology properties — you'll see a **symbol layer tree** on the left and configuration options on the right. The tree lets you stack multiple layers to compose complex symbols; add, remove, reorder, duplicate, or lock colors on any layer.

At the top level, set global properties: **Unit** (Millimeters, Points, Pixels, Map units, etc.), **Opacity**, **Color**, and — for markers — **Size** and **Rotation**, or for lines, **Width**. Changing the top-level color cascades to all unlocked sub-layers. Use the **Save Symbol** button to store your creation in the style library with a name and tags.

**Marker symbols** support layer types like Simple marker, SVG marker, Font marker, Raster image marker, Ellipse marker, Filled marker, and Geometry generator. Simple markers give you control over fill color, stroke style, join/cap style, rotation, offset, and anchor point.

**Line symbols** offer Simple line, Arrow, Marker line, Hashed line, Interpolated line, Lineburst, Filled line, Raster line, and Linear referencing types. Simple lines support custom dash patterns, pattern offsets, line trimming from start/end, and corner-aware dash adjustments via **Tweak dash pattern at sharp corners**.

**Fill symbols** split into interior types (Simple fill, Gradient fill, Shapeburst fill, Line/Point pattern fill, Random marker fill, SVG fill, Raster image fill) and outline types that reuse any line symbol for the polygon boundary. Under **Advanced**, you can clip features to canvas, force right-hand ring orientation, or add a buffer halo around markers.

For dynamic styling, use **Geometry generator** layers — write an expression like `buffer($geometry, 100)` or `centroid($geometry)` and QGIS renders it on the fly regardless of the original geometry type. SVG symbols can be parametrized with `param(fill)`, `param(outline)`, etc., and controlled via the **Dynamic SVG parameters** table.
