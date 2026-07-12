# Tracking GPS Data (QGIS 3.44)

QGIS can connect to a GPS receiver for live field mapping, letting you see your position on the map canvas in real time and digitize features directly from GPS coordinates. Before you begin, make sure your device is configured under **Settings > Options > GPS**.

The main interface is the GPS Toolbar — enable it via **View > Toolbars > GPS**. Once a device is detected you get buttons to connect/disconnect, recenter the map on your position, and digitize features. You can set a specific destination layer for GPS-digitized features (rather than relying on whichever layer happens to be active), which prevents accidentally writing points into the wrong layer.

The toolbar also exposes a quick-info display showing your current location, altitude, ground speed, bearing, and track length — toggle whichever fields you care about. A **Settings** drop-down on the toolbar lets you adjust mid-session options like auto-recentering behavior, whether track vertices are added automatically, and whether features commit immediately to their layer (bypassing the edit buffer).

For a more detailed view, open the GPS Information Panel with **View > Panels** (or `Ctrl+0`). Its **Position** tab shows latitude, longitude, altitude (both geoid and WGS 84 ellipsoid), HDOP/VDOP/PDOP, fix quality, satellite count, and total track length. The **Signal** tab displays a bar chart of satellite signal strengths so you can judge fix reliability at a glance.

See `fig01.png`.

To log all GPS data persistently, use **Settings > Log to GeoPackage/SpatiaLite** on the toolbar. QGIS creates `gps_points` and `gps_tracks` tables automatically — every incoming message goes into `gps_points`, and a complete track is written to `gps_tracks` when you disconnect. You can also log raw NMEA sentences to a text file if you need the unprocessed data.

For Bluetooth GPS devices, pair the unit through your OS first, note the COM port (Windows) or rfcomm device (Linux), then point QGIS at that port in the GPS options and hit **Connect**. If the connection fails, power-cycle the GPS, wait about 10 seconds, and retry — and make sure no other Bluetooth receiver nearby is paired to the same unit.

On Linux, the easiest path for USB devices (like a Garmin GPSMAP 60cs) is to run `gpsd /dev/ttyUSB0` as a middleware and let QGIS connect through it. On Windows, GPSGate serves the same role, or you can use **Autodetect** mode under **Settings > Options > GPS** to let QGIS find the device directly.
