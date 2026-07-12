# Opening Files (GIMP 2.10)

The quickest way to open an image is **File → Open…** (or **Ctrl+O**). This brings up the Open Image dialog where you can browse to your file. The left panel shows bookmarked Places — add your favorite folders with the **+** button so you're not hunting around every time. Select a file and a preview thumbnail appears on the right; if it looks stale, **Ctrl+click** the preview to regenerate it.

Need to type a path directly? Press **Ctrl+L** to toggle the Location text box at the top of the dialog. It supports auto-completion as you type.

To open an image from the web, use **File → Open Location…** and paste the URL. GIMP downloads and opens it just like a local file.

If you want to add an image into your current project as new layers rather than a separate image, use **File → Open as Layers…** (**Ctrl+Alt+O**). The selected file's layers land on top of your existing layer stack.

Drag-and-drop works too — drop a file onto the Toolbox to open it as a new image, or drop it onto an existing canvas to add it as a layer. You can drag straight from a browser or file manager.

GIMP identifies file types by inspecting magic headers in the file contents, not just the extension. If auto-detection ever fails on an unusual format, expand **Select File Type** at the bottom of the Open dialog and choose manually.

When you open a PDF, an extra dialog lets you pick specific pages (e.g., `4-7,9`), choose whether pages become separate images or layers, and set the resolution. PostScript files get a similar dialog with additional options for coloring mode and antialiasing strength.

If the image carries an embedded color profile, GIMP asks whether to convert to its built-in sRGB workspace or keep the original. Either choice works — GIMP handles conversion internally. Check **Don't ask me again** to silence the prompt (reversible under **Edit → Preferences → Color Management**).
