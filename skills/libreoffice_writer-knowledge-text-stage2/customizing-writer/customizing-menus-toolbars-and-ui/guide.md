# Customizing Menus, Toolbars, and UI (LibreOffice Writer 7.3.7)

Writer gives you a lot of freedom to reshape the interface to match the way you actually work. Menus, toolbars, even the overall UI layout — it's all fair game.

To get started with any customization, head to **Tools > Customize**. This opens the Customize dialog, which has tabs for **Menus**, **Toolbars**, **Notebookbar**, **Context Menus**, **Keyboard**, and **Events**. The **Scope** drop-down in the upper right lets you decide whether your changes apply to all of Writer or just the current document.

The Customize dialog is shown with the **Menus** tab active. The left side contains a **Search** field and a **Category** drop-down (set to "All commands") above a scrollable **Available Commands** list showing entries like 100%, 150%, 3D Color, About LibreOffice, and others. The right side has **Scope** set to "LibreOffice Writer" and **Target** set to "File," with the **Assigned Commands** list displaying the current File menu entries — New, Open…, Open Remote…, Recent Documents, Close, a separator, Wizards, Templates, another separator, Reload, Versions…, Save, Save As…, Save Remote…, and Save a Copy…. Between the two lists are right-arrow and left-arrow buttons for adding or removing commands, and to the far right are up/down arrow buttons for reordering. At the bottom left, a **Description** area shows the label, command name, and tooltip for the selected item, while the bottom right offers **Insert**, **Modify**, and **Defaults** buttons. The dialog footer contains **Help**, **Reset**, **OK**, and **Cancel** buttons.

**Tweaking an existing menu** is straightforward. On the **Menus** tab, pick the menu you want from the **Target** drop-down — you'll see its current commands listed under **Assigned Commands**. To add a command, find it in the **Available Commands** list on the left (use the **Search** box or filter by **Category**), then click the right arrow to move it over. Reorder items with the up/down arrows, or remove one by selecting it and clicking the left arrow. You can rename entries via **Modify > Rename** and insert separators or submenus from the **Insert** drop-down.

If you need an entirely **new menu**, click the symbol next to **Target** and choose **Add**. Give it a name, position it among the existing menus, and hit **OK**. Then populate it with commands using the same process described above.

**Customizing toolbars** works almost identically. Switch to the **Toolbars** tab, pick the toolbar from **Target**, and add or remove commands the same way. You can show or hide individual commands by toggling the checkbox next to each item in the **Assigned Commands** list. To **create a new toolbar**, click the symbol next to **Target**, select **Add**, name it, and choose whether to save it for Writer globally or just the current document.

The Customize dialog is shown with the **Toolbars** tab selected. The layout mirrors the Menus tab: the left side has the same **Search** field, **Category** drop-down (set to "All commands"), and **Available Commands** list, while the right side shows **Scope** set to "LibreOffice Writer" and **Target** set to "Standard." The key difference is that each entry in the **Assigned Commands** list now has a checkbox indicating whether that button is visible on the toolbar. Visible items such as New, Open, Save, Export Directly as PDF, and Print are checked, while items like Load URL, Templates, Open Remote, Save As, Email, Edit Mode, Read Only Mode, EPUB, and Print Directly are unchecked. The same right/left arrow buttons for adding/removing commands, up/down arrows for reordering, and the **Insert**, **Modify**, and **Defaults** buttons appear at the bottom, along with **Help**, **Reset**, **OK**, and **Cancel** in the dialog footer.

Toolbar buttons typically display icons rather than text. If a command doesn't have a default icon, select it and go to **Modify > Change Icon**. The Change Icon dialog lets you pick from built-in icons or **Import** a custom one (16×16 pixels, no more than 256 colors works best).

For a bigger UI overhaul, Writer offers alternative interface layouts. Go to **View > User Interface** to switch between variants like **Tabbed**, **Tabbed Compact**, and **Groupedbar Compact** — these replace the traditional menu bar and toolbars with a ribbon-style interface organized by context tabs. Once you've selected a variant, fine-tune which tabs appear using the **Notebookbar** tab back in **Tools > Customize**. Hit **Reset** any time you want to return to the defaults.

When you're happy with everything, click **OK** to save your changes and close the Customize dialog.

---

## UI Reference  —  Tools Menu

_Scope: Customize… (opens Menus/Toolbars/Notebookbar tabs)_

The Tools menu provides document proofing, language settings, automation, and application-wide configuration.

The Tools drop-down menu is shown open in the Writer menu bar. It lists entries from top to bottom: Spelling…, Automatic Spell Checking (with a checkbox, currently checked), Thesaurus… (grayed out), Language (with a submenu arrow), Word Count…, Accessibility Check…, Automatic Accessibility Checking (with an unchecked checkbox), a separator, AutoCorrect (with a submenu arrow), AutoText…, ImageMap (grayed out), a separator, Redact, Auto-Redact, Heading Numbering…, Line Numbering…, Footnote/Endnote Settings…, a separator, Mail Merge Wizard…, Bibliography Database, Address Book Source…, a separator, Update, Protect Document, Calculate (grayed out), Sort… (grayed out), a separator, Macros (with a submenu arrow), Development Tools (with an unchecked checkbox), a separator, XML Filter Settings…, Extensions…, Customize…, and Options… at the bottom.

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
