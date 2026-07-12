# Customizing the Interface (QGIS 3.44)

QGIS ships with a lot of UI surface, but you don't have to live with all of it. Panels, toolbars, and even individual menu items can be toggled on or off depending on what you actually use day to day.

**Showing and hiding panels** is done from **View > Panels**. That submenu lists every available panel — Layers, Browser, Processing Toolbox, Layer Styling, and so on. Tick or untick each one to control what's docked around your map canvas. You can also right-click any toolbar or the menu bar itself to get the same checklist. Panels can be dragged to new positions, stacked as tabs, or floated as independent windows.

**Toggling toolbars** works the same way: **View > Toolbars** (or right-click the toolbar area). Each entry — Map Navigation, Digitizing, Attributes, Selection, etc. — can be individually shown or hidden. If a toolbar goes missing, that's always where to recover it.

For quick full-screen workflows, use **View > Toggle Panel Visibility** (`Ctrl+Tab`) to hide all panels at once while keeping toolbars, or **View > Toggle Map Only** (`Ctrl+Shift+Tab`) to strip the interface down to just the map canvas. Hit the same shortcut again to bring everything back.

When you need deeper control — removing specific menu entries, hiding individual buttons, or disabling dialogs entirely — open **Settings > Interface Customization**. Tick **Enable customization** at the top, then uncheck any item in the tree: whole menus, specific toolbar buttons, status bar elements, or even widgets inside dialogs. Use the search box to find items by name, or click the "catch widget" tool and then click anything in the main window to locate it in the tree instantly.

See `fig01.png`.

Changes in the Customization dialog take effect after a restart. You can export your configuration to a `.ini` file with **Save To File** and share it across machines — handy for deploying a simplified QGIS to a team. To undo everything, uncheck **Enable customization** or hit the **Check All** button, then restart.

If you just want to reset the whole UI without touching customization settings, go to **Settings > Options > System** and click **Reset user interface to default settings** — this restores all panels and toolbars to their factory positions after a restart. You can also launch QGIS from the command line with `qgis --nocustomization` to bypass all interface customization in a single session.
