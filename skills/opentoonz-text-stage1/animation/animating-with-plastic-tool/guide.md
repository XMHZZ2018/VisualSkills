# Animating with the Plastic Tool (OpenToonz 1.7)

The **Plastic** tool deforms drawings via a triangular mesh controlled by a skeleton. Select the column/layer containing your artwork, activate the **Plastic** tool, and click **Create Mesh** in the Tool Options bar. Adjust **Mesh Edges Length** for density — lower values give smoother bends but cost more to compute — then hit **Apply**. A purple mesh column appears in the Xsheet, linked to your texture column.

To refine the mesh, set **Mode: Edit Mesh**. You can drag mesh points, or right-click an edge to **Swap Edge**, **Collapse Edge**, **Split Edge**, or **Cut Mesh** for finer local control.

Switch to **Mode: Build Skeleton** to lay down vertices. Your first click places the root (solid purple square, static during animation). Each subsequent click adds a connected child vertex. Insert mid-bone vertices by clicking directly on a connecting line; branch by selecting an existing vertex before clicking a new position. Enable **Snap To Mesh** to lock vertices precisely to mesh points.

With the skeleton built, set **Mode: Animate**. Select a vertex, drag it to a new pose, and a keyframe is created automatically at the current frame. Advance frames and repose to build your motion. Enable **Keep Distance** to lock bone lengths, or **Global Key** to keyframe every vertex when you move just one. Right-click a vertex for **Set Rest Key** (resets one vertex) or **Set Global Rest Key** (resets the whole skeleton to its build pose).

For overlapping limbs, type a **SO** (Stacking Order) value in the Tool Options bar per vertex — higher values render on top.

Use **Mode: Paint Rigid** to brush rigidity directly onto the mesh. Paint with **Rigid** (turns areas red and stiff) or **Flex** (restores green, bendable areas). Adjust **Thickness** to control brush size.

A mesh can hold multiple skeletons — press **+** beside the **Skeleton:** dropdown to add one, useful for turnarounds or shape changes. Delete unwanted skeletons with **-**. Keyframes in the Function Editor live under **Plastic Skeleton** and expose per-vertex **Angle**, **Distance**, and **SO** channels. You can link vertices with expressions like `vertex(2, "Shoulder_right").angle * -1` for automatic mirrored motion.

Right-click the Viewer while the Plastic tool is active to toggle display of **Show Mesh**, **Show Rigidity**, **Show SO**, and **Show Skeleton Onion Skin** independently.
