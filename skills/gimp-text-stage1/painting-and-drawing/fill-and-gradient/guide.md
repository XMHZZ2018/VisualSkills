# Bucket Fill and Gradient (GIMP 2.10)

The **Bucket Fill** tool floods an area with color or pattern. Grab it from **Tools > Paint Tools > Bucket Fill** or press **Shift+B**. By default it fills with the foreground color; hold **Ctrl+click** to use the background color instead, or switch to **Pattern fill** in the tool options. The **Affected Area** setting controls whether you fill the whole selection or only similar colors — hold **Shift** to toggle between them on the fly.

The **Threshold** slider determines how aggressively the fill spreads into neighboring pixels. Crank it up for multi-toned regions; keep it low for precision. If you're filling on a transparent layer and see a halo of the old color, raise the threshold or enable **Fill Transparent Areas**.

For line-art coloring (available since 2.10.10), choose **Fill by line art detection** — it intelligently closes gaps and fills right up to drawn lines. Tweak **Maximum growing size** and **Maximum gap length** to handle thin or broken strokes.

Quick fills without the tool: **Edit > Fill with FG Color** (**Ctrl+,**) or **Edit > Fill with Pattern** (**Ctrl+;**) instantly flood the entire selection or layer.

The **Gradient** tool lives at **Tools > Paint Tools > Gradient** (shortcut **G**). Click where you want the gradient to start, drag in the direction it should flow, and release. A shorter drag gives a sharper transition; a longer drag gives a smoother blend. Hold **Ctrl** to constrain the angle to 15-degree increments.

Pick a shape from the tool options — **Linear**, **Radial**, **Conical**, **Spiral**, or any of the **Shaped** variants that follow the selection boundary. Set **Repeat** to **Sawtooth Wave** or **Triangular Wave** for repeating stripe effects. The **Offset** slider pushes the gradient start further from your click point, steepening the visible transition.

In GIMP 2.10 the gradient is fully editable on-canvas: after dragging, you can move endpoints, drag color stops, add new stops from midpoints, and change segment blending — all before committing. Enable **Instant mode** if you prefer the old click-and-done behavior. Try the **Difference** blend mode for psychedelic swirl patterns that build up with each stroke.
