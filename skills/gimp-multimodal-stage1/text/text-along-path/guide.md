# Text Along a Path (GIMP 2.10)

Curving text along a vector path in GIMP is a two-stage trick: you create a path that defines the curve, then you tell your text to follow it. The result is a new path shaped like your letters — ready to stroke, fill, or transform however you like.

Start by drawing your curve with the **Paths** tool. Click to place anchor points and drag the handles to shape the arc or wave you want. This path is your guide rail — the text will flow along it from the first anchor to the last.

Next, grab the **Text** tool and type your text directly on the canvas. Don't worry about positioning it perfectly; what matters is the content and font size. Pick your typeface and size in the tool options now, because once the text becomes a path it's no longer editable as characters.

With the text layer still active, right-click on the text box to open the Text tool's context menu and choose **Text along Path**. GIMP immediately generates a new path in the Paths dialog — your letters are now vector outlines draped along the curve you drew earlier.

To make the curved text visible as actual pixels, go to the Paths dialog, select the new text-shaped path, then right-click and choose **Stroke Path** or convert it to a selection with **Select from Path** and fill it. Stroking with a paint tool gives you outlined letters; filling a selection gives you solid ones.

You can also transform the resulting path before rendering it. Switch to the **Perspective** tool or **Rotate** tool, set it to work on paths in the tool options, and reshape your curved text freely. Converting text to a path first and transforming the path produces much cleaner results than transforming rasterized text — no blurry pixels.

For extra flair, stroke the path with a textured or fuzzy brush, then apply **Colors > Map > Gradient Map** to recolor the stroked text with a gradient. The "Yellow Contrast" gradient over a fuzzy-brushed stroke gives a glowing neon look with almost no effort.

One last tip: if the text appears upside-down or reversed along your path, flip the direction of the original guide path (**Edit Path** mode, reverse the anchor order) before running **Text along Path** again. The text always flows in the direction the path was drawn.
