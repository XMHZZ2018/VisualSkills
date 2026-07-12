# Writing Script-Fu Scripts (GIMP 2.10)

Script-Fu is GIMP's built-in scripting language based on TinyScheme, a lightweight dialect of Lisp. Everything in Scheme lives inside parentheses, with the function name always coming first — so adding numbers looks like `(+ 3 5)` rather than `3 + 5`. Spacing matters: you must have whitespace after every operator or function name.

To experiment, open the interactive console via **Filters > Script-Fu > Console**. Type expressions into the **Current Command** field at the bottom, hit **Enter**, and results appear in the output area above. It's the fastest way to test ideas before committing them to a file.

See `fig01.png`.

Variables are declared with `let*`, which creates a local scope: `(let* ( (a 1) (b 2) ) (+ a b))`. To reassign a variable later, use `set!`. Functions are defined with `define` — the last expression evaluated is automatically the return value, so there's no explicit `return` keyword. Lists are central to Scheme; you create them with a leading apostrophe like `'(1 2 3)`, access the first element with `car`, and grab the rest with `cdr`.

When you're ready to write a real script, save it as a `.scm` file in one of GIMP's script folders (check **Edit > Preferences > Folders > Scripts** for paths). Every script needs two things: a main function that does the work, and a `script-fu-register` call that tells GIMP about the function's name, menu label, description, author info, and its parameters with types like `SF-STRING`, `SF-FONT`, `SF-ADJUSTMENT`, and `SF-COLOR`. After registering, call `script-fu-menu-register` to place it in a menu — for example, `"<Image>/File/Create/Text"` puts it under **File > Create > Text**.

After saving your `.scm` file, reload with **Filters > Script-Fu > Refresh Scripts** and your new entry appears in the menu. The registration parameters automatically generate a dialog with appropriate widgets (text fields, font pickers, color buttons, spinners) so users can configure the script without touching code.

Inside your script, use the Procedure Browser (**Help > Procedure Browser**) to discover available GIMP functions. All PDB functions return lists, so wrap calls in `car` to extract the value — e.g., `(car (gimp-image-new 10 10 RGB))`. A typical workflow creates an image, adds a layer with `gimp-layer-new`, inserts it with `gimp-image-insert-layer`, sets colors with `gimp-context-set-foreground`, draws text with `gimp-text-fontname`, resizes everything to fit, then displays the result with `gimp-display-new`. Finish with `(gimp-image-clean-all theImage)` to clear the dirty flag so GIMP won't nag about saving throwaway test output.
