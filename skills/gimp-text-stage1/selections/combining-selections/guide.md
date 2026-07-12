# Adding and Subtracting Selections (GIMP 2.10)

Every selection tool in GIMP has a mode setting in its **Tool Options** that controls how a new selection interacts with an existing one. By default you're in **Replace** mode — each new selection wipes out the old one. That's fine for starting fresh, but the real power comes from combining selections.

Hold **Shift** while drawing a new selection to enter **Add** mode. The new area merges with whatever's already selected — great for building up irregular shapes from simple ones. For example, start with a rectangle, grab the Free Select (Lasso) tool, hold **Shift**, and trace around an adjacent region to include it.

Hold **Ctrl** to enter **Subtract** mode. Anything you select gets carved out of the existing selection. This is how you punch holes or trim edges without starting over.

Hold **Shift+Ctrl** together for **Intersect** mode. Only the overlap between your new selection and the existing one survives — useful when you need the area where two shapes meet.

These modifier keys work with any selection tool (Rectangle, Ellipse, Free Select, Fuzzy Select, By Color, etc.), so you can mix tools freely. Start with **Select by Color** to grab a rough region, then subtract stray bits with the Lasso while holding **Ctrl**.

For precise touch-ups that are hard to nail with selection tools alone, switch to **Quick Mask** mode to paint corrections directly onto your selection.
