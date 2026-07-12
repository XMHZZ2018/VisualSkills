# Managing Plugins (QGIS 3.44)

QGIS has a plugin architecture that lets you extend the application with new tools and processing capabilities. Plugins come in two flavors: **Core Plugins**, which ship with every QGIS install and are maintained by the development team, and **External Plugins**, mostly written in Python and hosted at the official repository or third-party sources.

To get started, open **Plugins > Manage and Install Plugins…** — this launches the Plugin Manager dialog, your one-stop shop for browsing, installing, updating, and removing plugins.

The **Settings** tab at the bottom of the left panel controls what you see. You can toggle *Show also Experimental Plugins* (early-stage, not production-ready) and *Show also Deprecated Plugins* (unmaintained or superseded). There's also a handy *Check for Updates on Startup* option that polls for new versions every few days and notifies you when upgrades are available.

See `fig01.png`.

Browse plugins using the tabs along the top: **All**, **Installed**, **Not installed**, **New**, **Upgradeable**, and **Invalid**. A search bar at the top filters by name, author, description, or tags — useful when you know roughly what you're looking for but not the exact plugin name.

See `fig02.png`.

Select any plugin to see its metadata in the right panel — description, author, version history, rating, and links to its homepage and issue tracker. From there you can hit **Install**, **Upgrade Plugin**, **Reinstall Plugin**, or **Uninstall Plugin** depending on its current state. If you enabled experimental plugins in settings, you'll also see options to install or downgrade experimental versions specifically.

Once installed, each plugin shows a checkbox in the list. Uncheck it to temporarily deactivate the plugin without removing it — handy when you're troubleshooting conflicts or just want a leaner interface for a particular project.

If you have a plugin as a `.zip` file (downloaded directly from a developer's repo, for instance), switch to the **Install from ZIP** tab, point it at your file, and you're done. Encrypted archives are supported too.

To add a third-party plugin repository, go back to the **Settings** tab, click **Add…**, and fill in a name and URL (supports `http://` and `file://` protocols). You can disable or delete custom repositories later with the **Edit…** and **Delete** buttons. Authentication (basic or PKI) is supported for private repositories.
