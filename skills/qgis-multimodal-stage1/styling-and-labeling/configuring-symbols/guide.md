# Configuring Symbols (QGIS 3.44)

The Symbol Selector is your main workspace for building marker, line, and fill symbols. Open it from any layer's symbology properties, and you'll see two panels: a **symbol layer tree** on the left showing stacked sub-layers, and **settings** for whichever layer you've selected on the right.

Symbols are composed of one or more symbol layers that stack on top of each other. Use the toolbar beside the tree to add, remove, duplicate, reorder, or lock colors on individual layers. Locking a layer's color means it won't change when you adjust the global symbol color above — handy when you want a fixed outline but a user-switchable fill.

See `fig01.png`.

At the top level of the tree, set global properties: **Unit** (Millimeters, Points, Pixels, Map units, etc.), **Opacity**, **Color**, and — for markers — **Size** and **Rotation** (or **Width** for lines). Changing size or width here scales all sub-layers proportionally.

**Marker symbols** default to a Simple marker with configurable fill color, stroke, join/cap style, rotation, and offset. You can swap the layer type to SVG marker, Font marker, Raster image marker, Ellipse, Filled marker (which accepts any fill sub-symbol like gradients), or even an Animated marker (`.GIF`/`.WebP`) for temporal maps. SVG markers support dynamic parameters — use `param(fill)`, `param(outline)`, etc. in your SVG source so QGIS can recolor them on the fly.

**Line symbols** start as a Simple line — set dash patterns, trim distances from start/end, and corner-tweaking options. For fancier effects, switch to Arrow (curved or straight, single/double-headed), Marker line (repeats a marker at intervals or vertices), Hashed line (short perpendicular ticks), Interpolated line (width or color varies along the geometry), Lineburst (gradient across the stroke width), or Raster line.

**Fill symbols** cover polygon interiors and outlines separately. Interior types include Simple fill, Gradient fill, Shapeburst (boundary-to-center gradient), Line pattern fill (hatching), Point pattern fill (grid of markers with optional randomization), Random marker fill, SVG fill, and Raster image fill. Outline types mirror the line symbol options — Outline: Simple line, Outline: Marker line, Outline: Arrow, etc. — applied to exterior rings, interior rings, or both.

See `fig02.png`.

The **Geometry Generator** layer type is available for all symbol categories and lets you write an expression (like `buffer($geometry, 100)` or `centroid($geometry)`) that produces a new geometry at render time. The output geometry type doesn't need to match the original layer — so you can render point markers on a polygon centroid or draw buffers around lines.

Under the **Advanced** dropdown at the symbol level, you'll find **Clip features to canvas extent**, **Force right-hand rule** (for consistent polygon orientation), **Buffer settings** (halo around markers), and **Symbol levels** (control draw order across overlapping features).

To save a finished symbol for reuse, hit **Save Symbol**, choose a destination library, give it a name and tags, and optionally mark it as a favorite. You can browse and filter the symbol library from the preview panel below the settings — toggle between **List View** and **Icon View** as you like.
