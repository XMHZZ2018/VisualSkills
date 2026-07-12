No inline image references in these files. I have all the content needed from the markdown source. Here's the guide:

# Tracking GPS Data (QGIS 3.44)

QGIS connects directly to GPS receivers for live field mapping. Enable the GPS toolbar via **View > Toolbars > GPS** — it's your control center for the entire tracking session.

Before connecting, configure your device under **Settings > Options > GPS**. Use **Autodetect** mode or point QGIS to the correct serial port (e.g., COM4 on Windows, `/dev/ttyUSB0` or `/dev/ttyACM3` on Linux). For Bluetooth devices, pair the GPS first via your OS Bluetooth settings — the pairing code is usually `0000` — then note the assigned COM port.

Once ready, hit **Connect** in the GPS Information panel (**View > Panels > GPS Information** or `Ctrl+0`). The panel's **Position** tab shows live coordinates, altitude, speed, bearing, accuracy, and satellite count. The **Signal** tab displays per-satellite signal strength.

Set a destination layer for digitized features using the toolbar's layer selector — this prevents accidentally writing GPS points into the wrong layer. The toolbar adapts its tools (point, line, polygon creation) to match the selected layer type. Features are auto-committed if you enable **Automatically save added features** in the toolbar's **Settings** menu.

For logging, toggle **Log to GeoPackage/SpatiaLite** in the settings dropdown. QGIS writes every fix to a `gps_points` table and saves the full track to `gps_tracks` on disconnect. You can also log raw NMEA sentences to a text file.

On Linux, `gpsd` works as a reliable middleware — just `sudo apt install gpsd` then `gpsd /dev/ttyUSB0`. On Windows, GPSGate serves the same role for devices that don't expose a direct serial connection.

Map recentering behavior is configurable: always recenter, recenter when leaving extent, or never. Enable **Rotate map to match GPS direction** for a heads-up navigation view.
