No referenced images exist in this directory — just the markdown. I have enough from the source text to write the guide.

# Using the Python Console (QGIS 3.44)

Open the console via **Plugins → Python Console** or press `Ctrl+Alt+P`. You can also click the **Python Console** icon in the Plugins toolbar. This gives you an interactive Python shell right inside QGIS, pre-loaded with modules like `qgis.core`, `qgis.gui`, `QtWidgets`, `os`, `re`, and `math` — no imports needed.

Type commands in the input area at the bottom and press `Enter` to execute. Results appear in the output area above. Use the `Up`/`Down` arrow keys to cycle through your command history, or hit `Ctrl+Shift+Space` to browse it in a popup. Auto-completion is available with `Ctrl+Alt+Space`.

You can run shell commands directly by prefixing with `!` — for example, `!gdalinfo --version` or `var = !ogrinfo --formats | grep SQL` to capture output into a variable. To re-run something from the output panel, select the text and press `Ctrl+E` (it strips `>>>` prompts automatically).

For anything longer than a one-liner, click **Show Editor** on the toolbar to open the built-in code editor. It supports tabs, syntax highlighting, auto-indent, and code completion (`Ctrl+Space`). Run the entire script with `Ctrl+Shift+E`, or highlight a block and run just that selection with `Ctrl+E`. Save scripts with `Ctrl+S`, reformat code with `Ctrl+Alt+F`, and toggle comments with `Ctrl+:`.

Handy special commands in the console: type `_api` to open the C++ API docs, `_pyqgis` for the Python API docs, `_cookbook` for the PyQGIS Cookbook, or `?` for quick help. Click **Options…** on the toolbar to configure editor behavior, formatting rules, and the object inspector.
