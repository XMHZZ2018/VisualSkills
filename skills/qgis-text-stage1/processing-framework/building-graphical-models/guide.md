No images are present in the directory — just the markdown text. I have all the source material I need. Here's the guide:

# Building Graphical Models (QGIS 3.44)

The Model Designer lets you chain processing algorithms into a single reusable workflow. Open it from **Processing > Model Designer**. The canvas is where you'll visually wire inputs to algorithms and algorithms to each other.

Start by giving your model a name and group in the **Model Properties** panel — this determines where it appears in the Processing Toolbox. Then define your inputs from the **Inputs** panel on the left: drag parameters like Vector Layer or Raster Layer onto the canvas, double-click each to set descriptions, defaults, and whether they're mandatory or advanced.

Next, build the workflow by dragging algorithms from the **Toolbox** panel onto the canvas. When you add an algorithm, a dialog appears where each parameter has a dropdown offering **Value** (static), **Pre-calculated Value** (expression), **Model Input**, or **Algorithm Output** — this is how you wire things together. Mark any output you want exposed to the user with the **Model Output** option; leave intermediate outputs unmarked.

Connections appear automatically when you assign inputs, but you can also drag between the circular sockets on each item. If an algorithm depends on another without using its output directly (e.g., a DB import before a SQL query), set it explicitly in the **Dependencies** parameter.

Use **Edit > Add Group Box** to visually cluster related steps in large models. Reorder how inputs appear to the user via **Model > Reorder Model Inputs...** and control output layer stacking with **Model > Reorder Output Layers...**. Add comments to any element via right-click for your own documentation.

Run the full model with **F5** or just selected steps with **Shift+F5** — handy for debugging without re-running expensive early stages. You can also right-click any algorithm and choose **Run from Here...** to pick up mid-workflow using cached results from a prior run.

Save your model as a `.model3` file with **Ctrl+S**, or embed it in the project via **Save Model in project**. Models saved to the default `models` folder automatically appear in the Processing Toolbox and can be nested inside other models. Export to Python via **Export > Export as Script Algorithm...** when you need a standalone script.
