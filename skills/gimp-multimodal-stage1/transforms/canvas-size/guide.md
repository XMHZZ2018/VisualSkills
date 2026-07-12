# Changing Canvas Size (GIMP 2.10)

The "canvas" in GIMP is simply the visible area of your image. It doesn't have to match your layer sizes — you can grow it to add breathing room around your content, or shrink it to crop things down. Layers that extend beyond the canvas still exist; they're just hidden from view.

To get started, head to **Image > Canvas Size…** to open the Set Image Canvas Size dialog. You'll see fields for **Width** and **Height** at the top — type in your new dimensions. By default a chain icon links them together so they scale proportionally. Click the chain to break it if you want to adjust width and height independently. You can switch units from pixels to percent or anything else using the dropdown.

See `fig01.png`.

Below that you'll find the **Offset** section with **X** and **Y** values. These control where your existing image sits within the new canvas. You can type coordinates directly, use the arrow keys for fine nudging, or just drag the image around in the preview. Hit the **Center** button to instantly place your image dead-center on the canvas.

The **Layers** section at the bottom gives you a "Resize layers" dropdown. The default is **None**, meaning only the canvas changes and your layers stay as-is. You can also choose **All Layers**, **Image-sized layers**, **All visible layers**, or **All linked layers** depending on what should expand with the canvas. The "Fill with" option controls what fills the new space on resized layers — transparency, a color, or a pattern.

Once everything looks right, click **Resize**. If you enlarged the canvas without resizing layers, the new area will be transparent (shown as a checkerboard). You can flatten the image, use **Layer > Layer to Image Size** on the active layer, or add a new filled layer behind everything to cover that empty space.

For quick alternatives: **Image > Fit Canvas to Layers** instantly expands the canvas to match your largest layer, and **Image > Fit Canvas to Selection** trims or grows the canvas to match whatever you have selected. Both are one-click operations with no dialog — handy when you've pasted or moved something outside the current canvas bounds.
