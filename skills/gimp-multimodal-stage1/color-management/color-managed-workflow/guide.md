# Setting Up a Color-Managed Workflow (GIMP 2.10)

Every device in your pipeline — camera, scanner, monitor, printer — sees color a little differently. Without color management, you're editing blind: what looks great on your screen may print muddy or shift hue on someone else's display. ICC profiles act as translators, mapping each device's quirks into a shared language so your colors stay consistent from capture to output.

See `fig01.png`.

Start by setting your working color space. Open **Edit > Preferences**, then navigate to **Color Management**. The default RGB working space is sRGB, which is a safe bet for most web and general-purpose work. Leave it there unless you have a specific reason (like wide-gamut photography) to choose something else.

Next, assign your monitor profile. In that same **Color Management** preferences section, set the monitor profile to the ICC file for your display. If you've calibrated your monitor with hardware (using something like a Datacolor or X-Rite device), point GIMP to the resulting `.icc` file. This ensures GIMP compensates for your monitor's actual behavior when rendering colors on screen. On Linux, you may also need to load calibration LUTs into the video card using `xcalib` or `dispwin` at startup.

When you open an image that has an embedded profile, GIMP will ask whether to convert it to your RGB working space or keep the original profile. For most editing, click **Convert** — this translates the pixel values into your working space so all your tools and filters behave predictably. If you choose **Keep**, the image stays in its original space but GIMP will still display it correctly using the embedded profile.

See `fig02.png`.

If you receive an image with no embedded profile, you can manually assign one via **Image > Color Management > Assign Color Profile**. This doesn't change pixel values — it just tells GIMP how to interpret them. Only do this when you actually know (or can confidently guess) what profile the image was created in.

Leave **Image > Color Management > Enable Color Management** checked at all times. Unchecking it silently assigns a built-in sRGB profile, which can make your colors look wrong if the image was actually in a different space — and recovering can be messy.

For print work, enable soft proofing via **View > Color Management > Soft Proofing** and select your printer's ICC profile. This simulates on screen what the final print will look like, including any out-of-gamut colors the printer can't reproduce. You can optionally mark those out-of-gamut areas so you know exactly where to adjust before committing to paper.
