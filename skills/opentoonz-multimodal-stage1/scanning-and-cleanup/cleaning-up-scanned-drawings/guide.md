# Cleaning Up Scanned Drawings (OpenToonz 1.7)

Before scanned drawings can be painted or composited, they need to go through cleanup — a process that aligns them to pegbar holes, recognizes line art, and crops everything to fit your camera. The output is a proper Toonz raster level (TLV) with its own palette (TPL). Open the whole dialog from **Scan & Cleanup > Cleanup Settings…**.

See `fig01.png`.

At the top of the dialog you'll find the **Autocenter** checkbox. Turn it on, pick which side holds your **Pegbar Holes**, and choose the matching **Field Guide** (e.g., Acme or Oxbry). This tells OpenToonz where the registration holes are so every frame lines up. If holes can't be detected, you'll get an error but the drawing still processes with the remaining settings. Below that, **Rotate** and **Flip** handle orientation issues — handy for sheets scanned sideways or shadow levels drawn on the back of the paper.

For line processing, set the **Line Processing** dropdown to **Greyscale** (black lines) or **Color** (colored outlines). In greyscale mode, tweak **Sharpness** for line hardness, **Despeckling** to kill stray dots, **Brightness** to control line thickness, and **Contrast** for antialiasing intensity. The **Antialias** menu offers Standard, None (fully solid edges), or Morphological (edge-analyzed smoothing). For color mode, you additionally define up to 7 recognition colors using the color list and the **RGB Picker** tool — each color gets its own Brightness, Contrast, and hue range controls.

See `fig02.png`.

The Camera section sets the resolution and field size for the final output. If your cleanup camera is 1920×1080 at a 16-field size, drawings get cropped to that field and output at that resolution. Use the **N/S** and **E/W** offsets to shift the crop center if needed.

To check your work before committing, select a drawing in the Xsheet and choose **Scan & Cleanup > Preview Cleanup** — the Viewer updates live as you adjust parameters. Toggle **Scan & Cleanup > Opacity Check** (or **Alt+1**) to see solid pixels in black, antialiased edges in red, and despeckled areas in green. Alternatively, **Scan & Cleanup > Camera Test** shows just the crop and alignment without line processing — drag the red camera box directly in the Viewer to adjust framing.

Once everything looks right, select the frames you want in the Xsheet and run **Scan & Cleanup > Cleanup**. You'll get a per-frame prompt to process, skip, or cleanup all at once. Cells turn from blue to green as they're converted. For large batches, add scenes as cleanup tasks via the **Tasks** pane and run them in the background. Save your settings as a CLN file with the **Save** button at the bottom of the dialog — name it identically to an animation level and it auto-loads whenever that level is selected.
