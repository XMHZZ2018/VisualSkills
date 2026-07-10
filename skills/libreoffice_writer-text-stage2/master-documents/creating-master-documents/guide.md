# Creating Master Documents (LibreOffice Writer 7.3.7)

Master documents are great for managing long, multi-part projects like books or reports. They let you break content into separate subdocument files while keeping everything — page numbering, TOC, indexes — unified. There are three ways to create one: from scratch, by combining existing documents, or by splitting an existing document.

**Starting from scratch** is the most controlled approach. First, plan which parts live in the master document (title page, copyright, TOC, index) and which become subdocuments (your chapters). Create a template with all your page, paragraph, and character styles, then use it consistently for both the master and every subdocument — mismatched templates cause style conflicts.

To create the master document itself, open a new file from your template via **File > New > Templates**, make sure the first page uses your title page style, then go to **File > Send > Create Master Document** and save it. Next, create your subdocuments the same way — each one is just a normal Writer document based on the same template, saved with **File > Save As**.

Open the master document and add your front-matter pages. Use **Insert > More Breaks > Manual Break** to insert page breaks between sections (title page, copyright, TOC), setting the appropriate page style for each. For the TOC, set the page style to **Table of Contents** and insert one via **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**.

The Insert Break dialog presents three radio-button options under a "Type" heading: Line break, Column break, and Page break. When Page break is selected, a "Style" dropdown appears below it — in this example set to "Copyright Page" — along with a "Change page number" checkbox and a spinner field for specifying the starting page number. The dialog has Help, OK, and Cancel buttons at the bottom.

Now bring in the subdocuments. Open the Navigator (click its icon on the Sidebar), make sure it's in Master View by clicking the **Toggle Master View** icon, then select **Text** in the Navigator and click **Insert > File**. A handy trick: insert the *last* subdocument first, then keep inserting earlier ones before it — they'll land in the correct order without manual reordering.

The Navigator window in Master View displays a toolbar across the top with icons for Toggle Master View, Insert, Update, Move Up, Move Down, and other actions. Below the toolbar, the master document's structure is listed as an ordered tree: a "Text" entry at the top, followed by "Table of Contents" (with a nested "Text" child), then five subdocument files — Chapter1.odt, Chapter2.odt, Chapter3.odt, Chapter4.odt, and Chapter7.odt — each shown with a subdocument icon, and finally an "Alphabetical Index" entry with its own nested "Text" child at the bottom.

Once all chapters are inserted, use the **Move Up** and **Move Down** icons to arrange everything. Finally, add your bibliography and index as Text sections at the end of the master document.

**Combining existing documents** works well when you already have separate files — say, a collection of test results or short stories. Open the document you want as the title page, trim it to a single Heading 1, then choose **File > Send > Create Master Document**. This creates the master and a linked subdocument automatically. Open the master, click **Yes** to update links, then use **Insert > File** in the Navigator to add the remaining files. Use **Move Up** / **Move Down** to reorder, and run **Tools > Update > Links** to see all edits reflected.

**Splitting a document** is the quickest method. Open the document you want to divide and choose **File > Send > Create Master Document**. In the dialog, pick a folder and filename, then set the **Separated by** field to the outline level where splits should happen — usually **Outline: Level 1** for chapter headings. Writer automatically generates subdocument files named after the master document with sequential numbers.

Keep in mind that the automatically generated filenames (like `maindocnameX.odt`) won't match your chapter titles, so you may want to rename the subdocuments afterward. If the original document was associated with a template, the master document inherits it, but the subdocuments do not — you'll need to reassociate them manually.

---

## UI Reference  —  File Menu

_Scope: Send > Create Master Document_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown expanded from the menu bar, listing all top-level entries in a single vertical dropdown. From top to bottom the items are: New, Open…, Open Remote…, Recent Documents, Close, Wizards, Templates, Reload (greyed out), Versions…, Save, Save As…, Save Remote…, Save a Copy…, Save All (greyed out), Export…, Export As, Send, Preview in Web Browser, Print Preview, Print…, Printer Settings…, Properties…, Digital Signatures, and Exit LibreOffice. Horizontal separator lines group related commands together, and keyboard shortcuts such as Shift+Ctrl+S for Save As are displayed at the right edge of certain entries.

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
