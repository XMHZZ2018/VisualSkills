The markdown doesn't reference any inline images. I have all the information I need to write the guide.

# Installing and Using Plugins (GIMP 2.10)

GIMP's power comes largely from plugins — small external programs that run under GIMP's control and can manipulate images in nearly any way you can imagine. Dozens ship with GIMP itself (almost everything under the **Filters** menu is a plugin), and you can grab more from the community whenever you need extra functionality.

Most bundled plugins live transparently inside GIMP's menus. You've probably used them without realizing — "Normalize" for auto color correction, for instance, is a plugin. Even file import and export happen through plugins.

**Finding plugins.** Community plugins are freely available online, but quality varies widely. Stick to trusted sources; plugins are full executables and carry the same security risks as any software you install. Also confirm a plugin targets GIMP 2.10 specifically — major version changes often break compatibility.

**Installing on Linux.** For a single-file plugin like `borker.c`, just run `gimptool-2.0 --install borker.c` in a terminal. It compiles and drops the result into your personal plugin directory (`~/.gimp-2.10/plug-ins`). No root needed. For multi-file plugins, look for an `INSTALL` or `README` inside the directory.

**Installing on Windows.** Many plugins come with an installer that handles placement automatically. If you only get a binary, copy it into a subfolder of your plugin directory — the subfolder name must match the plugin filename. Check **Edit > Preferences > Folders > Plug-ins** to see where GIMP looks.

**Installing on macOS.** If you installed GIMP via Fink or MacPorts, `gimptool-2.0` works the same as on Linux. If you're using the GIMP.app bundle, look for a prebuilt version of the plugin from its author, since compiling your own requires a full GIMP development setup.

**Running an installed plugin.** Restart GIMP after installation. The plugin registers itself somewhere in the menus — usually under **Filters**, but not always. If you can't spot it, press **/** to open the command search and type the plugin's name.

<!-- figure: GIMP Preferences dialog showing the Folders > Plug-ins paths -->

**A few things to keep in mind while using plugins.** If a plugin crashes, GIMP will warn you about possible corruption — in practice this is rare, and you can usually keep working. Avoid editing an image while a plugin is actively processing it; the plugin won't know about your changes and may produce wrong results or crash. Run one plugin at a time on a given image to keep the undo history intact.
