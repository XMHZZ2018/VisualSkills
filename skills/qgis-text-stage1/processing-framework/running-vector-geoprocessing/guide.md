# Running Vector Geoprocessing (QGIS 3.44)

All core vector geoprocessing tools live under **Vector → Geoprocessing Tools**. Open the one you need, pick your input and overlay layers, and the result lands in a new temporary layer by default — or save directly to file/GeoPackage.

**Buffer** creates a polygon zone at a fixed distance around any geometry. Set your distance, choose an end cap style (round, flat, square) and join style, then tick **Dissolve result** if you want overlapping buffers merged into one multipart feature. Use a negative distance on polygons to shrink them inward.

**Dissolve** merges features into fewer geometries. Leave the dissolve field(s) empty to collapse everything into a single multipart feature, or pick one or more attribute fields so only features sharing the same value get combined. Enable **Keep disjoint features separate** to avoid lumping non-touching parts into one multipart geometry.

**Clip** cuts an input layer to the shape of an overlay polygon — only portions inside the overlay survive. Think of it as a cookie cutter. **Intersection** is similar but also carries attributes from both layers into the output, giving you just the overlapping area with combined fields.

**Difference** is the inverse of clip: it keeps only the parts of the input that fall *outside* the overlay. **Symmetrical Difference** removes the overlap from both layers and returns what's unique to each side, with attributes from both.

**Union** splits features at every overlap boundary between input and overlay, keeping all portions and combining attribute tables. Where features overlap you'll get stacked geometries — each with the relevant attributes from both layers.

All these tools support saving results as temporary layers, files, GeoPackage, or database tables. They also work from the Processing Toolbox or Python console via `processing.run("native:buffer", {...})`, `native:clip`, `native:intersection`, `native:difference`, `native:symmetricaldifference`, `native:union`, and `native:dissolve`.
