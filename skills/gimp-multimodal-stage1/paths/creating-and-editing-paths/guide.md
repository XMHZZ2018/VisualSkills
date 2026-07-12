# Creating and Editing Paths (GIMP 2.10)

Paths are Bézier curves — smooth, resolution-independent vector outlines you can stroke, fill, or convert into selections. They're lightweight (just stored coordinates), so you can have dozens without taxing your system.

Grab the Paths tool from **Tools > Paths**, click the pen-curve icon in the Toolbox, or just press **B**. Make sure the tool options are set to **Design** mode. Then click anywhere on the canvas to drop your first anchor point, and click again elsewhere to place a second — a straight segment connects them automatically. Keep clicking to add more points. A small "+" beside your cursor confirms you're still adding nodes.

See `fig01.png`.

To curve a segment, click-drag directly on the line between two anchors. Two handles sprout from the nearby anchor points — drag these to reshape the curve. The direction and length of a handle control how the path bends as it leaves that anchor. By default the two handles on a node move symmetrically; release the mouse button and move them independently, or hold **Shift** to re-lock symmetry.

See `fig02.png`.

Close a path by holding **Ctrl** and clicking the starting anchor. Once closed, hit the **Create selection from path** button in Tool Options (or press **Enter**) to turn it into a marching-ants selection. You can also use **Fill path** or **Stroke path** from Tool Options to paint directly along the outline.

Switch to **Edit** mode (hold **Ctrl** to toggle) when you need surgical changes: click a segment to insert a node, **Shift+Ctrl**-click a node or segment to delete it, or drag a bare node to pull out a new handle. **Move** mode (**Alt** or **Ctrl+Alt** toggle) lets you reposition an entire component or the whole path at once.

A path can contain multiple disconnected components — hold **Shift** and click in empty space to start a new subpath within the same path object. Each component can be open or closed independently.

Transform tools (Rotate, Scale, Perspective, etc.) work on paths too. In the transform tool's options, set **Transform:** to **Path**, and the active path will be reshaped without touching your pixels. Use the lock-chain icons in the Paths dialog to transform a path and a layer together in one operation.

Paths persist in GIMP's native XCF format. Manage them in **Windows > Dockable Dialogs > Paths** — from there you can rename, reorder, duplicate, or drag a path into another image window.
