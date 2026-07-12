# Managing and Creating Brushes (GIMP 2.10)

GIMP ships with a solid set of brushes, but you'll probably want to add your own before long. Brushes live in your personal folder at `~/.config/GIMP/2.10/brushes/` — drop any `.gbr`, `.gih`, or `.vbr` file in there, hit **Refresh** in the Brushes dialog, and they're ready to use without restarting.

The fastest way to make a custom brush is from a selection: grab an area with the rectangle or ellipse tool, do **Edit > Copy**, and the clipboard instantly appears as a temporary brush at the top of the Brushes dialog. In GIMP 2.10 you can make it permanent by clicking **Duplicate this brush** at the bottom of the panel.

See `fig01.png`.

For a more permanent grayscale brush, create a small image (say 35x35 pixels), draw your shape in black on white, then export it with a `.gbr` extension into your brushes folder. When you save as `.gbr`, a dialog lets you set the default spacing — this controls how close together the "stamps" are when you drag a stroke. Hit **Refresh** in the Brushes dialog and your new brush appears immediately.

Color brushes work the same way but start from an RGBA image (transparent background). The brush paints with its own colors rather than your foreground color. Save it as `.gbr` just like an ordinary brush.

Animated brushes (called "image hoses") use the `.gih` format. You build them from a multi-layer image where each layer holds one or more brush shapes. When saving as `.gih`, the GIH dialog lets you configure dimensions, ranks, and selection modes — **Incremental** cycles through shapes in order, **Random** picks one at random, and **Angular** selects based on stroke direction. These are marked with a small red triangle in the Brushes dialog.

To resize any brush on the fly, use the **Size** slider in the tool options, or just press **`[`** and **`]`** to shrink or grow by 1 pixel (**`{`** and **`}`** for jumps of 10). You can also hold **Ctrl+Alt** and scroll the mouse wheel for quick adjustments while painting.

Parametric brushes are created through the built-in **Brush Editor** — they generate simple geometric shapes and are fully resizable. Any brush you make there is automatically saved to your personal brushes folder. GIMP 2.10 also supports MyPaint brushes (`.myb`) if you want access to that ecosystem.
