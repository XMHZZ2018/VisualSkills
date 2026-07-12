# Layer Masks (GIMP 2.10)

A layer mask controls which parts of a layer are opaque, semi-transparent, or fully transparent — all without permanently altering your pixels. White areas on the mask reveal, black areas hide, and grays give you partial transparency.

**Adding a mask:** Select your target layer, then go to **Layer → Mask → Add Layer Mask**. In the dialog, choose how to initialize it — **White (full opacity)** leaves everything visible so you can paint away what you don't want, while **Black (full transparency)** hides everything so you paint in what you do want. You can also seed the mask from the current **Selection**, the layer's **alpha channel**, or a stored **Channel**. Check **Invert Mask** at the bottom to flip the result.

**Editing the mask:** Once added, a mask thumbnail appears beside the layer in the Layers dialog. Click that thumbnail (or use **Layer → Mask → Edit Layer Mask**) to direct your painting to the mask instead of the layer content — a white border on the thumbnail confirms you're editing the mask. Paint with black to hide, white to reveal, or gray for partial transparency. Click back on the layer thumbnail when you're done.

**Previewing and disabling:** Use **Layer → Mask → Show Layer Mask** to view the mask as a grayscale overlay directly on the canvas. **Layer → Mask → Disable Layer Mask** temporarily turns off the mask's effect without removing it — handy for before/after comparisons.

**Applying the mask:** When you're satisfied, **Layer → Mask → Apply Layer Mask** permanently merges the mask's transparency into the layer's alpha channel and removes the mask. This is destructive — the mask is gone after this.

**Deleting the mask:** If you want to discard the mask entirely without affecting the layer, use **Layer → Mask → Delete Layer Mask**. The layer returns to its original state as if the mask never existed.

**Mask to Selection:** You can convert any mask into a selection via **Layer → Mask → Mask to Selection**. White regions become selected, black becomes unselected, and grays become feathered selections. The mask itself stays intact. Variants like **Add to Selection**, **Subtract from Selection**, and **Intersect with Selection** let you combine the mask with an existing selection.
