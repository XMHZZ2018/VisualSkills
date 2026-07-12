# Selection and Layer Issues (GIMP 2.10)

If GIMP seems to ignore your painting or edits, the culprit is almost always one of these selection or layer problems.

**Floating selection blocking everything.** Open the Layers dialog (**Ctrl+L**) and check if the top entry says "Floating Selection." Until you deal with it, most tools won't work. Either anchor it to the layer below with **Ctrl+H**, or promote it to its own layer with **Shift+Ctrl+N** (right-click the floating selection for both options).

**Selection is hidden.** You may have turned off the marching-ants outline and forgotten. Go to **View > Show Selection** and make sure it's checked — the selection is still active even when invisible.

**Working outside the selection.** If you had a previous selection active, your tools only affect pixels inside it. Use the Quick Mask button to visualize what's actually selected (clear = selected, tinted = masked). To start fresh, hit **Select > None** (**Shift+Ctrl+A**). If the selection looks inverted, use **Select > Invert**.

**Layer is invisible or inactive.** In the Layers dialog, confirm your target layer is highlighted (active) and has the eye icon visible. Click the eye spot to toggle visibility; click the layer name to activate it. If no layer is active, you may have accidentally selected a channel instead — check the Channels dialog.

**Painting outside the layer boundary.** Layers can be smaller than the canvas. Look for a black-and-yellow dashed border — if you're painting beyond it, nothing happens. Fix this with **Layer > Layer to Image Size** to match the canvas, or **Layer > Layer Boundary Size** to set custom dimensions.

**Layer group is selected.** If the active item in the Layers dialog shows a +/− icon, it's a group, not a paintable layer. Expand it and click an individual layer inside to make it active.
