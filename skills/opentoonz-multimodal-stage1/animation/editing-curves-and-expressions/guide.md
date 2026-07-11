# Editing Curves and Expressions (OpenToonz 1.7)

The **Function Editor** is where you fine-tune animation timing. It shows every animatable parameter — object transforms, effect values — in two views: a **Spreadsheet** (one column per parameter, one row per frame) and a **Graph Editor** (curves plotted over time). They're two faces of the same data, so edits in one instantly appear in the other.

See `fig01.png`.

On the right side you'll find the objects/effects tree. Folders with an arrow icon are animated; click any parameter icon to show or hide its curve or column. Right-click a folder and choose **Show Animated Only** to cut the clutter.

To add a keyframe in the Spreadsheet, double-click a cell, type your value, and press **Enter**. Drag the vertical strip on the left edge of a keyframe cell to slide it to a different frame. In the Graph Editor, Ctrl-click (Cmd-click on Mac) directly on a curve to drop a new control point, or position the frame marker and click the **Set Key** button. Select points by clicking or dragging a box, then drag them to retime.

See `fig02.png`.

Between any two keyframes sits a segment, and you control how values travel across it with the **Interpolation** dropdown (top-right panel). Pick the segment, choose your type — **Linear**, **Speed In / Speed Out**, **Ease In / Ease Out**, **Exponential**, **Constant**, or **Similar Shape** — and hit **Apply**. Speed In / Speed Out gives you Bezier handles you can drag directly on the curve; right-click a point and choose **Unlink Handles** to break tangent continuity for sharp transitions.

For procedural control, set the interpolation to **Expression** and type a formula directly. The editor autocompletes recognized terms and color-codes them — operators in dark blue, variables in light blue, constants in green, errors in red. Key variables: `t` (0–1 across the segment), `f` (current frame number). Handy functions include `wave(length)` for oscillation, `random(min,max)` for noise, and `saw(length)` for sawtooth patterns. You can reference other objects with syntax like `col1.x` or `fx.blur2.value`, letting one parameter drive another.

See `fig03.png`.

If you need data from external sources (motion-capture rigs, 3D exports), choose the **File** interpolation, point it at a DAT/TXT file, and specify which column of values to read. To reuse curves across scenes, right-click any parameter in the tree and choose **Save Curve** to export a CURVE file, or **Load Curve** to bring one in.

Want to loop your animation? Right-click the dashed line past the last keyframe and choose **Activate Cycle** — the curve repeats indefinitely. To control multiple parameters together, display several curves at once; the strip above the Graph Editor shows combined keyframes you can drag to retime everything in sync.
