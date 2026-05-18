# Data Sources for Mail Merge (LibreOffice Writer 7.3.7)

Mail merge in Writer lets you produce multiple copies of a document — form letters, mailing labels, envelopes, stickers, you name it — each personalized with variable data like names, addresses, and amounts. The data itself comes from an external source: a spreadsheet, a text file, even a MySQL database. Before you can use any of that in a mail merge, though, you need to register the data source with LibreOffice so Writer knows where to find it.

To kick things off, open **File > Wizards > Address Data Source**. You can also reach this from the LibreOffice Start Center. The wizard walks you through connecting your data in just a few clicks.

On the first page of the wizard, pick the type of external address book you're working with. If you're using a spreadsheet (which is the most common case), select **Other external data source** and hit **Next**.

The Address Book Data Source Wizard dialog is displayed, with a Steps panel on the left listing five steps: 1. Address Book Type (currently highlighted), 2. Connection Settings, 3. Table Selection, 4. Field Assignment, and 5. Data Source Title. The main area on the right shows three radio button options for selecting the type of external address book — Firefox, Thunderbird, and Other external data source (which is selected) — along with Help, Back, Next, Finish, and Cancel buttons at the bottom.

The next page is the Connection Settings step — just click the **Settings** button to open the detailed connection dialog.

In the Create Address Data Source dialog that appears, set the **Database type** to **Spreadsheet** (or whatever matches your source), then click **Next**.

Now you'll need to point LibreOffice at the actual file. Click **Browse**, navigate to the spreadsheet that holds your address data, select it, and click **Open** to get back to the dialog.

The Database properties dialog is shown, with the Steps panel on the left listing two steps: 1. Advanced Properties and 2. Connection settings (currently highlighted). The main area on the right is labeled "General" and contains a "Path to the spreadsheet document" text field displaying a file path, alongside a Browse button for selecting the spreadsheet file.

Before moving on, it's worth clicking the **Test Connection** button to make sure everything is wired up correctly. You should see a confirmation message saying the connection was established successfully. If you get an error instead, double-check the file path and format.

Once the connection checks out, click **Finish**. On the final page you can click **Next** without worrying about the Field Assignment button — that's only needed later if you're using the full Mail Merge Wizard.

That's it. Your data source is now registered and available from within any Writer document. You only need to do this once per data source; after that, it's ready whenever you need it for letters, labels, or envelopes.

---

## UI Reference  —  Tools Menu

_Scope: Address Book Source…, Bibliography Database_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools drop-down menu is open in the Writer menu bar, showing a vertical list of entries grouped by separators. From top to bottom, the items are: Spelling…, Automatic Spell Checking (with a checkbox, currently checked), Thesaurus… (grayed out), Language, Word Count…, Accessibility Check…, Automatic Accessibility Checking (unchecked checkbox), AutoCorrect, AutoText…, ImageMap (grayed out), Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, Mail Merge Wizard…, Bibliography Database, Address Book Source…, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), Macros, Development Tools (unchecked checkbox), XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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
