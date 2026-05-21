# General LibreOffice Options (LibreOffice Writer 7.3.7)

All the settings covered here live under **Tools > Options** (or **LibreOffice > Preferences** on macOS). Click the marker next to **LibreOffice** on the left-hand side to expand the list, then pick the page you need on the right. If you ever mess something up, hit the **Reset** button at the bottom of any options page to snap everything back to where it was when you opened the dialog.

The **LibreOffice – User Data** page stores your name or initials, which Writer uses for document properties like "created by" and "last edited by," comment authorship, and mail-merge sender addresses. Fill it in accurately, or amend what's already there. If you'd rather keep your info out of the file's metadata, deselect **Use data for document properties**.

Under **LibreOffice – View**, you control how the document window looks and behaves — things like icon size, font rendering, and UI scaling. Adjust these to your personal taste; the *Getting Started Guide* has the full breakdown.

The **LibreOffice – Print** page is where you set your default printer and general printing behavior. The **Warnings** section on the right is worth turning on: it alerts you when the paper size or orientation in your document doesn't match what your printer actually supports, which saves you from clipped or misprinted pages.

See `fig01.png` for the general printing options dialog.

**LibreOffice – Paths** lets you redirect where LibreOffice looks for templates, documents, and other files. Handy if you keep project templates outside the default My Documents folder — you can add as many custom locations as you need.

If you open a document that uses fonts you don't have installed, LibreOffice quietly substitutes its own choices. You can override those on the **LibreOffice – Fonts** page by specifying your preferred replacement fonts. Liberation fonts (Serif, Sans, and Mono) are solid stand-ins for Times, Arial, and Courier.

The **LibreOffice – Security** page handles macro security and document-saving privacy. Under **Security Options and Warnings**, you can have Writer flag or auto-remove hidden information like tracked changes, versions, or notes before sharing a file. Click the **Options** button for finer control — enable **Remove personal information on saving** to strip user data from every save, or leave it off if you only want to scrub specific documents manually. By default, Ctrl+click opens hyperlinks; if you'd rather a plain click do it, deselect **Ctrl-click required to open hyperlinks**.

Finally, the **LibreOffice – Application Colors** page lets you toggle visibility and change colors for page margins, text boundaries, table borders, section boundaries, and other on-screen guides — useful for editing and layout work where you want a quick visual distinction from the defaults.

---

## UI Reference  —  Tools Menu

_Scope: Options… (Alt+F12) opening the comprehensive multi-tree Options dialog_

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

