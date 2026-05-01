The image is just a tiny/blank tracking pixel — not a meaningful screenshot. No figures needed here.

# Installing Zotero (Zotero 7)

Head over to the [Zotero download page](https://www.zotero.org/download/) and grab the installer for your operating system. While you're there, install the **Zotero Connector** for your browser too — it's what lets you save items directly from the web.

**On a Mac**, open the `.dmg` file you downloaded and drag Zotero into your **Applications** folder. From there you can launch it via Spotlight, Launchpad, or the Dock. Once it's installed, feel free to eject and trash the `.dmg`.

**On Windows**, just run the setup program — it handles everything for you.

**On Linux**, you have a couple of options. The simplest is the official tarball: download it, extract it, and run `zotero` from inside that directory. To get a proper launcher entry on Ubuntu or similar desktops, move the extracted folder somewhere permanent (like `/opt/zotero`), run the included `set_launcher_icon` script, and then symlink `zotero.desktop` into `~/.local/share/applications/`. Zotero should then show up in your app launcher.

If you'd rather use a package manager on Debian or Ubuntu, the community-maintained [zotero-deb](https://github.com/retorquere/zotero-deb) package is the recommended route — it wraps the official tarball and handles updates through `apt`. Unofficial packages exist for other distros, but they're third-party and may have sandboxing issues that break things.

Once Zotero is installed, you generally don't need to worry about updates — it updates itself automatically. If you ever want to check manually, go to **Help > Check for Updates…**. You can also just install a newer version right over the existing one without losing any data.

If something isn't working, double-check the [system requirements](https://www.zotero.org/support/system_requirements) to make sure your OS version is supported, and reach out on the [Zotero Forums](https://www.zotero.org/support/getting_help) if you're still stuck.
