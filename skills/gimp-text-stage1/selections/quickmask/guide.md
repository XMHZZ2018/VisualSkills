# Using QuickMask (GIMP 2.10)

QuickMask lets you *paint* a selection rather than trace its outline — far easier for complex shapes where lasso or path tools would be tedious.

Toggle QuickMask on by clicking the small button at the bottom-left corner of the image window, or hit **Shift+Q**, or go to **Select > Toggle QuickMask**. If you already have an active selection, the mask initializes from it.

Once active, a translucent red overlay covers the image. Clear areas are fully selected; red areas are unselected. The overlay's transparency shows you the full grayscale structure of the selection — something marching ants can't convey.

Grab any paint tool and paint with white to *add* to the selection, or black to *remove* from it. Gray values create partial selections, which is great for feathered edges and smooth transitions. You can also use the **Bucket Fill** or **Gradient** tool to fill regions — this won't destroy any existing mask work.

When you're happy with the painted mask, click the same bottom-left button again (or **Shift+Q**) to leave QuickMask mode. Your painted area converts back into a standard marching-ants selection, ready for whatever operation comes next.

To save a QuickMask for later reuse, exit QuickMask mode first, then use **Select > Save to Channel**. This stores it as a named channel you can reload anytime.

One handy trick: while in QuickMask mode, **Cut** and **Paste** operate on the selection channel itself, making it easy to transfer complex selections between images.
