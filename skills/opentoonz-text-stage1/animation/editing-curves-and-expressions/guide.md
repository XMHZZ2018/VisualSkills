# Editing Curves and Expressions (OpenToonz 1.7)

The **Function Editor** is your control center for keyframes and interpolations. Open it via **Windows > Function Editor**. The left pane shows either a Spreadsheet (numeric columns) or a Graph Editor (visual curves); the right side holds the interpolation controls and the objects/effects tree. Both views reflect the same data — edits in one appear in the other.

In the objects/effects tree, expand a folder (Stage or FX) and click a parameter icon to show its curve or column. Animated parameters display a wavy-line icon; static ones show a dotted line. Right-click a folder and choose **Show Animated Only** to filter clutter.

To add a keyframe in the Spreadsheet, double-click a cell, type your value, and press **Enter**. In the Graph Editor, Ctrl-click (Cmd-click on Mac) directly on the curve, or navigate to the desired frame and click the **Set Key** button in the toolbar. Drag control points to reposition them; Shift-click to multi-select.

Each segment between two keyframes carries an interpolation type. Select a segment, pick from the **Interpolation** dropdown (Linear, Speed In / Speed Out, Ease In / Ease Out, Ease In / Ease Out %, Exponential, Expression, File, Constant, or Similar Shape), then hit **Apply**. For Speed In / Speed Out, drag the Bezier handles on each control point — right-click a point and choose **Unlink Handles** to break tangent symmetry, or **Reset Handles** to recover collapsed ones.

For expression-driven segments, choose **Expression** as the interpolation type and write a formula in the text field. Use `t` (0–1 across the segment), `f` (current frame), or reference other objects like `col1.x` or `fx.blur2.value`. Standard math (`sin()`, `clamp()`, `random(min,max)`) and conditionals (`(f>10)?1:0`) are supported. Color-coded syntax highlighting confirms valid terms; errors show in red. Hit **Enter** to validate, then **Apply**.

To loop an animation, right-click the dashed tail past your last keyframe and choose **Activate Cycle**. You can also save any parameter's curve via right-click > **Save Curve** (exports a .curve file) for reuse across scenes, or **Export Data** to produce a .dat file for external tools.

When multiple curves are visible in the Graph Editor, the strip below the frame ruler lets you move shared keyframes and adjust Ease/Speed markers across all visible parameters simultaneously — handy for syncing a camera truck with an effect animation in one drag.
