# Image Composition & Grouping (LibreOffice Impress 7.3.7)

To move an image, click it to show selection handles, then hover until the cursor becomes a clenched hand and drag it into position. Resize by dragging any selection handle — corner handles scale width and height together, while side handles adjust only one dimension. Hold **Shift+Click** on a handle before dragging to keep the original proportions.

To rotate an image, enter rotation mode by clicking **Rotate** on the **Drawing** toolbar, or simply click again on an already-selected handle. The handles change color and shape. Drag a corner handle to rotate freely, or use the left/right handles to slant and the top/bottom handles to skew. The central handle is the rotation point — drag it to change the pivot. Hold **Shift** while rotating to snap to 15-degree increments.

For quick image adjustments, select the image and open the **Image** toolbar via **View > Toolbars > Image**. Click **Filter** to reveal the **Image Filter** toolbar, or go to **Format > Image > Filter** to apply a filter with default settings. **Invert** flips color values, **Smooth** softens with a blur, and **Sharpen** increases edge contrast — apply **Sharpen** multiple times to strengthen the effect.

To temporarily group objects, hold **Shift** and click each one, or drag a marquee around them. This lets you move or rotate them as a unit, but clicking elsewhere dissolves the selection. For a permanent group, select the objects and go to **Format > Group > Group** (or press **Ctrl+Shift+G**). You can also right-click and choose **Group** from the context menu. To select everything on a slide first, use **Edit > Select All** (**Ctrl+A**).

Need to tweak one object inside a group? Press **F3** or go to **Format > Group > Enter Group** to dive in. Edit or format individual pieces, then press **Ctrl+F3** or use **Format > Group > Exit Group** to step back out.

To ungroup permanently, select the group and choose **Format > Group > Ungroup** (**Ctrl+Alt+Shift+G**), or right-click and select **Ungroup**. Each object becomes independently selectable again.

When overlapping objects, use click-and-drag positioning to layer them as desired. A ghost image appears during the drag to help with placement, and you can nudge selected objects with the arrow keys for fine adjustments.

## Target mockup: polaroid photo stack

A "polaroid pile" composition is a classic pattern — see `polaroid_stack_target.jpg`. Three or four photos, each wrapped in a white rectangle with a thick bottom border (the polaroid frame), slightly overlapping, each rotated a few degrees (roughly −15°, 0°, +15°). The most important thing is to **get the photo in first**, then frame it — not the other way around. If you spend the task budget building empty rectangles, the photos never get inserted and the task fails outright.

A fast recipe:
1. **Insert > Image…** to place the first photo.
2. Resize it to the target photo area (not the full polaroid — leave room for the white border).
3. Draw a white rectangle behind it (**Arrange > Send to Back**) slightly larger on the left/right/top and noticeably larger on the bottom to form the white border.
4. Select photo + rectangle and group them (**Ctrl+Shift+G**) — this is one polaroid.
5. Duplicate the group with **Ctrl+D**, swap in the next photo via **Format > Area > Bitmap** or by deleting and re-inserting inside the group.
6. Rotate each group: select it, press **F4**, set **Rotation Angle** on the Rotation tab.

Budget the time: the three photos must all land on the slide well before the halfway point of the task. If you're still styling the first rectangle and no image is on the slide yet, abandon the pixel-perfect border and insert the remaining photos first.
