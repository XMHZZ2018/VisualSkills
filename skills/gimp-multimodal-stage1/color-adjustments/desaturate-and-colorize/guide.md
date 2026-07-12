# Desaturate and Colorize (GIMP 2.10)

Everything lives under the **Colors** menu. Open **Colors → Desaturate** to find the grayscale conversion tools, or **Colors → Colorize…** for tinting.

## Going Grayscale

The main workhorse is **Colors → Desaturate → Desaturate…**. This converts the active layer to shades of gray but keeps the image in RGB mode — meaning you can still paint color back onto specific areas afterward. The dialog gives you five mode choices: Luminance, Luma, Lightness (HSL), Average (HSI Intensity), and Value (HSV). For most photos, **Luminance** is the physically accurate pick — it preserves the relative brightness your eyes actually perceive. Luma is close but uses non-linearized values (it matches GIMP 2.8's old "Luminosity" option). Value (HSV) always produces the lightest result since it just takes the maximum channel.

If you need a smarter conversion that preserves local contrast between neighboring colors (useful when two different hues would otherwise collapse to the same gray), try **Colors → Desaturate → Color to Gray**. It uses a neighborhood-based algorithm — bump up the Radius and Iterations for cleaner results at the cost of processing time.

## Quick Sepia Tone

For that classic warm-brown vintage look, go to **Colors → Desaturate → Sepia…**. It handles the desaturation and toning in one shot. The **Effect strength** slider (0 to 1) controls blending — crank it to 1.0 for full sepia, or dial it back to keep some original tone peeking through. The **sRGB** checkbox toggles between gamma-corrected and linear processing.

See `fig01.jpg`.

## Colorize for Full Tinting

For more control — or a color other than brown — use **Colors → Colorize…** instead. This one renders the layer as grayscale seen through a colored filter. Drag the **Hue** slider to pick your tint (the full spectrum from 0.0 to 1.0), adjust **Saturation** for intensity, and tweak **Lightness** to brighten or darken the result. You can also click the **Color** button to pick a precise color visually, which auto-adjusts the sliders. This is the go-to for tinting a black-and-white portrait blue, giving a sunset photo a golden wash, or creating any single-tone effect beyond sepia.

One thing to remember: both Desaturate and Colorize only work on RGB layers. If your image is already in Grayscale or Indexed mode, convert it first with **Image → Mode → RGB**.
