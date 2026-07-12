# Aligning and Moving (GIMP 2.10)

The Align tool lets you snap layers precisely against other objects — the image edges, a selection, or another layer. Activate it via **Tools > Transform Tools > Align** or just press **Q**. Click a layer on the canvas to designate it as the "source" (you'll see small squares at its corners). Hold **Shift** and click to select multiple layers, or drag a rubber-band rectangle around them.

In the tool options, the **Relative to** dropdown picks your target: Image, Selection, Active Layer, Active Channel, or Active Path. Once that's set, the alignment buttons light up — left/center/right for horizontal, top/middle/bottom for vertical. Click the one you need and the source snaps into place.

See `fig01.png`.

The Distribute section handles spacing. Select several layers with **Shift**-click, then use the distribute buttons to spread them evenly — horizontally, vertically, or by their edges. An **Offset** value (positive or negative, in pixels) adds extra breathing room between distributed layers.

For batch alignment of all visible layers at once, go to **Image > Align Visible Layers…**. The dialog offers Horizontal and Vertical style modes: "None" leaves that axis alone, "Collect" gathers layers to one edge, and "Fill" spaces them evenly across the canvas. Check **Use the (invisible) bottom layer as the base** if you want to align against the bottom layer's bounds rather than the canvas edges. You'll need at least three visible layers for the Fill options to work.

The Move tool (**M**, or **Tools > Transform Tools > Move**) handles repositioning. By default it's set to move layers — click directly on a layer's content and drag. If you click an area belonging to a different layer, that layer becomes active and gets moved instead. Switch to "Move the active layer" mode in tool options if transparent regions keep tricking you into grabbing the wrong layer.

See `fig02.png`.

You can also move selections (just the marching-ants outline, not the pixels) or paths by toggling the mode in tool options. For selections, hold **Ctrl+Alt** while in Layer mode as a shortcut. Arrow keys nudge by one pixel; add **Shift** for 25-pixel jumps. Selections and layers snap to guides and grids when **View > Snap to Guides** is enabled.

Grouped layers (linked with the chain icon) move together regardless of which one is active. Guides turn red when hovered — just drag to reposition them. GIMP 2.10 shows live relative coordinates while you drag guides, so you always know exactly how far you've moved.
