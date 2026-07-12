# Transforming Layers (GIMP 2.10)

All flip and rotate commands live under **Layer → Transform**. **Flip Horizontally** and **Flip Vertically** mirror the active layer along the respective axis — no dialog, instant result.

For rotation, you get fixed presets: **Rotate 90° clockwise**, **Rotate 90° counter-clockwise**, and **Rotate 180°**. If you need a custom angle, choose **Arbitrary Rotation…** to type in an exact degree value.

**Offset** (**Layer → Transform → Offset**, or **Shift+Ctrl+O**) slides the layer's *content* without moving the layer itself. Set pixel values for X and Y, or click **Offset by x/2, y/2** to shift by exactly half the canvas — perfect for making tileable patterns. Under **Edge Behavior**, pick *Wrap around* to loop content seamlessly, *Fill with background color*, or *Make transparent*. Since GIMP 2.10.12 you can also click-and-drag directly on canvas to nudge the offset interactively.

To resize a layer without scaling its pixels, use **Layer → Layer Boundary Size**. This changes the layer's canvas area — use the X/Y offsets or the **Center** button to position existing content within the new boundary. If you just want the layer to match the image dimensions, **Layer → Layer to Image Size** does it in one click.

When you actually need to resize content, **Layer → Scale Layer…** opens a dialog for new Width and Height. Keep the chain icon linked to preserve aspect ratio. Choose an interpolation method: *None* is fast but blocky, *Linear* is a solid middle ground, *Cubic* is smoother, and *Sinc (Lanczos3)* gives the highest quality. Scaling up always softens detail — follow with **Filters → Enhance → Sharpen (Unsharp Mask)** if needed.
