# Opening Files (GIMP 2.10)

The most common way to open an image is **File > Open…** (or **Ctrl+O**). This brings up the Open Image dialog, where you can browse to your file using the folder tree on the left. The **Places** panel gives you quick access to bookmarks — hit the **+** button to save any frequently-used folder there, or **-** to remove one. When you select an image file in the center pane, a preview thumbnail and basic metadata appear on the right.

See `fig01.png`.

You can type a path directly into the **Location** text box at the top. If you don't see it, press **Ctrl+L** or click the pencil-and-paper icon to toggle it on. Start typing a filename and GIMP will auto-complete it for you.

GIMP identifies file types by inspecting their contents ("magic headers"), not just the extension. In rare cases where it can't figure out the format, expand **Select File Type** at the bottom of the dialog and pick it manually.

If you want to pull an image from the web, use **File > Open Location…** instead. A small dialog appears where you paste a URL, and GIMP fetches and opens the image directly.

To add an image into an already-open file as new layers rather than opening it separately, use **File > Open as Layers…** (**Ctrl+Alt+O**). It uses the same browsing dialog but drops the result on top of your current layer stack.

Drag-and-drop works too. Drag a file onto the GIMP Toolbox to open it as a new image, or drag it onto an existing canvas to add it as a new layer. This even works from web browsers — drag an image straight out of Firefox into GIMP.

When you open a non-XCF image that has an embedded color profile, GIMP will ask whether to convert it to the built-in sRGB workspace or keep the original profile. Either choice is fine; GIMP handles conversion internally. Check **Don't ask me again** if you'd rather skip that prompt in the future (you can re-enable it under **Edit > Preferences > Color Management**).

For PDFs and PostScript files, GIMP shows an extra import dialog where you specify which pages to load (e.g., `4-7,9`), whether to open them as separate images or as layers in one image, and what resolution to render at. Enable **Use Anti-Aliasing** to keep text smooth.
