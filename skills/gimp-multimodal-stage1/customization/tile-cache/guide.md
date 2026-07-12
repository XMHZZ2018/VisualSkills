The source markdown contains no inline image references, so there are no screenshots to load. I'll write the guide based on the text content.

# Setting Tile Cache for Performance (GIMP 2.10)

GIMP organizes image data into chunks called "tiles." While you work, these tiles live either in fast RAM or on the slower hard disk. The tile cache setting controls how much RAM GIMP is allowed to use before it starts swapping data to disk. Get it right and everything feels snappy; get it wrong and either GIMP crawls or your other apps start choking.

You'll find the setting under **Edit > Preferences**, then navigate to **System Resources** in the left-hand tree. The **Tile cache size** field is what you're after. You can also change the **Swap folder** location under the **Folders** section of the same dialog.
For a quick-and-dirty rule: set tile cache to about half your total RAM. If you have 8 GB or more and GIMP is your primary working application, bumping it to three-quarters of your RAM is perfectly reasonable. If you mostly make small screenshots or logos and don't want to think about it, the default is fine — just leave it alone.

For a more precise number, close GIMP, open all the other applications you'd normally run alongside it, and check how much free memory remains (on Linux, run `free` and look at the "-/+ buffers/cache" line; on macOS or Windows, check Activity Monitor or Task Manager). That free amount — minus a small safety margin — is your ideal tile cache value.

If tile cache is set too low, GIMP writes to disk constantly even when RAM is available, which makes editing feel sluggish for no good reason. Set it too high and your OS starts swapping other applications out to disk, which can cause freezes or even crashes in those programs.

After setting your value, pay attention over the next few sessions. If GIMP feels slow but switching to other apps is instant, bump the cache up a bit. If other programs complain about memory or start misbehaving, dial it back down.

One more trick: move GIMP's swap directory to your fastest available disk — ideally a different physical drive from where your working files live. You can change this under **Edit > Preferences > Folders > Swap**. This won't replace having enough RAM, but it softens the penalty when GIMP does need to hit the disk.
