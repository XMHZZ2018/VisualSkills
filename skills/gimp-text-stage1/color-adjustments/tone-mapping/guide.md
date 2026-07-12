# Tone Mapping (GIMP 2.10)

All five tone-mapping filters live under **Colors → Tone Mapping**. They compress high dynamic range (HDR) data into displayable luminance (0.0–1.0), so you'll get the best results after converting your image to 32-bit floating point linear light via **Image → Precision**.

**Fattal et al. 2002** reduces local gradient magnitudes to pull detail out of extreme highlights and shadows. Tweak **Alpha** (gradient threshold), **Beta** (local detail strength), **Saturation**, and **Noise** (threshold for suppressing enhancement in noisy areas). It's computationally heavy — try dialing in settings on a small selection first, save as a preset, then apply to the full image.

**Mantiuk 2006** constrains contrast across multiple spatial frequencies. Its controls are **Contrast** (compression amount), **Saturation**, and **Details** (gradient emphasis). Same performance tip applies: work on a crop first.

**Reinhard 2005** is a simpler global operator modeled on photoreceptor physiology — faster than Fattal or Mantiuk, though still not instant on large files. Adjust **Brightness**, **Chromatic adaptation** (response to color variation), and **Light adaptation** (response to luminance variation).

**Stress** is a lightweight spatial color-enhancement filter useful for quick local-contrast boosts without the full HDR pipeline.

**Retinex** mimics how the human retina and cortex adapt to poor lighting — great for recovering shadow detail in underexposed photos. It only works on RGB images. Set **Level** to Uniform (balanced), Low (boosts darks), or High (favors brights). **Scale** (default 240) controls filter depth, **Scale division** (keep at 3) sets multiscale iterations, and **Dynamic** governs saturation — higher values desaturate more. Dynamic is the slider you'll fiddle with most, since its sweet spot is very image-dependent.
