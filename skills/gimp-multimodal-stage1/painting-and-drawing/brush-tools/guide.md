# Brush Tools (GIMP 2.10)

GIMP's brush tools live under **Tools > Paint Tools** and cover five core painting instruments: the Pencil (**N**), Paintbrush (**P**), Airbrush (**A**), Ink (**K**), and MyPaint Brush (**Y**). They all work by dragging across the canvas to lay down brush strokes, but each has a distinct character. The Pencil produces hard, pixel-perfect marks with no anti-aliasing — ideal for icon work or precise pixel editing. The Paintbrush is the everyday workhorse, rendering smooth, fuzzy-edged strokes. The Airbrush builds up color over time like a spray can, controlled by its **Rate** and **Flow** sliders. The Ink tool simulates a calligraphy pen with an adjustable nib (circle, square, or diamond shape), and its stroke width responds to drawing speed. The MyPaint Brush, added in GIMP 2.10.6, opens up a huge library of third-party artistic brushes — just drop them into your `.mypaint/brushes` folder (find the path under **Preferences > Folders > MyPaint Brushes**).

See `fig01.png`.

All five tools share a common set of options in the Tool Options dock: **Mode**, **Opacity**, **Brush**, **Size**, **Aspect Ratio**, **Angle**, **Spacing**, **Hardness**, **Force**, and **Dynamics**. If the dock isn't visible, open it via **Windows > Dockable Windows > Tool Options**. The **Opacity** slider controls stroke transparency, while **Spacing** sets how far apart individual brush dabs are placed along the stroke. Bump up **Apply Jitter** to scatter those dabs randomly, creating spray-paint or stipple effects. Enable **Smooth Stroke** to iron out hand wobbles when drawing with a mouse — higher **Weight** values make the line more rigid.

See `fig02.png`.

Keyboard modifiers work the same way across the group. Hold **Ctrl** and click anywhere on the canvas to pick up that pixel's color into the foreground swatch — every brush tool becomes a color picker. Hold **Shift** and click two points to draw a perfectly straight line between them; keep holding Shift and clicking to chain segments together. Add **Ctrl+Shift** to constrain those lines to 15-degree increments (horizontal, vertical, or diagonal snaps).

The **Lock brush size to view** checkbox is a lifesaver when you zoom in and out frequently — it keeps the brush size constant relative to your screen rather than the canvas, so you don't have to resize the brush every time you change zoom level. For tablet users, the **Dynamics** section maps pen pressure, tilt, and velocity to brush parameters like size and opacity, giving you natural, expressive control that a mouse can't match.
