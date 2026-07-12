# Desaturate and Colorize (GIMP 2.10)

All desaturation tools live under **Colors → Desaturate**. The quickest way to go grayscale is **Colors → Desaturate → Desaturate…**, which gives you five modes — Luminance, Luma, Lightness (HSL), Average (HSI Intensity), and Value (HSV). Luminance is the most physically accurate choice; it preserves the relative brightness your eyes actually perceive. The others can be useful for creative effect, but they'll shift tonal relationships, especially in saturated areas.

Importantly, Desaturate only affects the active layer and keeps the image in RGB mode (R=G=B for each pixel), so you can still paint color back onto specific areas afterward.

For a smarter conversion that preserves local contrast between neighboring colors, try **Colors → Desaturate → Color to Gray**. It uses a local-difference algorithm, so two colors that look distinct but share the same luminance won't collapse into the same gray. Bump up the Iterations slider for cleaner results if you can spare the processing time.

To get a classic sepia look in one shot, go to **Colors → Desaturate → Sepia…**. The Effect strength slider (0 to 1) controls the blend — crank it to 1.0 for full warm-brown toning, or dial it back for a subtler hint.

For full control over colorizing, use **Colors → Colorize…** instead. This converts the layer to grayscale and views it through a colored tint — adjust Hue (0–1.0), Saturation (0–1.0), and Lightness (-1.0 to +1.0) to taste. You can also click the color swatch to pick a tint directly and the sliders will update to match. This is the go-to for sepia, cyanotype, or any single-hue toning effect where you want precise control over the warmth and intensity.
