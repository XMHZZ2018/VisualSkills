# Assigning Shortcut Keys (LibreOffice Writer 7.3.7)

Beyond the built-in keyboard shortcuts, you can define your own. This lets you wire up any standard LibreOffice command — or your own macros — to a key combination, scoped either to Writer alone or to the entire LibreOffice suite.

To get started, open the Customize dialog via **Tools > Customize** and switch to the **Keyboard** tab. The first thing you'll notice at the top right are the **LibreOffice** and **Writer** radio buttons — pick **Writer** if you only want the shortcut available in Writer, or **LibreOffice** to make it suite-wide.

The Customize dialog is open to the Keyboard tab. At the top, a large scrollable list labeled "Shortcut Keys" displays key combinations (such as F1, F2, Shift+F1, Ctrl+F1, etc.) in the left column and any currently assigned functions in the right column. Below this list are two side-by-side panes: "Category" on the left (showing a tree of command groups like Application, View, Insert, Format, Styles, Tools) and "Function" on the right (listing individual commands within the selected category). At the top-right corner, the "LibreOffice" and "Writer" radio buttons control the scope of the shortcut assignment. Along the bottom-right are the "Modify", "Delete", "Load…", "Save…", and "Reset" buttons, and the dialog is closed with "OK", "Cancel", or "Help" buttons at the bottom.

Browse the **Shortcut Keys** list at the top of the dialog and click the combination you want to use. Then, in the **Category** and **Function** lists below, find the command you're after. Once both are selected, hit the **Modify** button in the lower right — the key now appears in the **Keys** column next to your chosen function. Click **OK** to confirm and you're done. Repeat for as many shortcuts as you like.

Note that some keys like *F1* and *F10* appear grayed out — those are reserved by your operating system and can't be reassigned. In general, avoid overriding OS-level shortcuts to prevent unexpected behavior.

If you want to reuse your custom shortcuts later or share them with someone, click the **Save** button on the Customize dialog. You'll be prompted to name a keyboard configuration file (the extension is `.cfg`). Pick a location, save it, and you can reload it anytime with the **Load** button on the same dialog. This is handy if you work across multiple machines or want to keep separate profiles for different workflows.

To wipe a shortcut you no longer need, select it in the **Shortcut Keys** list and click **Delete**. The **Reset** button restores everything back to defaults if you ever need a fresh start.

---

## UI Reference  —  Tools Menu

_Scope: Customize… (opens Keyboard tab)_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools drop-down menu is shown expanded in the LibreOffice Writer menu bar. It lists entries from top to bottom: Spelling…, Automatic Spell Checking, Thesaurus…, a Language submenu, Word Count…, Accessibility Check… and Automatic Accessibility Checking, AutoCorrect submenu, AutoText…, Redact and Auto-Redact, then document structure items like Heading Numbering…, Line Numbering…, and Footnote/Endnote Settings…, followed by Mail Merge Wizard…, Bibliography Database, Address Book Source…, an Update submenu, Protect Document submenu, Calculate, Sort…, a Macros submenu, Development Tools, XML Filter Settings…, Extensions…, Customize…, and finally Options… at the bottom. Keyboard shortcuts are displayed to the right of many entries (e.g., F7 for Spelling, Ctrl+F7 for Thesaurus, Alt+F12 for Options).

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
