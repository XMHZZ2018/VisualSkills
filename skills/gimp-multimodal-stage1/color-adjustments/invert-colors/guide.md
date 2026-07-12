# Inverting Colors (GIMP 2.10)

GIMP gives you three flavors of color inversion, all living under the **Colors** menu. Each operates on the current layer and produces a different result depending on how it handles brightness and hue.

## Perceptual Invert

The standard invert — go to **Colors > Invert** — flips every pixel to its complementary color and reverses brightness, like creating a photographic negative. Dark goes light, red becomes cyan, blue becomes yellow, and so on. This is the one you want when you need a full tonal and chromatic reversal.

One thing to watch: don't mix this up with **Select > Invert**, which flips your selection mask, not your pixel colors. Totally different operation, confusingly similar name.

## Linear Invert

Head to **Colors > Linear Invert** for a mathematically "raw" inversion that works in linear light rather than the perceptual (gamma-corrected) space. It inverts all color components except the alpha channel. The visual result is similar to standard Invert but can differ subtly in midtone distribution — useful when you're compositing in linear workflows or need physically accurate light math.

## Value Invert

Found at **Colors > Value Invert**, this one only flips the Value (luminosity) channel in HSV space, leaving Hue and Saturation alone. Bright areas go dark and dark areas go bright, but colors stay on the same side of the wheel. It's handy when you want a luminosity negative without completely scrambling your palette.

See `fig01.jpg`.

A caveat: Value Invert isn't perfectly reversible. Applying it twice doesn't return you to the exact original — high-luminosity colors can drift slightly in hue and saturation due to rounding. Don't rely on a double-apply as an undo; use actual Undo instead.
