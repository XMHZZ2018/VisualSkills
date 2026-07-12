# Tools Not Working as Expected (GIMP 2.10)

When a tool suddenly stops doing anything visible, resist the urge to reinstall — the problem is almost always a stray setting or layer state. Here are the most common culprits and how to fix them fast.

**Floating selection blocking everything.** If most actions are greyed out or unresponsive, open the Layers dialog (**Ctrl+L**) and check whether the top entry says "Floating Selection." Until you deal with it, GIMP locks out nearly everything else. Either anchor it to the layer below with **Ctrl+H**, or promote it to its own layer with **Shift+Ctrl+N** by right-clicking the floating selection in the Layers dialog.

See `fig01.png`.

**Brush or eraser paints nothing.** The first thing to check is the **Tool Options** dock — make sure Opacity isn't dragged down to 0. That single slider is responsible for more confusion than any other setting. If opacity looks fine, open the **Brush Dialog** and see which brush is selected. If you accidentally chose the Clipboard Brush and haven't copied anything yet, it's literally an empty rectangle — just pick a normal brush and you're back in business.

**Move or transform tool has no effect.** Glance at the status bar at the bottom of the image window for clues, then look at the **Tool Options** for your transform tool. Near the top you'll see small toggle buttons for Layer, Selection, and Path. If the tool is set to transform a Selection or Path rather than the layer content, nothing visible will change on canvas. Switch it back to Layer mode.

**Eraser paints the background color instead of transparency.** Your layer doesn't have an alpha channel. Right-click the layer in the **Layers Dialog** and choose **Add Alpha Channel** — if that menu item is clickable, that's your problem. Once added, the eraser will properly reveal transparency.

**Brush produces unexpected colors.** You might be painting on a Layer Mask rather than the layer itself. In the Layers dialog, click the layer thumbnail (not the white/black mask thumbnail beside it) to redirect paint strokes to the actual image data. Similarly, check you haven't accidentally activated a Channel instead of a Layer — clicking any layer in the Layers dialog will fix that.

**Crop tool leaves empty space around the image.** After cropping, the canvas stays at its original size with blank area visible. Open the Crop tool's **Tool Options** and enable **Delete cropped pixels** so the canvas shrinks to match your crop boundary.
