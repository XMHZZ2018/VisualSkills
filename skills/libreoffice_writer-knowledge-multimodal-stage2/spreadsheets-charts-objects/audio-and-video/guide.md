# Audio and Video (LibreOffice Writer 7.3.7)

Linked audio and video files won't matter if you print your document, but they come alive when the document is opened on a computer or exported to PDF or HTML — readers can click the links to play them.

To drop a media file into your document, go to **Insert > Media > Audio or Video** on the Menu bar. This opens the Insert Audio or Video dialog. Pick your file and hit **Open** to place it. You can filter by file type in that dialog — it defaults to *All audio and video files*, but you can also choose unsupported formats like `.mov` if needed.

One important gotcha: Writer only *links* media files — it doesn't embed them into the document itself. If you move the document to another computer without bringing the media along, the links break and nothing plays. The safest approach is to keep your media files in the same folder as the document, then move everything together.

You can also insert media clips from the Gallery. Open the Gallery deck on the Sidebar, browse to a theme that contains media (like **Sounds**), and simply drag the clip into your document area.

When you select a media file, the **Media Playback** toolbar appears automatically — usually docked at the bottom of the workspace, just above the Drawing toolbar. If it doesn't show up, enable it via **View > Toolbars > Media Playback**.
The toolbar gives you everything you need: **Play**, **Pause**, and **Stop** buttons for basic control, a **Repeat** toggle for looping, and a **Position** slider to scrub through the file. There's also a **Timer** showing current position and total length, a **Mute** button, and a **Volume** slider. The **Media path** field shows where the file lives on disk. For video clips, a **View** dropdown lets you adjust the scaling of the playback. You can also click **Insert Audio or Video** right from this toolbar to add another file without going back to the menu.

---

## UI Reference  —  Insert Menu

_Scope: Media submenu: Audio or Video…, Gallery, Scan_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

Read the screenshot `ui-insert-menu.png` in this directory.

## Elements

- **Page Break** (Ctrl+Return) — Insert a manual page break at cursor.
- **More Breaks** (►) — Manual Row Break (Shift+Return), Column Break (Shift+Ctrl+Return), Manual Break… (dialog to choose break type and page style).
- **Image…** — Open file chooser to insert a raster or vector image.
- **Chart…** — Embed a chart OLE object.
- **Media** (►) — Gallery, Scan, Audio or Video…
- **OLE Object** (►) — Formula Object (Shift+Alt+E), QR and Barcode…, OLE Object…
- **Shape** (►) — 7 shape categories: Line, Basic Shapes, Block Arrows, Symbol Shapes, Stars and Banners, Callout Shapes, Flowchart — each opens a named-shape palette.
- **Section…** — Opens Insert Section dialog (tabs: Section, Columns, Indents, Area, Footnotes/Endnotes). Supports linked sections, write protection, and conditional hiding.
- **Text from File…** — Insert text from an external file.
- **Text Box** — Draw a floating text frame on the canvas.
- **Comment** (Ctrl+Alt+C) — Insert an annotation balloon.
- **Frame** (►) — Frame Interactively (draw) or Frame… (dialog).
- **Fontwork…** — Decorative text shapes gallery.
- **Hyperlink…** (Ctrl+K) — Hyperlink dialog with 4 type modes: Internet, Mail, Document, New Document.
- **Bookmark…** — Insert/manage bookmarks.
- **Cross-reference…** — Link to headings, bookmarks, figures, or other elements.
- **Special Character…** — Character picker dialog with search, font/block selectors, hex/decimal codes, favorites/recent.
- **Formatting Mark** (►) — No-break Space (Shift+Ctrl+Space), Non-breaking Hyphen, Soft Hyphen, Narrow No-break Space, Zero-width Space, Word Joiner.
- **Horizontal Line** — Insert a horizontal rule.
- **Footnote and Endnote** (►) — Insert Footnote, Endnote, or open the Footnote/Endnote dialog.
- **Table of Contents and Index** (►) — TOC/Index/Bibliography dialog, Index Entry, Bibliography Entry.
- **Page Number…** — Page number insertion dialog.
- **Field** (►) — Page Number, Page Count, Date/Time (fixed or variable), Title, Author, Subject, More Fields… (Ctrl+F2).
- **Header and Footer** (►) — Enable/disable headers and footers per page style.
- **Envelope…** — Envelope configuration dialog.
- **Signature Line…** — Digital-signature placeholder line.

