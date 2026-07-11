# Installing OpenToonz (OpenToonz 1.7)

Grab the installer for your OS from the official [OpenToonz download page](https://opentoonz.github.io/e/download/opentoonz.html). Nightly builds are also available there if you want to test bleeding-edge features, but treat those as unstable — not for production work.

## Windows

Run **OpenToonzSetup.exe**. If Microsoft Defender SmartScreen complains, click **More info** then **Run anyway**. Pick your language, accept the Terms of Use, and choose where to put the **OpenToonz stuff** folder. The installer asks whether to overwrite settings from a previous install (your personal settings are always preserved). Optionally create a desktop shortcut, hit **Install**, and you're done.

Alternatively: `choco install opentoonz`

## macOS

Right-click **OpenToonz.pkg** in Finder and select **Open** (this bypasses Gatekeeper). Click **Continue**, choose a language, accept the license, pick a destination disk (defaults to Macintosh HD), then hit **Install**. Close the installer when it finishes.

Alternatively: `brew cask install opentoonz`

## Linux

Most major distros package OpenToonz natively: `pacman -S opentoonz` (Arch), `dnf install opentoonz` (Fedora), `sudo zypper install opentoonz` (openSUSE), `sudo emerge media-gfx/opentoonz` (Gentoo), or `nix-env -iA nixos.opentoonz` (NixOS). Debian users need to add the deb-multimedia repo first, then `sudo apt install opentoonz opentoonz-data`.

For a distro-agnostic option, use Flatpak (`flatpak install flathub io.github.OpenToonz`) or Snap (`sudo snap install opentoonz`).

## BSD

On FreeBSD, build from ports: `cd /usr/ports/multimedia/opentoonz && make install clean`. On DragonFly BSD, just `pkg install opentoonz`.
