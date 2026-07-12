# Fixing Export Problems (GIMP 2.10)

Most image formats have limitations that can silently wreck your work on export. The two biggest surprises: JPEG doesn't support transparency, and GIF maxes out at 256 colors.

**Transparency turns white or black in JPEG** — JPEG simply can't store alpha channels. When you export, GIMP fills every transparent pixel with the current background color (white by default). If your image needs transparency, export as PNG or TIFF instead via **File > Export As** and choose the appropriate format.

**Colors shift or band in GIF** — GIF supports a maximum of 256 colors total. GIMP merges similar colors together to hit that limit, which often produces noticeable shifts, especially in gradients or photos. You have two options: switch to a format like PNG that handles millions of colors, or convert to Indexed Mode yourself first via **Image > Mode > Indexed** so you can hand-tune the palette and dithering before the export flattens things.

Going the manual Indexed route gives you control — you pick the algorithm, adjust problem colors, and preview the result before committing. That's worth it for animations or cases where GIF is non-negotiable.

The short version: if you see unexpected results on export, check whether the format actually supports what you're trying to preserve. Transparency needs PNG/TIFF; full color needs PNG. When the format is locked in, convert manually so you're in the driver's seat.
