No referenced images were found in the directory — the markdown is text-only. I have all the source content needed to write the guide.

# Managing Plugins (QGIS 3.44)

QGIS uses a plugin architecture to extend its functionality. Plugins come in two flavors: **Core Plugins** (bundled with every install) and **External Plugins** (community-maintained, mostly Python, hosted at plugins.qgis.org or third-party repos).

To get started, open **Plugins > Manage and Install Plugins…** — this launches the Plugin Manager dialog where all the action happens.

The **Settings** tab at the bottom-left controls what you see. Turn on **Show also Experimental Plugins** if you want bleeding-edge tools, or **Show also Deprecated Plugins** to surface unmaintained ones. You can also add third-party repositories here with **Add…**, disable them with **Edit…**, or remove them entirely with **Delete**.

Browse plugins using the tabs across the top: **All**, **Installed**, **Not installed**, **New**, **Upgradeable**, and **Invalid**. The search bar at the top filters by name, author, description, or tags — handy when you know roughly what you need.

Select any plugin to see its metadata on the right: description, author, version, rating, and links. From there you can hit **Install**, **Upgrade Plugin**, **Reinstall Plugin**, or **Uninstall Plugin** depending on its current state. To temporarily disable an installed plugin without removing it, just uncheck its checkbox in the list.

If you have a plugin as a `.zip` file (downloaded directly or shared by a colleague), switch to the **Install from ZIP** tab, point it at the file, and you're done — encrypted archives are supported too.

Installed external plugins land in the `python/plugins` folder of your active user profile. For custom C++ plugin paths, configure them under **Settings > Options > System**.
