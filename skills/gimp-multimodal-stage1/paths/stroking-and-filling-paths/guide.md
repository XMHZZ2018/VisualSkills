# Stroking and Filling Paths (GIMP 2.10)

Paths on their own don't touch your pixels — they're just vector outlines sitting in the background. To actually render them onto the canvas, you either *stroke* the path (draw along it) or *fill* the enclosed area.

**Stroking a path** means painting along its outline. You can trigger it from **Edit > Stroke Path**, from the right-click menu in the Paths dialog, or by hitting the **Stroke Path** button in the Paths tool options. Any of these opens the Choose Stroke Style dialog, where you pick your method.

See `fig01.png`.

The dialog gives you two modes. **Stroke line** draws a simple line using the current foreground color (or active pattern if you toggle to Pattern). Expand the **Line Style** section and you get control over cap style (Butt, Round, Square), join style (Miter, Round, Bevel), miter limit, dash pattern, and antialiasing. Adjust the line width in pixels or another unit of your choice.

Alternatively, select **Stroke with a paint tool** and pick any tool from the dropdown — Paintbrush, Clone, Smudge, Eraser, whatever you like. The stroke then uses that tool's current settings, which means brush size, opacity, and dynamics all apply. Check **Emulate brush dynamics** if you want pressure-like variation along the stroke.

See `fig02.png`.

You can stroke the same path multiple times with different brushes or widths to build up layered effects — the creative possibilities here are wide open.

**Filling a path** is simpler. Go to **Edit > Fill Path** and a small dialog asks whether to fill with the current **Solid color** (foreground) or the active **Pattern**. Antialiasing is on by default. The fill covers all areas enclosed by the path from its start to end point, so make sure your path actually forms a closed shape if you want a clean fill.

Both commands only become active when a path exists in the image — if they're grayed out, draw or import a path first.
