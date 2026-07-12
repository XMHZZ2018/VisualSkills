# Saving and Exporting Images (GIMP 2.10)

In GIMP 2.10, "saving" and "exporting" are two distinct operations. **File → Save** (Ctrl+S) only writes the native XCF format, which preserves layers, transparency, and undo history — everything about your project. Think of XCF as your working file.

To produce a JPEG, PNG, GIF, or any other common format, you need **File → Export As…** (Shift+Ctrl+E). This opens a file browser where you type a filename with the desired extension (e.g., `photo.jpg`) or pick a format from the **Select File Type** dropdown at the bottom. Once you choose a name and destination, click **Export** to open the format-specific options dialog.

**JPEG** is best for photographs. The Quality slider (0–100) is the main control; the default of 85 works well for most images. Check **Show preview in image window** to eyeball the compression before committing. Under Advanced Options, **Progressive** and **Optimize** are usually worth enabling for web use.

**PNG** is ideal for graphics with sharp edges, text, or transparency. Compression level (up to 9) is lossless — higher just means slower encoding, not lower quality. Leave pixelformat on automatic unless you specifically need 16-bit output.

**GIF** supports only 256 colors and simple transparency. For animations, tick **As animation**, set **Loop forever**, and adjust the delay between frames in milliseconds.

After your first export, a shortcut appears: **File → Export** (Ctrl+E) re-exports to the same file and format without reopening the dialog — handy for iterating. If you originally opened a JPEG or PNG, this command shows as **Overwrite filename.ext**, letting you update the original file in one step.

Keep in mind: exporting does not mark your image as "saved" in GIMP's eyes. You'll still get a warning on close if you haven't done a **File → Save** to XCF. Save your XCF for continued editing; export when you need a deliverable.
