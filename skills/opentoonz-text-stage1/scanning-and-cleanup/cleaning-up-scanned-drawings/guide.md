# Cleaning Up Scanned Drawings (OpenToonz 1.7)

Scanned drawings need cleanup before you can paint or edit them in OpenToonz. The process autocenters drawings to pegbar holes, recognizes line art, and crops/resizes everything to fit your camera. The output is a TLV level with a paired TPL palette.

Open the cleanup dialog via **Scan & Cleanup > Cleanup Settings…**. You'll see three sections: Cleanup, Processing, and Camera. Dial in settings on one drawing, then apply them to the whole level.

**Autocenter** aligns drawings using pegbar holes captured during scanning. Enable the checkbox, pick which side the **Pegbar Holes** are on, and choose the matching **Field Guide** (e.g., Acme or Oxberry). Preview with **Scan & Cleanup > Preview Cleanup** to confirm registration is correct. Use **Rotate** and **Flip** if drawings were scanned at a different orientation.

For **Line Processing**, set the mode to **Greyscale** (black lines) or **Color** (colored lines). Key sliders: **Sharpness** controls edge hardness, **Despeckling** removes small dust spots (value = max pixel size removed), **Brightness** controls line thickness (lower = thicker), and **Contrast** controls antialiasing solidity. Toggle **Scan & Cleanup > Opacity Check** (Alt+1) to visualize solid pixels in black, antialias in red, and despeckled areas in green.

For color line processing, add up to 7 colors with the **+** button. Each color gets its own **H Range** (hue tolerance) and **Line Width**. Use the RGB Picker tool to sample colors directly from your scan.

The **Camera** section sets the crop and resolution of cleaned output. Match it to your scene camera or make it larger if you need overflow. Adjust the **N/S** and **E/W** offsets to shift the center. Use **Scan & Cleanup > Camera Test** to see a red crop box overlaid on your drawing and drag its handles to resize interactively.

Save settings as CLN files via the **Save** button at the bottom of the dialog. Name a CLN file identically to a level and store it in the same folder — OpenToonz will auto-load it for that level. Hit **Reset** to revert to scene defaults.

When you're ready, select drawings in the Xsheet and run **Scan & Cleanup > Cleanup**. A per-frame dialog lets you **Cleanup**, **Skip**, **Cleanup All**, or **Cancel**. Processed cells turn green. For background processing, add scenes as cleanup tasks in the **Tasks** pane using the **Add Cleanup Task** button, then hit **Start**.

Enable **File > Preferences… > Drawing > Keep Original Cleaned Up Drawings As Backup** to store originals in a `nopaint` subfolder — you can revert anytime via **Level > Revert to Cleaned Up**.
