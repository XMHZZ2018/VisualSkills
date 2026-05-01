# Installing Zotero (Zotero 7)

Head to the [Zotero download page](https://www.zotero.org/download/) and grab the installer for your operating system. While you're there, install the **Zotero Connector** browser extension too — it's how you'll save items from the web.

**On Mac**, open the downloaded `.dmg` file and drag **Zotero** into your **Applications** folder. Launch it from Spotlight, Launchpad, or the Dock. Once installed, feel free to eject and delete the `.dmg`.

**On Windows**, just run the setup program — it handles everything.

**On Linux**, download the tarball, extract it, and run `zotero` from that directory. To add it to your launcher, move the folder somewhere permanent (like `/opt/zotero`), run `set_launcher_icon` to fix the icon path, then symlink `zotero.desktop` into `~/.local/share/applications/`. If you'd rather use a package manager, the community-maintained [zotero-deb](https://github.com/retorquere/zotero-deb) repo lets you install and update via `apt`.

**On Chromebook**, you'll need to set up a Linux environment first — see Zotero's dedicated Chromebook guide for details.

Zotero updates itself automatically in the background. If you want to check manually, go to **Help > Check for Updates…**. You can also install a new version right over your existing one without losing any data.

If anything goes wrong, double-check the [system requirements](https://www.zotero.org/support/system_requirements) and reach out on the [Zotero Forums](https://www.zotero.org/support/getting_help) for help.
