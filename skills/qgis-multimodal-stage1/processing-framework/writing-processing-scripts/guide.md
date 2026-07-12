# Writing Processing Scripts (QGIS 3.44)

You can write custom Processing algorithms in Python two ways: by extending `QgsProcessingAlgorithm` (full control, works in plugins) or by using the `@alg` decorator (less boilerplate, but locked to the Scripts provider).

To get started, open the Processing Toolbox and click **Scripts > Create new script from template** at the top. This drops you into the Processing Script Editor with the required class skeleton already filled in. Save your `.py` file into the default `scripts` folder and it shows up in the Toolbox automatically.

Your class needs a handful of mandatory methods. `name()` returns a unique lowercase ID. `displayName()` is what users see. `createInstance()` returns a fresh copy of your class. `initAlgorithm()` declares inputs and outputs using parameter types like `QgsProcessingParameterFeatureSource`, `QgsProcessingParameterDistance`, or `QgsProcessingParameterRasterDestination`. Use `'INPUT'` and `'OUTPUT'` as names for the main parameters — it's convention and keeps things predictable in the Sketcher.

The real work happens in `processAlgorithm(self, parameters, context, feedback)`. Pull values out with helpers like `self.parameterAsSource()` or `self.parameterAsDouble()`. To chain other algorithms, call `processing.run('native:buffer', {...}, is_child_algorithm=True, context=context, feedback=feedback)` — the `is_child_algorithm=True` flag is important so Processing knows it's a sub-step.

Check `feedback.isCanceled()` between heavy operations so users can bail out without waiting. Report progress with `feedback.setProgress(percent)` and send messages with `feedback.pushInfo(text)`. If something truly breaks, raise a `QgsProcessingException` — Processing handles the rest regardless of whether the algorithm was launched from the Toolbox, the sketcher, or the console.

The `@alg` decorator approach is more compact: stack `@alg.input` and `@alg.output` decorators above your function, and Processing wires up the UI for you. The trade-off is you can't ship these in a plugin — they always land under the user's Scripts provider.

Always declare every output your algorithm produces (layers, numbers, strings). Processing auto-loads declared layer outputs into the project, and numeric/string outputs become available to downstream algorithms in models. Never load layers yourself, and never pop up message boxes — let the framework handle the UI.

If your algorithm crashes intermittently, override `flags()` and return `QgsProcessingAlgorithm.FlagNoThreading` to force it onto the main thread — Processing runs algorithms in a background thread by default, and some PyQGIS calls aren't thread-safe.
