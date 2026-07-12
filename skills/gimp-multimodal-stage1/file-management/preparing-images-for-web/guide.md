# Preparing Images for the Web (GIMP 2.10)

The goal is simple: make your images look good while keeping file sizes small enough that pages load quickly. The format you choose depends on what's in the image.

Use **JPEG** for photographs — they handle millions of colors and complex detail gracefully. Use **PNG** for anything with flat colors, sharp edges, or fewer tones: icons, buttons, screenshots, logos. PNG compression is lossless, so crank it to maximum without worry — it won't degrade quality or slow down display, it just takes a moment longer to export.

When your image has an alpha channel you don't need (most photos won't, but graphics often do), flatten it before export via **Image > Flatten Image**. This merges everything onto a solid background and drops the transparency data, trimming file size. Only keep the alpha channel if you actually need transparent or semi-transparent areas in your final output.

To squeeze a PNG even smaller without changing dimensions, convert to Indexed mode via **Image > Mode > Indexed**. This reduces the palette to 256 colors. It works great for simple graphics but avoid it for photographs or anything with smooth gradients — you'll get ugly banding.

See `fig01.png`.

For JPEG exports, open **File > Export As**, type a `.jpg` extension, and hit **Export** to reach the quality dialog. The default settings strike a safe balance. If you want to go smaller, drag the **Quality** slider down — a value around 75 still looks solid for most web use while cutting file size dramatically. Enable **Show preview in image window** so you can judge degradation in real time. Be aware that every re-save as JPEG compounds quality loss, so keep your lossless XCF or PNG as the master copy.

See `fig02.png`.

For images that need transparency on the web, PNG with alpha is the modern standard. Make sure an alpha channel exists — check the **Windows > Dockable Dialogs > Channels** dialog for an "Alpha" entry, or add one via **Layer > Transparency > Add Alpha Channel**. The checkerboard pattern you see on canvas represents transparent pixels. Export as PNG and the transparency carries through cleanly, including soft semi-transparent edges that GIF could never handle.

See `fig03.png`.
