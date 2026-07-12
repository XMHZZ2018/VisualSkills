# Customizing the Interface (QGIS 3.44)

The quickest way to toggle panels and toolbars is to right-click any toolbar or the menu bar — a checklist appears letting you tick on or off whatever you need. You can also reach these lists via **View > Panels** and **View > Toolbars** (on Linux KDE, look under **Settings** instead).

For a distraction-free canvas while digitizing or presenting, hit `Ctrl+Tab` to hide all panels at once (same shortcut brings them back). Go further with **View > Toggle Map Only** (`Ctrl+Shift+Tab`), which strips away panels, toolbars, menus, and the status bar, leaving just the map. Pair it with `F11` for full-screen and you have a clean presentation view.

For permanent, fine-grained control, open **Settings > Interface Customization**. Tick **Enable customization**, then uncheck any menu, sub-menu, toolbar icon, panel, status bar element, or individual widget you want gone. The **Switch to catching widgets in main application** button is especially handy — click any element on the main QGIS window and its entry gets unchecked automatically. You can also search items by name in the dialog's search box. Hit **Apply**, then restart QGIS for changes to take effect.

Customization configs can be saved to a `.ini` file and loaded on another machine, making it easy to roll out a simplified interface across a team. To undo everything, uncheck **Enable customization** or run `qgis --nocustomization` from the command line. You can also reset via **Settings > Options > System** and pressing **Reset user interface to default settings**.
