# Cropping Images (GIMP 2.10)

The Crop tool trims away the parts of an image you don't need — whether that's removing distracting borders, tightening the composition around a subject, or hitting a specific output size. It works across all layers by default.

Grab the tool from the Toolbox icon, from **Tools > Transform Tools > Crop**, or just press **Shift+C**. Then click and drag anywhere on the canvas to draw a crop rectangle. The area outside the rectangle darkens so you can preview what stays. Don't worry about precision on the first drag — you can resize by pulling any edge or corner, and reposition the whole rectangle by dragging from its center. The status bar updates dimensions and aspect ratio in real time as you adjust.

See `fig01.png`.

Once you're happy, press **Enter** or double-click inside the rectangle to commit. Arrow keys nudge the rectangle by one pixel (hold **Shift** for 25-pixel jumps). Hold **Ctrl** while dragging to expand from center; hold **Shift** to lock a fixed dimension.

In the Tool Options, check **Fixed** and set the dropdown to **Aspect ratio** if you need a specific proportion (type "1:1" for a square, for instance). Enable **Allow Growing** if you want the crop boundary to extend beyond the current canvas — GIMP fills the extra space with transparency. One gotcha: by default the canvas size doesn't shrink after cropping. Check **Delete cropped pixels** in Tool Options if you want the canvas trimmed to match.

For automated cropping, **Image > Crop to Selection** trims the canvas to the bounding box of your current selection — handy after making a careful selection of your subject. **Image > Crop to Content** detects uniform-color borders and removes them automatically, similar to the old "Autocrop" but smarter about multi-layer images.

**Image > Zealous Crop** goes further: it removes same-color strips not just at the edges but also from the interior of the image. Be cautious — it analyzes only the active layer but crops all layers, so you can lose content on other layers unexpectedly.

See `fig02.png` for the Zealous Crop before/after example.

The **Auto Shrink** button in the Crop Tool Options snaps your rectangle to the nearest sharp contrast edge on the active layer — useful for quickly fitting a crop around an isolated object on a clean background.
