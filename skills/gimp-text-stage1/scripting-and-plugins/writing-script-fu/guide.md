# Writing Script-Fu Scripts (GIMP 2.10)

Script-Fu is GIMP's built-in scripting language based on TinyScheme. Everything in Scheme lives inside parentheses, with the function name always first: `(+ 3 5)` returns 8. Open the interactive console via **Filters > Script-Fu > Console** to experiment as you go.

Declare local variables with `let*` — each binding is a pair of name and value wrapped in parens: `(let* ( (a 1) (b 2) ) (+ a b))`. Change a variable later with `set!`. Define reusable functions with `(define (MyFunc param1 param2) body)` — the last expression is the return value automatically.

Lists are central to Scheme. Quote a literal list with an apostrophe: `'(1 2 3)`. Use `car` to grab the first element and `cdr` for the rest. Every GIMP procedure returns a list, even single values, so wrap calls in `car` to extract results: `(car (gimp-image-new 10 10 RGB))`.

Save your scripts as `.scm` files in one of the folders listed under **Edit > Preferences > Folders > Scripts**. Name your main function `script-fu-text-box` (or similar `script-fu-` prefix) so it groups neatly in the Procedure Browser. After saving, reload with **Filters > Script-Fu > Refresh Scripts**.

Register your script so GIMP builds a dialog for it. Call `script-fu-register` with the function name, menu label, description, author, copyright, date, image type (use `""` if creating new images), then parameter declarations like `SF-STRING`, `SF-FONT`, `SF-ADJUSTMENT`, or `SF-COLOR`. Follow it with `script-fu-menu-register` to place it in the menu tree — for example, `(script-fu-menu-register "script-fu-text-box" "<Image>/File/Create/Text")` puts it under **File > Create > Text**.

Inside the function body, call GIMP procedures directly: `gimp-image-new`, `gimp-layer-new`, `gimp-image-insert-layer`, `gimp-text-fontname`, `gimp-image-resize`, `gimp-layer-resize`. Set colors with `gimp-context-set-foreground` and `gimp-context-set-background`, fill a layer with `gimp-drawable-fill`, and show the result with `gimp-display-new`. Call `gimp-image-clean-all` at the end if you want to suppress the "unsaved changes" prompt on trivial outputs.

The Procedure Browser (**Help > Procedure Browser**) is your best friend — it documents every callable function, its parameters, and return values. Between that and the Script-Fu Console for live testing, you can build anything from simple text-box generators to complex batch-processing scripts.
