# Creating and Editing Paths (GIMP 2.10)

Paths are vector Bézier curves — resolution-independent shapes you can stroke, fill, or convert to selections. Grab the Paths tool via **Tools → Paths** or press **B**.

Make sure the Tool Options are set to **Design** mode. Click anywhere on the canvas to place your first anchor point, then click elsewhere to add more — each new point connects to the previous one with a straight segment. To curve a segment, just click-drag it; handles will appear at each anchor letting you sculpt the bend. Drag a handle to control the curve's direction and intensity.

Close a path by holding **Ctrl** and clicking the first anchor point. Once closed, hit **Create selection from path** in Tool Options to get marching ants, or use **Fill path** / **Stroke path** to paint it directly.

Switch to **Edit** mode (hold **Ctrl** to toggle) for finer surgery: click a segment to insert a node, **Shift+Ctrl**-click a node or segment to delete it, or drag a node to sprout a new handle. In **Move** mode (**Alt** or **Ctrl+Alt** toggles), drag the path to reposition it — clicking outside the path moves all components at once.

Hold **Shift** and click empty canvas to start a disconnected subpath within the same path object. Select multiple nodes with **Shift**-click, then drag to move them together. The **Polygonal** checkbox in Tool Options restricts everything to straight segments if curves aren't needed.

Paths survive in the **Paths dialog** (**Windows → Dockable Dialogs → Paths**) and are saved with XCF files. You can copy paths between images via that dialog's context menu. Any Transform tool (Rotate, Scale, Perspective) can target a path — just set the **Transform:** option to "Path" in Tool Options. Use transform-lock icons to link a path and layer so they scale or rotate together.
