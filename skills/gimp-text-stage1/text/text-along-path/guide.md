# Text Along a Path (GIMP 2.10)

Start by drawing a path — grab the **Paths** tool and click to place anchor points forming the curve you want your text to follow. Drag the handles to smooth things out. This path is your text's rail.

Switch to the **Text** tool and type your text directly on the canvas. Don't worry about positioning it perfectly — it just needs to exist as a text layer. Keep the text layer active and selected.

Now the key move: in the **Text** tool options, click **Text along Path**. GIMP bends your text to follow the active path, producing a new path in the Paths dialog that represents your curved letterforms.

That new path isn't visible pixels yet — it's just outlines. To make it real, go to the Paths dialog, right-click the new text path, and choose **Path to Selection**. Create a new layer, then fill the selection with **Edit > Fill with Foreground Color** (or bucket-fill with whatever you like).

Alternatively, you can stroke the path instead of filling it. Use **Edit > Stroke Path...** to trace the letter outlines with a brush — try a fuzzy brush for a glowing effect, then apply **Colors > Map > Gradient Map** for stylized results.

For even fancier transforms, use **Path from Text** in the Text tool's right-click context menu to convert your original text to a path, then warp it with the **Perspective** or **Warp Transform** tool before stroking or filling.

One tip: tighter curves need smaller font sizes or wider letter spacing to avoid overlapping glyphs. Adjust spacing in the Text tool options before running **Text along Path** if letters bunch up on sharp bends.
