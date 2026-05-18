# Loading and Saving Options (LibreOffice Writer 7.3.7)

Head over to **Tools > Options** and expand **Load/Save** on the left to find all the settings that control how Writer opens and saves your documents. The General page is the one you'll use most.

Under the **Load** section, you'll see **Load user-specific settings with the document**. When this is on, Writer applies the original author's settings (like printer config) when you open their file. If you're working in an office where documents bounce between people and printers, you might want to turn this off so your own system settings take priority. Note that some things — like data source links, spacing options for paragraphs before text tables, and field function update settings — always load with the document regardless.

There's also **Load printer settings with the document**. Leaving it enabled means a document could try to print to a network printer you don't have access to, so disable it if that's a concern.

See `fig01.png`.

The **Save** section is where you set up your safety net. **Save AutoRecovery information every __ minutes** tells Writer how often to stash recovery data. Keep this on — if Writer crashes, you'll be glad it saved a snapshot ten minutes ago instead of never. You can adjust the interval to taste.

**Edit document properties before saving** pops up the document's Properties dialog the first time you save (or use Save As), handy if you like to fill in metadata early. **Always create backup copy** saves the previous version of your file with a `.bak` extension in a separate folder. You can find (or change) that folder under **Tools > Options > LibreOffice > Paths**.

Under **Default File Format and ODF Settings**, pick the ODF format version and set what **Always save as** defaults to — for instance, ODF Text Document (`.odt`). If you regularly exchange files with Microsoft Office users, you could set this to a Word format instead, though you'll get a warning when saving in non-ODF formats. The **Warn when not saving in ODF or default format** checkbox controls that nudge.

If you work on long documents or anything you can't afford to lose, seriously consider enabling both AutoRecovery and backup copies. They work independently: AutoRecovery protects against crashes, while backup copies protect against accidental overwrites. Belt and suspenders.

---

## UI Reference  —  Tools Menu

_Scope: Options… > Load/Save subtree_

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

