# Creating and Managing Layers (GIMP 2.10)

Layers in GIMP work like a stack of transparent slides — the bottom layer is your background, and everything above composites on top of it. You manage them through the Layers dialog and the **Layer** menu.

To create a fresh layer, go to **Layer → New Layer…** and you'll get a dialog where you set the name, dimensions, fill type (foreground color, white, transparency, etc.), and blending mode. The new layer appears directly above whatever layer is currently active. You can also quickly duplicate the active layer with **Layer → Duplicate Layer** — handy for experimenting without risk.

Pasting with **Ctrl+V** creates a "floating selection," which is a temporary layer. You need to either anchor it to the layer below (click the anchor icon) or promote it to a proper layer via **Layer → To New Layer** before doing anything else.

To remove a layer, just hit **Layer → Delete Layer** or click the trash icon at the bottom of the Layers dialog.

Reordering layers lives under **Layer → Stack**. Use **Raise Layer** and **Lower Layer** to nudge a layer one position, or jump straight to the top or bottom with **Layer to Top** / **Layer to Bottom**. You can also drag layers directly in the Layers dialog.

Toggle a layer's visibility by clicking its eye icon — Shift-click the eye to solo that layer and hide all others. Click between the eye and the thumbnail to add a chain-link icon, which groups layers together for moves and transforms.

When you're ready to combine work, **Image → Merge Visible Layers…** (Ctrl+M) collapses all eye-icon-visible layers into one, with options to clip the result to the image or bottom layer bounds. For final export, **Image → Flatten Image** squashes everything into a single opaque layer with no alpha channel — use this right before saving to formats like JPEG that don't support transparency.
