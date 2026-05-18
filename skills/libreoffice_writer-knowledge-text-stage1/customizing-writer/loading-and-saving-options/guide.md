# Loading and Saving Options (LibreOffice Writer 7.3.7)

Head over to **Tools > Options** and expand **Load/Save** on the left to find all the settings that control how Writer opens and saves your documents. The General page is the one you'll use most.

Under the **Load** section, you'll see **Load user-specific settings with the document**. When this is on, Writer applies the original author's settings (like printer config) when you open their file. If you're working in an office where documents bounce between people and printers, you might want to turn this off so your own system settings take priority. Note that some things — like data source links, spacing options for paragraphs before text tables, and field function update settings — always load with the document regardless.

There's also **Load printer settings with the document**. Leaving it enabled means a document could try to print to a network printer you don't have access to, so disable it if that's a concern.

See `fig01.png`.

The **Save** section is where you set up your safety net. **Save AutoRecovery information every __ minutes** tells Writer how often to stash recovery data. Keep this on — if Writer crashes, you'll be glad it saved a snapshot ten minutes ago instead of never. You can adjust the interval to taste.

**Edit document properties before saving** pops up the document's Properties dialog the first time you save (or use Save As), handy if you like to fill in metadata early. **Always create backup copy** saves the previous version of your file with a `.bak` extension in a separate folder. You can find (or change) that folder under **Tools > Options > LibreOffice > Paths**.

Under **Default File Format and ODF Settings**, pick the ODF format version and set what **Always save as** defaults to — for instance, ODF Text Document (`.odt`). If you regularly exchange files with Microsoft Office users, you could set this to a Word format instead, though you'll get a warning when saving in non-ODF formats. The **Warn when not saving in ODF or default format** checkbox controls that nudge.

If you work on long documents or anything you can't afford to lose, seriously consider enabling both AutoRecovery and backup copies. They work independently: AutoRecovery protects against crashes, while backup copies protect against accidental overwrites. Belt and suspenders.
