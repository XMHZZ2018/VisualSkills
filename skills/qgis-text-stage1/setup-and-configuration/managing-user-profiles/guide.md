I now have everything I need. Here's the guide:

# Managing User Profiles (QGIS 3.44)

A user profile bundles all your settings, plugins, authentication configs, custom projections, and project templates into a single isolated folder. By default you get one profile called `default`, but you can create as many as you need — great for separating work clients, demos, or testing new plugins without risking your main setup.

To create a new profile, go to **Settings > User Profiles > New profile…** and give it a name. QGIS immediately launches a fresh instance using that profile, starting from a clean slate. Your original session stays open and untouched.

Switching profiles is just as easy — pick the one you want from **Settings > User Profiles** and a new QGIS window opens with that profile's configuration. The active profile name shows in square brackets in the title bar so you always know which one you're in.

To control which profile loads at startup, open **Settings > Options > User Profiles** tab. You can stick with "Use last closed profile," pin a specific one via "Always use profile," or choose "Choose profile at start up" to get a selector dialog each time. You can also customize the profile icon from the **Profile Display** section.

From the command line, launch a specific profile directly with `qgis --profile myprofile` — if it doesn't exist yet, QGIS creates it on the fly.

Profile folders live at `~/.local/share/QGIS/QGIS3/profiles/` on Linux, `%AppData%\Roaming\QGIS\QGIS3\profiles\` on Windows, and `~/Library/Application Support/QGIS/QGIS3/profiles/` on macOS. Use **Open Active Profile Folder** to jump straight there.

If QGIS starts misbehaving, try running under a fresh profile — it's the fastest way to rule out corrupted settings as the culprit.
