# Using Script-Fu Scripts (GIMP 2.10)

Script-Fu is GIMP's built-in scripting language based on Scheme. Think of scripts as powerful macros — they automate repetitive tasks or complex sequences you'd rather not do by hand every time.

To install a new script, drop the `.scm` file into one of GIMP's script folders. You can find (or add) these paths under **Edit > Preferences > Folders > Scripts**. Once the file is in place, refresh without restarting GIMP by going to **Filters > Script-Fu > Refresh Scripts**. The new script should now appear somewhere in the menus.

If you can't locate it, check under **Filters** first — that's where most land. You can also hit **/** to open the command search and type the script's name. If it doesn't show up at all, there's likely a syntax error in the file.

There are two flavors of Script-Fu. *Standalone* scripts create images from scratch and don't need an open file. Most of the old standalone scripts were removed in 2.10 for looking dated, but you can still grab them from the [gimp-data-extras](https://gitlab.gnome.org/GNOME/gimp-data-extras) repository. *Image-dependent* scripts operate on your current image and typically live under **Filters** or **Colors**. A few end up in more logical spots — for example, **Edit > Paste as... > New Brush**.

A common gotcha: you run a script, click **OK**, and nothing seems to happen. Before assuming it's broken, check **Edit > Undo**. If the script did its job, it'll be listed as the last undo action — the changes may just be subtle.
