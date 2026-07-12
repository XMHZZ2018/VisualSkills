# Symmetry Painting (GIMP 2.10)

Symmetry Painting lets you paint with automatic mirroring, tiling, or radial repetition. It works with all brush-based tools — Pencil, Paintbrush, Eraser, Airbrush, MyPaint brush, Clone, Smudge, Dodge, and Ink.

Open the dialog via **Windows > Dockable Dialogs > Symmetry Painting**. You'll get a small dockable panel with a single **Symmetry** dropdown, set to "None" by default. Pick a mode and green dotted guide lines appear on your canvas — just start painting.

See `fig01.png`.

**Mirror** reflects your strokes across one or more axes. Check **Horizontal Symmetry**, **Vertical Symmetry**, or **Central Symmetry** — or combine them. The axis defaults to the image center, but you can reposition it with the **Vertical axis position** and **Horizontal axis position** fields. There's also a **Disable brush transform** checkbox: normally the brush tip itself gets flipped along with the stroke, but if you want only the path mirrored (not the brush shape), toggle that on. You'll mostly notice this with asymmetrical brushes.

See `fig02.png`.

**Tiling** repeats your stroke across the canvas in a grid pattern — great for creating seamless tiles or repeating patterns in one go. Set **Interval X** and **Interval Y** to control spacing (in pixels) between repetitions. **Shift** offsets alternating rows horizontally, handy for brick-like layouts. Leave **Max strokes X/Y** at 0 for unlimited repeats that fill the canvas, or set a cap if you want a finite grid.

**Mandala** arranges strokes radially around a center point, like spokes on a wheel. Set the center with **Center abscissa** and **Center ordinate**, then choose the **Number of points** to control how many copies radiate out. Six points gives you snowflake geometry; crank it higher for denser kaleidoscope effects. As with Mirror, **Disable brush transform** is available if you want the brush tip orientation preserved.

See `fig03.png`.

Once you've chosen a mode and tweaked settings, just paint normally — every stroke you make is instantly replicated according to the active symmetry. Switch back to "None" in the dropdown when you're done, and the guides disappear.
