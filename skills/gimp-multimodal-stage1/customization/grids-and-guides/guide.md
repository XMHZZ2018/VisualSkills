# Using Grids and Guides (GIMP 2.10)

Every image in GIMP has a grid attached to it — it's just invisible by default. Toggle it on with **View > Show Grid** and you'll see plus-shaped crosshairs at every intersection, spaced 10 pixels apart. If you find yourself turning it on constantly, check "Show grid" in **Edit > Preferences > Image Window Appearance** so it's always there when you open an image.

The default crosshair style is subtle, but you have options. Go to **Image > Configure Grid…** to change the line style (dots, crosshairs, dashed, double-dashed, or solid), pick foreground/background colors, and adjust the spacing and offset. These changes apply only to the current image — for global defaults, use the Default Image Grid page in Preferences.

See `fig01.png`.

Once you have a grid visible, enable **View > Snap to Grid** to make your pointer magnetically lock to grid lines within 8 pixels. You can adjust that threshold under **Edit > Preferences > Tool Options**. Snapping works even with the grid hidden, though that's rarely useful.

Guides give you more flexibility than the fixed grid. Click on a ruler (top or side of the canvas) and drag inward — a blue dashed line follows your pointer. Release it where you want. For precise placement, use **Image > Guides > New Guide…** and type an exact pixel position and direction (horizontal or vertical).

See `fig02.png`.

To reposition a guide, grab the **Move** tool (or press **M**), hover near the guide until your cursor changes to a hand, then drag. To delete one, just drag it back off the canvas onto the ruler. Remove all guides at once with **Image > Guides > Remove all Guides**.

Like the grid, guides support snapping — enable **View > Snap to Guides** and layers or selections will lock to nearby guides as you drag them. If the blue lines are getting distracting, temporarily hide them with **View > Show Guides**, but remember to turn them back on or you'll wonder why new guides seem broken.

One bonus trick: the **Slice Using Guides** plugin (**Filters > Web > Slice Using Guides**) can chop your image along guide positions into separate files — handy for web graphics.

If you need a grid baked into the actual image pixels (not just an overlay), use the **Filters > Light and Shadow > Grid** plugin, which renders permanent grid lines with more style options than the display grid offers.
