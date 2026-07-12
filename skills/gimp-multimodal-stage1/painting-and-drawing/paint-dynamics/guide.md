# Paint Dynamics (GIMP 2.10)

Paint Dynamics connect brush parameters — like size, opacity, or color — to how you physically move your stylus or mouse. The result is strokes that feel more natural: press harder to get a thicker line, move faster to fade opacity, or let color shift as you change direction. Dynamics are designed for drawing tablets, but several inputs (velocity, direction, random, fade) also work with a plain mouse.

To pick a dynamics preset, look at the **Dynamics** area in the Tool Options for any paint tool. Click the drop-down button to reveal the preset list (Pressure Opacity, Random Color, Track Direction, etc.) and select one. For the full dockable dialog, go to **Windows > Dockable Dialogs > Paint Dynamics**, where you can also create, duplicate, or delete presets.

See `fig01.png`.

To build your own dynamics, open the **Paint Dynamics Editor** by clicking the edit icon next to the preset name. The editor shows a matrix: rows are brush parameters (Opacity, Size, Color, Hardness, Jitter, and more) and columns are inputs (Pressure, Velocity, Direction, Tilt, Wheel, Random, Fade). Click a checkbox to link any parameter to any input — click again to unlink. Keep it simple; enabling too many connections at once makes the brush unpredictable. Note that built-in presets are read-only — duplicate one first if you want to modify it.

See `fig02.png`.

For finer control, open the curve editor from the drop-down at the top of the Editor. Each enabled connection gets its own response curve. Drag the curve to reshape how the input maps to the output — for example, make brush size ramp up quickly at low pressure then plateau, or have color sweep through the gradient non-linearly. A **Reset Curve** button brings it back to default.

See `fig03.png`.

Finally, check the **Dynamics Options** section at the bottom of Tool Options. The **Fade length** slider sets how many pixels a fade-based dynamic takes to complete its transition. The **Repeat** drop-down controls what happens past that length: **None** holds the final value, **Sawtooth wave** restarts from the beginning, and **Triangular wave** bounces back and forth. Under **Color Options**, pick which gradient the brush samples from when color dynamics are active — if no color dynamic is enabled, GIMP just uses your foreground color as usual.
