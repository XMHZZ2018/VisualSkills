# Brightness, Contrast, and Exposure (GIMP 2.10)

For a quick tonal fix, open **Colors → Brightness-Contrast…**. You get two sliders — drag **Brightness** positive to lighten or negative to darken, and **Contrast** positive to punch things up or negative to flatten them. A neat shortcut: click directly on the canvas and drag vertically to adjust brightness or horizontally to adjust contrast, then hit **Return** to apply. If you want finer control afterward, click **Edit these Settings as Levels** to jump into the Levels tool with your current values preserved.

When you need to recover shadow detail without blowing highlights, use **Colors → Exposure…** instead. The **Exposure** slider adds stops of exposure compensation (think photography), while **Black level** lets you clip away muddy shadow information you don't need.

For targeted shadow/highlight recovery, open **Colors → Shadows-Highlights…**. The **Shadows** slider lightens or darkens only the dark tones, and **Highlights** does the same for bright areas. Each has a **color adjustment** slider controlling saturation — leave Shadows at 100% for a natural boost, but experiment with Highlights since bright areas often lack color data. Under **Common**, increase **Compress** to restrict the effect to extreme tones, adjust **Radius** to control transition softness (higher = smoother but risk of halos), and pull **White point adjustment** negative if you have blown detail above pure white.

Brightness-Contrast is your fast "good enough" tool; Exposure and Shadows-Highlights give you surgical control when the image matters.
