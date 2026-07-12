# Using Python-Fu (GIMP 2.10)

Python-Fu is GIMP's built-in Python scripting environment — a set of Python modules wrapping *libgimp* so you can automate tasks, write plug-ins, or just experiment with GIMP's internals interactively.

To open the console, go to **Filters > Python-Fu > Console**. By default that's the only item in the Python-Fu submenu.

See `fig01.png`.

The console window is essentially an interactive Python shell pre-loaded with GIMP's libraries. You type commands at the `>>>` prompt, press **Enter**, and see results (or errors) printed directly in the scrollable output area above.

See `fig02.png`.

At the bottom of the console you'll find four buttons. **Save** dumps the entire session (input and output) to a file — handy for keeping a record of what worked. **Clear** wipes the display (careful, you can't get it back). **Close** dismisses the console.

The most useful button is **Browse**. It opens the Procedure Browser, which lists every function in GIMP's PDB (Procedural Database). Find the procedure you want, hit **Apply**, and the console pastes a ready-made call with placeholder parameter names. Replace those placeholders with real values — for example, `image = pdb.gimp_image_new(400, 300, RGB)` — and press **Enter** to run it.

One thing to watch: PDB constants like `RGB-IMAGE` or `OVERLAY-MODE` need their hyphens swapped to underscores in Python — so use `RGB_IMAGE`, `OVERLAY_MODE`.

You're not limited to PDB calls either. You can use GIMP's object-oriented Python bindings directly, like `image = gimp.Image(400, 300, RGB)`, which does the same thing in a more Pythonic way.
