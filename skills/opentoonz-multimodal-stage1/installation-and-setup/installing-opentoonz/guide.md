# Installing OpenToonz (OpenToonz 1.7)

Grab the installer for your platform from the official OpenToonz download page. You'll find Windows and macOS installers front-and-center; nightly builds live at the bottom of that same page if you want to test bleeding-edge features (fair warning — nightlies can be unstable, so keep them out of production work).

## Windows

Run **OpenToonzSetup.exe**. Microsoft Defender SmartScreen may complain the installer isn't signed — click **More info** then **Run anyway** to proceed. Pick your language, accept the Terms of Use, and choose where to put the **OpenToonz stuff** folder (defaults to `C:\OpenToonz_stuff`). There's a checkbox to overwrite settings from a previous install while preserving your personal preferences — leave it ticked unless you have a reason not to. Optionally add a desktop shortcut, hit **Install**, and you're done.

See `fig01.png`.

If you use Chocolatey, it's just `choco install opentoonz`.

## macOS

Right-click **OpenToonz.pkg** in Finder and choose **Open** (this bypasses Gatekeeper for unsigned packages). The installer walks through Introduction, License, Destination Select, and Installation Type panels — accept the license, pick your disk (usually Macintosh HD), then click **Install**. Close the installer when it finishes.

See `fig02.png`.

Homebrew users can run `brew cask install opentoonz` instead.

## Linux

Most major distros package OpenToonz in their repositories. On Fedora: `dnf install opentoonz`. Arch: `pacman -S opentoonz`. openSUSE: `zypper install opentoonz`. Gentoo: `emerge media-gfx/opentoonz`. For Debian, you'll need to add the deb-multimedia repository and its signing key first, then `apt install opentoonz opentoonz-data`.

For a distro-agnostic option, Flatpak (`flatpak install flathub io.github.OpenToonz`) and Snap (`snap install opentoonz`) both work well.

## BSD

FreeBSD users can build from ports: `cd /usr/ports/multimedia/opentoonz && make install clean`. On DragonFly BSD it's a simple `pkg install opentoonz`.
