# Using the Mail Merge Wizard (LibreOffice Writer 7.3.7)

The Mail Merge Wizard walks you through creating personalized form letters without manually placing every field yourself. To get started, open a new document via **File > New > Text Document**, then launch the wizard from **Tools > Mail Merge Wizard**.

The first thing the wizard asks is which starting document to use. You can work from your current document, create a new one, open an existing file, or pick a template. For a fresh letter, just keep **Use the current document** selected and hit **Next**. If the document doesn't have a registered data source yet, a warning appears — click **Exchange Database** to browse for and register your spreadsheet or database file.

The Mail Merge Wizard dialog shows a "Select Starting Document for the Mail Merge" step. On the left side, a Steps panel lists all five stages: Select Starting Document (currently highlighted), Select Document Type, Insert Address Block, Create Salutation, and Adjust Layout. The main area on the right presents radio buttons for "Use the current document" (selected by default) with an "Exchange Database…" button beneath it, "Create a new document", "Start from existing document" and "Start from a template" each with their own "Browse…" buttons, and "Start from a recently saved starting document" with a dropdown selector.

Next, you choose the document type. Since we're making a form letter, select **Letter** and move on.

The address block step is where most of the work happens. You'll point the wizard at your address list (a spreadsheet or database), choose an address block format, and — critically — make sure the field names match up. If your spreadsheet uses "Last Name" but the wizard expects "<Surname>", click **Match Fields** to manually map each element. The dialog shows a preview so you can flip through records and verify everything looks right before continuing. Check the **Suppress lines with just empty fields** option to keep your addresses tidy.

The Match Fields dialog is titled "Match Fields" and instructs you to "Assign the fields from your data source to match the address elements." It contains a three-column scrollable table: the left column lists address elements such as \<Title\>, \<First Name\>, \<Last Name\>, \<Company Name\>, \<Address Line 1\>, and \<Address Line 2\>; the middle column ("Matches to field") has dropdown selectors showing the mapped data-source field names (e.g., "FirstName", "LastName", "Street", "No"), with "\< none \>" for unmatched elements like Title and Company Name; the right column ("Preview") displays sample data from the current record (e.g., "Bert", "Lederstrumpf", "Neuenkirchener Str.", "72"). Below the table, an "Address block preview" area shows the fully assembled address: "Mr. / Bert Lederstrumpf / Neuenkirchener Str. 72 / 45793 Pusemuckel". OK, Cancel, and Help buttons appear at the bottom.

The salutation step lets you set up greetings like "Dear Mr. Lederstumpf" automatically. Select **This document should contain a salutation**, then choose **Insert personalized salutation** if you want gender-specific greetings. You'll pick a field (like "Gender\_ID") and a value (like "f") to distinguish between male and female salutations. If you don't have gender data or prefer something neutral, just leave the **Field name** and **Field value** boxes empty and type a general salutation in the list box instead.

Finally, the **Adjust Layout** step lets you fine-tune where the address block and salutation sit on the page. You can nudge the address block's position using the "From top" and "From left" controls, and move the salutation up or down. The preview pane on the right updates in real time so you can see exactly how the letter will look.

The Mail Merge Wizard is shown at step 5, "Adjust layout," which is highlighted in the left-hand Steps panel. The main area is headed "Adjust Layout of Address Block and Salutation" and is split into controls on the left and a live preview on the right. The Address Block Position controls include a "From top" spinner set to 5.49 cm and a "From left" spinner set to 2.50 cm, each with minus and plus buttons, and an "Align to text body" checkbox (checked). Below that, a Salutation Position section offers "Move Up" and "Move Down" buttons. The preview pane on the right displays a miniature page with an address block containing merge field placeholders (e.g., \<First Name\> \<Last Name\>) near the top and a salutation line ("Dear Mr. \<Last Name\>") positioned below it. At the bottom of the dialog are Help, \< Back, Next \>, Finish, and Cancel buttons, along with a Zoom dropdown set to "Entire page".

Once you click **Finish**, you're back in a normal Writer document with merge fields embedded in it. Type out the body of your letter, then go to **File > Print**. Writer will ask if you want to print a form letter — click **Yes**. The Mail Merge dialog appears, where you can select which records to include and choose to send output to the **Printer** directly or save to **File** for review. Saving to file lets you output everything as a single document or as individual files, which is handy if you want to proofread before printing.

---

## UI Reference  —  Tools Menu

_Scope: Mail Merge Wizard…_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools dropdown menu is open in the LibreOffice Writer menu bar, appearing between "Form" and "Window." It displays a vertical list of menu items grouped by function: at the top are Spelling…, Automatic Spell Checking (with a checked checkbox), Thesaurus… (greyed out), Language (with a submenu arrow), Word Count…, Accessibility Check…, and Automatic Accessibility Checking (unchecked). Below a separator are AutoCorrect (with a submenu arrow), AutoText…, and ImageMap (greyed out). The next group contains Redact, Auto-Redact, Heading Numbering…, Line Numbering…, and Footnote/Endnote Settings…. Further down are Mail Merge Wizard…, Bibliography Database, and Address Book Source…. Another group lists Update (with a submenu arrow) and Protect Document (with a submenu arrow), followed by Calculate (greyed out) and Sort… (greyed out). Near the bottom are Macros (with a submenu arrow) and Development Tools (unchecked checkbox). The final group contains XML Filter Settings…, Extensions…, Customize…, and Options….

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
