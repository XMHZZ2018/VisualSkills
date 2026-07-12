# Tools Not Working as Expected (GIMP 2.10)

When a tool seems dead, the most common culprit is a **floating selection**. Open the **Layers** dialog (**Ctrl+L**) and check whether the top entry says "Floating Selection." If it does, either anchor it with **Ctrl+H** or promote it to its own layer with **Shift+Ctrl+N**. Until you deal with it, most operations are locked out.

If your brush or eraser paints but nothing shows up, open **Tool Options** and confirm **Opacity** isn't set to 0. Also check the **Brushes** dialog — if you accidentally have the Clipboard Brush selected and the clipboard is empty, you'll get zero output. Just pick a normal brush and you're back in business.

Erasing produces white instead of transparency? That means the layer lacks an alpha channel. Right-click the layer in the **Layers** dialog and choose **Add Alpha Channel**. After that, the eraser will reveal the checkerboard (transparency) as expected.

Getting weird colors from your brush or eraser? You're probably painting on a **Layer Mask** or a **Channel** instead of the actual layer. Click the layer thumbnail in the **Layers** dialog to redirect your strokes to the image content.

For the **Move** tool or any transform tool (rotate, scale, etc.) that seems frozen: glance at the status bar for messages, then check **Tool Options** at the top — make sure the tool is set to transform the **Layer**, not a **Selection** or **Path**.

Finally, if the **Crop** tool leaves empty canvas around your result, enable **Delete cropped pixels** in the Crop tool's **Tool Options** before dragging your crop area.
