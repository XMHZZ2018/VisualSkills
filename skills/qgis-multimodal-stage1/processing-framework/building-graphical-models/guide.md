# Building Graphical Models (QGIS 3.44)

The Model Designer lets you chain processing algorithms into a single reusable workflow. Instead of running five tools by hand every time, you wire them together once and execute the whole chain with one click — swapping inputs as needed.

Open the designer from **Processing > Model Designer**. You'll get a canvas in the center and a set of panels on the left: **Inputs** (parameters your model will ask for), **Toolbox** (all available algorithms), **Model Properties** (name and group), **Variables**, and **Undo History**. Give your model a name and group in Model Properties first — you'll need both before saving.

See `fig01.png`.

Start by defining inputs. Drag an input type (Vector Layer, Raster Layer, Number, etc.) from the **Inputs** panel onto the canvas. Double-click to configure it — set a description, default value, and whether it's mandatory or hidden under the **Advanced** section. Each input becomes a green box on the canvas that you'll wire into algorithms later.

Next, add algorithms from the **Toolbox** panel — double-click or drag them onto the canvas. A configuration dialog appears where each parameter has a dropdown letting you choose its source: a static **Value**, a **Pre-calculated Value** (expression), a **Model Input**, or the **Algorithm Output** of a previous step. Wire your inputs into the algorithm parameters, mark any final outputs with the **Model Output** option so they're exposed when the model runs, then click **OK**.

See `fig02.png`.

Connections between elements appear as arrows automatically. You can also drag between the circular sockets on each box — outputs on the right, inputs on the left. If an algorithm depends on a prior step but doesn't consume its output directly (e.g., two SQL operations on the same database), use the **Dependencies** parameter to enforce execution order.

Use **Edit > Add Group Box** to visually cluster related steps in large models — you can name and color each box. Toggle **View > Show Comments** to annotate individual steps with notes visible only inside the designer.

Run the model with **F5** or **Model > Run Model…**. You can also select a subset of steps and hit **Shift+F5** to run only those, which is invaluable for debugging expensive workflows without re-running everything. Right-click any algorithm after a run to choose **View Output Layers** and inspect intermediate results without marking them as formal model outputs.

Save your model with **Ctrl+S** — it writes a `.model3` file. Drop it in the default `models` folder and it appears in the Processing Toolbox like any built-in algorithm. You can also embed it directly in a project file via **Model > Save Model in project**. For sharing or automation, **Model > Export > Export as Script Algorithm…** generates a standalone Python script you can run from the console.

Document your model with **Model > Edit Model Help…** — fill in descriptions for each parameter and output so future users (including you in six months) know what the model expects.

See `fig03.png`.
