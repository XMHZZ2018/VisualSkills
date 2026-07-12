# Using Python-Fu (GIMP 2.10)

Python-Fu is GIMP's built-in Python scripting environment — a set of Python modules wrapping *libgimp* that let you automate tasks, write plug-ins, or just experiment interactively with GIMP's internals.

To open the console, go to **Filters → Python-Fu → Console**. This launches an interactive Python shell preconfigured with access to GIMP's procedure database (PDB) and library routines.

The console window works like any Python interpreter. Type a command at the `>>>` prompt, hit **Enter**, and you'll see the output (or error) immediately above. It's a great scratchpad for testing ideas before committing them to a full plug-in.

At the bottom of the console you'll find four buttons. **Save** dumps the entire session (input and output) to a file. **Clear** wipes the console history — careful, there's no undo on that. **Close** dismisses the window.

The real power move is **Browse**. Clicking it opens the Procedure Browser with an extra **Apply** button. Find the procedure you want, hit **Apply**, and a templated call gets pasted into your console — something like `pdb.gimp_image_new(width, height, type)`. Replace the placeholder names with real values (e.g., `pdb.gimp_image_new(400, 300, RGB)`) and press **Enter**.

One gotcha: PDB constants like `RGB-IMAGE` or `OVERLAY-MODE` need hyphens swapped for underscores in Python — use `RGB_IMAGE`, `OVERLAY_MODE`.

You're not limited to PDB calls either. You can use the object-oriented API directly — for example, `image = gimp.Image(400, 300, RGB)` does the same thing as the PDB version above.
