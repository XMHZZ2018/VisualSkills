# Bucket Fill and Gradient (GIMP 2.10)

The Bucket Fill tool floods an area with a solid color or pattern in a single click. Grab it from **Tools > Paint Tools > Bucket Fill** or press **Shift+B**. By default it fills with the foreground color; hold **Ctrl+click** to use the background color instead, or press **Alt** to toggle between them on the fly.

In the tool options, you choose between three fill types: FG Color Fill, BG Color Fill, or Pattern Fill. Below that, the Affected Area setting controls *what* gets filled — "Fill whole selection" dumps color across the entire selection (or layer), while "Fill similar colors" works like a smart flood-fill, spreading outward from your click point until colors differ too much from the source pixel.

See `fig01.png`.

The **Threshold** slider is your main lever for "Fill similar colors" mode. Crank it up and the fill bleeds further into neighboring hues; keep it low for tight, precise fills. If you're filling on a transparent layer and see a halo of the old color around edges, bump the threshold a bit higher so semi-transparent pixels get caught too. Also make sure the **Lock** option in the Layers dialog is unchecked if you want to fill fully transparent regions.

Starting in GIMP 2.10.10, there's a third mode — **Fill by line art detection** — designed for coloring hand-drawn artwork. It intelligently closes small gaps in linework so color doesn't leak through. Tweak "Maximum gap length" and "Maximum growing size" in the options to control how aggressively it seals those gaps.

For quick flat fills without the Bucket tool at all, use **Edit > Fill with FG Color** (**Ctrl+,**) or **Edit > Fill with Pattern** (**Ctrl+;**) to instantly flood the current selection.

The **Gradient** tool (**G**) creates smooth color transitions. Activate it from **Tools > Paint Tools > Gradient**, then click and drag across your canvas — the direction and length of your drag line define where the gradient starts, ends, and how sharp the transition is. A short drag gives a tight, punchy blend; a long drag makes it gentle.

The two big decisions are which gradient preset to use (pick from the drop-down in tool options) and which **Shape** to apply. Linear is the default straight-line blend, Radial gives you a circular spotlight effect, and the Shaped variants follow the contour of your selection — great for bevels and 3D-looking fills. The **Repeat** setting (None, Sawtooth Wave, Triangular Wave) tiles the gradient along the drag direction for striped or wave effects.

In GIMP 2.10, gradient editing happens live on canvas. After dragging your line, you can click stops (the small squares on the line) to reposition them, change their colors, or add new ones. GIMP automatically creates a custom gradient copy so your edits are preserved across sessions. The **Offset** slider pushes the gradient's starting point away from your click, letting you control how much of the foreground color stays solid before the blend begins.

See `fig02.png`.

Hold **Ctrl** while dragging to constrain the gradient line to 15-degree angles — handy for perfectly horizontal or vertical blends.
