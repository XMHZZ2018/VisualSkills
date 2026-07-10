# Redaction and Removing Personal Data (LibreOffice Writer 7.3.7)

## Removing Personal Data

Before sharing a document, you'll probably want to strip out personal metadata — things like author names, version history, comments, and hidden information. LibreOffice gives you a couple of ways to handle this.

First, head to **Tools > Options > LibreOffice > Security** and click **Options**. This opens a dialog where you can tell LibreOffice to warn you whenever files contain personal data, and even have it automatically remove that information on save. You can set these warnings to trigger when saving, sending, printing, or creating PDFs.

The "Security Options and Warnings" dialog is divided into two sections. The upper "Security Warnings" section has four checkboxes controlling when LibreOffice warns that a document contains recorded changes, versions, hidden information, or notes: "When saving or sending," "When signing," "When printing," and "When creating PDF files." The lower "Security Options" section has four additional checkboxes: "Remove personal information on saving," "Recommend password protection on saving," "Ctrl-click required to follow links," and "Block any links from documents not among the trusted locations (see Macro Security)." The dialog has Help, OK, and Cancel buttons at the bottom.

To scrub personal data from a specific file, go to **File > Properties**. On the General tab, uncheck **Apply user data** and click **Reset Properties**. This clears out author names from the created and modified fields, deletes modification and printing dates, resets editing time to zero, sets the creation date to now, and bumps the version number back to 1.

If you want to ditch version history, go to **File > Versions**, select the versions from the list, and click **Delete**. Alternatively, just use **Save As** to save a clean copy with a different name — that drops the version history entirely.

## Redaction

Sometimes you need to black out sensitive content while keeping the rest of the document visible — think legal discovery or court filings. LibreOffice has a built-in redaction workflow for exactly this.

Open your document in Writer, then click **Tools > Redact**. The document gets handed off to Draw, where a Redaction toolbar appears. Use the **Rectangle Redaction** or **Freeform Redaction** tools to mark the areas you want hidden — they'll show up as transparent gray shapes so you can still see what you're covering. You can optionally click **Export Directly as PDF** to create a review copy where redacted items appear in transparent gray.

When you're ready to finalize, click the **Redacted Export** tool and choose black or white for the redaction color. The gray shapes become opaque, the document exports as a pixelized PDF, and the redacted text is completely gone — no selecting it, no recovering it.

## Auto-Redaction

For documents where you need to redact the same words or names repeatedly, **Tools > Auto-Redact** is a huge time-saver. It opens the Automatic Redaction dialog, where you can define a list of target terms. Add targets by name, set them to match by content, toggle case sensitivity or whole-word matching, and save your target lists for reuse across documents. Every match in the document gets redacted automatically.

The "Automatic Redaction" dialog features a "Redaction Targets" table with columns for Target Name, Type, Content, Case Sensitive, and Whole Words. To the right of the table are buttons for Load Targets, Save Targets, Add Target, Edit Target, and Delete Target. An "Add Target" sub-dialog is shown overlaying the main dialog, containing a Name field (pre-filled with "Target 1"), a Type dropdown set to "Text," a Content text field, and two checkboxes for "Case Sensitive" and "Whole Words Only," along with Help, OK, and Cancel buttons. The main dialog also has Help, OK, and Cancel buttons at its bottom.

---

## UI Reference  —  File Menu

_Scope: Properties… (document metadata on General tab)_

The File menu manages the full document lifecycle: creating, opening, saving, exporting, printing, and closing documents.

The File dropdown menu is shown expanded from the menu bar. It lists items in order from top to bottom: New, Open…, Open Remote…, Recent Documents, Close, then a separator, followed by Wizards, Templates, Reload (greyed out), Versions…, then a separator, Save, Save As…, Save Remote…, Save a Copy…, Save All (greyed out), then a separator, Export…, Export As, Send, Preview in Web Browser, then a separator, Print Preview, Print…, Printer Settings…, Properties…, Digital Signatures, and finally Exit LibreOffice.

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

## UI Reference  —  Tools Menu

_Scope: Redact, Auto-Redact tools_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools dropdown menu is shown expanded from the menu bar. It lists items from top to bottom: Spelling…, Automatic Spell Checking (with a checkbox, currently checked), Thesaurus… (greyed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (with an unchecked checkbox), then a separator, AutoCorrect, AutoText…, ImageMap (greyed out), then a separator, Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, then a separator, Mail Merge Wizard…, Bibliography Database, Address Book Source…, then a separator, Update, Protect Document, Calculate (greyed out), Sort… (greyed out), then a separator, Macros, Development Tools (with an unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

## Elements

- **Spelling…** (F7) — Open the spelling dialog.
- **Automatic Spell Checking** (Shift+F7) — Toggle live spell-check underlines.
- **Thesaurus…** (Ctrl+F7) — Look up synonyms (requires thesaurus dictionary).
- **Language** (►) — Set language For Selection / For Paragraph / For All Text, Hyphenation…, More Dictionaries Online…
- **Word Count…** — Show detailed word/character counts.
- **Accessibility Check…** (Alt+8) / **Automatic Accessibility Checking** — Audit document for accessibility issues.
- **AutoCorrect** (►) — While Typing (toggle), Apply, Apply and Edit Changes, AutoCorrect Options… (5-tab dialog: Replace, Exceptions, Options, Localized Options, Word Completion).
- **AutoText…** (Ctrl+F3) — Manage reusable text blocks.
- **Redact** / **Auto-Redact** — Document redaction tools.
- **Heading Numbering…** — Configure outline numbering for headings.
- **Line Numbering…** — Enable/configure line numbers (position, interval, separator).
- **Footnote/Endnote Settings…** — Configure footnote/endnote formatting.
- **Mail Merge Wizard…** — Step-by-step mail merge.
- **Bibliography Database** / **Address Book Source…** — Database connections.
- **Update** (►) — Refresh: Update All, Page Formatting, Fields (F9), Indexes and Tables, Links, Charts.
- **Protect Document** (►) — Protect Fields (checkbox), Protect Bookmarks (checkbox).
- **Calculate** (Ctrl++) / **Sort…** — In-document calculation and sorting.
- **Macros** (►) — Run Macro…, Edit Macros…, Organize Macros, Digital Signature…, Organize Dialogs…
- **Development Tools** — Toggle developer panel.
- **XML Filter Settings…** / **Extensions…** (Ctrl+Alt+E) / **Customize…**
- **Options…** (Alt+F12) — Opens the comprehensive Options dialog with tree navigation: LibreOffice (User Data, General, View, Print, Paths, Fonts, Security, etc.), Load/Save, Languages, LibreOffice Writer, and more.
