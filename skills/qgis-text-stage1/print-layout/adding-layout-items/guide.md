The markdown file is essentially a table of contents with no inline images. It lists the layout item types available in QGIS 3.44's print layout. I have enough context from this source to write the reference guide.

# Adding Layout Items (QGIS 3.44)

Once your print layout is open, you add items by grabbing them from the **Add Item** menu or the left-side toolbar. Click the tool, then click-and-drag a rectangle on the canvas where you want the item to appear — that's it for placement.

**Maps** are the centerpiece. Use **Add Item > Add Map**, draw the rectangle, and the current map canvas content fills it. You can have multiple map items (e.g., an overview inset) each locked to different extents or CRS settings.

For a **legend**, go **Add Item > Add Legend**. It auto-links to a map item and pulls in all visible layers. In the Item Properties panel, uncheck **Auto update** if you want to curate which entries appear, reorder them, or rename labels.

**Scale bars** (**Add Item > Add Scale Bar**) attach to a specific map item. Pick your style (single box, double box, numeric) and units from the properties panel — it updates live as you resize or re-zoom the linked map.

**Tables** come in two flavors: attribute tables that pull feature data from a layer, and fixed/manual tables for custom content. Add them via **Add Item > Add Attribute Table** or **Add Item > Add Fixed Table**, then configure which columns and rows to show.

**Pictures and north arrows** live under **Add Item > Add Picture** (raster/SVG) or **Add Item > Add North Arrow** (preloaded directional symbols). Point the picture item at a file path or pick from the built-in SVG library. A **Marker** item works similarly but uses map symbol styling.

After placing any item, switch back to the **Select/Move Item** tool (white arrow, top of the toolbar) to reposition or resize. Fine-tune position, size, rotation, and frame settings in the **Item Properties** panel on the right.
