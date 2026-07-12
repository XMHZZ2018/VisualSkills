# Channel Mixer and Components (GIMP 2.10)

Everything lives under **Colors > Components**. This submenu is your toolkit for pulling apart an image's color channels, tweaking them individually, and putting them back together — whether you're doing creative color grading or preparing files for print.

See `fig01.png`.

**Channel Mixer** (**Colors > Components > Channel Mixer**) lets you rebalance how much each input channel (Red, Green, Blue) contributes to each output channel. By default, every output channel draws 100% from its matching input (the slider sits at 1.0, the others at 0.0). Drag any slider between −2 and +2 to blend channels — bumping the Green slider up on the Red output channel, for instance, pushes reds toward warmer tones. If the result clips highlights or looks blown out, tick **Preserve Luminosity** to keep overall brightness in check while still shifting the color balance.

**Extract Component** (**Colors > Components > Extract Component**) pulls a single channel out of your image and renders it as grayscale. Pick the component you want — RGB Red, Green, Blue, or values from HSV, HSL, CMYK, LAB, and more — and the filter maps that component's intensity to a gray image. Handy when you need a luminosity mask or want to isolate saturation for retouching.

**Decompose** (**Colors > Components > Decompose**) splits the entire image into all channels of a chosen color model at once. Select a model (RGB, HSV, HSL, CMYK, LAB, LCH, YCbCr variants) and decide whether to output separate images or separate layers within one image — **Decompose to Layers** checked keeps things tidy in a single file. This only works on RGB-mode images. For print workflows, the **Foreground as registration color** option stamps crop marks across all CMYK plates for alignment.

**Compose** (**Colors > Components > Compose**) does the reverse: it reassembles grayscale layers or images back into a full-color image. It's available when your active image is grayscale. Choose a target color space, then assign which layer feeds each channel slot. You can even swap channels around here — assigning the Red layer to the Blue slot and vice versa — for dramatic color shifts. A fun trick: decompose as RGB, then recompose as LAB for unexpected color effects.

**Recompose** (**Colors > Components > Recompose**) is the shortcut for round-trip editing. After you Decompose an image, tweak individual channel layers (curves, levels, painting), then hit Recompose to rebuild the original without manually re-assigning channels.

The typical workflow: Decompose your image, edit the grayscale channel layers to taste (boost contrast on the L channel, desaturate via the Saturation layer, paint on a mask), then Recompose. Channel Mixer is faster for simple cross-channel blending; Decompose/Compose gives you full per-channel editing freedom.
