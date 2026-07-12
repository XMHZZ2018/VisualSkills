# Creating and Editing Text (GIMP 2.10)

Activate the Text tool from the Toolbox (the **A** icon), through **Tools > Text**, or just press **T**. Click anywhere on your canvas and start typing — GIMP immediately creates a new text layer and shows an on-canvas toolbox above your text for quick formatting changes.

By default the text box is **Dynamic**, meaning it grows as you type and you press **Enter** for new lines. Switch to **Fixed** in Tool Options if you'd rather draw a bounding rectangle first and have text wrap automatically within it — just click-and-drag to define the frame before typing.

See `fig01.png`.

The Tool Options panel lets you set the font (click the **Aa** button to browse installed fonts), size, color, justification, indent, line spacing, and letter spacing. You can even scroll your mouse wheel over the font button to cycle through fonts without opening the selector.

To edit existing text, make the text layer active in the Layers dialog, grab the Text tool, and click the text on canvas. Select characters by click-and-drag or **Shift+Arrow keys**, then restyle them using the floating toolbox — change font, size, bold/italic/underline, baseline offset, kerning, or color for just that selection.

See `fig02.png`.

Right-click your text to access the context menu with **Cut**, **Copy**, **Paste**, **Open text file**, **Path from text**, and **Text along path**. The last two are especially handy: **Path from text** converts letter outlines into an editable path (visible in the Paths dialog), and **Text along path** bends your text to follow a previously created path.

For vertical writing (useful for East-Asian scripts or design work), enable one of the vertical orientation options in the text editor — available since GIMP 2.10.6. You can also enter special Unicode characters with **Ctrl+Shift+U** followed by the hex code and **Enter**.

Be aware that once you modify a text layer with non-text tools (transforms, filters, painting), editing the text again will discard those modifications. GIMP warns you and offers to create a fresh text layer instead, preserving the modified version untouched.

For fancy effects beyond simple text rendering, convert your text to a selection or path, then fill, stroke, or transform it freely with any GIMP tool.
