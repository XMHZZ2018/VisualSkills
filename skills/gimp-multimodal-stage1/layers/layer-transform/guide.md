# Transforming Layers (GIMP 2.10)

Every transform operation lives under **Layer > Transform**. This submenu acts on the active layer only — it won't touch other layers in your stack, so make sure you've selected the right one in the Layers dialog before you start.

<!-- figure: The Layer > Transform submenu showing all flip, rotate, and offset options -->

**Flipping** is the simplest operation here. **Layer > Transform > Flip Horizontally** mirrors the layer left-to-right; **Flip Vertically** mirrors it top-to-bottom. No dialog, no options — it just happens instantly.

For **rotation**, you get three fixed presets: **Rotate 90° clockwise**, **Rotate 90° counter-clockwise**, and **Rotate 180°**. These are lossless since pixels land on exact grid positions. If you need a non-right-angle rotation, use **Arbitrary Rotation…** instead — it opens the Rotate tool dialog on the active layer, where you can type a precise angle or drag interactively.

**Offset** (**Layer > Transform > Offset**, or **Shift+Ctrl+O**) shifts the layer's *content* within its boundary. Set X and Y pixel values to slide things around, or click **Offset by x/2, y/2** to push content to the center — this is the classic trick for making tileable patterns. Under Edge Behavior, choose *Wrap around* to loop content that slides off one edge back onto the other, *Fill with background color* to leave solid color behind, or *Make transparent* if the layer has an alpha channel.

To change a layer's dimensions without scaling its pixels, use **Layer > Layer Boundary Size**. This resizes the "canvas" of just that layer — content outside the new boundary gets cropped, and new areas come in transparent. Use the X/Y offset fields (or the **Center** button) to position the existing content within the new boundary. If you just want the layer boundary to match the image, **Layer > Layer to Image Size** does it in one click.

**Layer > Scale Layer** actually resamples the content — pixels get added or removed. In the dialog, set your target Width and Height (keep the chain icon linked to preserve aspect ratio). The Interpolation dropdown controls quality: *None* is fast but blocky, *Linear* is a solid default, *Cubic* is higher quality, and *Sinc (Lanczos3)* gives the best results at the cost of speed. Enlarging always introduces some blur; you can follow up with **Filters > Enhance > Sharpen (Unsharp Mask)** to recover a bit of crispness, but starting from a higher resolution is always better.
