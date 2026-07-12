# Adding and Managing Fonts (GIMP 2.10)

GIMP uses FreeType 2 and Fontconfig under the hood, so it supports TrueType, OpenType, Type 1, CFF, and many other font formats out of the box. Getting new fonts into GIMP is mostly about putting the file in the right folder.

**On Linux**, drop the font file into `~/.fonts` to make it available system-wide (including GIMP). If you only want GIMP to see it, place it in the `fonts` folder inside your personal GIMP directory instead.

**On Windows**, drag the font file into `C:\windows\fonts` — that makes it available to all applications. For fonts Windows can't handle natively, place them in your GIMP profile's `fonts` folder.

**On macOS**, drag fonts into the **Fonts** folder inside your Home's **Libraries**, or double-click the file to open Font Book and install from there. For Type 1 fonts, keep both the `.pfb` and `.pfm` files together.

You can also add custom directories to GIMP's font search path via **Edit > Preferences > Folders > Fonts**. Any font placed in a listed folder will appear after the next restart.

If you install a font while GIMP is already running, open the Fonts dialog (**Windows > Dockable Dialogs > Fonts**) and hit the **Refresh** button at the bottom — no restart needed.

**Troubleshooting:** If GIMP crashes on startup while scanning fonts, a malformed font file is likely the culprit. Upgrading Fontconfig past version 2.2.0 usually fixes this. As a temporary workaround, launch GIMP with `--no-fonts` (you'll lose the Text tool, but you can isolate the bad file). On Windows, a console window may pop up when GIMP encounters a bad font — don't close it, or GIMP will shut down. Just minimize it and carry on.
