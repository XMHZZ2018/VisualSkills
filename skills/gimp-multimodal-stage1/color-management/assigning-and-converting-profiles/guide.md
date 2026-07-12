# Assigning and Converting Color Profiles (GIMP 2.10)

All color profile operations live under **Image > Color Management**. There are four commands: Assign, Convert, Discard, and Save. The key distinction is that *assigning* a profile re-labels your pixel data without changing it (colors shift on screen), while *converting* actually transforms pixel values to look the same under a different profile.

**Assigning a profile** is what you want when an image arrives without an embedded ICC profile — or with the wrong one. GIMP defaults to its built-in sRGB, so if your file is actually AdobeRGB1998, the colors will look off until you fix it. Go to **Image > Color Management > Assign Color Profile**, pick the correct profile from the drop-down (or choose **Select color profile from disk…** at the bottom of the list to browse), then click **Assign**.

See `fig01.png`.

**Converting to a profile** is the right move when you want to change color spaces — say, preparing a print-ready file. Open **Image > Color Management > Convert to Color Profile**, choose your destination profile, then set a rendering intent (Perceptual, Relative Colorimetric, Saturation, or Absolute) and decide whether to enable **Black Point Compensation**. Click **Convert** and GIMP remaps every pixel value so colors look consistent under the new profile.

See `fig02.png`.

For either dialog, you can click the "+" icon next to **Profile details** to inspect embedded metadata tags in any profile before committing.

**Discarding a profile** resets the image back to GIMP's built-in sRGB — handy when you want to export a file with no embedded profile. Access it via **Image > Color Management > Discard Color Profile**. This is only available when the image currently carries a non-built-in profile. Remember, discarding changes appearance but not channel values — it's an assign operation under the hood.

**Saving a profile to disk** lets you extract whatever ICC profile is currently assigned. Use **Image > Color Management > Save Color Profile to File**, navigate to a folder, and give it a filename ending in `.icc` or `.icm` (some tools won't recognize other extensions). You can even save GIMP's built-in sRGB this way.
