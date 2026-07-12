# Converting Between Paths and Selections (GIMP 2.10)

Paths and selections are closely related in GIMP, and you can freely convert between them. The key thing to understand is that a path is one-dimensional (just an outline), while a selection is two-dimensional (an area that can be partially selected). That means converting a selection to a path loses any feathering or partial-selection info — you'll get a hard-edged, all-or-nothing outline back if you round-trip it.

## Selection to Path

To turn your current selection into a path, go to **Select > To Path**. The marching ants won't disappear — GIMP keeps both the selection and the new path alive. You'll find the resulting path over in the Paths dialog. From there you can grab the **Paths** tool and tweak individual anchor points to refine the outline with more precision than the selection tools typically allow.

The Selection Editor and Paths dialog also offer advanced options for this conversion if you need finer control over how closely the path traces the selection boundary.

## Path to Selection

Going the other direction is just as straightforward. With your path active, choose **Select > From Path** or hit **Shift+V**. If your path isn't closed, GIMP will connect the endpoints with a straight line to form a complete selection boundary. The original path stays untouched — you're just generating a new selection from it.
You can also click the **Path to Selection** button at the bottom of the Paths dialog for quick one-click access without touching the menu.

## When This Is Useful

This workflow shines when you need to make a rough selection with something fast (like the fuzzy select or lasso tool), convert it to a path, then fine-tune the curves with Bézier precision. Just remember: once you go through the selection-to-path-to-selection round trip, any soft edges from feathering will be gone — similar to running **Select > Sharpen** on the original selection.
