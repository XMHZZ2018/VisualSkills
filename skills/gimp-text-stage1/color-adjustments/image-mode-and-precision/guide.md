# Image Mode and Precision (GIMP 2.10)

GIMP works in three color modes. You'll spend most of your time in **RGB** — it supports millions of colors and is required for most filters and tools. Switch modes via **Image → Mode** and pick **RGB**, **Grayscale**, or **Indexed**.

**Grayscale** strips your image down to shades of gray in a single channel. Useful for black-and-white work, but convert a copy — once saved, you lose the original color data.

**Indexed** limits the image to 256 colors or fewer, which keeps file sizes small (great for GIFs). When you select **Image → Mode → Indexed**, a dialog lets you generate an optimum palette, use a web-optimized palette, go pure black-and-white, or pick a custom palette. If smooth gradients look banded after conversion, enable one of the dithering options (Floyd-Steinberg usually works well). Note that many filters and tools are grayed out in Indexed mode — switch back to RGB if you need them.

To change bit depth, go to **Image → Precision**. You'll choose between 8-bit, 16-bit, or 32-bit, and between integer or floating point storage. For the highest quality editing, pick **32-bit floating point** with **Linear light** encoding — this matches GIMP's internal processing pipeline. If RAM is tight or layers are huge, **16-bit floating point** is a solid compromise. Stick with **8-bit integer** only on very constrained machines, and pair it with **Perceptual gamma (sRGB)** to avoid posterized shadows.

When dropping from 32-bit float down to 8-bit integer, GIMP will prompt you with dithering options for layers, text layers, and channels. Try converting without dithering first; add it only if you see banding artifacts. Skip dithering on text layers unless you're okay losing editability.

Regardless of what you set in the Precision menu, GIMP 2.10 does all internal math at 32-bit float — your choice only controls how data is held in RAM and written to disk.
