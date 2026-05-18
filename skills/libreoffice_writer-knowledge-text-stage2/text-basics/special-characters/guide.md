# Inserting Special Characters (LibreOffice Writer 7.3.7)

Sometimes you need characters that don't live on your keyboard — things like ©, ¼, ñ, or €. To insert them, place your cursor where the character should go, then either click the **Special Character** icon on the Standard toolbar or go to **Insert > Special Character**. The toolbar icon drops down a quick grid of your favorites and recently used characters — just click one to pop it in. If the one you need isn't there, hit **More Characters** to open the full dialog.

The Special Characters dialog has a **Search** field at the top left, a **Font** dropdown (set here to "Liberation Sans"), and a **Subset** dropdown (set here to "Latin-1") along the top. Below these controls is a large character grid showing accented Latin letters and symbols; clicking a character selects it and displays a large preview on the right along with its Unicode name (e.g., "LATIN SMALL LETTER O WITH ACUTE"), hexadecimal code (U+F3), and decimal value (243), plus an "Add to Favorites" button. At the bottom, the dialog shows a **Recent Characters** row (with a right-click context menu offering "Remove" and "Clear All") and a **Favorite Characters** row containing common symbols like €, ¥, £, ©, Σ, Ω, ≤, ≥, ∞, π, †, and ‡, with **Help**, **Insert**, and **Cancel** buttons along the bottom edge.

In the Special Characters dialog, you can browse any font's character set, search by name, and preview a character by single-clicking it (its Unicode value and name appear on the right). Double-click a character to insert it directly, or select it and click **Insert**. Characters you use get saved to the Recent Characters list automatically. If a character doesn't appear in the current font, try switching the **Font** dropdown — different fonts carry different symbol sets.

Beyond individual symbols, Writer gives you a handful of handy formatting marks via **Insert > Formatting Mark**. A **non-breaking space** (Ctrl+Shift+Space) glues two words together so they never split across lines. A **non-breaking hyphen** (Shift+Ctrl+Hyphen) does the same for hyphenated terms like "123-4567". There's also a **soft hyphen** (Ctrl+Hyphen), which is invisible unless the word needs to break at a line ending — useful for helping Writer hyphenate long words gracefully. For a **narrow no-break space** (slightly thinner than a regular space), press Alt+Shift while you type the space.

The lower portion of the Insert menu is shown with "Formatting Mark" highlighted, revealing its submenu to the right. The submenu lists eight entries: "Insert non-breaking space" (Ctrl+Shift+Space), "Insert non-breaking hyphen" (Ctrl+Shift+-), "Insert soft Hyphen" (Ctrl+-), "Insert Narrow No-break Space" (Alt+Shift+Space), "No-width Optional Break" (Ctrl+/), "Word Joiner", "Left-to-right Mark", and "Right-to-left Mark". The parent menu also shows surrounding items such as Hyperlink, Bookmark, Cross-reference, Special Character, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number, Field, Header and Footer, Envelope, and Signature Line.

For **en and em dashes**, you can let AutoCorrect handle them. Under **Tools > AutoCorrect > AutoCorrect Options**, the Replace dashes option converts typed hyphens on the fly: type a word, a space, a hyphen, another space, and a word to get an en dash; skip the spaces around two hyphens to get an em dash. You can also insert them manually through **Insert > Special Characters** by selecting U+2013 (en dash) or U+2014 (em dash) from the *General punctuation* subset. On macOS, Option+Hyphen gives you an en dash and Shift+Option+Hyphen gives you an em dash. On Windows, hold Alt and type 0150 or 0151 on the numeric keypad.

Other marks in the Formatting Mark submenu — **No-width Optional Break**, **Word Joiner**, **Left-to-right Mark**, and **Right-to-left Mark** — are mainly relevant for complex text layout (CTL) languages, so you can safely ignore them for everyday Western-language documents.

---

## UI Reference  —  Insert Menu

_Scope: Special Character… dialog, Formatting Mark submenu (non-breaking space/hyphen, soft hyphen)_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown fully expanded as a single vertical dropdown from the menu bar. It lists, from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (grayed out), then a separator, followed by Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line…. Several entries display a right-pointing arrow indicating submenus, and checkbox icons appear next to Hyperlink and Horizontal Line.

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
