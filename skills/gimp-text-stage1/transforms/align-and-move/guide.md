# Aligning and Moving (GIMP 2.10)

The **Align** tool snaps layers into precise positions relative to a target. Activate it via **Tools → Transform Tools → Align** or press **Q**. Click a layer on the canvas to make it the source (you'll see small squares at its corners), then use the **Relative to** dropdown in Tool Options to pick your target — the image, a selection, the active layer, a channel, or a path.

Once a target is set, the alignment buttons light up. The top row aligns horizontally (left edge, center, right edge) and the bottom row aligns vertically (top edge, middle, bottom edge). Hold **Shift** and click to select multiple layers as sources, or drag a rubber-band rectangle around them.

The **Distribute** section spaces multiple selected layers evenly. Choose a distribution direction and optionally set an **Offset** in pixels to add consistent gaps between elements. This is especially handy for animation frames or UI mockups where even spacing matters.

For batch alignment of all visible layers at once, use **Image → Align Visible Layers…** instead. The dialog offers Horizontal/Vertical Style options: **None** leaves that axis alone, **Collect** stacks layers to one edge, and **Fill** distributes them evenly across the canvas. Check **Use the (invisible) bottom layer as the base** to align against that layer rather than the canvas edge.

The **Move** tool (**Tools → Transform Tools → Move**, shortcut **M**) relocates layers, selections, paths, or guides. In its Tool Options, toggle between **Layer**, **Selection**, and **Path** mode. In Layer mode, "Pick a layer or guide" moves whatever you click on, while "Move the active layer" ensures only the current layer budges — useful when transparent areas would otherwise cause you to grab the wrong layer.

To move just a selection outline without affecting pixels, switch to Selection mode or hold **Ctrl+Alt** while in Layer mode. Arrow keys nudge by one pixel; add **Shift** to jump 25 pixels at a time. Linked layers (chain icon) always move together regardless of which one you drag.
