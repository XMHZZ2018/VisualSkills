# Basic Selection Tools (GIMP 2.10)

GIMP's three basic selection tools let you isolate regions of your image for editing. Grab them from **Tools → Selection Tools** or use their keyboard shortcuts: **R** for Rectangle, **E** for Ellipse, **F** for Free Select (Lasso).

**Rectangle Select** is the workhorse — click and drag to draw a box. Once the marching ants appear, you can resize by dragging the edge handles or move the whole selection by dragging its center. Enable **Rounded corners** in Tool Options for softer edges, or check **Fixed** to constrain to a specific aspect ratio or size. Hit **Enter** or click inside to confirm.

**Ellipse Select** works identically but produces circular or oval regions. Hold **Shift** after you start dragging to constrain it to a perfect circle, or **Ctrl** to expand from center. Combine both for a centered circle.

**Free Select (Lasso)** gives you freeform control. Click-and-drag for freehand drawing, or click-release-click for straight polygonal segments — you can mix both in one selection. Press **Backspace** to undo the last segment, **Escape** to cancel entirely. Close the shape by clicking the start point or double-clicking, then press **Enter** to validate.

All three tools share mode buttons in Tool Options: **Replace**, **Add**, **Subtract**, and **Intersect**. You can also use modifier keys — hold **Shift** before clicking to add to an existing selection, **Ctrl** before clicking to subtract. Check **Feather edges** to soften the selection boundary by a configurable pixel radius, which is great for natural-looking composites.

For rough work, start with the Lasso to get close, then refine in QuickMask mode (**Shift+Q**) for pixel-level precision.
