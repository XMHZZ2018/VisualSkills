# Threshold, Posterize, and Dither (GIMP 2.10)

These three filters under the **Colors** menu all reduce color information in different ways — from the extreme black-and-white of Threshold to the gentler color-reduction of Posterize and Dither. Pick whichever matches how aggressively you need to simplify.

**Threshold** converts your layer into pure black and white. Open it via **Colors > Threshold…** and you'll see a histogram of your image's tonal values. Drag the range sliders (or type values into the min/max boxes) to define which brightness values become white and which become black. Everything inside the range goes white; everything outside goes black. The **Channel** dropdown defaults to Value (all channels combined), but you can isolate Red, Green, Blue, or Luminance if that better separates your subject. Hit **Auto** for a quick starting point.

See `fig01.png`.

Threshold is great for cleaning up scanned text or creating selection masks. One useful trick: decompose your image into components with **Colors > Components > Decompose**, find the channel that best isolates your subject, then apply Threshold to that channel. Copy the result into a Quick Mask on your original image and you have a rough selection you can refine with painting tools.

**Posterize** is less extreme — it reduces colors per channel rather than flattening to two values. Open it with **Colors > Posterize…** and set the number of levels (2–256) for each RGB channel. A setting of 3 levels gives you up to 27 possible colors (3×3×3). The result looks like a stylized, flat-color version of your image. Lower values produce bold poster-art effects; higher values are subtler.

**Dither** goes a step further by applying a dithering algorithm while reducing levels, which fights the ugly banding that raw quantization produces. Find it at **Colors > Dither…** and set independent level counts for Red, Green, Blue, and Alpha channels. The key choice here is the dithering method: **Floyd-Steinberg** (the default) gives the smoothest results for most photos, **Bayer** produces a distinctive crosshatch pattern, and **Blue Noise** is considered the least visually distracting option. The random and arithmetic methods offer alternatives for specific artistic or technical needs.

See `fig02.png`.

One note on Threshold specifically: it kills anti-aliasing entirely. If you need a high-contrast adjustment that preserves smooth edges, reach for **Colors > Levels** instead and push the input sliders toward each other — you'll get a similar look without the jagged staircase edges.
