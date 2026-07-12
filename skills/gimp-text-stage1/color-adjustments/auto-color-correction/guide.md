# Automatic Color Correction (GIMP 2.10)

All automatic color tools live under **Colors > Auto**. They redistribute pixel brightness and color across the histogram without requiring manual input — just pick one and see what happens.

**Equalize** (**Colors > Auto > Equalize**) flattens the Value channel histogram so every brightness level gets roughly equal representation. It stretches frequently-occurring colors apart and compresses rare ones. The effect can be dramatic — great for revealing hidden detail, but sometimes oversaturates. Works on RGB and Grayscale layers.

**White Balance** (**Colors > Auto > White Balance**) stretches each RGB channel independently after discarding the extreme 0.05% of pixels at both ends. By trimming outliers (dust specks, sensor noise), it produces cleaner whites and blacks than a naive stretch. Expect some hue shifts since channels are handled separately. RGB only.

**Stretch Contrast** (**Colors > Auto > Stretch Contrast**) finds the actual min/max in each channel and stretches them to the full 0–255 range. Unlike White Balance, it keeps every pixel — so a single bright outlier can limit the stretch. Enable **Keep Colors** to apply the same stretch across all channels (preserving hues) or **Non-Linear Components** to operate on gamma-corrected values like the legacy Normalize filter.

**Color Enhance** (**Colors > Auto > Color Enhance**) boosts saturation without touching hue or lightness. It converts to CIE LCh, stretches the Chroma range to its maximum, then converts back. Use it when the image looks washed-out but the luminance is already fine. Disabled on Grayscale images.

Since each command uses a different strategy, results vary per image. Try them all — they're non-destructive if you undo — and pick whichever histogram spread looks best for your particular shot. For finer control, reach for the **Levels** tool instead.
