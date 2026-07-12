# Drawing Simple Shapes and Lines (GIMP 2.10)

GIMP isn't a vector drawing app, but it handles basic shapes and lines just fine once you know the trick: selections become shapes, and Shift turns any brush into a straight-line tool.

**Straight lines** work with any paint tool — Pencil, Paintbrush, Airbrush, even Eraser. Pick your tool, set a foreground color, then click once on the canvas to place a starting dot. Now hold **Shift** and move the mouse — you'll see a thin preview line following your cursor. Click again to commit the stroke. Keep holding **Shift** and clicking to chain additional connected segments.

**Rectangles and ellipses** use the selection-then-fill approach. Grab the **Rectangle Select** tool (or **Ellipse Select** for ovals) from the toolbox, then click-drag on the canvas to define your shape. Once you release, you have a selection — the marching ants outline.

To make a **filled shape**, choose your foreground color and use the **Bucket Fill** tool to flood the selection. For a **stroked outline** instead, go to **Edit > Stroke Selection**, pick a line width and style, and hit Stroke. Either way, finish by removing the selection with **Select > None**.

Hold **Shift** while dragging a selection to constrain it to a perfect square or circle. Hold **Ctrl** to expand the selection from its center rather than a corner.

For anything beyond these basics — complex paths, curves, or precise vector shapes — consider the **Paths** tool or an external app like Inkscape, then import the result.
