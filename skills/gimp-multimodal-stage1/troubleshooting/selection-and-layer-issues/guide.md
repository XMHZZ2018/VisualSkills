# Selection and Layer Issues (GIMP 2.10)

When GIMP suddenly won't let you paint, filter, or do much of anything, the culprit is almost always one of a handful of selection or layer problems. Here's how to identify and fix each one.

**Floating selection blocking everything.** If most actions are greyed out, open the Layers dialog (**Ctrl+L**) and check whether the top entry says "Floating Selection." You need to deal with it before GIMP will let you do anything else. Either anchor it to the layer below with **Ctrl+H**, or promote it to its own layer with **Shift+Ctrl+N** (right-click the floating selection for both options).

See `fig01.png`.

**Hidden selection outline.** Sometimes you've toggled off the marching ants to get a cleaner view and then forgotten about it. If your tools seem to only affect part of the canvas for no obvious reason, go to **View > Show Selection** and make sure it's checked. The selection is still active even when its outline is invisible.

**Working outside the selection.** You may have an old selection still active somewhere you're not looking. If you can't see any marching ants but painting still does nothing, there might be a tiny or off-screen selection. Clear it with **Select > None** (**Shift+Ctrl+A**). If you *can* see a selection but it seems inverted, toggle the Quick Mask button to visualize it — the clear area is selected, the tinted area is not. Fix an inverted selection with **Select > Invert**.

**Invisible layer.** Open the Layers dialog and confirm your target layer is both active (highlighted) and visible (eye icon showing on the left). If the eye is missing, click in that space to restore visibility. If the wrong layer is highlighted, click the correct one to activate it.

**Acting outside the layer boundary.** Layers can be smaller than the canvas. Look for a black-and-yellow dashed border — if you're painting beyond it, nothing will happen. Fix this with **Layer > Layer to Image Size** to snap the layer bounds to the full canvas, or **Layer > Layer Boundary Size** to set custom dimensions.

**Layer group selected.** If you get a "Cannot paint on layer groups" error, you've accidentally selected the group header instead of an individual layer. Expand the group (click the + icon) in the Layers dialog and click directly on the layer you actually want to edit.
