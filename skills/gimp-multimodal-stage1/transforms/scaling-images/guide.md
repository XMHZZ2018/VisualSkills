# Scaling Images (GIMP 2.10)

Open your image and head to **Image > Scale Image…** to bring up the Scale Image dialog. This is the go-to command when you need to resize the entire image — all layers, the canvas, everything gets resampled together.

See `fig01.png`.

The dialog has two main sections. Up top you'll find **Width** and **Height** fields — these control the pixel dimensions of your image. A chain-link icon sits between them; while it's connected, changing one dimension automatically adjusts the other to keep proportions intact. Click the chain to break it if you deliberately want to stretch or squash, but that's rarely what you want.

Below that are **X resolution** and **Y resolution** fields. These only matter for print output — they tell printers how many pixels to pack per inch. For anything destined for a screen (web, email, social media), you can ignore resolution entirely and just work in pixels.

For screen use, pick a pixel width that suits your target: 600–800 px is a solid range for web images, 1920 px for full HD displays. Type the value into the **Width** field and let the chain handle the height.

Under **Quality**, choose an **Interpolation** method. **Cubic** is the default and works well for most cases — it produces smooth results when scaling down. If you're making an image larger, know that no interpolation method can invent detail that isn't there; the image will soften. You can recover some sharpness afterward with **Filters > Enhance > Unsharp Mask**.

Hit **Scale** when you're happy with the settings, and the deed is done.

If you only need to resize a single layer rather than the whole image, use the **Scale** tool instead (**Shift+S**, or **Tools > Transform Tools > Scale**). Click the layer, drag the corner handles, and confirm in the floating adjustment dialog. Hold **Shift** to lock the aspect ratio while dragging.

One thing to keep in mind: scaling down is almost always safe, but scaling up degrades quality. Capture at the resolution you need whenever possible — resampling is a compromise, not a substitute for source resolution.
