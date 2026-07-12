# Managing User Profiles (QGIS 3.44)

A user profile in QGIS bundles everything — global settings, GUI customization, installed plugins, processing scripts, authentication configs, and project templates — into a single isolated folder. By default you get one profile called `default`, but you can create as many as you like for different workflows, clients, or testing.

To create a new profile, go to **Settings > User Profiles > New profile…** and type a name. QGIS immediately launches a fresh instance with that profile active, giving you a clean slate to configure however you want. The profile folder lives under your OS user directory (e.g., `~/.local/share/QGIS/QGIS3/profiles/` on Linux, `%AppData%\Roaming\QGIS\QGIS3\profiles\` on Windows, or `~/Library/Application Support/QGIS/QGIS3/profiles/` on macOS).

Switching profiles is simple: open **Settings > User Profiles** and pick the one you want. QGIS opens a new window running under that profile. When more than one profile exists, the active profile name shows in square brackets in the title bar.

To control which profile loads at startup, open **Settings > Options > User Profiles**. You can choose to always use the last closed profile, lock it to a specific one via the **Always use profile** dropdown, or select **Choose profile at start up** to get a selector dialog each time QGIS launches.

See `fig01.png`.

The **Profile Display** section in that same dialog lets you adjust the icon size in the profile selector and assign a custom icon to the active profile — handy for visual identification when you're juggling several.

You can also launch a specific profile from the command line with `qgis --profile myprofilename`. If the named profile doesn't exist yet, QGIS creates it on the fly. This flag overrides whatever startup profile setting you've configured in the GUI.

One practical tip: if QGIS is misbehaving and you suspect a corrupted profile, spin up a fresh one to test whether the bug persists. If you can't even create a new profile through the menu, just rename the broken profile's folder in the `profiles` directory and restart — QGIS will generate a new `default` automatically.
