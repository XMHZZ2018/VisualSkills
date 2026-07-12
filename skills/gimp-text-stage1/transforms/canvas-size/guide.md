# Changing Canvas Size (GIMP 2.10)

The canvas is the visible area of your image. It doesn't have to match the layer size — you can grow it to add breathing room around your content, or shrink it to crop things down.

Open the dialog via **Image → Canvas Size…**. You'll see Width and Height fields at the top. By default they're linked with a chain icon, so changing one scales the other proportionally. Click the chain to break the link if you need independent control over each dimension.

Below that, the **Offset** section lets you position your existing image within the new canvas. Drag the preview, type X/Y values directly, or hit **Center** to drop it right in the middle. When shrinking the canvas, you're effectively choosing which part of the image stays visible.

The **Layers** section at the bottom controls what happens to your layers. The "Resize layers" dropdown defaults to **None** (only the canvas changes), but you can pick **All Layers**, **Image-sized layers**, **All visible layers**, or **All linked layers** to resize them along with the canvas. The "Fill with" option sets what fills newly exposed layer area — Transparency, Background color, Foreground color, White, or Pattern.

Once everything looks right, click **Resize**. Any new canvas area will be transparent (checkerboard pattern) until you flatten the image or use **Layer → Layer to Image Size** to extend a layer into that space.

For quick alternatives: **Image → Fit Canvas to Layers** expands the canvas to match your largest layer, and **Image → Fit Canvas to Selection** trims or expands the canvas to exactly match your current selection bounds. No dialog needed — they just do it.
