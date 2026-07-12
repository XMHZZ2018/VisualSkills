# Layer Masks (GIMP 2.10)

A layer mask controls which parts of a layer are opaque, semi-transparent, or fully transparent — without ever destroying pixel data. Think of it as a grayscale stencil: white reveals, black hides, and gray values give you partial transparency. Because the mask lives alongside the layer rather than altering it directly, you can always revise or remove it later.

To add a mask, go to **Layer > Mask > Add Layer Mask**. A dialog appears offering several initialization options. "White (full opacity)" keeps everything visible so you can paint away what you want hidden. "Black (full transparency)" hides the entire layer, letting you paint in what you want revealed. You can also seed the mask from the current selection, the layer's own alpha channel, or a grayscale copy of the layer content. Check **Invert Mask** at the bottom of the dialog to flip whichever option you chose.

See `fig01.png`.

Once the mask exists, its thumbnail appears to the right of the layer thumbnail in the Layers panel. To paint on the mask, make sure it's the active target — go to **Layer > Mask > Edit Layer Mask** (a check mark appears next to it) or simply click the mask thumbnail in the Layers panel. Now any brush work in white reveals the layer, black conceals it, and grays blend in between.

If you want to see the raw mask itself on canvas (handy for spotting missed edges), toggle **Layer > Mask > Show Layer Mask**. To temporarily disable a mask's effect without deleting it, use **Layer > Mask > Disable Layer Mask** — the canvas shows the layer as if no mask exists, but the mask data stays intact.

When you're satisfied and want to commit the transparency permanently into the layer's alpha channel, choose **Layer > Mask > Apply Layer Mask**. This merges the mask into the layer and removes it. If you'd rather throw it away entirely and restore the layer to its unmasked state, use **Layer > Mask > Delete Layer Mask** instead.

You can also convert a mask into a selection. **Layer > Mask > Mask to Selection** replaces the current selection with one derived from the mask's white areas; gray areas become feathered edges. Related commands let you add, subtract, or intersect the mask with an existing selection.

See `fig02.png`.
