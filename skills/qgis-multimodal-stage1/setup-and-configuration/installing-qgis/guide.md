# Installing QGIS (QGIS 3.44)

QGIS offers several installation paths depending on your platform and needs. The quickest route for most people is grabbing a pre-built binary; building from source is there if you need bleeding-edge features or want to contribute.

## Installing from binaries

Standard installers are available for Windows and macOS, and binary packages (`.rpm` and `.deb`) or software repositories cover most GNU/Linux distributions. Head to **https://qgis.org/download/** and pick the installer that matches your OS — the site auto-detects your platform and highlights the recommended download. Run the installer, accept the defaults, and you're done.

## Installing from source

If you need to compile QGIS yourself — maybe you want a specific unreleased fix or you're developing a plugin that touches core — clone the repository and follow the `INSTALL.md` file bundled with the source. The canonical instructions live at **https://github.com/qgis/QGIS/blob/release-3_44/INSTALL.md**. When building a particular release rather than the development trunk, swap `master` for the release branch (e.g., `release-3_44`) since build dependencies can differ between versions.

## Installing on external media

You can run QGIS entirely from a USB flash drive — handy for fieldwork on shared machines. The trick is launching QGIS with the `--profiles-path` command-line option pointed at a folder on the drive. This redirects all user profiles, plugins, and **QSettings** to portable storage so nothing touches the host system. Check **Settings > User Profiles** documentation for details on how the profiles directory is structured.

## Downloading sample data

The official user guide references the "Alaska dataset" throughout its examples. Grab it from **https://github.com/qgis/QGIS-Sample-Data/archive/master.zip** and unzip it somewhere convenient. The dataset uses the Alaska Albers Equal Area projection (EPSG:2964) and includes raster layers, vector layers, and a small GRASS database — everything you need to follow along with the tutorials. If you plan to use QGIS as a GRASS frontend, additional sample locations like Spearfish are available at the GRASS GIS download page.
