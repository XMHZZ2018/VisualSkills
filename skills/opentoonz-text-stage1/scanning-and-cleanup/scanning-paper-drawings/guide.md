# Scanning Paper Drawings (OpenToonz 1.7)

> **Note:** OpenToonz currently does not support native scanning. Use the separate GTS scanning/cleaning tool instead. This guide documents the built-in workflow in case it's reactivated in a future release.

Start by telling OpenToonz which scanner driver to use. Go to **Scan & Cleanup → Define Scanner…** and pick **Internal** if your model is directly supported, or **TWAIN** to use the manufacturer's drivers. On Windows, Internal requires disabling the **Windows Image Acquisition (WIA)** service; TWAIN requires it enabled. TWAIN selection resets each session.

Three scan modes are available. **Black and White** is fastest — you set a single threshold and every pixel lands on one side. **Greyscale** captures a tonal range (useful with the later Autoadjust cleanup). **Color** preserves different line colors (e.g., black outlines vs. red shadow lines) so you can separate them in cleanup.

If you plan to use autocentering during cleanup, the pegbar holes must scan as solid black. Stick thin black tape inside the automatic feeder opposite the lamp, or lay a black sheet under the scanner cover. Use thicker animation paper to avoid jams and light bleed-through. Keep drawings at least 1 cm clear of the peg holes — avoid colored reinforcements and similarly-shaped marks in that zone.

Before scanning, define your animation level. Select a cell in the Xsheet, then **Level → New → New Level…**, pick **Scan Level** from the **Type** dropdown, and set the frame range, step, and increment. Levels save to the project's **+inputs** folder by default; change it in the **Path** field. Alternatively, double-click a cell and type a name plus frame number directly.

To scan, select the target drawings in the Xsheet and open **Scan & Cleanup → Scan Settings…** to choose paper format, mode, and whether to use the **Paper Feeder** or **Reverse Order**. Then run **Scan & Cleanup → Scan**. With a paper feeder the batch runs automatically; without one, you'll be prompted to swap each sheet. Scanned frames save as sequenced TIFs (e.g., `animation.0001.tif`) and their Xsheet names turn from red to black.

For directly supported scanners you can speed things up with a cropbox: **Scan & Cleanup → Set Cropbox** scans once and shows a red rectangle you can resize and reposition. Subsequent scans only read that region. Reset it anytime with **Scan & Cleanup → Reset Cropbox**.
