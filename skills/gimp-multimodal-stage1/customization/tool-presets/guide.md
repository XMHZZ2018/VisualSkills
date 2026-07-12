# Tool Presets (GIMP 2.10)

Tool presets let you save a specific configuration of any tool — brush size, opacity, dynamics, whatever — and recall it instantly later. If you find yourself constantly re-tweaking the same settings, presets eliminate that friction.

Every tool options dialog has four small buttons along its bottom edge: **Save**, **Restore**, **Delete**, and **Reset**. That's your quickest path to saving whatever you've currently got dialed in, or snapping back to a previously saved state.

For a broader view of everything you've saved, open the Tool Presets Dialog via **Windows > Dockable Dialogs > Tool Presets**. This lists all presets — both the ones GIMP ships with and any you've created — each showing its associated tool icon and a name. Clicking any preset immediately activates that tool with those saved settings.

You can tag presets to organize them however makes sense to you, which is handy once the list grows. Double-click a preset's name to rename it, or double-click its icon to open the Tool Preset Editor.

To create a new preset, select a tool in the Toolbox (or pick an existing preset as a starting point), then hit the **Create a new tool preset** button at the bottom of the dialog. The Tool Preset Editor opens so you can name it and choose which resources to save — you can include or exclude things like the active brush, pattern, gradient, font, or color via checkboxes.

Only presets you've created are fully editable. The built-in ones appear grayed out in the editor, but you can duplicate one by creating a new preset from it and then tweaking the copy. Presets are saved to the first writable folder listed under **Edit > Preferences > Folders > Tool Presets**.

Right-clicking in the dialog gives you a context menu with a few extras: **Copy Tool Preset Location** puts the file path on your clipboard, and **Show in File Manager** opens the preset's folder directly. If you've manually dropped a `.gtp` file into your presets folder, hit **Refresh tool presets** to pick it up without restarting GIMP.

The Tool Preset Editor also has a dock menu option called **Edit Active Tool Preset** — when enabled, the editor automatically tracks whichever preset you select, so you can rapidly flip through and adjust multiple presets in sequence.
