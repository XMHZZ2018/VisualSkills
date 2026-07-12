# Tool Presets (GIMP 2.10)

Tool presets let you save your favorite tool configurations and recall them instantly — no more re-dialing settings every time you switch tasks.

Every tool options dialog has four buttons at the bottom: **Save**, **Restore**, **Delete**, and **Reset**. Hit **Save** to snapshot your current settings into a named preset you can pull up later.

To see all your presets in one place, open **Windows > Dockable Dialogs > Tool Presets**. Clicking any preset in the list activates that tool with its saved settings immediately. You can tag presets to organize them however you like — by project, by technique, whatever works.

To create a new preset, select a tool in the Toolbox (or pick an existing preset as a starting point), then click **Create a new tool preset** at the bottom of the dialog. The Tool Preset Editor opens so you can name it and choose which resources (brush, pattern, gradient, etc.) get saved with it.

Double-click a preset's icon to open the editor, or double-click its name to rename it inline. In the editor you can change the icon and toggle which settings are included. Note: built-in presets that ship with GIMP are read-only — duplicate one first if you want to tweak it.

Right-click a preset for extra options like **Copy Tool Preset Location** (grabs the file path) or **Show in File Manager** to find the `.gtp` file on disk. If you manually drop preset files into your `tool-presets` folder, hit **Refresh tool presets** to pick them up.

Presets are stored in the first writable path listed under **Edit > Preferences > Folders > Tool Presets**, so you can back them up or share them across machines easily.
