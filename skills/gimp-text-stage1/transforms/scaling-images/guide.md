# Scaling Images (GIMP 2.10)

Open your image and head to **Image > Scale Image…** to bring up the Scale Image dialog. This is where you control the pixel dimensions of your entire image — all layers scale together.

The dialog shows **Width** and **Height** fields at the top. Type your target size in pixels — for web use, something between 600 and 800 pixels wide is a solid choice. The chain icon between the fields keeps proportions locked by default, so changing one dimension automatically adjusts the other. Click the chain to break it if you intentionally want to stretch or squash (you usually don't).

Below the dimensions you'll find **X resolution** and **Y resolution**. These only matter for print output — they have zero effect on how the image appears on screen. For print, set these to match your printer's expectations (typically 300 pixels/in for quality output).

Under **Quality**, pick an **Interpolation** method. **Cubic** is the default and works well for most cases. This determines how GIMP invents new pixels when enlarging or blends them when shrinking.

Hit **Scale** when you're happy. Keep in mind that scaling up always introduces blur — GIMP interpolates missing detail but can't invent it. You can sharpen afterward with **Filters > Enhance > Unsharp Mask**, but starting with a high-resolution source is always better.

If you only need to resize a single layer rather than the whole canvas, use the **Scale Tool** instead (**Shift+S**). Click the layer, drag the corner handles, and confirm in the floating dialog. Hold **Shift** to lock the aspect ratio, or **Ctrl** to scale from center.
