# Inverting Colors (GIMP 2.10)

GIMP offers three ways to invert colors, each operating differently on the current layer. All live under the **Colors** menu — no dialogs, no options, just instant results.

**Invert** (**Colors → Invert**) is the classic full inversion: every pixel's color and brightness flip to their opposite. Dark goes bright, bright goes dark, and hues become their complementary colors — red becomes cyan, yellow becomes magenta, and so on. This is the perceptual invert, working in the perceptually-uniform color space. Applying it twice returns you to the original.

**Linear Invert** (**Colors → Linear Invert**) does the same flip but in linear light rather than perceptual space. The visual difference is subtle — midtones shift slightly differently — but it matters for compositing workflows where you need mathematically correct light values. It also leaves the alpha channel untouched.

**Value Invert** (**Colors → Value Invert**) only flips luminosity while preserving hue and saturation. A bright green becomes a dark green instead of turning magenta. One caveat: due to rounding, applying it twice does *not* perfectly restore the original image, especially for high-luminosity colors. If you need a full round-trip inversion, use the standard **Invert** instead.

Don't confuse any of these with **Select → Invert**, which flips your *selection* rather than pixel colors.
