# Using the Python Console (QGIS 3.44)

Open the console from **Plugins > Python Console** or press `Ctrl+Alt+P`. You can also click the **Python Console** icon in the Plugins toolbar. What appears is a small interactive shell docked at the bottom of QGIS — an input line, an output area, and a toolbar across the top.

See `fig01.png`.

The console pre-imports the modules you'll reach for most often: `qgis.core`, `qgis.gui`, `processing`, the main Qt modules, plus Python's `math`, `os`, `re`, and `sys`. Just start typing — no boilerplate needed. Press `Enter` to execute a command, or use `Up`/`Down` arrows to scroll through your command history. Hit `Ctrl+Shift+Space` to pop open the full history list and double-click any previous command to re-run it.

Auto-completion covers PyQGIS, PyQt5, GDAL/OGR, and standard Python. Trigger it manually with `Ctrl+Alt+Space`. You can also run shell commands directly by prefixing them with `!` — for example, `!gdalinfo --version` — and even capture output into a variable with `var = !cmd`.

A handy trick: select any text in the output area (even lines with `>>>` prompts) and press `Ctrl+E` to re-execute it. Great for tweaking a one-liner you ran a few minutes ago.

When you need more than a one-liner, click **Show Editor** in the toolbar. This opens a full code editor panel alongside the console. It supports tabbed editing, syntax highlighting, auto-completion (`Ctrl+Space`), automatic indentation, and bracket matching.

See `fig02.png`.

Run your entire script with `Ctrl+Shift+E`, or highlight a section and press `Ctrl+E` to run just that selection. Results appear in the interactive console output. Use `Ctrl+S` to save, **Toggle comment** (`Ctrl+:`) to comment blocks, and **Reformat code** (`Ctrl+Alt+F`) to auto-format with your configured formatter. The **Object Inspector** (enable it in Python settings) gives you a tree view of classes and functions in your script — click one to jump to its definition.

You can share scripts directly to GitHub as a Gist, check syntax with `Ctrl+4`, and dock or undock the editor with the **Dock Code Editor** button. For console-wide settings — font, auto-completion behaviour, formatter rules — click **Options…** in the toolbar.
