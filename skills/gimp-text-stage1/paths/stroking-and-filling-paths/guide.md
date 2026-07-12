# Stroking and Filling Paths (GIMP 2.10)

Paths are invisible by default — they only affect pixels once you stroke or fill them.

## Stroking a Path

To stroke, go to **Edit > Stroke Path** from the image menu, or right-click a path in the **Paths dialog** and choose **Stroke Path**. You can also hit the **Stroke Path** button in the Paths tool options.

The **Choose Stroke Style** dialog gives you two modes. **Stroke line** draws using the current foreground color (or active pattern if you toggle to **Pattern**). Set your **Line width**, pick a **Cap style** (Butt, Round, Square) for open endpoints, and a **Join style** (Miter, Round, Bevel) for corners. Expand **Line Style** to tweak the **Miter limit**, choose a **Dash preset**, or design a custom dash pattern pixel by pixel. Leave **Antialiasing** checked for smooth curves.

Alternatively, select **Stroke with a paint tool** and pick any tool from the dropdown — Paintbrush, Clone, Smudge, even the Eraser. GIMP uses that tool's current settings to trace along the path, which opens up creative effects you can't get with a plain line.

You can stroke the same path multiple times with different brushes or widths to layer effects.

## Filling a Path

Head to **Edit > Fill Path…** to fill the enclosed area of your path. The dialog lets you choose **Solid color** (uses the current foreground color) or **Pattern** (uses the active toolbox pattern). Keep **Antialiasing** enabled for clean edges. The fill covers all regions bounded by the path from its start to end point.
