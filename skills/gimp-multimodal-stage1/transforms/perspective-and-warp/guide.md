# Perspective, Warp, and 3D Transform (GIMP 2.10)

The Perspective tool lives at **Tools > Transform Tools > Perspective** (or hit **Shift+P**). Click on your layer and four corner handles appear — drag any of them to skew the image into a new shape. Despite its name, this is really a free-distortion tool; it doesn't enforce vanishing-point rules. Hold **Shift** to constrain handles along edges and diagonals, or **Ctrl** to transform around the center point. When you're happy, click **Transform** in the dialog that appears.

See `fig01.png`.

Since GIMP 2.10.10, the **Readjust** button in that dialog resets the handles back to a square while preserving the transformation you've already applied — handy for building complex distortions in multiple passes.

For true 3D manipulation, grab the 3D Transform tool at **Tools > Transform Tools > 3D Transform** (**Shift+W**). This lets you set a vanishing point, then rotate the layer around X, Y, and Z axes. Hold **Shift** to lock the current axis, **Ctrl** to force Z-axis rotation, or **Alt** to work in the layer's local frame rather than the global one. The "Unified interaction" checkbox in tool options lets you pan, shift the vanishing point, and rotate without switching tabs.

The Cage Transform tool (**Tools > Transform Tools > Cage Transform**, or **Shift+G**) gives you freeform control. Click around the region you want to deform — much like drawing a lasso selection — then close the shape by clicking the starting point. GIMP automatically switches to deform mode: drag any anchor point to warp the enclosed area. Select multiple anchors with **Shift+click** or by rubber-banding a rectangle around them. Press **Enter** to commit.

See `fig02.png`.

Warp Transform (**Tools > Transform > Warp Transform**, shortcut **W**) works like a brush that pushes pixels around directly on the canvas. The default mode is "Move pixels," but the dropdown also offers Grow, Shrink, and Swirl (clockwise or counter-clockwise). Adjust **Size** and **Strength** in tool options to control how far pixels travel per stroke. The "Abyss policy" setting determines what fills areas where data is pulled from outside the layer boundary — options include None (transparent), Clamp (stretch edges), Loop (tile), Black, or White.

One neat trick: the Warp tool's **Animate** section at the bottom of tool options can generate intermediate frames between original and warped states. Set your frame count, click **Create Animation**, and export the resulting image as a GIF with the "As animation" option checked.

If you want a single tool that does it all, the Unified Transform (**Tools > Transform Tools > Unified Transform**, **Shift+L**) combines rotate, scale, shear, and perspective into one operation. Different handle shapes appear on canvas — diamonds for shear, squares for scale, small corner diamonds for perspective. Drag outside the layer to rotate. The pivot (circle with crosshair at center) can be repositioned anywhere, even off-canvas.

See `fig03.png`.
