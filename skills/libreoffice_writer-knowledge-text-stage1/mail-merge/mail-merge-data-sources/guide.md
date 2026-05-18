# Data Sources for Mail Merge (LibreOffice Writer 7.3.7)

Mail merge in Writer lets you produce multiple copies of a document — form letters, mailing labels, envelopes, stickers, you name it — each personalized with variable data like names, addresses, and amounts. The data itself comes from an external source: a spreadsheet, a text file, even a MySQL database. Before you can use any of that in a mail merge, though, you need to register the data source with LibreOffice so Writer knows where to find it.

To kick things off, open **File > Wizards > Address Data Source**. You can also reach this from the LibreOffice Start Center. The wizard walks you through connecting your data in just a few clicks.

On the first page of the wizard, pick the type of external address book you're working with. If you're using a spreadsheet (which is the most common case), select **Other external data source** and hit **Next**.

See `fig01.png`.

The next page is the Connection Settings step — just click the **Settings** button to open the detailed connection dialog.

In the Create Address Data Source dialog that appears, set the **Database type** to **Spreadsheet** (or whatever matches your source), then click **Next**.

Now you'll need to point LibreOffice at the actual file. Click **Browse**, navigate to the spreadsheet that holds your address data, select it, and click **Open** to get back to the dialog.

See `fig02.png`.

Before moving on, it's worth clicking the **Test Connection** button to make sure everything is wired up correctly. You should see a confirmation message saying the connection was established successfully. If you get an error instead, double-check the file path and format.

Once the connection checks out, click **Finish**. On the final page you can click **Next** without worrying about the Field Assignment button — that's only needed later if you're using the full Mail Merge Wizard.

That's it. Your data source is now registered and available from within any Writer document. You only need to do this once per data source; after that, it's ready whenever you need it for letters, labels, or envelopes.
