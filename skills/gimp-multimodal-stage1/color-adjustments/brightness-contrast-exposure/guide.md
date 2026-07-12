# Brightness, Contrast, and Exposure (GIMP 2.10)

GIMP gives you three tools under the **Colors** menu for tonal adjustments, each suited to a different situation. Here's the quick rundown.

**Brightness-Contrast** is the fast, no-fuss option. Open it via **Colors > Brightness-Contrast…** and you get two sliders — drag Brightness left to darken or right to brighten, and Contrast to flatten or punch up the tonal range. There's a neat shortcut: click directly on the canvas and drag vertically to adjust brightness, or horizontally for contrast, all without touching the dialog. Hit **Enter** when it looks right.

See `fig01.png`.

If you realize mid-adjustment that you need finer control, click **Edit these Settings as Levels** at the bottom of the dialog — it hands your current values straight to the Levels tool so you can refine shadows and highlights independently. This tool also works on indexed-color layers as of GIMP 2.10.

**Exposure** is the better choice when you need to lift shadows and midtones without blowing out highlights — think of it like adding a stop of light in a camera. Open it from **Colors > Exposure…**. The **Black level** slider lets you clip unneeded deep shadows, while the **Exposure** slider adds brightness in a way that respects highlight detail.

**Shadows-Highlights** gives you the most surgical control when a photo has both crushed shadows and hot highlights. Find it at **Colors > Shadows-Highlights…**. The **Shadows** slider lightens (positive) or deepens (negative) dark areas, and the **Highlights** slider darkens (negative) or lifts bright areas. Each has a companion **color adjustment** slider that manages saturation shifts caused by the tonal change — the defaults are usually fine for shadows, but highlights sometimes need tweaking since they carry less color data.

Under the **Common** section, **Radius** controls how soft the transition is between adjusted and untouched areas (higher values = softer but possible halos), and **Compress** limits the effect to only the extreme darks and lights when pushed higher. **White point adjustment** can recover detail above 100% luminance by pulling overbright values back into visible range.

For all three tools, enable **Preview** to see changes live on the canvas, and use **Split view** to compare before/after side by side. Each also supports **Presets** if you find a correction you want to reuse across images.
