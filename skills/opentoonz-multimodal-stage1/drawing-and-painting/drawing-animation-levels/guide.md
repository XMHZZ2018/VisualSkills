# Drawing Animation Levels (OpenToonz 1.7)

OpenToonz supports three level types for drawing: **Toonz Vector** (PLI, infinite resolution), **Toonz Raster** (TLV, bitmap with palette), and **Raster** (TIF sequence, bitmap with shared palette). Pick your default under **File > Preferences… > Drawing** in the **Default Level Type** dropdown — this also pre-fills Width, Height, and DPI for new raster-type levels.

To create a new level, select an empty Xsheet/Timeline cell and go to **Level > New > New Level…** (or right-click the cell and choose **New Level…**). Set the type, frame count, Step (how many cells each drawing holds), and Increment (numbering gap between drawings). The column header turns light yellow for vector, light green for Toonz Raster, or light blue for Raster levels.

If you'd rather skip the dialog entirely, set **Autocreation** to **Enabled** in Preferences — just pick an empty cell and start drawing. One step further: set it to **Use Xsheet as Animation Sheet** and you can work like a traditional animator, laying down keys first, then breakdowns, then inbetweens. New drawings inherit their number from the current frame, and holds fill automatically until the next drawing.

The **Brush** tool gives you freehand pressure-sensitive strokes. In its tool options bar, **Size Min/Max** controls thickness range (tablet pressure interpolates between them), **Accuracy** governs how faithfully the stroke follows your hand (vector only), and **Smooth** stabilizes jittery input. Enable **Break** on vector levels to auto-split strokes at sharp angles for easier filling. Save frequently-used combos with the **Preset +** button.

The **Geometric** tool draws rectangles, circles, ellipses, polygons, polylines, and arcs with a uniform thickness. Hold **Shift** while drawing a rectangle or ellipse for a regular shape (square/circle); hold **Alt** to draw from center. Toggle **Auto Group** so each closed shape lives on its own layer, preventing unwanted intersections.

For vector tweening, use the **Inbetween** command. Duplicate a key drawing in the Level Strip, modify it to create the second key, select the full frame range between them, and click the **INBETWEEN** bar that appears on the right. Choose an interpolation curve — **Linear**, **Ease In**, **Ease Out**, or **Ease In / Ease Out** — and OpenToonz generates the in-between drawings by interpolating stroke positions.

See `fig01.png`.

**Onion Skin** lets you see surrounding frames as ghosted overlays while drawing. Click the small diamond markers to the left of the Xsheet frame column to activate *relative* onion skin (follows the current frame), or click the fainter markers further left for *fixed* mode (always shows a specific frame). Customize transparency via **File > Preferences… > Onion Skin** — lower **Paper Thickness** makes ghosts more transparent, and you can tint previous/following frames with distinct colors. Right-click the Viewer and choose **Extend Onion Skin to Scene** to see all columns, not just the current level.

See `fig02.png`.

**Shift and Trace** simulates a light table for inbetweening. Enable it via **View > Shift and Trace** — the previous and next key drawings appear as references. Activate **View > Edit Shift** to reposition those references: drag inside a drawing's bounding box to move it, drag outside to rotate, drag corner handles to scale. You can also Ctrl-drag to sketch a path-of-action arc between reference points — the drawings auto-align along that arc. Toggle **View > No Shift** to flip back to the unshifted view and check your work, or **View > Reset Shift** to start positioning over.
