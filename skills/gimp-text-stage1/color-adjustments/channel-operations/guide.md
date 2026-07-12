# Channel Mixer and Components (GIMP 2.10)

Everything lives under **Colors → Components**. This submenu is your toolkit for pulling apart and reassembling color channels — whether you're fine-tuning RGB balance, extracting a single component as grayscale, or splitting an image into an entirely different color model.

**Channel Mixer** (**Colors → Components → Channel Mixer**) lets you control how much each input channel (Red, Green, Blue) contributes to each output channel. Sliders range from -2 to +2, where 1.0 means "use 100% of that input." Want warmer highlights? Bump the Green slider up on the Red output channel. Check **Preserve Luminosity** to keep overall brightness stable while you shift the color balance — it scales values down so nothing clips to white.

**Extract Component** (**Colors → Components → Extract Component…**) pulls a single channel out of your image as a grayscale layer. Pick any component — RGB Red, HSV Saturation, LAB Lightness, etc. — from the dropdown. Enable **Invert** to flip the result, or **Linear input** to bypass gamma correction. Handy for building masks from specific tonal ranges.

**Decompose** (**Colors → Components → Decompose…**) splits an RGB image into separate grayscale layers (or images) for an entire color model: RGB, HSV, HSL, CMYK, LAB, LCH, or YCbCr variants. Check **Decompose to Layers** to keep everything in one file. Once decomposed, you can edit individual channels — tweak the L channel in LAB for luminosity adjustments, for instance — then reassemble.

**Compose** (**Colors → Components → Compose…**) does the reverse: it takes grayscale layers or images and builds a full-color image from them. Choose your target color space, assign a layer to each channel slot, and hit OK. Pro tip: decompose as RGB, then recompose as LAB (or vice versa) for unexpected and often striking color effects.

**Recompose** (**Colors → Components → Recompose**) is the shortcut for round-tripping — it takes a previously decomposed image and reconstructs the original using whatever edits you made to the channel layers, no dialog needed.
