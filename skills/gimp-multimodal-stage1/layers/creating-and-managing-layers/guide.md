# Creating and Managing Layers (GIMP 2.10)

Layers in GIMP work like a stack of transparent slides — each one holds part of your composition, and you can edit any layer without touching the others. The Layers dialog (usually docked on the right) is your home base for all of this.

To create a new layer, go to **Layer > New Layer…** and you'll get a dialog where you set the name, dimensions, and fill type (transparent, white, foreground color, etc.). The new layer lands just above whichever layer is currently active. You can also click the **New Layer** button at the bottom of the Layers dialog for the same result.

See `fig01.png`.

Duplicating a layer is even simpler — **Layer > Duplicate Layer** creates an identical copy (with " copy" appended to the name) right above the original. If the original is the background layer without an alpha channel, the duplicate gets one automatically.

To delete a layer you no longer need, select it and hit **Layer > Delete Layer**, or click the trash icon at the bottom of the Layers dialog. Gone, just like that.

Reordering layers changes what's on top and what's behind. Use **Layer > Stack > Raise Layer** and **Layer > Stack > Lower Layer** to nudge a layer up or down one position. For bigger jumps, **Layer to Top** and **Layer to Bottom** send it straight to either end of the stack. You can also just drag layers up and down in the Layers dialog.

See `fig02.png`.

When you want to combine layers, you have a few options. **Image > Merge Visible Layers…** (or **Ctrl+M**) collapses all layers with the eye icon turned on into one, giving you options for how the final layer should be sized — expanded to fit everything, clipped to the canvas, or clipped to the bottom layer. Hidden layers survive this operation unless you check **Discard invisible layers**.

For a more final collapse, **Image > Flatten Image** squashes everything — all layers, all transparency — into a single opaque layer. This is typically what you do right before exporting to a format like JPEG that doesn't support layers or transparency.

A couple of useful extras: click the eye icon next to a layer to toggle its visibility, and click between the eye and the thumbnail to enable the chain-link icon, which lets you group layers so they move and transform together. To quickly find which layer an element belongs to, hold **Alt** and click on it in the canvas.
