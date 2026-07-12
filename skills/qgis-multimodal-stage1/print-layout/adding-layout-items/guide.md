Now I have sufficient information from the source material. The extracted markdown doesn't contain inline image references — it's a table of contents plus the full print layout overview. I'll write the reference guide based on this content.

# Adding Layout Items (QGIS 3.44)

To get started, open a print layout via **Project > New Print Layout** from the main QGIS window and give it a name. You'll land on a blank canvas — this is your composition surface.

All layout items live under the **Add Item** menu or on the left-side **Toolbox** toolbar. To place any item, select its tool (e.g., **Add Map**, **Add Legend**, **Add Scale Bar**) and then click-and-drag a rectangle on the canvas where you want it to appear. The item fills that rectangle immediately.

For a map, pick **Add Item > Add Map** and draw your rectangle — QGIS renders the current map canvas view inside it. You can have multiple map items on the same page or across pages, each with its own extent and scale. The first map placed becomes the layout's *reference map*, which other items (scale bars, legends, north arrows) automatically bind to.

A legend is added with **Add Item > Add Legend** — draw a box, and it auto-populates from visible layers. Scale bars (**Add Item > Add Scale Bar**) snap to the reference map's scale by default, or to whichever map they overlap. North arrows and pictures go through **Add Item > Add North Arrow** or **Add Item > Add Picture**.
For tabular data, use **Add Item > Add Attribute Table** (pulls attributes from a layer) or **Add Item > Add Fixed Table** (manually entered content). HTML frames (**Add Item > Add HTML**) let you embed rich content or even live URLs.

Once placed, click the **Select/Move Item** tool (`V`) to reposition or resize. Drag corner handles to scale; use the **Item Properties** panel on the right to fine-tune settings like rotation, exact coordinates, or linked map. Items dropped onto an existing map inherit that map's context — so a scale bar placed over an inset map reads that inset's scale, not the main map's.

You can group items with **Items > Group** (`Ctrl+G`), lock them in place with **Items > Lock Selected Items** (`Ctrl+L`), and reorder their stacking via **Items > Raise** / **Lower**. The **Items** panel on the right lists everything on the canvas and lets you toggle visibility or select items hidden behind others.
To remove any item, select it and press `Delete`. Undo/redo (`Ctrl+Z` / `Ctrl+Y`) works throughout, and the **Undo History** panel lets you jump back to any prior state.
