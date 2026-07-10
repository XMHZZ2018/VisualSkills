# Exporting to PDF (LibreOffice Writer 7.3.7)

LibreOffice Writer can export any document to PDF, which is handy when you need to share a file that looks the same everywhere. There are two ways to go about it: a quick one-click method, or a more detailed approach with full control over the output.

For a fast export, click the **Export Directly as PDF** icon on the Standard toolbar, or go to **File > Export As > Export Directly as PDF**. This uses whatever PDF settings you last configured and just asks for a filename and location — no fuss.

When you need more control, use **File > Export as > Export as PDF**. This opens the PDF Options dialog, which has six tabs: *General*, *Initial View*, *User Interface*, *Links*, *Security*, and *Digital Signatures*.

The PDF Options dialog is shown with the General tab selected. The left side contains a Range section with radio buttons for All, Pages, and Selection, plus a "View PDF after export" checkbox, an Images section with radio buttons for Lossless compression and JPEG compression (set to 90% quality) and a "Reduce image resolution" checkbox (set to 300 DPI), and a Watermark section with a "Sign with watermark" checkbox. The right side has a General section with checkboxes for Hybrid PDF, Archive (PDF/A, ISO 19005) with a PDF/A version dropdown set to PDF/A-3b, Universal Accessibility (PDF/UA), Tagged PDF, and Create PDF form with a Submit format dropdown set to FDF, followed by a Structure section with checkboxes for Export outlines (checked), Export placeholders, Comments as PDF annotations, Export automatically inserted blank pages, and Use reference XObjects. Help, Export, and Cancel buttons appear at the bottom.

On the **General** tab, you pick which pages to export (all, a range, or just the selection), choose between lossless and JPEG image compression, and set the image resolution. You can also opt into PDF/A for archival, tagged PDF for accessibility, or embed a watermark across every page. Under *Structure*, turning on **Export outlines** gives readers a clickable table of contents in their PDF viewer.

The **Initial View** tab controls how the PDF looks when someone first opens it — whether it starts on a specific page, shows bookmarks or thumbnails in a side pane, and what magnification to use.

Over on the **User Interface** tab, you can hide the menu bar, toolbar, or window controls in the viewer, and even force the PDF to open in full-screen mode. These options are especially useful if you're building a kiosk-style or presentation PDF.

The PDF Options dialog is shown with the Links tab selected. It contains a General section with three checkboxes: "Export outlines as named destinations" (unchecked), "Convert document references to PDF targets" (unchecked), and "Export URLs relative to file system" (checked). Below that is a Cross-document Links section with three radio buttons: "Default mode" (selected), "Open with PDF reader application", and "Open with Internet browser".

The **Links** tab determines how hyperlinks behave. You can export Writer outline levels as named destinations, convert references to other document formats (like .odt) into .pdf links, and choose whether cross-document links open in the PDF reader or in a web browser.

For locking things down, the **Security** tab lets you set an *open password* (required to view the PDF) and a *permissions password* (restricts printing, copying, or editing). Once a permissions password is set, you can fine-tune exactly what's allowed — for example, permitting high-resolution printing but blocking content copying.

The PDF Options dialog is shown with the Security tab selected. On the left is a File Encryption and Permission section containing a "Set Passwords..." button, with status text indicating "No open password set / PDF document will not be encrypted" and "Permission password set / PDF document will be restricted". On the right are three groups of permission controls: a Printing section with radio buttons for Not permitted, Low resolution (150 dpi), and High resolution (selected); a Changes section with radio buttons for Not permitted, Inserting/deleting/rotating pages, Filling in form fields, Commenting/filling in form fields, and Any except extracting pages (selected); and a Content section with checkboxes for "Enable copying of content" (checked) and "Enable text access for accessibility tools" (checked).

Finally, the **Digital Signatures** tab lets you attach a certificate to prove the PDF hasn't been tampered with. Click **Select** to pick a certificate from your key store, enter the certificate password if needed, and optionally fill in location and contact info. The key store path is configured under **Tools > Options > LibreOffice > Security > Certificate Path**.

Once everything looks right, click **Export**, choose your filename, and you're done.

---

## UI Reference  —  File Menu

_Scope: Export As > Export as PDF, Export Directly as PDF_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown expanded in the LibreOffice Writer menu bar. It displays a vertical list of menu items in order: New, Open..., Open Remote..., Recent Documents, Close, Wizards, Templates, Reload (greyed out), Versions..., Save, Save As..., Save Remote..., Save a Copy..., Save All (greyed out), Export..., Export As, Send, Preview in Web Browser, Print Preview, Print..., Printer Settings..., Properties..., Digital Signatures, and Exit LibreOffice. Keyboard shortcuts are shown to the right of some items, such as Shift+ for Save As and Shift+ for Print Preview.

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
