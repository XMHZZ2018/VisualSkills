# Converting Between Paths and Selections (GIMP 2.10)

Paths and selections are interchangeable in GIMP, but they live in different dimensions. A selection is a 2D area (pixels can be partially selected), while a path is a 1D outline. That means converting between them isn't lossless — any feathering or partial selection gets flattened into a hard-edged, all-or-none boundary, similar to running **Select > Sharpen**.

**Selection to Path:** Go to **Select > To Path**. The image won't visibly change, but a new path appears in the Paths dialog. From there you can grab the **Path tool** and fine-tune the outline with full Bézier precision — handy when the marching ants got *almost* the right shape but need cleanup.

You can also reach this through the **Selection Editor** or the **Paths dialog** itself, which exposes advanced conversion options for tweaking how closely the path traces the selection boundary.

**Path to Selection:** Go to **Select > From Path**, click the **Path to Selection** button in the Paths dialog, or hit **Shift+V**. If your path isn't closed, GIMP connects the endpoints with a straight line before converting. The original path stays intact — you're creating a selection *from* it, not replacing it.

This round-trip is great for precision work: make a rough selection with any selection tool, convert to a path, adjust the curves by hand, then convert back to a crisp selection for masking or editing.
