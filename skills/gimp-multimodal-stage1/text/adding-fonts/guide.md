# Adding and Managing Fonts (GIMP 2.10)

GIMP uses FreeType 2 for rendering and Fontconfig for managing fonts. It picks up anything in Fontconfig's system path plus its own font search path, which you can customize under **Edit > Preferences > Folders > Fonts**. Out of the box, FreeType 2 handles TrueType, OpenType, Type 1, CFF, BDF, and several other formats — so most font files you'll encounter just work.

**On Linux**, drop font files into `~/.fonts` to make them available system-wide (GIMP and every other app). If you only want a font visible to GIMP, put it in the `fonts` folder inside your personal GIMP directory (typically `~/.config/GIMP/2.10/fonts`). The font shows up next time you launch GIMP, or immediately if you hit the **Refresh** button in the Fonts dialog.

**On Windows**, drag the font file into `C:\Windows\Fonts` — that installs it for all applications. For fonts Windows can't handle natively, place them in your GIMP personal `fonts` folder instead.

**On macOS**, drag fonts into `~/Library/Fonts`, or double-click the file and use **Font Book** to install. For Type 1 fonts, you need both the `.pfb` and `.pfm` files in the same location.

To browse and select fonts, open the Fonts dialog via **Windows > Dockable Dialogs > Fonts**. Click any font to make it active for the Text tool. You can switch between grid and list views from the dialog's tab menu, and press **Ctrl+F** to search by name. Hold the mouse button over a font preview to see a larger sample.

See `fig01.png`.

If you install new fonts while GIMP is already running, click the **Refresh font list** button at the bottom of the Fonts dialog (or right-click in the font display and choose **Rescan Font List**) to pick them up without restarting.

**Troubleshooting:** If GIMP crashes on startup while scanning fonts, a malformed font file is usually to blame — upgrade Fontconfig past version 2.2.0 to fix this. As a quick workaround, launch with `gimp --no-fonts`, though you'll lose the Text tool. On Windows, a bad font may pop open a console window with an error — don't close it, or GIMP will terminate. Just minimize the console and carry on. If symbol fonts cause crashes, updating Pango to 1.4 or later resolves the issue and makes those fonts usable again.
