# Scanning Paper Drawings (OpenToonz 1.7)

> **Note:** OpenToonz currently does not support native scanning. Use the separate GTS scanning and cleaning tool instead (available from the OpenToonz download page). This guide is preserved for reference in case the feature is reactivated.

Paper drawings — animation levels, backgrounds, overlays — need to be scanned into OpenToonz before you can work with them. The process boils down to three stages: set up your scanner, define your animation levels, then scan.

**Choosing a scanner driver.** Head to **Scan & Cleanup > Define Scanner…** and pick either **Internal** (for directly supported USB scanners) or **TWAIN** (for everything else). If you go Internal on Windows, you'll need to disable the **Windows Image Acquisition (WIA)** service via Control Panel > Administrative Tools > Services. On macOS, remove any TWAIN drivers for that scanner instead. TWAIN users need to re-select their driver each time OpenToonz restarts.

See `fig01.png`.

**Scanning modes.** You have three choices: **Black and White** is fastest and produces the lightest files — you just set a threshold and every pixel becomes black or white (antialiasing comes later in cleanup). **Greyscale** captures a tonal range and takes longer, but lets you use Autoadjust during cleanup to smooth differences between key drawings and in-betweens. **Color** preserves colored lineart (e.g., black outlines with red shadow lines) so cleanup can distinguish them later without manual painting.

**Prep for autocentering.** If you plan to autocenter during cleanup, the pegbar holes must scan as solid black. For a paper feeder, stick thin black tape opposite the lamp so it sits behind the holes. For the flatbed, place a black sheet under the cover. Use reasonably thick paper, skip colored hole reinforcements, and keep your drawing at least 1 cm away from the pegbar holes.

**Defining levels before scanning.** You need to tell OpenToonz what you're about to scan. Select a cell in the Xsheet/Timeline, then go to **Level > New > New Level…**, choose **Scan Level** from the Type menu, set your frame range and numbering increment, and hit **OK**. The level names appear in red in the Xsheet — that just means no image files exist on disk yet. By default, scanned files land in the project's **+inputs** folder.

See `fig02.png`.

**Running the scan.** Select the drawings you want in the Xsheet, open **Scan & Cleanup > Scan Settings…** to pick your paper format and mode, toggle **Paper Feeder** if your scanner has one, then fire off the scan with **Scan & Cleanup > Scan**. If you're using the feeder, everything rolls through automatically; otherwise you'll get prompted to swap each sheet. Scanned frames save as compressed TIFs (e.g., `animation.0001.tif`) and the Xsheet names turn black once files exist on disk.

See `fig03.png`.

**Cropbox optimization.** For directly supported scanners, you can speed things up with **Scan & Cleanup > Set Cropbox** — this scans one sheet, shows a red rectangle you can resize and drag, and then only that region gets scanned on subsequent passes. The final image stays at full paper-format size; you're just telling the hardware where to focus. Reset it anytime with **Scan & Cleanup > Reset Cropbox**.
