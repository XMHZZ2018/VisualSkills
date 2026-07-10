# Creating a Form Letter (LibreOffice Writer 7.3.7)

A form letter lets you send the same document to many people, with names, addresses, and other details filled in automatically from a data source. Think of it as a template with placeholders that get swapped out for real data at print time.

Before you start, you'll need a registered data source — a spreadsheet or database containing your recipient info. If you haven't set one up yet, go through the Address Book Data Source Wizard or register your spreadsheet via **Tools > Address Book Source**. On the final page, give it a name, confirm the location, and click **Finish** to register it.

To build the letter, create a new document with **File > New > Text Document** (or open an existing one). Then bring up your data source by going to **View > Data Sources** (or just press *Shift+Ctrl+F4*). You'll see a panel appear above your document showing the registered sources.

See `fig01.png`.

In that panel, find your data source (e.g. *Addresses*), expand the **Tables** folder, and select the sheet containing your records. You'll see the column headings — things like SURNAME, FNAME, ADDRESS, CITY, and so on — along with a preview of the data.

Now type the static parts of your letter — the greeting, body text, closing — everything that stays the same for every recipient. When you reach a spot where personalized data should appear, just click on the appropriate column heading in the data source panel and drag it into your document at the cursor position. Add spaces or punctuation around the fields as needed, and press *Enter* at the end of each line in the address block.

See `fig02.png`.

Once your merge fields are in place, you're ready to print. Go to **File > Print** and click **Yes** when Writer asks if you want to print a form letter. The Mail Merge dialog opens, letting you choose whether to print all records or just a selection — use *Ctrl+click* to pick individual ones, or *Shift+click* to select a range.

In the **Output** section, pick **Printer** to send straight to the printer, or **File** to save the merged letters for proofreading first. If you save to file, you can output everything as a single document or as individual documents with auto-generated filenames based on a database field like SURNAME.

See `fig03.png`.

If your data has fields that might be empty (like a second address line), you can suppress the resulting blank lines. Place your cursor at the end of that paragraph, then go to **Insert > Field > More Fields**, select the **Functions** tab, and choose **Hidden Paragraph**. In the **Condition** box, enter something like `![Addresses.Sheet1.AD2]` — this hides the paragraph whenever that field is empty.

That's it — your form letter is ready to merge and send. Save the document as a template if you plan to reuse the layout for future mailings.

---

## UI Reference  —  Edit, View, Window & Help Menus

_Scope: View > Data Sources (Shift+Ctrl+F4) toggle for mail merge data panel_

These menus provide standard editing operations, display controls, window management, and help access.

## Edit Menu

(see screenshot `ui-edit-menu.png`)

- **Undo** (Ctrl+Z) / **Redo** (Ctrl+Y) / **Repeat** (Shift+Ctrl+Y)
- **Cut** (Ctrl+X) / **Copy** (Ctrl+C) / **Paste** (Ctrl+V) — standard clipboard operations.
- **Paste Special** (►) — Paste Unformatted Text (Shift+Ctrl+Alt+V), Paste Special… (Shift+Ctrl+V), Paste as Nested Table, Paste as Rows Above, Paste as Columns Before.
- **Select All** (Ctrl+A)
- **Selection Mode** (►) — Standard (default) or Block Area (Shift+Alt+F8) for column selection.
- **Find…** (Ctrl+F) — Opens the inline Find toolbar.
- **Find and Replace…** (Ctrl+H) — Opens the Find and Replace dialog (see [Formatting Dialogs](formatting-dialogs.md)).
- **Go to Page…** (Ctrl+G) — Jump to a specific page number.
- **Track Changes** (►) — Record, Show, Manage, Accept/Reject individual or all changes, Compare/Merge documents.
- **Comment** (►) — Reply, Resolve, Delete comments and comment threads.
- **Reference** (►) — Insert Footnote/Endnote, Index Entry, Bibliography Entry.
- **Fields…** / **External Links…** / **OLE Object** (►) — Context-sensitive editing commands.
- **Exchange Database…** — Switch the document's database source.
- **Direct Cursor Mode** — Toggle: click anywhere on the page to place the cursor.
- **Edit Mode** (Shift+Ctrl+M) — Toggle between edit and read-only mode.

## View Menu

(see screenshot `ui-view-menu.png`)

- **Normal** / **Web** — Radio pair for print-layout vs web-layout editing view.
- **User Interface…** — Choose from 7 UI variants (Standard Toolbar, Tabbed, Single Toolbar, Sidebar, etc.).
- **Toolbars** (►) — Toggle ~27 available toolbars on/off. Includes Customize… and Lock Toolbars.
- **Status Bar** — Toggle status bar visibility.
- **Rulers** (►) — Toggle horizontal ruler (Shift+Ctrl+R) and vertical ruler.
- **Scrollbars** (►) — Toggle horizontal and vertical scrollbars.
- **Grid and Helplines** (►) — Display Grid, Snap to Grid, Helplines While Moving.
- **Formatting Marks** (Ctrl+F10) — Show/hide paragraph marks, spaces, tabs.
- **Text/Table/Section Boundaries**, **Images and Charts**, **Whitespace** — Visibility toggles (all on by default).
- **Show Tracked Changes** — Toggle track-change markup display.
- **Field Shadings** (Ctrl+F8) / **Field Names** (Ctrl+F9) / **Field Hidden Paragraphs** — Field display options.
- **Sidebar** (Ctrl+F5) — Toggle the right sidebar panel.
- **Styles** (F11) / **Gallery** — Quick access to sidebar panels.
- **Navigator** (F5) — Toggle the document structure navigator.
- **Data Sources** (Shift+Ctrl+F4) — Toggle the database data-source view.
- **Full Screen** (Shift+Ctrl+J) — Hide menus/toolbars for maximum editing area.
- **Zoom** (►) — Presets (Entire Page, Page Width, 50%–200%) and full Zoom & View Layout dialog.

## Window Menu

- **New Window** — Open a second window for the same document.
- **Close Window** (Ctrl+W) — Close the current window.
- Active document list — bullet marks the current window.

## Help Menu

- **LibreOffice Help** (F1), **What's This?**, **User Guides**
- **Show Tip of the Day**, **Search Commands** (Shift+Escape)
- **Get Help Online**, **Send Feedback**, **Restart in Safe Mode…**
- **Get Involved**, **Donate to LibreOffice**, **License Information**, **About LibreOffice**

