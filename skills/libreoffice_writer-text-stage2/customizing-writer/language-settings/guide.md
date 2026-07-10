# Language Settings (LibreOffice Writer 7.3.7)

Getting your language settings right affects spell checking, hyphenation, currency, date formats, and more. There are three things you'll typically want to configure: dictionaries, locale and language options, and spelling/grammar behavior.

LibreOffice ships with several language modules out of the box, each of which can include a spelling dictionary, a hyphenation dictionary, and a thesaurus. If you need additional languages, head to **Tools > More Dictionaries Online** on the Menu bar — this opens your browser with links to downloadable dictionary packs. Just follow the prompts to install what you need.

To adjust your locale and document language, open the Options dialog (click the expansion symbol by **Language Settings**) and choose **Languages**. On the right-hand side you'll find settings for your user interface language, the locale (which controls number formatting, currency, and date patterns), and the default language for documents. If you're working in a mixed-language environment — say, an English interface but German locale for numbering and currency — you can set these independently. To apply a language change only to the file you currently have open, tick **For the current document only**.

The Languages page of the Options dialog is divided into several sections. At the top, the **Language Of** section contains a **User interface** dropdown (set here to "Default - English (USA)"). Below that, the **Formats** section has dropdowns for **Locale setting** (e.g., "Default - English (Australia)"), **Default currency** (e.g., "Default - AUD"), a **Decimal separator key** checkbox labeled "Same as locale setting ( . )", and a **Date acceptance patterns** field (e.g., "D/M/Y;D/M"). Further down, the **Default Languages for Documents** section provides a **Western** language dropdown (e.g., "English (USA)") along with checkboxes and dropdowns for **Asian** and **Complex text layout** languages (both set to "[None]"), and a **For the current document only** checkbox. At the bottom, an **Enhanced Language Support** section includes an "Ignore system input language" checkbox.

For Asian languages (Chinese, Japanese, Korean) or complex text layout languages (Hindi, Thai, Hebrew, Arabic), enable the corresponding checkboxes under **Enhanced Language Support**. This will add extra pages to the Language Settings section the next time you open the Options dialog.

Spelling and grammar options live under **Language Settings > Writing Aids**. If you want on-the-fly spell checking, make sure **Check spelling as you type** is selected — you can also toggle this from **Tools > Automatic Spell Checking** on the Menu bar. For grammar checking as you type, enable **Check grammar as you type** as well. If you work with technical documents full of uppercase words or part numbers, consider ticking **Check uppercase words** and **Check words with numbers** so the checker doesn't skip them. **Check special regions** extends checking into headers, footers, frames, and tables.

The Writing Aids page of the Options dialog is divided into three sections. The top section, **Available Language Modules**, lists installed modules with checkboxes — here showing Hunspell SpellChecker (selected), Lightproof grammar checker (English), Libhyphen Hyphenator, and MyThes Thesaurus, all enabled, with an **Edit…** button to the right. The middle section, **User-defined Dictionaries**, lists custom dictionaries such as "standard [All]" (highlighted), "en-GB [English (UK)]", "en-US [English (USA)]", "technical [All]", and "List of Ignored Words [All]", each with a checkbox, and **New…**, **Edit…**, and **Delete** buttons on the right. The bottom section, **Options**, contains checkboxes for "Check spelling as you type" (unchecked), "Check grammar as you type" (checked), "Check uppercase words" (checked), "Check words with numbers" (unchecked), and "Check special regions" (checked), with a "Get more dictionaries online…" link at the very bottom.

The Writing Aids page also shows your available language modules (like Hunspell SpellChecker, Lightproof grammar checker, and MyThes Thesaurus) and any user-defined dictionaries. You can create new custom dictionaries here, edit existing ones, or delete ones you no longer need — though system-installed dictionaries can't be removed. A handy tip: words you add via "Add to Dictionary" during a spell check go into the standard dictionary, while words you mark "Ignore All" land in the List of Ignored Words dictionary.

For sentence-level grammar checking, LibreOffice uses checkers that are enabled by default for your system language. To fine-tune what gets flagged, go to **Language Settings > English Sentence Checking**, select **English spelling dictionaries**, and click **Options** to review the available rules. After changing grammar settings, restart LibreOffice or reload the document for them to take effect.

---

## UI Reference  —  Tools Menu

_Scope: Options… > Language Settings subtree_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools dropdown menu is shown open in the Writer menu bar. It lists the following items from top to bottom: Spelling…, Automatic Spell Checking (shown with a checked checkbox), Thesaurus… (grayed out), Language (with a submenu arrow), Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked checkbox), AutoCorrect (with a submenu arrow), AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update (with a submenu arrow), Protect Document (with a submenu arrow), Calculate (grayed out), Sort… (grayed out), Macros (with a submenu arrow), Development Tools (unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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
