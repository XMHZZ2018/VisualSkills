# Modifying Selections (GIMP 2.10)

All selection-modification commands live under the **Select** menu. Once you have an active selection (marching ants), these let you refine its shape and edges without redrawing it from scratch.

See `fig01.png`.

**Feather** (**Select > Feather…**) softens the selection's edges by blending them gradually into the unselected area. You set a radius in pixels — larger values produce a wider, softer transition. This is handy when you've already made a hard-edged selection and want to avoid a harsh cutout look. The "Selected area continues outside image" checkbox matters when your selection touches the canvas edge: checked keeps that border crisp, unchecked feathers it like any other edge.

**Sharpen** (**Select > Sharpen**) does the opposite of feathering — it snaps every partially-selected pixel to fully selected or fully unselected, giving you a hard binary edge. No dialog; it just runs.

**Shrink** (**Select > Shrink…**) pulls the selection boundary inward by a specified number of pixels. It preserves existing feathering, though corners may shift slightly. **Grow** (**Select > Grow…**) pushes the boundary outward by the amount you enter. One quirk: growing a rectangular selection produces rounded corners, because every edge point expands equally (think of inflating a balloon). If you need sharp corners, use **Select > Rounded Rectangle…** with a 0% radius instead.

**Border** (**Select > Border…**) converts your selection into a band that straddles the original edge — half inside, half outside. You choose the width and a border style: **Smooth** preserves antialiasing and generally looks best, **Hard** strips it for a pixel-crisp result, and **Feathered** fades the border outward (though feathering after the fact usually gives better control). The image must have an alpha channel, and the original selection should have been made with antialiasing enabled.

**Invert** (**Select > Invert**, or **Ctrl+I**) flips the selection: everything that was selected becomes unselected, and vice versa. Don't confuse this with **Colors > Invert**, which inverts pixel values.

**Distort** (**Select > Distort…**) randomly deforms the selection contour — useful for organic, roughened edges. The dialog exposes **Threshold** (higher = smaller result), **Spread** and **Granularity** (higher = more deformation), and **Smooth** (higher = less deformation). Results are unpredictable, so experiment freely and undo what doesn't work.
