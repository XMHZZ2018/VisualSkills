# Threshold, Posterize, and Dither (GIMP 2.10)

All three live under the **Colors** menu and reduce color complexity — but each does it differently.

**Threshold** (**Colors > Threshold…**) converts your image to pure black and white. The dialog shows a histogram; drag the two input values or click-drag directly on the graph to set which intensity range becomes white (everything else goes black). The **Channel** dropdown defaults to Value (all channels combined) but you can target Red, Green, Blue, Luminance, or Alpha individually. Hit **Auto** for a quick starting point, then fine-tune. This is great for cleaning up scanned text or building selection masks via Quick Mask.

**Posterize** (**Colors > Posterize…**) keeps your image in color but crushes it down to fewer levels per channel. Set **Posterize Levels** between 2 and 256 — that's the number of distinct values each RGB channel can hold. A level of 3 means up to 27 total colors (3³). Low values give a bold, flat, pop-art look; higher values are subtler.

**Dither** (**Colors > Dither…**) also reduces levels per channel, but compensates with a dithering pattern so gradients don't turn into ugly banding. You get independent sliders for **Red levels**, **Green levels**, **Blue levels**, and **Alpha levels**. The key choice is the **Dithering method**: **Floyd-Steinberg** (default, smooth error diffusion), **Bayer** (visible crosshatch pattern), **Random** (noisy), various **Arithmetic** options (spatially stable), or **Blue Noise** (least distracting to the eye). If you're using a random method, tweak the **Random seed** or click **New Seed** for a different result.

As a rule of thumb: use Threshold when you want a hard black/white mask, Posterize for a stylized flat-color effect, and Dither when you need fewer colors but want to preserve the illusion of smooth tones.
