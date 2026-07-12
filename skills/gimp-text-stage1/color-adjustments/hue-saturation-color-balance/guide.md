# Hue, Saturation, and Color Balance (GIMP 2.10)

To shift colors across your image, open **Colors > Hue-Saturation…**. Pick a primary color to target (R, Y, G, C, B, M) or leave it on **Master** to affect everything at once. Drag the **Hue** slider (-180 to 180) to rotate colors around the color wheel, adjust **Saturation** to boost or mute vibrancy, and tweak **Lightness** to brighten or darken that color range specifically. The **Overlap** slider controls how much adjacent color ranges bleed into each other — subtle, but useful when neighboring hues shift unevenly.

For a simpler saturation-only adjustment, use **Colors > Saturation…**. It offers a single **Scale** slider and lets you choose the color space for computation (Native, CIE LAB/Lch, or CIE Yuv).

If you want to work in perceptual color space instead, **Colors > Hue-Chroma…** gives you Hue, Chroma (color purity), and Lightness sliders based on the LCh model — often more visually uniform than HSL adjustments.

To fix color casts from lighting, go to **Colors > Color Balance…**. Select whether to adjust **Shadows**, **Midtones**, or **Highlights**, then push the three sliders between their complementary pairs: Cyan–Red, Magenta–Green, and Blue–Yellow. Enable **Preserve Luminosity** to keep overall brightness intact while shifting the color.

For white-balance corrections, **Colors > Color Temperature…** is more direct. Set the **Original temperature** (what the camera captured at) and the **Intended temperature** (what you want). Raising the Kelvin value warms the image; lowering it cools things down. Both fields have presets accessible via the triangle button — handy for common lighting scenarios like daylight (~5500K) or tungsten (~3200K).

None of these tools work on Grayscale images — convert to RGB first. All dialogs support **Preview** and **Split view** so you can compare before and after in real time.
