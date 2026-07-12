# Running Vector Geoprocessing (QGIS 3.44)

All the core vector geoprocessing tools live under **Vector > Geoprocessing Tools**. Open any of them and you'll get a dialog where you pick an input layer, set parameters, and choose where to save the result — a temporary layer, GeoPackage, file, or database table.

**Buffer** creates a polygon zone at a fixed distance around every feature in your layer. Head to **Vector > Geoprocessing Tools > Buffer**, set your **Distance** (negative values shrink polygons inward), choose an **End cap style** (round, flat, or square) and a **Join style** (round, miter, or bevel). Tick **Dissolve result** if you want overlapping buffers merged into a single multipart feature. You can also drive the distance from a field for per-feature control.

See `fig01.png`.

**Dissolve** merges features that share a common attribute value — or all features at once — into multipart geometries. Open it from the same **Vector > Geoprocessing Tools** menu, optionally pick one or more **Dissolve field(s)**, and adjacent polygon boundaries disappear. Enable **Keep disjoint features separate** if you don't want disconnected pieces lumped into one multipart feature.

**Clip** trims an input layer to the extent of an overlay polygon layer — only the portions that fall inside the overlay are kept. Think of it as a cookie cutter. The attribute values stay untouched, though derived properties like area will obviously change, so update those manually if they're stored as fields.

**Intersection** is the flip side: it extracts the overlapping portions between your input and an overlay layer, and the output inherits attributes from *both* layers. This is handy when you need to know which parcel falls inside which zoning boundary, for example.

**Difference** does the opposite — it removes the overlapping parts and keeps only what's outside the overlay. **Symmetrical difference** keeps everything from both layers *except* the overlap, giving you a layer of non-shared areas with attributes from both sources.

**Union** combines two layers completely: features get split at every intersection, and every resulting piece carries attributes from whichever layer(s) it belonged to. Note that features on the same layer won't split each other in a single pass — run it again on the output if you need that.

For quick spatial subsetting without a polygon mask, **Extract/clip by extent** lets you draw a bounding box or pick one from a bookmark, layout, or coordinates, and pulls out (or clips) features within that rectangle.

All these tools are also accessible from the Processing Toolbox and callable from Python with `processing.run("native:buffer", {...})` and friends — hover over an algorithm name in the toolbox to see its ID.
