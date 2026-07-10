# Saving and Protecting Documents (LibreOffice Writer 7.3.7)

You can save a document in Writer using several commands, and the differences matter. **File > Save** keeps the current filename and location. **File > Save As** (or Ctrl+Shift+S) lets you pick a new name, location, or file format. If you need to stash a copy while keeping the original open, use **File > Save a Copy** — the copy is saved but never opened. And **File > Save All** saves every open document in one go. For remote files, **File > Save Remote** stores the document on a remote server directly.

Writer can automatically save recovery copies at regular intervals. Head to **Tools > Options > Load/Save > General**, tick **Save AutoRecovery information every**, and set your preferred interval (the default is 10 minutes). While you're there, consider enabling **Always create backup copy** for an extra safety net.

If you need to share files with Microsoft Office users, go to **File > Save As** and pick a `.docx` format from the **File type** drop-down. Note that any changes you make from that point on will only appear in the Word version — you'd need to reopen the `.odt` original to keep working in ODF. To default to Word format permanently, go to **Tools > Options > Load/Save > General**, find **Default File Format and ODF Settings**, set **Document type** to *Text document*, and choose your preferred Word format under **Always save as**.

Writer offers two kinds of document protection: password-based and OpenPGP encryption. To password-protect a file, use **File > Save As** and tick the **Save with password** checkbox in the lower-left corner, then click **Save**.

The lower portion of the Save As dialog shows a **File name** field and a **File type** drop-down (set here to "ODF Text Document (.odt)"). Below these are three checkboxes: **Save with password** (unchecked), **Automatic file name extension** (checked, shown with a blue checkmark), and **Encrypt with GPG key** (unchecked). A greyed-out **Edit filter settings** checkbox also appears at the bottom.

A Set Password dialog appears with two sections. Enter a password in the **File Encryption Password** fields to fully lock the file — nobody opens it without the password. For a lighter touch, click **Options**, select **Open file read-only** under *File Sharing Password*, and optionally set a separate editing password so some people can read while others can also edit.

The Set Password dialog is divided into two sections. The upper section, labeled **File Encryption Password**, contains an "Enter password to open" field and a "Confirm password" field, followed by a note warning that the document will only open with the password and that the password is case-sensitive. Below this is a collapsible **Options** expander, which reveals the **File Sharing Password** section containing an "Open file read-only" checkbox, an "Enter password to allow editing" field, and a "Confirm password" field. **OK** and **Cancel** buttons appear at the bottom right of the dialog.

Be warned: LibreOffice uses strong encryption, so if you lose the password, the document is effectively gone. To change or remove a password later, open the document and go to **File > Properties > General**, then click **Change Password**.

For OpenPGP encryption, you'll need GPG software and a personal key pair already set up on your system. In the **Save As** dialog, select **Encrypt with GPG key** instead of (or alongside) the password option, click **Save**, and choose the recipient's public key from the list that appears. The recipient must have the corresponding private key to decrypt the file.

Writer can also open and save files on remote servers over FTP, WebDAV, Windows Share, SSH, or cloud services like Google Drive and Microsoft OneDrive. For details on setting up remote connections, see the *Getting Started Guide*.

---

## UI Reference  —  File Menu

_Scope: Save, Save As, Save Remote, Save a Copy, Save All, Properties, Digital Signatures_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File menu is shown open as a single-column drop-down from the menu bar (which also displays Edit, View, Insert, and Format). The menu lists items in order from top to bottom: New, Open…, Open Remote…, Recent Documents, Close, then a separator, followed by Wizards, Templates, Reload (greyed out), and Versions…. After another separator come Save, Save As…, Save Remote…, Save a Copy…, and Save All (greyed out). The next group contains Export…, Export As, Send, and Preview in Web Browser. A final group shows Print Preview, Print…, Printer Settings…, Properties…, Digital Signatures, and Exit LibreOffice. Some entries display keyboard shortcuts to their right (e.g., Shift+ for Save As, Shift+ for Print Preview).

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
