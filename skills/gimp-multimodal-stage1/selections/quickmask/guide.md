# Using QuickMask (GIMP 2.10)

QuickMask lets you paint a selection rather than trace its outline. Instead of wrestling with lasso or path tools for complex shapes, you simply grab a brush and paint the area you want selected — far more intuitive for organic or detailed selections.

A GIMP selection is actually a grayscale channel where pixel values range from 0 (unselected) to 255 (fully selected). The marching ants you normally see are just a contour drawn at the halfway point. QuickMask reveals the full structure of that channel as a translucent colored overlay — by default, red — so you can see exactly what's partially selected, not just the boundary.

To enter QuickMask mode, click the small button at the bottom-left corner of the image window, or use **Select > Toggle QuickMask**, or press **Shift+Q**. If you already have an active selection, the mask initializes from it.
Once you're in QuickMask mode, pick any paint tool and start painting. White paint adds to the selection (those pixels become fully clear through the overlay). Black paint removes from the selection (those pixels get covered by the red mask). Gray values create partial selections — useful for feathered edges and smooth transitions.

You're not limited to brushes. The Bucket Fill and Gradient tools work too — you can even use selection tools to define a region and then fill it, all without destroying what you've already painted on the mask.

When you're happy with the mask, click the same bottom-left button again (or **Shift+Q**) to leave QuickMask mode. Your painted mask converts back into a standard marching-ants selection, ready for whatever operation comes next.

To save a QuickMask for later reuse, make sure QuickMask mode is toggled off (so you see marching ants), then go to **Select > Save to Channel**. This stores the selection as a named channel you can reload anytime.

One handy trick: while in QuickMask mode, **Cut** and **Paste** operate on the selection channel itself, not the image. This gives you a quick way to transfer a complex selection between images.
