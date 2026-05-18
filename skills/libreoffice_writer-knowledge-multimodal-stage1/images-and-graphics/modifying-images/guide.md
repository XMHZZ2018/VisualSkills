# Modifying Images (LibreOffice Writer 7.3.7)

Writer comes with a surprisingly decent set of image-editing tools built right in. They won't replace GIMP for serious work, but for everyday tweaks — cropping, resizing, color adjustments — they do the job without ever leaving your document.

When you select an image, the **Image** toolbar appears (enable it permanently via **View > Toolbars > Image**). From here you can access filters, color adjustments, flip/rotate buttons, and a transparency slider. Two companion toolbars — the **Color** toolbar and the **Image Filter** toolbar — can be opened from it as well.

See `fig01.png`.

**Cropping** an image in Writer doesn't actually remove pixels — it just hides part of the image. The quickest way is to right-click the image, choose **Crop** from the context menu, then drag the crop handles that appear at the corners and midpoints. For precise control, right-click and select **Properties**, then go to the **Crop** tab. There you can enter exact values for **Left**, **Right**, **Top**, and **Bottom**. Two modes are available: **Keep scale** preserves proportions while changing the image size, and **Keep image size** maintains the dimensions but zooms in.

See `fig02.png`.

To **resize** an image, just drag its sizing handles. Hold **Shift** while dragging a corner handle to keep the original proportions. For exact dimensions, right-click the image, select **Properties**, and use either the **Crop** tab (scale percentages) or the **Type** tab (absolute width and height). On the Type tab, tick **Keep ratio** for symmetrical resizing, and use the **Original Size** button to revert any scaling.

**Rotating and flipping** is straightforward. Right-click the image and go to **Rotate or Flip** in the context menu — you'll find options for 90°, 180° rotations and vertical/horizontal flips. For arbitrary angles, right-click, choose **Properties**, open the **Image** tab, and type your desired angle in the **Rotation Angle** field. You can also rotate interactively: select the image, click the **Rotate** icon on the Image toolbar, then drag a rotation handle.

For **color and appearance** tweaks, use the Image toolbar's controls. The **Image Mode** dropdown lets you switch to grayscale, black-and-white, or watermark. The **Color** toolbar adjusts individual RGB channels plus brightness, contrast, and gamma. Various **Image Filters** — Smooth, Sharpen, Solarization, Aging, Posterize, and more — are available for quick special effects. If something goes wrong, just press **Ctrl+Z** to undo.

Bump up the **Transparency** percentage on the Image toolbar to make an image see-through — handy for watermarks or background images. And if you need to slim down your document's file size, right-click the image, choose **Compress**, and adjust quality or dimensions in the **Compress Image** dialog. Hit **Calculate New Size** to preview the savings before committing.
