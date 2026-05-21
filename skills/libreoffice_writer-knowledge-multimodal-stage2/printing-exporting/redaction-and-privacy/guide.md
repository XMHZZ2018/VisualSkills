# Redaction and Removing Personal Data (LibreOffice Writer 7.3.7)

## Removing Personal Data

Before sharing a document, you'll probably want to strip out personal metadata — things like author names, version history, comments, and hidden information. LibreOffice gives you a couple of ways to handle this.

First, head to **Tools > Options > LibreOffice > Security** and click **Options**. This opens a dialog where you can tell LibreOffice to warn you whenever files contain personal data, and even have it automatically remove that information on save. You can set these warnings to trigger when saving, sending, printing, or creating PDFs.

See `fig01.png` for the security options and warnings dialog.

To scrub personal data from a specific file, go to **File > Properties**. On the General tab, uncheck **Apply user data** and click **Reset Properties**. This clears out author names from the created and modified fields, deletes modification and printing dates, resets editing time to zero, sets the creation date to now, and bumps the version number back to 1.

If you want to ditch version history, go to **File > Versions**, select the versions from the list, and click **Delete**. Alternatively, just use **Save As** to save a clean copy with a different name — that drops the version history entirely.

## Redaction

Sometimes you need to black out sensitive content while keeping the rest of the document visible — think legal discovery or court filings. LibreOffice has a built-in redaction workflow for exactly this.

Open your document in Writer, then click **Tools > Redact**. The document gets handed off to Draw, where a Redaction toolbar appears. Use the **Rectangle Redaction** or **Freeform Redaction** tools to mark the areas you want hidden — they'll show up as transparent gray shapes so you can still see what you're covering. You can optionally click **Export Directly as PDF** to create a review copy where redacted items appear in transparent gray.

When you're ready to finalize, click the **Redacted Export** tool and choose black or white for the redaction color. The gray shapes become opaque, the document exports as a pixelized PDF, and the redacted text is completely gone — no selecting it, no recovering it.

## Auto-Redaction

For documents where you need to redact the same words or names repeatedly, **Tools > Auto-Redact** is a huge time-saver. It opens the Automatic Redaction dialog, where you can define a list of target terms. Add targets by name, set them to match by content, toggle case sensitivity or whole-word matching, and save your target lists for reuse across documents. Every match in the document gets redacted automatically.

See `fig02.png` for the Automatic Redaction dialog.

---

## UI Reference  —  Tools Menu

_Scope: Redact and Auto-Redact commands_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

Read the screenshot `ui-tools-menu.png` in this directory.

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

