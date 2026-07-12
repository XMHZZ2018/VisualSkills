# Basic Selection Tools (GIMP 2.10)

GIMP's three basic selection tools let you isolate regions of your image so edits only affect what's inside the "marching ants." You'll find all of them under **Tools > Selection Tools** in the menu bar, or just remember their single-key shortcuts: **R** for Rectangle, **E** for Ellipse, and **F** for Free Select (Lasso).

See `fig01.png`.

**Rectangle Select** is the workhorse — click and drag to draw a box. You don't need to be precise on the first try; once the marching ants appear, grab any edge handle or corner to resize, or drag inside the selection to reposition it. Hold **Shift** after you start dragging to constrain it to a perfect square. Hold **Ctrl** after starting to expand from center instead of from a corner. When you're happy, press **Enter** or just switch to another tool to confirm.

In the Tool Options panel, **Rounded corners** lets you soften the rectangle's edges with an adjustable radius. **Fixed** constrains the selection to a set aspect ratio, width, height, or size — handy when you need an exact crop. Toggle **Highlight** to darken everything outside the selection so you can see exactly what you're keeping.

See `fig02.png`.

**Ellipse Select** works identically to Rectangle — you're still dragging a bounding box, but the selection inside is an oval. Hold **Shift** after clicking to force a circle; **Ctrl** after clicking centers it on your start point; both together give a centered circle. To draw a filled circle on your canvas, make a circular selection and hit **Edit > Fill with Foreground Color** (or use the Bucket Fill tool). For an outlined circle, use **Edit > Stroke Selection**.

**Free Select (Lasso)** is your freehand option. Click-and-drag to draw a loose shape, or click point by point to create straight-edged polygon segments — you can mix both in one selection. Close the shape by clicking the starting point, then press **Enter** to confirm. **Backspace** removes the last segment if you make a mistake; **Escape** cancels everything. The Lasso shines for quick rough selections; for precision, rough it in with Lasso then refine in QuickMask mode.

All three tools share selection **modes** in the Tool Options: Replace (default), Add, Subtract, and Intersect. Instead of memorizing these buttons, use the keyboard — hold **Shift** before clicking to add to an existing selection, **Ctrl** before clicking to subtract from it, and **Ctrl+Shift** to intersect. Enable **Feather Edges** when you want a soft, gradual boundary instead of a hard cutoff — bump the radius up for higher-resolution images.

See `fig03.png` for the selection mode buttons.
