# Animating with the Plastic Tool (OpenToonz 1.7)

The Plastic tool lets you deform drawings through a mesh-and-skeleton system. You build a triangular mesh over your artwork, place a skeleton inside it, then pose that skeleton across frames — OpenToonz interpolates the deformation for you.

Start by selecting the column/layer containing your artwork (the "texture column"), then activate the **Plastic** tool from the toolbar. Hit **Create Mesh** in the tool options bar to open the mesh dialog. Adjust **Mesh Edges Length** to control triangle density — lower values give smoother bends but cost more at render time. Set **Mesh Margin** to a few pixels to preserve antialiasing, then click **Apply**. A new purple column appears in your Xsheet, and the green wireframe mesh draws over your art in the Viewer.

See `fig01.png`.

To refine the mesh, switch **Mode:** to **Edit Mesh**. You can drag mesh points, or right-click edges to **Swap Edge**, **Collapse Edge**, **Split Edge**, or **Cut Mesh** — useful for adding local density where bends need to be smoother.

With the mesh ready, switch **Mode:** to **Build Skeleton**. Click in the Viewer to place the root vertex (shown as a solid purple square), then keep clicking to chain additional vertices outward. To branch, select an existing vertex first and click elsewhere. You can insert mid-bone vertices by clicking directly on a connecting line, or delete one with **Del**. Enable **Snap To Mesh** in the tool options to lock vertices precisely onto mesh points.

See `fig02.png`.

Once the skeleton is built, switch **Mode:** to **Animate**. Select a vertex and drag it to a new position — a keyframe is created automatically at the current frame. Advance along the timeline, repose the skeleton, and repeat. Enable **Global Key** in the tool options if you want every vertex keyframed simultaneously when you move just one. To lock bone lengths, check **Keep Distance**. Right-click a vertex and choose **Set Rest Key** to snap it back to its original build pose at the current frame.

For overlapping limbs (like an arm crossing in front of a body), set the **SO** (Stacking Order) value per vertex in the tool options — higher values render on top.

If parts of your character should stay rigid (a shield, a belt buckle), switch **Mode:** to **Paint Rigid** and brush red rigidity onto those mesh regions. Paint with **Flex** selected to restore flexibility (green). Right-click in the Viewer while the Plastic tool is active to toggle visibility of mesh wireframe, rigidity shading, stacking order, and skeleton onion skin.

You can also drive vertices with expressions in the Function Editor. The syntax is `vertex(column_number, "vertex_name").angle` — handy for mirroring shoulder rotations or linking joints procedurally.
