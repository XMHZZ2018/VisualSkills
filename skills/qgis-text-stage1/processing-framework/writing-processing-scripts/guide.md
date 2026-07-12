# Writing Processing Scripts (QGIS 3.44)

You have two approaches for writing custom processing algorithms: extending `QgsProcessingAlgorithm` (full control, works in plugins) or using the `@alg` decorator (simpler but limited to your personal Scripts provider).

To get started, open the Processing Toolbox and click **Scripts > Create new script from template** — this gives you a skeleton with all the mandatory methods already stubbed out. Save your `.py` file in the default `scripts` folder and it automatically appears in the Toolbox.

Your class needs a handful of required methods: `name()` returns a unique lowercase ID, `displayName()` gives it a human-readable label, `createInstance()` returns a fresh copy, `initAlgorithm()` declares inputs/outputs, and `processAlgorithm()` does the actual work.

Inside `processAlgorithm`, call `processing.run()` to chain existing algorithms — pass `is_child_algorithm=True` along with the `context` and `feedback` objects so cancellation and progress reporting propagate correctly. Retrieve parameter values with helpers like `self.parameterAsSource()` or `self.parameterAsDouble()`.

Use the `feedback` object for all user communication: `feedback.setProgress(percent)` updates the progress bar, `feedback.pushInfo(text)` logs messages, and `feedback.isCanceled()` lets you bail out early. For fatal errors, raise `QgsProcessingException`. Never use message boxes or print statements.

The `@alg` decorator approach skips the boilerplate — decorate your function with `@alg(name=..., label=..., group=..., group_label=...)`, then stack `@alg.input` and `@alg.output` decorators to declare parameters. The function signature is `(instance, parameters, context, feedback, inputs)`.

Always explicitly declare every output your algorithm produces (layers, numbers, strings). Processing auto-loads declared layer outputs into the project, and extra numeric outputs make your script composable in the Graphical Modeler. If your algorithm crashes unexpectedly, override `flags()` to return `QgsProcessingAlgorithm.FlagNoThreading` — this forces execution on the main thread.
