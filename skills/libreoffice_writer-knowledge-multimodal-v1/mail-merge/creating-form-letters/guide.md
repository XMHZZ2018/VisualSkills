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
