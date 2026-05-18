# Exporting to EPUB and Other Formats (LibreOffice Writer 7.3.7)

EPUB has become the go-to format for e-readers, tablets, and smartphones. It's essentially an archive of HTML files bundled with images and supporting files. Writer handles EPUB export reasonably well for text-heavy documents, though content like illustrations, tables, and cross-references may not come through perfectly.

**Quick export** is the fastest route: go to **File > Export As > Export Directly as EPUB**. This uses whatever EPUB settings you last configured, prompts you for a filename and location, and you're done — no dialog, no fuss.

If you want more control, use **File > Export As > Export as EPUB** instead. This opens the EPUB Export dialog where you can fine-tune the output.

The EPUB Export dialog is divided into three sections stacked vertically. At the top, the **General** section contains three dropdown fields: Version (set to "EPUB 3.0" and highlighted in blue), Split method (set to "Heading"), and Layout method (set to "Reflowable"). Below that, the **Customize** section provides text fields with accompanying **Browse…** buttons for Cover image and Media directory. The bottom **Metadata** section has five text fields — Identifier, Title (pre-filled with the document title "Chapter 10 Printing, Exporting, E-mailing, Sig…"), Author, Language, and Date (showing a placeholder timestamp "0000-00-00T00:00:00"). The dialog has **Help**, **OK**, and **Cancel** buttons along the bottom edge.

Under **General**, pick your EPUB **Version** (2.0 or 3.0 — most modern e-readers handle 3.0 fine). The **Split method** determines how chapters are divided: *Heading* splits on heading styles, while *Page break* splits at each page break. For **Layout method**, choose *Reflowable* to let the ebook adapt to the reader's screen size, or *Fixed* to preserve exact page layout.

The **Customize** section lets you set a **Cover image** path and a **Media directory** for bundled multimedia. If you leave the cover image blank, Writer will automatically use any image named `cover.gif`, `cover.jpg`, `cover.png`, or `cover.svg` it finds. The media directory defaults to a folder with the same name as your document in the current directory.

**Metadata** fields — Identifier, Title, Author, Language, Date — give your EPUB the tags e-readers and libraries use for searching and sorting. These pull from **File > Properties** by default, so setting your document properties ahead of time saves a step here.

For broader format needs beyond EPUB, Writer can also export to XHTML, PDF, and several image formats. Just go to **File > Export**, pick your format from the **File format** dropdown (you'll see options like PNG, XHTML, EPUB, JPEG, and more), give it a name, and click **Export**.

The Export dialog shows a **File name** field at the top (containing "WG6007-PrintExportEmail_bb_gp") with an **Export…** button to its right, and a **File format** dropdown below it currently displaying "PNG - Portable Network Graphic (.png)". The dropdown list is expanded, revealing the available export formats: XHTML (.html;.xhtml), PDF - Portable Document Format (.pdf), EPUB Document (.epub), JPEG - Joint Photographic Experts Group (.jpg;.jpeg;.jfif;.jif;.jpe), Writer Layout XML (.xml), and PNG - Portable Network Graphic (.png). Checkboxes for **Automatic file name extension** and **Selection** are visible on the left, with **Cancel** and **Help** buttons on the right.

If you can't find the format you need under **File > Save As** or **File > Export**, consider Calibre — a free, open-source e-book manager available on Windows, macOS, and Linux at [https://calibre-ebook.com](https://calibre-ebook.com). It handles a wide range of conversions from `.odt` files and gives you more control over the final result.

---

## UI Reference  —  File Menu

_Scope: Export…, Export As > EPUB entries_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown expanded from the menu bar (which also displays Edit, View, Insert, and Format). It lists items top to bottom: New, Open…, Open Remote…, Recent Documents, Close, then a separator, followed by Wizards, Templates, Reload (greyed out), and Versions…. After another separator come the save options: Save, Save As…, Save Remote…, Save a Copy…, and Save All (greyed out). The next group contains Export…, Export As, Send, and Preview in Web Browser. Below a final separator are Print Preview, Print…, Printer Settings…, Properties…, Digital Signatures, and Exit LibreOffice.

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
