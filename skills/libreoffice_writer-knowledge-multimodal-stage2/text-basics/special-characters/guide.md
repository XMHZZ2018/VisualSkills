# Inserting Special Characters (LibreOffice Writer 7.3.7)

Sometimes you need characters that don't live on your keyboard — things like ©, ¼, ñ, or €. To insert them, place your cursor where the character should go, then either click the **Special Character** icon on the Standard toolbar or go to **Insert > Special Character**. The toolbar icon drops down a quick grid of your favorites and recently used characters — just click one to pop it in. If the one you need isn't there, hit **More Characters** to open the full dialog.

See `fig01.png`.

In the Special Characters dialog, you can browse any font's character set, search by name, and preview a character by single-clicking it (its Unicode value and name appear on the right). Double-click a character to insert it directly, or select it and click **Insert**. Characters you use get saved to the Recent Characters list automatically. If a character doesn't appear in the current font, try switching the **Font** dropdown — different fonts carry different symbol sets.

Beyond individual symbols, Writer gives you a handful of handy formatting marks via **Insert > Formatting Mark**. A **non-breaking space** (Ctrl+Shift+Space) glues two words together so they never split across lines. A **non-breaking hyphen** (Shift+Ctrl+Hyphen) does the same for hyphenated terms like "123-4567". There's also a **soft hyphen** (Ctrl+Hyphen), which is invisible unless the word needs to break at a line ending — useful for helping Writer hyphenate long words gracefully. For a **narrow no-break space** (slightly thinner than a regular space), press Alt+Shift while you type the space.

See `fig02.png`.

For **en and em dashes**, you can let AutoCorrect handle them. Under **Tools > AutoCorrect > AutoCorrect Options**, the Replace dashes option converts typed hyphens on the fly: type a word, a space, a hyphen, another space, and a word to get an en dash; skip the spaces around two hyphens to get an em dash. You can also insert them manually through **Insert > Special Characters** by selecting U+2013 (en dash) or U+2014 (em dash) from the *General punctuation* subset. On macOS, Option+Hyphen gives you an en dash and Shift+Option+Hyphen gives you an em dash. On Windows, hold Alt and type 0150 or 0151 on the numeric keypad.

Other marks in the Formatting Mark submenu — **No-width Optional Break**, **Word Joiner**, **Left-to-right Mark**, and **Right-to-left Mark** — are mainly relevant for complex text layout (CTL) languages, so you can safely ignore them for everyday Western-language documents.

---

## UI Reference  —  Insert Menu

_Scope: Special Character… command and Formatting Mark submenu (non-breaking space/hyphen, soft hyphen)_

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

_Scope: Insert Special Characters split-button_

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

