# Adding Images to a Document (LibreOffice Writer 7.3.7)

Writer supports photos, drawings, scanned images, clip art, and charts — basically any graphic or image file you can throw at it. The most common raster formats (GIF, JPG, PNG, BMP) all work fine, and vector formats are supported too. Before you insert anything, think about whether the document will be printed in color or grayscale, and whether your images are at an appropriate resolution (72–96 dpi is plenty for screen-only documents).

**Drag and drop** is the quickest way to get an image in. Open a file browser, find your image, and drag it straight into the Writer document — a faint vertical line shows where it will land. This embeds a copy by default; hold **Ctrl+Shift** while dragging to link the file instead.

If you prefer a dialog, click where you want the image, then go to **Insert > Image** on the Menu bar (or click the **Insert Image** icon on the Standard toolbar). The Insert Image dialog lets you browse to the file and select it. Check **Preview** to see a thumbnail before committing, then click **Open**.

See `fig01.png`.

At the bottom of that dialog you'll notice a **Link** checkbox. When checked, Writer stores a reference to the file on disk rather than embedding a copy. This keeps your document small and means any external edits to the image show up automatically next time you open the file. The downside: if you move the document to another machine without the image files, they won't display.

To **copy and paste** an image, just copy it in any application (or another LibreOffice document), switch to your Writer document, click where you want it, and press **Ctrl+V** or use **Paste** from the context menu. Be aware that if the source application closes before you paste, the clipboard contents may be lost.

If you linked images but later decide you want them embedded, go to **Edit > Links to External Files**. The Edit Links dialog lists every linked file — select the ones you want, click **Break Link**, and confirm with **Yes**.

See `fig02.png`.

To go the other direction — converting an embedded image to a linked one — right-click the image, choose **Properties**, switch to the **Image** tab, and click the **Browse** button next to the **Link File name** field. Point it to the file on disk and click **Open**, then **OK**.

For **scanning directly into Writer**, make sure your scanner is connected, then choose **Insert > Media > Select Source** to pick the scanner device. Position your cursor where the image should go and run **Insert > Media > Scan > Request** to open the scanning software and pull the image straight in. You'll generally get better results scanning into a dedicated graphics app first and cleaning the image up before inserting it into Writer.

The **Gallery** sidebar (**View > Gallery** or the Gallery icon on the Sidebar) gives you quick access to reusable clip art, graphics, and sounds bundled with LibreOffice. You can drag objects from the Gallery directly into your document, or copy and link them as needed.

---

## UI Reference  —  Insert Menu

_Scope: Image… command to open file chooser for inserting images_

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

---

## UI Reference  —  Standard Toolbar

_Scope: Insert Image button_

The first toolbar row below the menu bar provides quick access to file operations, clipboard, editing, and insert commands.

Read the screenshot `ui-standard-toolbar.png` in this directory.

## Elements

Row (left → right):

- **New** (Ctrl+N, split-button ▼) — New document; dropdown lists all document types.
- **Open** (Ctrl+O) — Open file dialog.
- **Save** (Ctrl+S, split-button ▼) — Save; dropdown: Save As…, Export…, Save a Copy…, Save as Template…, Save Remote File…
- **Export Directly as PDF** — One-click PDF export.
- **Print** (Ctrl+P) — Print dialog.
- **Toggle Print Preview** (Shift+Ctrl+O)

| *(separator)* |

- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V, split-button ▼)
- **Clone Formatting** — Paint-format brush; double-click for persistent mode.

| *(separator)* |

- **Undo** (Ctrl+Z, split-button ▼) / **Redo** (Ctrl+Y)

| *(separator)* |

- **Find and Replace** (Ctrl+H) — Opens Find & Replace dialog.
- **Check Spelling** (F7)
- **Toggle Formatting Marks** (Ctrl+F10) — Show/hide ¶ marks, spaces, tabs.

| *(separator)* |

- **Insert Table** (Ctrl+F12, split-button ▼) — Dialog or visual grid picker for row×column count.
- **Insert Image** — File picker for images.
- **Insert Chart** — Embed chart OLE object.
- **Insert Text Box** — Draw a text frame on canvas.
- **Insert Page Break** (Ctrl+Return)
- **Insert Field** (split-button ▼) — Page Number, Page Count, Date/Time, Title, Author, Subject, More Fields…
- **Insert Special Characters** (split-button ▼) — Full character picker or favorites quick-pick.

| *(separator)* |

- **Insert Hyperlink** (Ctrl+K) — Hyperlink dialog.
- **Insert Footnote** / **Insert Endnote**
- **Insert Bookmark** — Bookmark dialog.
- **Insert Cross-reference** — Cross-reference dialog.
- **Insert Comment** (Ctrl+Alt+C)
- **Show Track Changes Functions** — Toggle Track Changes toolbar.

| *(separator)* |

- **Insert Line** — Line-drawing mode; double-click for persistent mode.
- **Basic Shapes** (split-button ▼) — 4×6 shape palette.
- **Show Draw Functions** — Toggle Drawing toolbar.

