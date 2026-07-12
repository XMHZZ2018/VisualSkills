# Rotating and Flipping (GIMP 2.10)

For quick fixed-angle rotations of the entire image, go to **Image → Transform** and pick **Rotate 90° clockwise**, **Rotate 90° counter-clockwise**, or **Rotate 180°**. This is the fastest way to fix portrait/landscape orientation from a camera.

When you need an arbitrary angle, grab the **Rotate tool** via **Tools → Transform Tools → Rotate** (or press **Shift+R**). Click on the canvas and a dialog appears where you type an exact angle or drag directly on the image. Hold **Ctrl** while dragging to snap to 15-degree increments. You can reposition the rotation center by dragging the crosshair or entering **Center X/Y** coordinates in the dialog — it even works outside the canvas bounds.

Use **Corrective (Backward)** direction in Tool Options when straightening a crooked photo — just visually align the grid and GIMP applies the inverse rotation to fix it.

To flip the whole image as a mirror, use **Image → Transform → Flip Horizontally** or **Flip Vertically**. For flipping individual layers or selections, activate the **Flip tool** with **Tools → Transform Tools → Flip** (or **Shift+F**), then click the canvas. Toggle between horizontal and vertical in Tool Options, or hold **Ctrl** to switch on the fly.

A handy trick: place a guide on the canvas first, then click it with the Flip tool active — GIMP uses that guide as the flip axis instead of the layer center.
