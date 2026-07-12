# Layer Blend Modes (GIMP 2.10)

GIMP 2.10 offers 38 layer modes organized into seven groups: Normal, Lighten, Darken, Contrast, Inversion, HSV Components, and LCh Components. You set the blend mode from the **Mode** dropdown at the top of the **Layers** dialog. Each mode controls how the pixels of the upper layer combine with those below it — effects are cumulative through the stack, though setting anything other than Normal on the very bottom layer does nothing.

The **Normal** group is the default. Normal simply shows the top layer (use opacity to reveal what's underneath). Dissolve scatters pixels randomly in semi-transparent areas — useful for gritty textures. The group also includes special-purpose modes like Erase (punches transparency through the layer below) and Color Erase (selectively removes specific colors).

The **Lighten** group makes things brighter. Screen is the workhorse here — it inverts both layers, multiplies, then inverts back, producing a washed-out brightening effect (black has no effect, white stays white). Dodge divides the lower layer by the inverse of the upper, simulating the darkroom technique of reducing exposure. Addition simply sums pixel values, often clipping to white.

The **Darken** group does the opposite. Multiply is the classic: it multiplies pixel values together, so white is neutral and anything else darkens. Burn inverts the bottom layer, divides by the top, then inverts again — think of it as a more aggressive Multiply. Linear Burn adds both layers and subtracts 1.0 for an even heavier darkening.

See `fig01.png`.

The **Contrast** group boosts midtone separation. Overlay combines Multiply and Screen depending on whether the bottom pixel is above or below 50% brightness — great for punching up flat images. Soft Light is gentler and keeps edges smooth. Hard Light flips the logic so the top layer drives the split, producing vivid colors and sharp edges. Vivid Light pushes things further by applying Burn in shadows and Dodge in highlights simultaneously.

The **Inversion** group includes Difference (subtracts and takes the absolute value — handy for comparing two layers, since identical pixels go black) and Grain Extract/Merge, which let you isolate and reapply texture grain from a duplicate layer.

The **HSV Components** group decomposes color. HSV Hue takes only the hue from the upper layer while keeping saturation and value from below — perfect for recoloring objects without changing their shading. HSV Saturation does the same for color intensity. Place a solid white layer on top, set it to HSV Saturation, and the image turns grayscale instantly.

The **LCh Components** group works the same way but uses the perceptually uniform CIELCh color space. LCh Hue and LCh Chroma correspond to their HSV counterparts but produce more natural-looking results because LCh better matches how human vision perceives lightness differences. LCh Color combines hue and chroma in one mode, and Luminance adjusts brightness without shifting saturation.

A good way to explore these modes: duplicate your image layer, apply a modification to the copy (blur, invert, rotate), then flip through the Mode dropdown on the top layer to see what each blend does to your specific content.
