# Assigning and Converting Color Profiles (GIMP 2.10)

All color profile operations live under **Image → Color Management**. There are four actions: assign, convert, discard, and save.

**Assign Color Profile** re-tags the image with a different ICC profile without touching pixel values. Use it when an image arrives without an embedded profile (GIMP defaults to sRGB) and you know it actually belongs to another color space — say, AdobeRGB1998. Open **Image → Color Management → Assign Color Profile**, pick the correct profile from the drop-down or choose **Select color profile from disk…**, then hit **Assign**. The colors will shift on screen because you've changed what the numbers *mean*, not the numbers themselves.

**Convert to Color Profile** actually transforms pixel data so the image looks the same under the new profile. Head to **Image → Color Management → Convert to Color Profile**, choose your destination profile, then set the **Rendering Intent** (Perceptual, Relative Colorimetric, Saturation, or Absolute) and decide whether to enable **Black Point Compensation**. Click **Convert** when ready. This is what you want before sending to a printer or handing off to a workflow that expects a specific color space.

**Discard Color Profile** strips the current profile and reassigns GIMP's built-in sRGB. Pixel values stay unchanged — only the interpretation shifts. It's handy when you want to export a file without an embedded profile, since GIMP's built-in sRGB profiles are never written into exported files. Find it at **Image → Color Management → Discard Color Profile**.

**Save Color Profile to File** writes a copy of the image's current ICC profile to disk via **Image → Color Management → Save Color Profile to File**. Navigate to your desired location, give it a `.icc` or `.icm` extension, and click **Save**. This works for any assigned profile, including GIMP's built-in sRGB.

The key distinction: *assign* relabels without changing pixels (appearance shifts), while *convert* remaps pixels to preserve appearance under a new profile.
