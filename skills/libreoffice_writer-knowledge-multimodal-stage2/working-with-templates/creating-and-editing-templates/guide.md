# Creating and Editing Templates (LibreOffice Writer 7.3.7)

Templates are your starting points — pre-built documents with formatting, styles, and even boilerplate text baked in. You can create them from scratch, pull them from online sources, or tweak existing ones to fit your needs.

**Creating a template from a document** is the most common approach. Open any Writer document (new or existing), set up the formatting, styles, and any content you want to reuse — think company logos, standard headings, or a pre-filled salutation. When it looks right, go to **File > Templates > Save as Template**. Give it a name, pick a category like *My Templates* or *Business Correspondence*, optionally check **Set as default template**, and hit **Save**.

See `fig01.png`.

You can also create templates through **wizards** for common document types. Head to **File > Wizards** and pick from options like **Letter**, **Fax**, or **Agenda**. Walk through the wizard pages, and on the last step you'll specify a template name and save location. Click the Path icon (three dots) if you want to change the default folder, then click **Finish** to save.

**Importing templates from other sources** is straightforward. The official repository lives at *extensions.libreoffice.org* — you can get there by clicking **Get more extensions online...** in the Extension Manager (**Tools > Extension Manager**). On the Extensions page, click the **Templates** tag filter, optionally narrow by **Writer**, and hit **Search**. Download what you need, then import it.

To import via the Templates dialog, click **Manage** on the upper right, choose **Import**, select your target category, and click **OK**. A file browser opens — find your downloaded template and click **Open**. Alternatively, you can import through **Tools > Extension Manager** by clicking **Add**, selecting the template package, and clicking **Open**. Restart LibreOffice after installing extension-packaged templates.

See `fig02.png`.

**Editing an existing template** starts from the Templates dialog (**File > Templates > Manage Templates**). Find the template you want, right-click it, and choose **Edit** from the context menu. The template opens like a regular document — make your changes, then save normally. Keep in mind that editing a template doesn't retroactively update documents already created from it; the connection between a document and its template is fixed at creation time.

You can also find where templates are physically stored on disk via **Tools > Options > LibreOffice > Paths**, which is handy if you want to manually copy template files into the right folders or share them with colleagues.

---

## UI Reference  —  File Menu

_Scope: Templates submenu: Edit Template, Save as Template_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

Read the screenshot `ui-file-menu.png` in this directory.

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

