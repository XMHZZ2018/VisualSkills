# Automatic Color Correction (GIMP 2.10)

GIMP's automatic color correction tools live under **Colors > Auto**. They adjust brightness and color distribution on the active layer without any manual tweaking — just pick one and see what happens. Each command works differently, so try them all and keep whichever looks best for your particular image.

See `fig01.png`.

**Equalize** (**Colors > Auto > Equalize**) flattens the Value histogram so that every brightness level gets roughly equal representation. It stretches frequently-occurring pixel values further apart, which can dramatically boost contrast and reveal hidden detail. The trade-off is that results are unpredictable — sometimes stunning, sometimes garish. It works on RGB and Grayscale layers.

**White Balance** (**Colors > Auto > White Balance**) stretches the Red, Green, and Blue channels independently, but first discards the extreme 0.05% of pixels at each end of every channel's histogram. That trimming means stray dust specks or sensor noise won't skew the stretch. The result tends to produce pure whites and pure blacks, making it especially good for photos with a dull, washed-out look. Note that because each channel is stretched separately, slight hue shifts can occur. RGB only.

**Stretch Contrast** (**Colors > Auto > Stretch Contrast**) is similar to White Balance but keeps every pixel — it finds the actual min and max in each channel and stretches to fill the full range. Because it doesn't discard outliers, a handful of very bright or dark pixels can limit how far the histogram actually spreads. Enable **Keep Colors** in its options dialog to apply the same stretch to all three channels (preserving hues), or toggle **Non-Linear Components** to operate on gamma-corrected values like the old Normalize filter. Works on RGB, Grayscale, and Indexed.

See `fig02.png` for the original layer and its histograms.

**Color Enhance** (**Colors > Auto > Color Enhance**) doesn't touch brightness at all. Instead it converts to CIE LCh space and stretches the Chroma range to its maximum, then converts back. The effect is a saturation boost that preserves both hue and lightness — handy when an image looks flat in color but fine in exposure. It's disabled for Grayscale images.

As a general workflow: start with White Balance for everyday photos, try Equalize if you want a more aggressive correction, use Stretch Contrast when you need control over the hue-preservation option, and finish with Color Enhance if the colors still feel muted. All of these are non-destructive to undo — just hit **Edit > Undo** if the result isn't what you wanted.
