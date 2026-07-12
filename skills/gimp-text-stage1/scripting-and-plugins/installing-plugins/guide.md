# Installing and Using Plugins (GIMP 2.10)

GIMP plugins are external programs that extend GIMP's capabilities — everything in the **Filters** menu is actually a plugin, and many core features like image import/export and color correction (Normalize) are plugins too. Several dozen ship with GIMP and work out of the box.

To find additional plugins, browse community sites and repositories. Before downloading, confirm the plugin is compatible with GIMP 2.10 — plugins built for other major versions may not work correctly. Only install plugins from sources you trust, since they run as full executables on your system.

To install a downloaded plugin, place it in your personal plugin directory under `~/.gimp-2.10/plug-ins/`. Each plugin must live in its own subfolder named identically to the plugin file. You can check or add plugin search paths via **Edit > Preferences > Folders > Plug-ins**.

On Linux, a single-file C plugin like `borker.c` can be compiled and installed in one shot with `gimptool-2.0 --install borker.c`. On Windows, most plugins come with an installer or a ready-to-copy binary — just drop it into a recognized plugin folder. On macOS with a package manager (Fink, DarwinPorts), installation works the same as Linux.

After installing, restart GIMP. To find your new plugin in the menus, press **/** to open the command search and type the plugin's name — the menu path is determined by the plugin itself.

While using plugins, avoid editing the image with other tools until the plugin finishes. If a plugin crashes, GIMP will warn you about possible corruption — in practice this is rare, but save your work if you're mid-project. Don't run multiple plugins on the same image simultaneously, as this can corrupt the undo history.
