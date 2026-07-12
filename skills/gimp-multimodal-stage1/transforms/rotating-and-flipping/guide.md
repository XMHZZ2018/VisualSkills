# Rotating and Flipping (GIMP 2.10)

For quick fixed-angle rotations — the kind you need when a camera photo comes in sideways — head to **Image > Transform** and pick **Rotate 90° clockwise**, **Rotate 90° counter-clockwise**, or **Rotate 180°**. These operate on the entire image and are the fastest way to switch between portrait and landscape orientation.

When you need an arbitrary angle, grab the Rotate tool. Activate it via **Tools > Transform Tools > Rotate**, click its icon in the Toolbox, or press **Shift+R**. Click on the canvas and a Rotation adjustment dialog appears where you can type an exact angle (anywhere from −180° to +180°) and reposition the center of rotation by adjusting the Center X/Y values — or just drag the crosshair directly on the canvas. Hold **Ctrl** while dragging to snap the angle to 15-degree increments.

See `fig01.png`.

The **Direction** setting in tool options matters. Normal mode rotates the layer the way you'd expect. Corrective mode is handy for straightening crooked photos — visually align a horizon line and GIMP applies the inverse rotation to fix the skew. Since GIMP 2.10.10, the **Readjust** button lets you "bake in" the current rotation and reset the handles, so you can build up complex rotations in multiple passes.

You can also rotate a single layer without affecting others through **Layer > Transform > Arbitrary Rotation**.

For flipping, go to **Image > Transform > Flip Horizontally** or **Flip Vertically** to mirror the whole image. If you only want to flip the active layer or a selection, use the Flip tool instead: **Tools > Transform Tools > Flip** or press **Shift+F**. Click the canvas and it flips horizontally by default; toggle to vertical in the Tool Options or hold **Ctrl** to switch direction on the fly. Flipping a selection creates a new floating selection layer automatically.

See `fig02.png`.

A nice trick in GIMP 2.10: place a guide on the canvas and click it with the Flip tool active — the guide becomes the flip axis instead of the layer center. Combine this with the **Clipping** option set to **Clip** to keep the result within bounds.
