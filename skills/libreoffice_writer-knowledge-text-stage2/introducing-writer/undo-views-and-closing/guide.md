# Undoing Changes, Multiple Views, and Closing (LibreOffice Writer 7.3.7)

Made a mistake? Just press **Ctrl+Z**, or go to **Edit > Undo**, or click the **Undo** icon on the Standard toolbar. If you want to undo several actions at once, click the small triangle next to the **Undo** icon — you'll get a dropdown list of recent changes and can select multiple sequential ones to revert in one go.

The Standard toolbar shows the Undo button (a curved yellow arrow, circled for emphasis) with a small dropdown triangle beside it. Clicking that triangle reveals a dropdown list headed "Actions to undo: 6," with individually listed actions such as "Apply Styles: Caption," "Change style: Frame1," "Insert caption: 'Sidebar propertie'," "Paste clipboard," "Insert page break," and "Delete comment," with additional entries below. The first six items are highlighted in blue, indicating they are selected for undoing as a batch.

Once you've undone something, **Redo** becomes active. Hit **Ctrl+Y**, choose **Edit > Redo**, or click the **Redo** icon. Just like Undo, you can click the dropdown arrow next to it to redo several changes at once.

## Displaying multiple views

You can open several views of the same document simultaneously — handy when you need to copy content between pages or compare sections at different zoom levels. Go to **Window > New Window** and a new window opens with the same document. Each window gets an automatically numbered title bar (e.g., `:1`, `:2`). Any edit you make in one window is immediately reflected in all others.

Switch between open windows by clicking on them directly, or pick one from the **Window** menu list — the active window has a checkmark. To close an extra view, use **Window > Close Window**, press **Ctrl+W**, or click the **Close** icon on the Menu bar or Title bar.

## Reloading a document

If you've made a mess of things since your last save, you can throw away all changes at once. Go to **File > Reload** and confirm with **Yes** in the dialog that appears. The document reverts to whatever was last saved — quick and painless.

## Classifying document contents

For sensitive documents, Writer supports the TSCP standard for document classification. Open the classification toolbar via **View > Toolbars > TSCP Classification**. It offers list boxes for selecting security levels across BAF categories (Intellectual Property, National Security, Export Control) and BAILS levels (Non-Business, General Business, Confidential, Internal Only). Classifications are stored as metadata under **File > Properties**, Custom Properties tab. Note that content with a higher classification level cannot be pasted into a document with a lower one.

## Closing a document

When you're done, go to **File > Close** or click the **X** on the Title bar. On Windows and Linux, closing the last document also quits LibreOffice entirely; on macOS, use **LibreOffice > Quit LibreOffice** instead. If multiple documents are open and you only want to close one, **File > Close** (or the **X** on that window) does the trick. If there are unsaved changes, Writer will prompt you to save or discard them before closing.

---

## UI Reference  —  File Menu

_Scope: Close, Exit LibreOffice (Ctrl+Q)_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown expanded from the Menu bar, listing all entries in a single vertical column. From top to bottom the items are: New, Open…, Open Remote…, Recent Documents, Close, then a separator, followed by Wizards, Templates, Reload (greyed out), and Versions…. After another separator come Save, Save As…, Save Remote…, Save a Copy…, and Save All (greyed out). The next group contains Export…, Export As, Send, and Preview in Web Browser. A final group lists Print Preview (with a checkbox icon and a Shift shortcut hint), Print…, Printer Settings…, Properties…, Digital Signatures, and finally Exit LibreOffice at the very bottom.

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
