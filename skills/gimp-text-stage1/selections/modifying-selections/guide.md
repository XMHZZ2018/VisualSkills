# Modifying Selections (GIMP 2.10)

All of these commands live under **Select** in the image menubar. Once you have a selection, these let you reshape it without redrawing.

**Feather** (**Select > Feather...**) softens the selection's edges by blending them into the surrounding area over a pixel radius you specify. You can also feather at selection-creation time with the tool's "Feather Edges" option, but this command lets you add more after the fact. Enable "Selected area continues outside image" if your selection touches the canvas edge and you want that edge to stay crisp.

**Sharpen** (**Select > Sharpen**) does the opposite — it removes any partial transparency on selection edges, snapping everything to fully selected or fully unselected. Useful when you need a hard-edged mask.

**Shrink** (**Select > Shrink...**) pulls the selection boundary inward by a given distance. Feathering is preserved but may warp at sharp corners. **Grow** (**Select > Grow...**) pushes it outward by the same logic. Note that growing a rectangular selection produces rounded corners — if you need sharp corners, use **Select > Rounded Rectangle...** with a 0% radius instead.

**Border** (**Select > Border...**) replaces your selection with a band that straddles its original edge — half inside, half outside. You choose the width and a border style: **Smooth** preserves antialiasing (usually what you want), **Hard** strips it, and **Feathered** fades outward but rarely looks great — better to border then feather separately.

**Invert** (**Select > Invert**, or **Ctrl+I**) flips the selection so everything previously outside is now inside, and vice versa. Don't confuse this with the color-invert filter.

**Distort** (**Select > Distort...**) randomly deforms the selection contour. Tweak **Threshold** (higher = smaller result), **Spread** and **Granularity** (higher = more deformation), and **Smooth** (higher = less deformation) until you get an organic-looking edge. Results are unpredictable — experiment freely.
