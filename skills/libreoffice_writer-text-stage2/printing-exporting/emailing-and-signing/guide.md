# Emailing and Digitally Signing Documents (LibreOffice Writer 7.3.7)

## Emailing Documents

LibreOffice makes it easy to send your current document as an email attachment in several formats. Head to **File > Send > Email Document** (or **File > Send > Email as OpenDocument Text**) and your default email client opens with the file already attached. From there, just fill in the recipient, subject, and message body, then send.

If you'd rather send it in a different format, choose *Email as Microsoft Word* to convert to .docx first, or *Email as PDF* to export a PDF before attaching. With the PDF option, Writer pops open the PDF Options dialog so you can tweak settings before the file is handed off to your mail client.

Need to send to a bunch of people at once? You can use your email program's built-in features, or tap into Writer's mail merge facilities — the Mail Merge Wizard or manual merge without the wizard. Chapter 14 of the Writer Guide covers mail merge in detail.

## Digital Signing of Documents

Digital signatures let you prove a document is authentic and hasn't been tampered with. To sign, you need a personal key (certificate) — a private key you keep secret, paired with a public key that gets embedded in the document. You can obtain a certificate from a certificate authority, whether private or governmental.

When you sign a document, a checksum is computed from the content plus your personal key. Anyone who later opens the file in LibreOffice can verify the checksum against the stored one; if they match, the document is unchanged. LibreOffice can also check the public key against the certificate authority's website, so forgery is caught. A signed document shows an icon in the Status bar — double-click it to view the certificate. You can add multiple signatures, but changing the document after signing invalidates existing signatures.

## Applying a Digital Signature

To sign your document, go to **File > Digital Signatures > Digital Signatures**. If the document has unsaved changes, Writer will prompt you to save first — click **Yes** twice (once to confirm, once to actually save). The Digital Signatures dialog lists any existing signatures; click **Sign Document** to add yours.

The Digital Signatures dialog displays a table with columns for "Signed by," "Digital ID issued by," "Date," "Description," and "Signature type," listing anyone who has already signed the document content. Below the table is a checkbox labeled "Use AdES-compliant signature when there is a choice." Along the bottom are buttons for **View Certificate…**, **Sign Document…**, **Remove**, and **Start Certificate Manager…**, with **Help** and **Close** buttons in the corners.

In the Select Certificate dialog that appears, pick your certificate, optionally add a description, and click **Sign**. The certificate shows up in the list with a status icon next to its name. Click **Close** to finish applying the signature.

The Select Certificate dialog is titled "Select the certificate you want to use for signing" and presents a table with columns for "Issued to," "Issued by," "Type," "Expiration date," and "Certificate usage," where your available certificates are listed. Below the table is a **View Certificate…** button and a **Description** text field where you can enter an optional description for the signature. The dialog finishes with **Help**, **Sign**, and **Cancel** buttons at the bottom.

## Including a Signature Line

You can also insert a visible signature placeholder into your document via **Insert > Signature Line**. This creates a graphic box where you fill in the suggested signer's name, title, and email. Options like allowing comments and showing the sign date are available. Once placed, the signature line can be signed with an actual digital certificate.

The Signature Line dialog has a "Suggested Signer" section at the top with three text fields: Name (e.g., "John Doe"), Title (e.g., "Director"), and Email (e.g., "john.doe@example.org"). Below that is a "More" section containing two checkboxes — "Signer can add comments" and "Show sign date in signature line" — both checked by default, followed by a large "Instructions to the signer" text area. The dialog closes with **Help**, **OK**, and **Cancel** buttons.

---

## UI Reference  —  File Menu

_Scope: Send submenu (email as ODF/Word/PDF), Digital Signatures_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown expanded from the menu bar, listing entries from top to bottom: New, Open…, Open Remote…, Recent Documents, Close, Wizards, Templates, Reload (greyed out), Versions…, Save, Save As…, Save Remote…, Save a Copy…, Save All (greyed out), Export…, Export As, Send, Preview in Web Browser, Print Preview, Print…, Printer Settings…, Properties…, Digital Signatures, and Exit LibreOffice. Keyboard shortcuts such as Shift+Ctrl+S for Save As are shown to the right of applicable entries.

## Elements

- **New** (►) — Create a new document of any type (Text, Spreadsheet, Presentation, Drawing, etc.). Ctrl+N for Text Document.
- **Open…** (Ctrl+O) — Open an existing file.
- **Open Remote…** — Open a file from a remote server.
- **Recent Documents** (►) — List of recently opened files.
- **Close** — Close the current document.
- **Wizards** (►) — Step-by-step creation wizards: Letter, Fax, Agenda, Document Converter, Address Data Source.
- **Templates** (►) — Edit Template, Save as Template, Manage Templates (Shift+Ctrl+N).
- **Reload** — Reload document from disk (greyed on unsaved documents).
- **Versions…** — Manage saved versions of the document.
- **Save** (Ctrl+S) — Save in current format.
- **Save As…** (Shift+Ctrl+S) — Save with a new name or format.
- **Save Remote…** — Save to a remote server.
- **Save a Copy…** — Save a copy without changing the working file.
- **Save All** — Save all open documents.
- **Export…** — Export in a non-native format.
- **Export As** (►) — Export as PDF (dialog or direct), Export as EPUB (dialog or direct).
- **Send** (►) — Email document in various formats (ODF, Word, PDF), send via Bluetooth, create Master/HTML document.
- **Preview in Web Browser** — Open document preview in default browser.
- **Print Preview** (Shift+Ctrl+O) — Toggle print-preview layout.
- **Print…** (Ctrl+P) — Open the Print dialog.
- **Printer Settings…** — Configure printer options.
- **Properties…** — Open the 6-tab document properties dialog (General, Description, Custom Properties, Security, Font, Statistics).
- **Digital Signatures** (►) — Digital Signatures…, Sign Existing PDF…
- **Exit LibreOffice** (Ctrl+Q) — Quit the entire suite.

---

## UI Reference  —  Insert Menu

_Scope: Signature Line…_

The Insert menu provides commands for adding content elements — breaks, images, tables, shapes, fields, footnotes, hyperlinks, and more — into the document.

The Insert menu is shown expanded from the menu bar, listing entries from top to bottom: Page Break, More Breaks, Image…, Chart…, Media, OLE Object, Shape, Section…, Text from File…, Text Box, Comment, Frame, Fontwork…, Caption… (greyed out), Hyperlink…, Bookmark…, Cross-reference…, Special Character…, Formatting Mark, Horizontal Line, Footnote and Endnote, Table of Contents and Index, Page Number…, Field, Header and Footer, Envelope…, and Signature Line… at the very bottom.

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
