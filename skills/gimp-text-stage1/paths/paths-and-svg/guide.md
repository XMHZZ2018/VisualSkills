No inline image references in this file. I have all the information I need to write the guide.

# Importing and Exporting SVG Paths (GIMP 2.10)

SVG (Scalable Vector Graphics) is a resolution-independent vector format, and GIMP paths map almost perfectly to SVG path data — so you can move paths between GIMP and dedicated vector editors like Inkscape without losing information.

To **export** a path, open the **Paths dialog** (accessible via **Windows > Dockable Dialogs > Paths**), right-click the path you want to save, and choose **Export Path…**. Save it as an `.svg` file. The resulting file preserves every anchor point and curve handle exactly as you drew them.

To **import** a path from an SVG file, right-click in the **Paths dialog** and select **Import Path…**. Browse to your `.svg` file and confirm. The path appears in the dialog ready for stroking, selecting, or further editing.

GIMP can also load SVG shapes that aren't bare paths — rectangles, circles, ellipses, polygons — and converts them into editable paths on import. This is handy when you receive artwork from a vector app and only need the outlines.

If you want to open an entire SVG as a rasterized image instead, just use **File > Open…** and select the SVG file directly. GIMP will render it to pixels at whatever resolution you choose in the import dialog.

The real power here is the round-trip workflow: sketch rough paths in GIMP, export to SVG, refine them in Inkscape's more powerful node tools, then import back into GIMP for painting or compositing.
