# Cropping Images (GIMP 2.10)

The quickest way to crop is with the **Crop Tool**. Grab it from the Toolbox, via **Tools → Transform Tools → Crop**, or just press **Shift+C**. Click and drag on your image to draw a crop rectangle — don't worry about precision yet, since you can resize it afterward by dragging any edge or corner. Move the whole rectangle by clicking its center and dragging. When it looks right, press **Enter** or double-click inside the rectangle to commit.

In the Tool Options, check **Fixed** and set it to **Aspect ratio** if you need a specific proportion (type something like "1:1" or "16:9" in the box below). Enable **Allow growing** if your crop needs to extend beyond the current canvas — GIMP fills the extra space with transparency. The **Expand from center** option (or hold **Ctrl** while dragging) grows the rectangle outward from your initial click point.

By default, GIMP keeps the original canvas size after cropping. If you want the canvas trimmed to match, check **Delete cropped pixels** in the Tool Options. To crop only the active layer instead of the whole image, check **Current layer only**.

For automated approaches, **Image → Crop to Selection** trims the canvas to the bounding box of your current selection — handy after you've carefully selected your subject. **Image → Crop to Content** detects uniform-color borders and removes them automatically, similar to the old Autocrop.

**Image → Zealous Crop** goes further: it removes same-color strips not just at the edges but also from the interior of the image. Be careful with this one — it analyzes only the active layer but crops all layers, so you can lose data on other layers unexpectedly.

For compositional help while cropping, enable **View → Snap to Guides** and place guides where you want your crop boundaries. The **Auto Shrink** button in Tool Options will also snap the crop rectangle to the nearest sharp contrast edge it can find on the active layer.
