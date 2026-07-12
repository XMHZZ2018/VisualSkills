# Using Script-Fu Scripts (GIMP 2.10)

Script-Fu is GIMP's built-in scripting engine based on the Scheme language. Think of scripts as powerful macros — they tap directly into GIMP's internal functions to automate repetitive or complex tasks you'd rather not do by hand every time.

## Installing a Script

Drop your downloaded `.scm` file into one of GIMP's script folders. To find (or add) these folders, open **Edit > Preferences**, then navigate to **Folders > Scripts**. Any folder listed there is a valid home for your script.

You don't need to restart GIMP afterward. Just hit **Filters > Script-Fu > Refresh Scripts** and the new script will register itself into the menus. If you can't spot it, try the command search shortcut — press **/** and type part of the script's name. If it still doesn't appear, the script likely has a syntax error.

## Where Scripts Live in the Menus

There are two flavors. *Standalone* scripts don't need an open image — they create one from scratch. Most of the old standalone scripts were removed in 2.10 for looking dated, but you can still grab them from the [gimp-data-extras](https://gitlab.gnome.org/GNOME/gimp-data-extras) repository and install them yourself.

*Image-dependent* scripts operate on whatever you currently have open. You'll find most of them under **Filters**, with some under **Colors**. A few land in context-appropriate spots — for example, **Edit > Paste as… > New Brush** is actually a Script-Fu.

## Quick Troubleshooting

A classic gotcha: you open a script dialog, click **OK** with default values, and nothing visibly happens. The script probably *did* run — check **Edit > Undo** to see if it registered an action. Many scripts make subtle changes (like modifying a channel or adding a layer behind your current one) that aren't immediately obvious on the canvas.
