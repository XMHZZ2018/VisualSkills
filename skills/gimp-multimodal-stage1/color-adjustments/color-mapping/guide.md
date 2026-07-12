# Color Mapping (GIMP 2.10)

All color mapping filters live under **Colors > Map**. They remap pixel colors based on luminosity, hue ranges, or direct replacement — useful for recoloring images, creating stylized effects, or swapping specific tones.

## Gradient Map

Pick a gradient first in the **Gradients** dialog (**Windows > Dockable Dialogs > Gradients**), then apply it via **Colors > Map > Gradient Map**. There's no dialog — it runs instantly. The filter maps pixel intensity to gradient position: your darkest pixels get the left-end color, the lightest get the right-end color, and everything in between follows the gradient's curve. Great for duotones or quick color grading.

## Palette Map

This works the same way as Gradient Map but uses palette entries instead of a gradient. Open **Windows > Dockable Dialogs > Palettes**, choose one, then run **Colors > Map > Palette Map**. Each pixel's luminosity determines which palette slot it picks up — black maps to the first entry, white maps to the last, intermediates spread across the palette in index order. Works on both RGB and grayscale images.

## Color Rotation

Open **Colors > Map > Rotate Colors** to swap one hue range for another. You define a source range and a destination range on two color wheels by dragging the arrow handles (or entering From/To angles). The filter rotates every pixel whose hue falls in the source range into the corresponding position in the destination range — so you can turn a blue sky orange without touching the greens.

See `fig01.png`.

The **Gray Handling** section lets you decide what happens to near-neutral pixels. Set the **Gray threshold** to catch low-saturation colors, then choose **Treat as this** (rotate them as if they had a particular hue) or **Change to this** (force them to a specific hue/saturation outright). Leave Hue and Saturation at zero if you just want grays to stay gray.

## Color Exchange

For a simpler swap — one specific color to another — use **Colors > Map > Color Exchange**. Click the **From color** button (or use the eyedropper on your image) to pick the color you want gone, then set the **To color** for its replacement. The **Red/Green/Blue Threshold** sliders widen the match range per channel; higher values catch more neighboring shades around your chosen color.

See `fig02.png`.

## Sample Colorize

To colorize a grayscale or desaturated image from another image's colors, go to **Colors > Map > Sample Colorize**. The dialog shows Destination (your target) on the left and Sample (color source) on the right. You can sample from any open image or choose **From Gradient** to use the active gradient instead. Hit **Get Sample Colors** to load the color ramp, adjust **Input/Output Levels** to control tone distribution, and enable **Smooth Sample Colors** if the transitions look harsh.
