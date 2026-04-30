# Printing Mailing Labels and Envelopes (LibreOffice Writer 7.3.7)

Labels are handy for printing address lists where each label holds a different address, but they also work for batch-printing identical labels — think return-address stickers or CD labels. Before you start, jot down the brand and type of your label sheets so you can match them in the dialog.

To get going, open **File > New > Labels**. On the **Labels** tab, pick your **Database** and **Table** from the drop-downs on the right, then select each address field (like FNAME, ADDRESS1, CITY, etc.) from the **Database field** list and click the left arrow to drop it into the **Label text** area. Add punctuation, spaces, and line breaks between fields until your label looks right.

See `fig01.png`.

Down in the **Format** section, choose your label **Brand** and **Type** to match your physical sheets. If your labels aren't listed, select **[User]** in the Type box and flip to the **Format** tab to enter custom dimensions — horizontal pitch, vertical pitch, width, height, margins, columns, and rows. You can save a custom layout for reuse by clicking **Save** and giving it a name.

On the **Options** tab, make sure **Synchronize contents** is checked. This ensures edits you make to the first label propagate to all the others. Then hit **New Document**. You'll get a one-page document with a grid of label frames, each filled with your merge fields. The printed output expands to as many pages as your data requires.

See `fig02.png`.

A small **Synchronize Labels** button appears near the top-left of the screen. If you need to tweak formatting — change the font, fix punctuation, add a field — edit the upper-left label only, then click **Synchronize Labels** to push those changes to every label on the page.

When you're happy, go to **File > Print** and click **Yes** to confirm the mail merge. In the Mail Merge dialog you can print all records, or use Ctrl+click to cherry-pick individual ones. Click **OK** to send them to the printer (or choose **File** in the Output section to save to a file instead).

To edit a saved label file later, open it like any Writer document. You can right-click a label record, choose **Paragraph > Edit Style**, and adjust the font, size, or indents — but you can't regenerate labels from the source data without recreating the merge.

## Envelopes

For envelopes, go to **Insert > Envelope**. On the **Envelope** tab, drag your address fields from the database into the **Addressee** box, just like you did for labels. If your envelopes aren't pre-printed, check the **Sender** box and fill in your return address. Use the **Format** and **Printer** tabs to set envelope size and feed direction.

See `fig03.png`.

Click **New Document** to create the envelope template. To merge and print, choose **File > Print**, confirm the merge, and select your records the same way as with labels.
