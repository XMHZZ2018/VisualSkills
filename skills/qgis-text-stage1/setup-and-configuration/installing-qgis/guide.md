# Installing QGIS (QGIS 3.44)

The easiest way to get QGIS is from pre-built binaries. Head to **https://qgis.org/download/** and grab the standard installer for Windows or macOS, or add the appropriate repository/package (deb or rpm) on Linux. Run the installer and you're done.

If you need to build from source — say, for a custom build or development work — clone the repository and follow the `INSTALL.md` file bundled with the source code (also available at **https://github.com/qgis/QGIS/blob/release-3_44/INSTALL.md**). Building a specific release? Switch to the `release-X_Y` branch rather than `master`, since build instructions can differ between versions.

You can also install QGIS on a flash drive for portable use. The trick is to launch QGIS with the `--profiles-path` option pointing to a directory on the external media. This redirects all plugins, settings, and **QSettings** storage to that drive, so you can carry a fully configured QGIS environment between machines.

Once installed, grab the sample dataset from **https://github.com/qgis/QGIS-Sample-Data/archive/master.zip** and unzip it anywhere convenient. This Alaska dataset (EPSG:2964, Albers Equal Area) includes the raster and vector files used throughout the official user guide — handy for following along with tutorials.

Launch QGIS from your applications menu, Start menu, Dock, desktop shortcut, or by typing `qgis` in a terminal. You can also double-click any `.qgz` or `.qgs` project file to open QGIS directly into that project. To quit, use **Project › Exit QGIS** (`Ctrl+Q` on Windows/Linux, `Cmd+Q` on macOS).
