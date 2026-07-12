# Hue, Saturation, and Color Balance (GIMP 2.10)

GIMP gives you several tools under the **Colors** menu for shifting hues, tweaking saturation, and correcting color casts. None of these work on Grayscale images — convert to RGB first if the menu entries are grayed out.

## Hue-Saturation

Open **Colors > Hue-Saturation…** to adjust hue, saturation, and lightness for specific color ranges. The dialog shows six primary/complementary color buttons (R, Y, G, C, B, M) arranged in a circle, plus a **Master** button that affects everything at once. Pick a color range, then drag the **Hue** slider (-180 to 180) to rotate colors around the wheel, **Lightness** (-100 to 100) to brighten or darken that range, and **Saturation** (-100 to 100) to intensify or mute it.

See `fig01.png`.

The **Overlap** slider controls how much adjacent color ranges bleed into each other. At zero, only the selected range shifts; crank it up and neighboring hues get pulled along too — handy when a color straddles two ranges. Hit **Reset Color** to undo changes for the currently selected range without touching the others.

## Color Balance

For quick color-cast correction, go to **Colors > Color Balance…**. Choose whether to adjust **Shadows**, **Midtones**, or **Highlights**, then push the three sliders between complementary pairs: Cyan–Red, Magenta–Green, and Blue–Yellow. This is the fastest way to neutralize an unwanted tint in a photo — push a bluish shadow toward yellow, or warm up flat midtones with a nudge toward red.

Keep **Preserve Luminosity** checked (it is by default) so brightness stays stable while you shift colors around. The **Reset Range** button zeroes out the current tonal range without disturbing the others.

## Color Temperature

Head to **Colors > Color Temperature…** when you want to fix white balance in Kelvin. Set the **Original temperature** to what the camera captured (or your best guess), then adjust **Intended temperature** to where you want it. Raising the value warms the image (more amber); lowering it cools things down (more blue). Both fields have preset menus — click the triangle icon beside either value to pick common lighting conditions like daylight, tungsten, or shade.

See `fig02.jpg` for the before/after comparison.

## Hue-Chroma and Saturation

Two simpler alternatives live nearby. **Colors > Hue-Chroma…** works in the LCh color model — its **Chroma** slider adjusts color purity in a perceptually uniform way, which can feel more natural than the classic Saturation slider. **Colors > Saturation…** is even more minimal: just a **Scale** slider and a choice of color space (Native, CIE LAB/Lch, or CIE Yuv) for the computation. Use these when you just need a global saturation bump without per-channel fiddling.
