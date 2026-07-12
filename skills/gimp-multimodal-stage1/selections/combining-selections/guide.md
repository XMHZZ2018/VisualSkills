# Adding and Subtracting Selections (GIMP 2.10)

Every selection tool in GIMP has a **Mode** setting in its Tool Options that controls how a new selection interacts with whatever's already selected. You don't need to get your selection perfect in one shot — just combine multiple passes.

**Replace** is the default: each new selection wipes out the old one entirely. That's fine for simple shapes, but the real power comes from the other three modes.

Hold **Shift** while dragging to enter **Add** mode. Your new selection merges with the existing one, expanding the selected area. This is great for grabbing irregular shapes piece by piece — start with a rectangle, then switch to the **Free Select** (Lasso) tool and, still holding **Shift**, loop around the extra region you want to include.

See `fig01.png`.

Hold **Ctrl** while dragging to enter **Subtract** mode. Anything you select now gets carved out of the existing selection. Handy when your initial selection grabbed too much — just subtract the excess.

Hold **Shift**+**Ctrl** together to enter **Intersect** mode. Only the overlap between the new and existing selections survives. Use this when two simple shapes together define a complex region more easily than tracing it by hand.

You don't have to stick with one tool across passes. Make a rectangle select, then add to it with the Ellipse tool, then subtract a sliver with the Lasso — each modifier key works the same regardless of which selection tool is active.

If you still end up with rough edges or tiny selection defects, switch to **Quick Mask** mode for pixel-level touch-ups. Paint white to add to the selection, black to subtract — it's often easier than wrestling with tool outlines at high zoom.
