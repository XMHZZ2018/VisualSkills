No inline image references in this file. The content is purely text-based. I have everything I need to write the guide.

# Setting Tile Cache for Performance (GIMP 2.10)

GIMP organizes image data into chunks called "tiles." These tiles live either in fast RAM or on the slower hard disk. The tile cache setting tells GIMP how much RAM it's allowed to use before spilling data to disk. Get this right and everything feels snappy; get it wrong and either GIMP crawls or your other apps starve.

To adjust it, open **Edit > Preferences**, then navigate to **System Resources**. You'll find the tile cache size setting there, specified in megabytes.

For most people with a modern machine (2 GB RAM or more), setting the tile cache to about half your total RAM is a solid starting point. If GIMP is your primary application and you won't be multitasking heavily, bumping it up to 3/4 of your RAM is perfectly reasonable.

If GIMP feels sluggish but switching to other apps is instant, increase the value — GIMP needs more breathing room. If other programs complain about memory or start misbehaving, dial it back.

A quick way to calculate: check how much free RAM (including buffer/cache) you have while your other usual apps are running. That free amount, minus a small safety margin, is your tile cache sweet spot.

One more trick — move the swap directory to your fastest disk, or at least a different physical disk than your working files. You can change this under **Edit > Preferences > Folders**. This keeps GIMP's overflow traffic from competing with your file I/O.

Bottom line: start at 50% of RAM, nudge up or down based on how your system feels, and put swap on the fastest available disk.
