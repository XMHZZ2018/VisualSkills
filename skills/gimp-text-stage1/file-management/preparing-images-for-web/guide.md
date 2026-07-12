# Preparing Images for the Web (GIMP 2.10)

The golden rule: use JPEG for photographs (lots of colors, fine detail) and PNG for graphics like icons, buttons, or screenshots (fewer colors, sharp edges). Pick the wrong format and you'll either bloat file size or destroy quality.

Open your image and check whether it has an alpha channel you don't need. If transparency isn't part of your design, flatten the image via **Image > Flatten Image** — this removes the alpha channel and composites everything onto a solid background. Photographs typically load without alpha, so you can skip this step for most photos.

Export with **File > Export As** and type your desired extension (`.png` or `.jpg`) in the filename. For PNG, crank compression to maximum — it's lossless, so quality stays identical; only export time increases. For JPEG, the default quality setting balances size and fidelity nicely. Drop the quality slider to around 75 for a noticeably smaller file that still looks good on screen. Enable **Show preview in image window** in the JPEG export dialog to judge degradation in real time before committing. Avoid quality below 40 unless you genuinely don't care about artifacts.

If you need even smaller PNGs — say for simple graphics — convert to indexed color via **Image > Mode > Indexed**. This caps the palette at 256 colors and can slash file size. Don't do this to photographs or anything with smooth gradients; you'll get ugly banding.

For transparency on the web, PNG with alpha is your best bet — it supports smooth, partial transparency (soft glows, drop shadows). Make sure an alpha channel exists in the Channels dialog; if not, add one via **Layer > Transparency > Add Alpha Channel**. The checkerboard pattern in GIMP represents transparent pixels that will be see-through in a browser. Export as PNG and you're set.

One last thing: avoid re-saving JPEGs repeatedly. Each save cycle recompresses and degrades quality further. Work in XCF (GIMP's native format) and only export to JPEG as a final step.
