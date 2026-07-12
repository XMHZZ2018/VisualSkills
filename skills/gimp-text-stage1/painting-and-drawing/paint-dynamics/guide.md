# Paint Dynamics (GIMP 2.10)

Paint Dynamics link brush parameters — like size, opacity, and color — to how you physically move a stylus or mouse. The result is strokes that feel more natural, as if responding to real pressure, speed, or direction.

To pick a dynamics preset, look at the **Dynamics** area in your Tool Options. Click the dropdown button to reveal presets like **Pressure Opacity**, **Speed Size Opacity**, or **Random Color**. Select one and start painting — that's it for basic use.

For the full list with management options, open **Windows > Dockable Dialogs > Paint Dynamics**. From there you can duplicate, delete, or create new presets. Built-in presets are locked; duplicate one first if you want to tweak it.

The heart of the system is the **Paint Dynamics Editor** — open it via the edit button in Tool Options or by double-clicking a preset. You'll see a matrix: rows are brush parameters (Opacity, Size, Color, Hardness, Jitter, etc.) and columns are inputs (Pressure, Velocity, Direction, Tilt, Wheel, Random, Fade). Click a checkbox to connect any parameter to any input. Fewer connections usually means more predictable results.

Mouse users aren't left out — Velocity, Direction, Random, and Fade all work without a tablet. Pressure, Tilt, and Wheel require a graphics tablet.

For finer control, open the curve editor from the dropdown inside the dynamics editor. Drag the curve to reshape how an input maps to the parameter — for example, make brush size ramp up fast then plateau, or bounce back down via a bell shape.

**Fade** deserves special attention: it changes a parameter over the length of a stroke. Set the fade distance in **Dynamics Options** (below the dynamics selector in Tool Options). The repeat mode — **None**, **Sawtooth wave**, or **Triangular wave** — controls what happens when your stroke exceeds that distance.

When **Color** is enabled in dynamics, the brush pulls color from the active gradient instead of the foreground swatch. Pair this with Fade or Velocity for strokes that shift hue naturally across a gradient.
