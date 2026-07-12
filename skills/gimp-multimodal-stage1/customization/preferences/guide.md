# Configuring Preferences (GIMP 2.10)

Open the Preferences dialog from **Edit > Preferences**. On the left you'll see a tree of category pages — click any one to jump straight to its settings. Everything you change here is saved to your personal `gimprc` file automatically.

See `fig01.png`.

**System Resources** is where you tell GIMP how much of your machine it can use. The key values are *Tile cache size* (how much RAM GIMP claims before swapping to disk — set this to about 50–75% of your physical RAM for best performance), *Number of threads* (match your CPU core count), and *Minimum undo levels* (defaults to 5, raise it if you undo often). Swap compression defaults to "Best performance," which is fine for most setups. You can also toggle automatic update checks and set thumbnail sizes for the file-open dialog here.

See `fig02.png`.

**Interface** controls language, preview thumbnails, and keyboard shortcuts. Switch GIMP's language from the dropdown at the top (requires a restart). Under Previews, you can enable or disable layer/channel thumbnails and adjust their size. The Keyboard Shortcuts section lets you enable dynamic shortcuts — hover a menu item and press a key combo to bind it on the fly. Use **Configure Keyboard Shortcuts** for a searchable list of all actions and their bindings. If you want your shortcuts to persist, keep "Save keyboard shortcuts on exit" checked.

Under **Display**, you can change the checkerboard style used to indicate transparency and calibrate your monitor resolution. The calibration tool is a bit playful — grab a soft ruler and match on-screen measurements to real-world inches.

**Input Devices** is essential if you use a drawing tablet. Click **Configure Extended Input Devices** to map your stylus buttons, pressure curves, and tilt. You can also choose whether all input devices share the same active tool or each remembers its own. Below that, **Input Controllers** lets you assign actions to mouse-wheel events and arrow-key combinations — handy for binding zoom or brush-size changes to hardware you already reach for.

**Folders** at the bottom of the tree controls where GIMP looks for temporary files and swap space. Point the swap folder at a fast disk with plenty of free space if you work with large images. The sub-pages (Brushes, Patterns, Gradients, etc.) each define a search path — a personal folder (writable, for your custom resources) and a system folder (read-only, shipped with GIMP). Add new directories with the folder-chooser button and reorder them with the arrow buttons to control loading priority.

See `fig03.png`.
