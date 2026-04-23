# Shape Styling & Colors (LibreOffice Impress 7.3.7)

Select any shape and you can restyle it quickly using the **Line and Filling** toolbar. If it's not visible, turn it on via **View > Toolbars > Line and Filling**. From there, the **Area Style/Filling** drop-down lets you pick a fill type — **None**, **Color**, **Gradient**, **Hatching**, **Bitmap**, or **Pattern** — and then choose a specific option from the adjacent list.

For more control over fills, right-click the shape and choose **Area**, or go to **Format > Object and Shape > Area**. The Area dialog opens with tabs for each fill type. Click **Color** to pick from a palette, or hit **Pick** to open the full color chooser where you can enter exact **RGB**, **Hex**, **HSB**, or **CMYK** values.

To create a custom color, open the Area dialog, go to **Color**, set your RGB values, then click **Add** in **Custom Palette** and give it a name. It'll appear in the Custom palette for reuse. You can delete custom colors the same way — select **Custom** from the **Palette** drop-down, pick the color, and hit **Delete**.

Gradients work similarly — open the Area dialog, click **Gradient**, choose a preset, and tweak **Type**, **Angle**, **From Color**, and **To Color** under **Options** if the defaults don't fit.

To style a shape's border, select the shape and use the **Line and Filling** toolbar to set **Line Style**, **Line Width**, and **Line Color**. For full control, open the Line dialog via **Format > Object and Shape > Line** (or right-click and choose **Line**). There you'll find tabs for **Line** properties, **Shadow**, **Line Styles**, and **Arrow Styles**. You can adjust corner style, cap style, transparency, and even add arrow heads to connectors.

The **Properties** sidebar works just as well — click **Properties**, then expand the **Area** or **Line** panels to adjust fill, color, transparency, and borders without opening a separate dialog. Hit **More Options** on any panel's title bar for the full dialog.

Shadows on lines and shapes are configured from the **Shadow** tab in their respective dialogs, where you set color, distance, blur, and transparency.

## Recoloring many shapes to a brand palette

When a task asks you to recolor every shape on a slide (or across slides) according to a brand palette, **do not loop shape-by-shape through the right-click > Area dialog** — it is the single biggest time sink on this kind of task. Two faster paths:

1. **Group-by-role multi-select.** If multiple shapes share the same target color (e.g. all "primary" shapes become brand-blue), Shift+click all of them first, then open **Format > Object and Shape > Area** once. The Area dialog applies the fill to every selected shape in one step. See `multiselect_recolor.jpg` for the expected target: all selected shapes show selection handles simultaneously before the dialog is opened.

2. **Custom palette first.** If your task gives you N brand hex codes, open the Area dialog once, enter the first hex in **Pick > Hex**, and click **Add** in the **Custom Palette** to save it with a clear name. Repeat for each hex. After that, applying a color is a single click on the saved swatch rather than a full hex-typing sequence per shape. See `custom_palette_saved.jpg` for the expected state of the Custom palette after all brand colors are added.

## Using the sidebar instead of right-click Area

The right-click context menu can be flaky — clicks sometimes land on the slide behind the shape and dismiss the menu before "Area…" is selected. The **Properties sidebar** (opened via the rightmost sidebar rail, see `properties_sidebar_area.jpg`) is more reliable: the **Area** panel has a fill-color dropdown that opens a color picker in place, and the picker stays anchored to the sidebar rather than floating over the slide. Prefer the sidebar when you are repeatedly changing fills.
