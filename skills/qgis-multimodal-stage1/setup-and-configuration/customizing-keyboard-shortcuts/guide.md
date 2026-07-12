# Customizing Keyboard Shortcuts (QGIS 3.44)

QGIS ships with a full set of default keyboard shortcuts, but you can remap any of them or add new ones. Open the configuration dialog via **Settings > Keyboard Shortcuts…** — this brings up a list of every available action alongside its current shortcut (if any).

Use the **Search** box at the top to quickly filter the list. Type a keyword — like "sketching" or "layer" — and the table narrows to matching actions instantly. Select the action you want to modify, then choose one of the three buttons at the bottom of the dialog:

**Change** lets you record a brand-new key combination. Click the button, then press the keys you want (e.g., `Ctrl+Shift+E`). QGIS will warn you if the combination conflicts with an existing shortcut, so you can resolve collisions right away.

**Set None** strips the shortcut entirely — handy when you want to free up a combo for something else without immediately reassigning it.

**Set Default (None)** reverts the action back to whatever QGIS originally assigned. If the action never had a default shortcut, it clears to blank.

See `fig01.png`.

Once you've tweaked everything you need, click **Close** to apply your changes to the current session. Shortcuts persist in your user profile, so they'll be waiting next time you launch QGIS.

You can also share configurations across machines. Click **Save…** to export your shortcuts as an `.XML` file (choose between only your custom changes or the entire set) or as a `.PDF` for documentation. On another installation, use **Load…** to import that `.XML` and get the same bindings instantly — great for standardizing shortcuts across a team or restoring your setup after a fresh install.
