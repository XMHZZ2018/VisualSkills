# Gradients, Patterns, and Palettes (GIMP 2.10)

GIMP ships with a rich library of gradients, patterns, and palettes — and you can extend all three with your own creations or downloads. Here's how they work in practice.

## Gradients

A gradient is an ordered set of colors you can apply as a fill or along a brushstroke. To fill a selection with a gradient, pick one from the Toolbox's Brush/Pattern/Gradient area (or open **Windows > Dockable Dialogs > Gradients**), then drag across your selection with the **Gradient tool**. Colors distribute perpendicular to the drag direction, over its length.

See `fig01.png`.

The first four gradients in the list are dynamic — they derive from your current Foreground and Background colors, so changing those in the Toolbox Color Area updates the gradient instantly. "FG to Transparent" is especially handy for vignettes and soft overlays.

You can also paint with gradient colors: switch any brush tool's **Dynamics** to **Color From Gradient**, then set the **Fade length** and **Repeat** style under Fade Options. The brushstroke will cycle through the gradient's colors over the distance you specified.

See `fig02.png`.

To create a custom gradient, duplicate an existing one in the Gradients dialog and open it in the **Gradient Editor**. Save custom `.ggr` files (or SVG gradients) into the `gradients` folder in your personal GIMP directory and they'll load automatically next session.

## Patterns

A pattern is a small image used to tile-fill regions. Select the **Bucket Fill** tool, switch it to **Pattern fill** in Tool Options, and click the pattern swatch to browse available patterns. You can also paint patterns with the **Clone** tool or use them when stroking a path or selection.

Patterns don't have to be opaque — translucent ones let lower layers show through, which is a quick way to build texture overlays. To add your own, save any image as `.pat` (via **File > Export As**) or just drop a `.png`, `.jpg`, or `.gif` into the `patterns` folder in your GIMP profile. The Tileable Blur filter (**Filters > Blur > Tileable Blur**) helps you smooth seams on patterns you've created from photos or rendered textures.

## Palettes

A palette is a curated set of discrete colors — useful when you want to constrain your painting to a fixed scheme or when working with indexed (GIF) images. Open **Windows > Dockable Dialogs > Palettes** to browse what's available; double-click any palette to open the **Palette Editor**. Clicking a swatch sets your foreground color; **Ctrl+click** sets the background.

You can build a palette from any open image: right-click in the Palettes dialog, choose **Import Palette**, and select the source image (or even a gradient). Custom palettes are saved as `.gpl` files — plain text, easy to hand-edit or share. Indexed images each carry their own private palette (max 256 colors), visible in the **Colormap** dialog rather than the Palettes dialog.

See `fig03.png`.
