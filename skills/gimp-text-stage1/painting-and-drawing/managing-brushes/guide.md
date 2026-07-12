# Managing and Creating Brushes (GIMP 2.10)

GIMP uses brushes across all 10 paint tools — not just the Paintbrush, but also the Eraser, Clone, Airbrush, and others. Pick any brush by clicking its icon in the Brushes dialog, or click the brush symbol in the Toolbox to open that dialog directly.

**Adding new brushes** is straightforward. Drop your brush file into the `brushes` folder inside your personal GIMP directory (e.g., `~/.config/GIMP/2.10/brushes/`), then hit **Refresh** in the Brushes dialog. No restart needed. GIMP recognizes `.gbr` (ordinary/color brushes), `.gih` (animated brushes), `.vbr` (parametric), and `.myb` (MyPaint) formats.

**The fastest way to create a brush**: select an area of any image, do a **Edit > Copy**, and it instantly appears as "Clipboard" at the top of the Brushes dialog — ready to paint with. Click **Duplicate this brush** to make it permanent.

**For a custom grayscale brush**, create a small image via **File > New** (e.g., 35x35 px, grayscale, white fill), draw your shape in black, and save it with a `.gbr` extension into your brushes folder. Hit **Refresh** and start painting. For a color brush, do the same but use an RGBA image instead.

**Changing brush size** works several ways. The most direct is the **Size** slider in tool options. Keyboard shortcuts are handy too: press **`[`** or **`]`** to shrink/grow by 1 pixel, or **`{`** / **`}`** to jump by 10. You can also hold **Ctrl+Alt** and scroll the mouse wheel.

**Animated brushes** (image hoses) cycle through multiple shapes as you paint — marked by a red triangle in the Brushes dialog. To create one, build a multi-layer image where each layer holds a brush variant, then save as `.gih`. The GIH dialog lets you configure dimensions, ranks, and selection modes: **Incremental** (sequential), **Random**, or **Angular** (direction-sensitive). You can combine up to four dimensions for brushes that respond to direction, alternation, color, and tablet pressure simultaneously.

Every brush also has a **Spacing** property controlling the gap between consecutive stamps in a stroke — adjustable in the Brushes dialog. Lower spacing gives smoother lines; higher spacing shows individual marks.
