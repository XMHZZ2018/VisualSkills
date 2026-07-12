# Printing Images (GIMP 2.10)

Before you hit print, you'll want to make sure your image will come out at the right physical size. Pixels don't have a fixed real-world dimension — GIMP uses *resolution* (pixels per inch) to bridge that gap.

Open **Image → Print Size…** to set your print dimensions without altering pixel data. Pick a unit you like (inches, cm), set one dimension, and GIMP adjusts the other proportionally via the chain link. The resolution updates automatically — aim for 300 ppi for crisp prints, 150–200 ppi for acceptable quality, and avoid anything below 100 unless it's a poster viewed from a distance.

The X and Y resolution fields let you fine-tune independently if you break the chain icon between them. Increasing resolution shrinks the printed size (more pixels packed per inch) but keeps all your image data intact — no resampling, no quality loss. This is fundamentally different from scaling the image down.

When you're ready to print, go to **File → Print** (or just **Ctrl+P**). The Print dialog gives you tabs for **Page Setup**, **Image Settings**, **Image Quality**, and more. Under Image Settings you can adjust position offsets, centering, and whether to ignore page margins. The preview pane on the right shows exactly how your image will land on the page.

Hit **Print Preview** for a final check, then **Print** to send it off.
