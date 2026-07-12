# Tone Mapping (GIMP 2.10)

The Tone Mapping filters live under **Colors > Tone Mapping** and are designed to squeeze high dynamic range (HDR) data into a displayable range. They work best after you convert your image to 32-bit floating point precision via **Image > Precision > 32 bit floating point (linear light)** — without that, you won't see much benefit.

<!-- figure: The Colors > Tone Mapping submenu showing all five filter options -->

**Fattal et al. 2002** reduces local gradient magnitudes to compress luminance. It's great for revealing shadow detail in contrasty scenes. The key sliders are Alpha (gradient threshold for detail), Beta (local detail strength), Saturation, and Noise (threshold for suppressing detail in flat areas). Fair warning: this one is slow on large images. A good trick is to make a small selection first, dial in your settings, save them as a preset, then apply to the full image.

**Mantiuk 2006** takes a perceptual approach, constraining contrast across multiple spatial frequencies. Its controls are simpler — Contrast (compression amount), Saturation, and Details (gradient emphasis). It shares Fattal's speed characteristics, so the same preset-on-a-crop workflow applies here too.

**Reinhard 2005** is a global operator inspired by photoreceptor physiology — faster than Fattal or Mantiuk, though still not instant on big files. You get Brightness (overall image brightness), Chromatic adaptation (how well it handles color shifts across the image), and Light adaptation (response to luminance variation). It's a solid default when you want a quick, natural-looking result without micromanaging local detail.

**Stress** is a simpler spatial color re-mapping filter also found in this submenu. It doesn't come from the HDR research literature like the others, but it can still help even out tonal distributions in tricky lighting.

**Retinex** mimics the way human vision adapts to poor lighting — the name is short for "retina + cortex." It's particularly good at pulling detail out of underexposed regions. The Level control has three modes: Uniform treats all intensities equally, Low boosts darker areas, and High favors the brighter zones. Scale (default 240) sets filter depth, Scale division (keep it at 3) controls multiscale iterations, and Dynamic adjusts color saturation — higher values desaturate. Note that Retinex only works on RGB images; grayscale and indexed modes disable the menu entry.

All of these filters share common UI elements: Presets for saving and recalling settings, Input Type and Clipping controls, Blending Options, and a Preview with Split view so you can compare before and after in real time.
