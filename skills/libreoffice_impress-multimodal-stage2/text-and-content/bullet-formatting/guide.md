# Bullet Formatting (LibreOffice Impress 7.3.7)

Impress gives you two flavors of lists — unordered (bullets) and ordered (numbers) — and the way you create them depends on whether you're working in an AutoLayout text box or a plain text box.

In AutoLayout text boxes, the outline styles are already set up as unordered lists with up to nine indent levels, each carrying its own bullet character and font size. Just click the placeholder text, start typing, and press *Enter* to add new points. To push a point deeper, hit *Tab* or press *Alt+Shift+Right Arrow*; to bring it back out, use *Shift+Tab* or *Alt+Shift+Left Arrow*. You can also use **Demote** and **Promote** in the **Lists** panel on the Sidebar or via **Format > Lists**.

See `fig01.png`.

For plain text boxes, you'll need to toggle bullets on yourself. Click inside the text box, then hit **Toggle Unordered List** or **Toggle Ordered List** on the Text Formatting toolbar, or find the same buttons in the **Lists** panel in the Properties deck on the Sidebar. You can also go to **Format > Lists** and pick **Unordered List** or **Ordered List** from there.

To pick a different bullet or numbering style quickly, click the small triangle next to **Toggle Unordered List** or **Toggle Ordered List** in the toolbar or Sidebar. This pops open a gallery of preset bullet shapes or numbering formats — dots, diamonds, squares, arrows, checkmarks, Roman numerals, and more. At the bottom you'll find **More Bullets** or **More Numbering** for even wider choices.

See `fig02.png`.

For full control, open the **Bullets and Numbering** dialog. Select your list items, then right-click and choose the dialog, or reach it through the **Lists** panel. On the left you'll see levels 1 through 10 (select a level or the range 1–10 to apply changes across all levels at once). The **Properties** area lets you set the **Type** (bullet character, number style, or image), **Color**, and **Rel. size** (as a percentage of the text size). Below that, **Position** controls the indent and spacing, and **Alignment** sets how the bullet or number sits relative to the text.

See `fig03.png`.

The **Scope** option at the bottom is worth noticing: choose **Selection** to change only the selected items, or **Slide** to apply to the whole slide. Hit **Apply to Master** if you want the change to propagate through the master slide to all slides using that layout.

To reorder list items without changing their indent level, use **Move Up** / **Move Down** on the Outline toolbar, in the **Lists** panel, or via **Format > Lists**. The keyboard shortcuts *Alt+Shift+Up Arrow* and *Alt+Shift+Down Arrow* do the same thing. Use *Shift+Enter* if you ever need a soft return — a new line within the same bullet point, without creating a new list item.

---

## UI Reference  —  Format Menu

_Scope: Lists submenu, Bullets and Numbering dialog entry_

The Format menu controls text and object formatting: character/paragraph styles, alignment, spacing, shapes, rotation, and arrangement of objects on slides.

Read the screenshot `ui-format-menu.png` in this directory.

## Elements

- **Text** `▸` — Text layout options
- **Spacing** `▸` — Line Spacing: 1 (Ctrl+1) / 1.5 (Ctrl+5) / 2 (Ctrl+2), Increase/Decrease Paragraph Spacing, Increase/Decrease Indent
- **Align Text** `▸` — Left (Ctrl+L), Center (Ctrl+E), Right (Ctrl+R), Justified (Ctrl+J), Top, Center, Bottom
- **Lists** `▸` — List formatting options
- **Clear Direct Formatting** (Shift+Ctrl+M) — Remove manual formatting
- **Styles** `▸` — Style application submenu
- **Character...** — Opens Character formatting dialog
- **Paragraph...** — Opens Paragraph formatting dialog
- **Bullets and Numbering...** — List style configuration dialog
- **Theme...** — Presentation theme settings
- **Table** `▸` — Table formatting options
- **Image** `▸` — Image adjustment options
- **Text Box and Shape** `▸` — Text box and shape formatting
- **Shadow** (checkbox) — Toggle drop shadow on selected object
- **Interaction...** — Configure click actions on objects
- **Name...** — Name the selected object
- **Alt Text...** — Set alternative text for accessibility
- **Distribute Selection** `▸` — Distribute objects evenly
- **Rotate** — Enter rotation mode for selected object
- **Flip** `▸` — Flip horizontally or vertically
- **Convert** `▸` — Convert object types
- **Align Objects** `▸` — Align objects relative to each other or the slide
- **Arrange** `▸` — Bring forward, send backward, etc.
- **Group** `▸` — Group, ungroup, enter/exit group

---

## UI Reference  —  Insert Menu

_Scope: Special Character... entry for custom bullet characters_

The Insert menu covers all content insertion: images, charts, tables, text boxes, comments, hyperlinks, OLE objects, special characters, and header/footer settings.

Read the screenshot `ui-insert-menu.png` in this directory.

## Elements

- **Image...** — File chooser dialog with preview and link-to-file options
- **Audio or Video...** — File chooser for media files
- **Chart...** — Inserts an editable default column chart as an embedded OLE object
- **Table...** — Opens Insert Table dialog (columns/rows spinners, default 5×2)
- **Media** `▸` — Gallery, Photo Album, Scan `▸`, Animated Image...
- **OLE Object** `▸` — Formula Object (Shift+Alt+E), QR and Barcode..., OLE Object...
- **Shape** `▸` — Shape category submenu
- **Snap Guide...** — Insert a snap guideline
- **Text Box** (F2) — Draw a text frame on the slide
- **Comment** (Ctrl+Alt+C) — Insert a yellow sticky-note comment
- **Fontwork...** — Decorative text effects gallery
- **Hyperlink...** (Ctrl+K) — Opens non-modal Hyperlink dialog with four link types: Internet, Mail, Document, New Document
- **Special Character...** — Character picker with search, font/block filters, favourites (greyed unless editing a text frame)
- **Formatting Mark** `▸` — Non-printing formatting marks
- **Slide Number** — Insert slide-number field at cursor
- **Field** `▸` — Date, time, and other field types
- **Header and Footer...** — Dialog with Slides and Notes and Handouts tabs for date/time, footer text, slide/page numbers, and "do not show on first slide" option
- **Form Control** `▸` — Form control insertion

