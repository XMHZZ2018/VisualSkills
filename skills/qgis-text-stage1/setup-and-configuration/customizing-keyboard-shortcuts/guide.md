Now I have all the information I need. Here's the guide:

# Customizing Keyboard Shortcuts (QGIS 3.44)

QGIS ships with default shortcuts for most features, but you can remap any of them or add new ones. Open the configuration dialog via **Settings > Keyboard Shortcuts...**.

At the top of the dialog you'll find a search box — type a few characters to filter the action list. Once you locate the action you want to remap, select it and choose one of the three buttons at the bottom:

**Change** lets you press a new key combination to assign it right there. **Set None** clears the shortcut entirely, and **Set Default (None)** reverts it to the original QGIS default.

Repeat for as many actions as you like — nothing is committed until you click **Close**, which applies all your changes at once.

To share your configuration across machines, click **Save...** and export as an `.XML` file (you can save just your custom shortcuts or the full set) or as a `.PDF` for reference. On another installation, use **Load...** to import that `.XML` and restore your layout instantly.

Shortcuts you define here are stored in your active user profile, so different profiles can carry independent shortcut schemes.
