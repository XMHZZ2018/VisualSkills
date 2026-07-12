# Creating and Editing Text (GIMP 2.10)

Activate the Text tool from **Tools → Text**, click the **A** icon in the Toolbox, or just press **T**. Click anywhere on your canvas and start typing — GIMP creates a new text layer automatically, named after your first few words.

By default the text box is **Dynamic**, meaning it grows as you type. If you'd rather constrain the text, drag out a rectangle first and it switches to **Fixed** mode, wrapping text at the box edge. Either way, press **Enter** for a new line.

To edit existing text later, make the text layer active in the Layers dialog, grab the Text tool, and click the text on canvas. Be cautious: if you've applied transforms (rotate, distort) to the text layer in the meantime, re-editing will discard those changes — GIMP will warn you first.

The floating toolbox above your text lets you change font, size, bold/italic/underline, baseline offset, and kerning for just the selected characters. Select text by click-dragging or **Shift+Arrow keys**, then adjust. Use **Alt+Arrow keys** as a shortcut for baseline and kerning tweaks.

In the Tool Options dock, you'll find global settings: **Font**, **Size**, **Color**, **Justify**, **Indent**, line spacing, letter spacing, and the **Box** mode toggle. The **Antialiasing** and **Hinting** options control rendering smoothness — keep antialiasing on for clean curves at most sizes.

Right-click on text for the context menu, which includes **Path from text** (converts letter outlines into an editable path) and **Text along path** (bends your text to follow an existing path — great for curved or circular layouts). You can also insert Unicode characters with **Ctrl+Shift+U** followed by the hex code and **Enter**.

For fancy effects, convert text to a selection or path, then fill, stroke, or transform freely using any GIMP tool.
