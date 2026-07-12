The source document is relatively brief and doesn't reference any inline images. Let me write the practical reference guide based on this content.

# Importing and Exporting SVG Paths (GIMP 2.10)

SVG (Scalable Vector Graphics) is a vector format, meaning shapes stay crisp at any size. GIMP is primarily a raster editor, but its paths are vector entities internally — and they map almost perfectly to SVG path data. That tight compatibility means you can move paths between GIMP and dedicated vector tools like Inkscape without losing fidelity.

**Exporting paths to SVG** happens through the Paths dialog. Open it via **Windows > Dockable Dialogs > Paths**, right-click the path you want to save, and choose **Export Path...**. GIMP writes a clean SVG file containing just the path data — no rasterization, no quality loss. This is handy when you've traced something in GIMP and want to refine it in a proper vector editor.

**Importing paths from SVG** works the same way, in reverse. In the Paths dialog, right-click and select **Import Path...**. Point it at any SVG file — one you made in Inkscape, downloaded from the web, or exported from another GIMP session. The vector outlines land in your Paths list, ready to stroke, fill, or convert to selections.

One nice bonus: GIMP doesn't just import `<path>` elements. It also pulls in basic SVG shapes — rectangles, circles, ellipses, polygons — and converts them into GIMP paths. You won't get fancy SVG filters or text, but geometric primitives come through fine.

Keep in mind that importing a path is different from opening an SVG as an image. If you use **File > Open** on an SVG file, GIMP rasterizes the whole thing into pixels at whatever resolution you choose. The Paths dialog import specifically preserves the vector data as editable paths — that's what you want when you plan to manipulate the outlines further.
A typical workflow: design detailed vector shapes in Inkscape, export as SVG, import the paths into GIMP, then use them as selections or stroke them with GIMP's richer brush engine. It bridges the gap between vector precision and raster creativity.
