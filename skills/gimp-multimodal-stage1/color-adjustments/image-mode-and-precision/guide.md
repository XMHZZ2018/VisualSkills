# Image Mode and Precision (GIMP 2.10)

Every image in GIMP lives in one of three color modes — RGB, Grayscale, or Indexed — and at a chosen bit depth. You switch between them via **Image > Mode** for color modes, or **Image > Precision** for bit depth and channel encoding.

<!-- figure: The Image > Mode submenu showing RGB, Grayscale, and Indexed options -->

**RGB** is your default working mode. It gives you millions of colors and full access to every filter and tool. If you ever find menu items grayed out, chances are you're in Indexed or Grayscale — flip back to RGB via **Image > Mode > RGB** and the options reappear.

**Grayscale** (**Image > Mode > Grayscale**) reduces the image to a single luminance channel — shades of gray from black to white. The number of tonal steps depends on your precision setting: 255 at 8-bit integer, 65535 at 16-bit. Useful for black-and-white photography or prepress work, but many filters won't be available.

**Indexed** (**Image > Mode > Indexed**) limits the palette to 256 colors or fewer — the classic GIF workflow. When you convert, a dialog lets you choose palette generation: generate an optimum palette, use a web-optimized one, go pure black-and-white, or pick a custom palette. If smooth gradients look banded after conversion, enable one of the dithering options (Floyd-Steinberg works well for stills; Positioned Color Dithering suits animations). Be aware that converting to Indexed and saving means you lose the original color data, so work on a copy.

For **precision**, open **Image > Precision**. You'll see bit-depth choices (8-bit, 16-bit, 32-bit) in both integer and floating-point variants, plus a channel encoding toggle between **Perceptual gamma (sRGB)** and **Linear light**. Internally, GIMP 2.10 processes everything at 32-bit float regardless of what you pick here — the setting controls how data is stored in RAM.

The practical advice: for maximum quality, choose **32-bit floating point** with **Linear light**. If RAM is tight or layers are huge, drop to 16-bit float or integer. Stick with **Perceptual gamma (sRGB)** at 8-bit — linear encoding at 8-bit produces ugly posterized shadows. Also switch to Perceptual gamma before soft proofing, since the gamut check misbehaves in linear mode.

When converting from 32-bit float down to 8-bit integer, GIMP shows a conversion dialog offering dithering options for layers, text layers, and channels separately. Try without dithering first; add it only if you see banding. Skip dithering on text layers unless you're okay losing editability.
