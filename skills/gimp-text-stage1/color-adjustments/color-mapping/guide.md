# Color Mapping (GIMP 2.10)

All color mapping filters live under **Colors → Map**. They remap pixel colors based on luminosity, hue ranges, or direct replacement.

**Gradient Map** is the simplest — pick a gradient in the Gradients dialog, then hit **Colors → Map → Gradient Map**. No dialog appears; it instantly maps your darkest pixels to the left end of the gradient and lightest pixels to the right. Great for quick duotone or tinted effects.

**Palette Map** works the same way but uses the active palette instead of a gradient. Open **Windows → Dockable Dialogs → Palettes**, choose one, then apply via **Colors → Map → Palette Map**. Black maps to the first palette entry, white to the last, everything else spreads across the palette in index order.

**Color Rotation** swaps one hue range for another. Open it at **Colors → Map → Rotate Colors**, then set a Source Range (the colors you want to change) and a Destination Range (what they become) using the color wheel handles or the From/To angle sliders. The **Gray Handling** section lets you pull low-saturation pixels into the rotation — bump the Gray Threshold slider up and choose whether gray should be treated as the source hue or directly changed to a specific color.

**Color Exchange** does a targeted find-and-replace on a single color. Open **Colors → Map → Color Exchange**, click the **From color** button (or use the eyedropper on your image), pick a **To color**, then widen or narrow the **Red/Green/Blue Threshold** sliders to catch nearby shades. Higher thresholds affect more pixels around the chosen color.

**Sample Colorize** (**Colors → Map → Sample Colorize**) is the most flexible — it colorizes a grayscale or desaturated image by borrowing colors from another open image or a gradient. Use the **Get Sample Colors** button to load the color ramp, adjust **Input Levels** and **Output Levels** to taste, and check **Smooth Sample Colors** if transitions look harsh.
