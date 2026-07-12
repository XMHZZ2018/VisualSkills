# Saving and Exporting Images (GIMP 2.10)

In GIMP 2.10, "saving" and "exporting" are two distinct operations. **Save** writes your work in GIMP's native XCF format — the only format that preserves layers, paths, channels, and undo history. When you need a JPEG, PNG, or any other standard format, you **export** instead.

When you open a non-XCF file (say, a .jpg), GIMP imports it as a new XCF project. The title bar shows an asterisk and "(imported)" to remind you. Use **File > Save** (Ctrl+S) to store the full project as an XCF, or **File > Save As…** (Ctrl+Shift+S) to pick a new name or location. Only XCF is allowed here — if you type a different extension, GIMP will show a mismatch warning and point you toward Export.

To produce a shareable file, go to **File > Export As…** (Shift+Ctrl+E). A file browser lets you choose a destination and filename — the extension you type determines the format. You can also expand **Select File Type** at the bottom to pick from a list. Once you click **Export**, a format-specific options dialog appears.

For **JPEG**, the key setting is the **Quality** slider (0–100). The default of 85 works well for most images; going above 95 rarely helps. Check **Show preview in image window** to judge compression artifacts live. Under **Advanced Options**, **Progressive** is on by default and **Subsampling** defaults to 4:4:4 for best quality — lower subsampling shrinks the file but softens color edges.

See `fig01.png`.

For **PNG**, the dialog is simpler. PNG is lossless, so there's no quality slider — just a **Compression level** (default 9, maximum compression, no quality loss). Check **Interlacing** if the image will load progressively on a web page. The **automatic pixelformat** dropdown lets you force 8-bit or 16-bit output with or without alpha if you need a specific channel layout.

See `fig02.png`.

For **GIF**, remember it's limited to 256 colors and single-bit transparency. Convert your image to indexed mode first (**Image > Mode > Indexed**). The export dialog offers animation controls — **Loop forever**, a default **delay between frames**, and a **frame disposal** mode — which matter when your layers represent animation frames.

**TIFF** supports multiple compression algorithms (LZW, Deflate, JPEG, or none) and since GIMP 2.10.12 can save layers as separate pages. **WebP** gives you a choice between lossless and lossy modes with an image quality slider, plus a **Source Type** hint (Photo, Drawing, Icon, Text) that guides the compressor.

After your first export, a convenient shortcut appears: **File > Export** (Ctrl+E) re-exports to the same file and format without reopening the dialog. If the file was originally imported, this menu item reads **Overwrite filename.ext** — one click to update the original. Note that exporting never clears the "dirty" flag; only saving to XCF does that, so GIMP will still warn you on close if you haven't saved the project.
