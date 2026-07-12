# Configuring Preferences (GIMP 2.10)

Open the Preferences dialog via **Edit → Preferences**. A category tree on the left lets you jump between pages — everything from memory allocation to keyboard shortcuts lives here.

**System Resources** is where you tune performance. Bump up the **Tile cache size** if you work with large files (default is 3000 MiB) — this controls how much RAM GIMP uses before swapping to disk. Set **Number of threads** to match your CPU cores, and adjust **Maximum undo memory** based on how aggressively you use undo. Leave **Swap compression** on "Best performance" unless you're tight on disk space.

Under **Interface**, you can change GIMP's language, toggle layer/channel previews, and manage keyboard shortcuts. Enable **Use dynamic keyboard shortcuts** if you want to assign hotkeys by hovering over a menu item and pressing a key combo. Hit **Configure Keyboard Shortcuts** for a full list of assignable actions.

The **Display** page controls how transparency renders (checkerboard style and size) and lets you calibrate your monitor resolution — useful if print-size preview looks off.

For tablet or stylus users, head to **Input Devices**. Click **Configure Extended Input Devices** to map your hardware. Check "Share tool and tool options between input devices" if you don't want separate tool states per device. You can also save or reset device settings from this page.

**Folders** sets the Temp and Swap directories GIMP uses for working data. If your system drive is slow or full, point the swap folder to a faster disk. Under the expandable **Data Folders** sub-pages (Brushes, Patterns, Gradients, etc.), you can add custom search paths so GIMP picks up your downloaded resources at startup — just make sure the folders exist and are writable.

All settings persist in your `gimprc` file, so power users can edit that directly if preferred.
