# Image Embedding (LibreOffice Impress 7.3.7)

When you insert an image into Impress, it's embedded by default — the image data lives inside the presentation file itself. That's usually what you want, because it means the file is self-contained and will look right on any machine. But there's also a linking option, and understanding the difference matters if you're sharing your work.

To insert an image, head to **Insert > Image** on the Menu bar. The Insert Image file browser opens, where you can navigate to your file and preview it by checking the **Preview** box on the lower left.

See `fig01.png`.

Here's the key detail: at the bottom of that file browser, you'll see an **Insert as Link** checkbox. If you leave it unchecked (the default), the image gets fully embedded into the presentation. If you check it, Impress only stores a reference to the file on disk — the image isn't actually inside the presentation.

Linking makes sense in a few situations. If the image file is very large, linking keeps your presentation file small. It's also handy when the same image appears across many presentations — say, a shared company background — since you maintain one source file. And sometimes you only need the image visible while working locally, like a holiday slideshow you'll only ever open on your own machine.

The downside of linking is portability. Move the presentation to another computer, and any linked images break because the original file paths no longer resolve. So if you plan to share, present on a different machine, or archive your work, embedding is the way to go.

To convert a linked image to an embedded one, the simplest approach is to remove the linked image, then re-insert it through **Insert > Image** without the **Insert as Link** checkbox selected. Once re-inserted, the image data is stored directly in the presentation file. Click **Open** and the image drops onto the center of your slide with selection handles ready for positioning.

After embedding, you can resize, crop, and format the image to fit your presentation needs — the image is now fully self-contained and safe to share.

---

## UI Reference  —  Insert Menu

_Scope: Image... entry with file chooser, preview, and Insert as Link checkbox_

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

