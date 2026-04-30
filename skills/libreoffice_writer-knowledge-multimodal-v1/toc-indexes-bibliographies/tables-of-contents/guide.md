# Tables of Contents (LibreOffice Writer 7.3.7)

A table of contents (TOC) in Writer is built automatically from the headings in your document. When you change a heading's text or its page shifts, the TOC picks that up the next time you update it. The key requirement is consistent use of paragraph styles — apply **Heading 1** for chapter titles, **Heading 2** and **Heading 3** for subsections, and Writer takes care of the rest.

To insert a default TOC, click where you want it to appear and go to **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**. Leave the defaults and click **OK**. You'll get a gray-shaded block with clickable hyperlinks — the shading is just an on-screen reminder that the area is a field, and it won't print or export to PDF.

If headings aren't showing up, double-check that they're tagged with the right paragraph style. If an entire outline level is missing, verify the settings under **Tools > Chapter Numbering**. To turn off the gray background, head to **Tools > Options > LibreOffice > Application Colors** and deselect *Index and table shadings*.

When you add, delete, or move headings, the TOC goes stale. Right-click anywhere inside it and choose **Update Index** to refresh. Be sure **Edit > Track Changes > Show** is off before updating, or deleted headings may linger and page numbers can get confused.

See `fig01.png`.

For deeper customization, right-click the TOC and select **Edit Index** to reopen the dialog. The **Type** tab controls the scope — you can build the TOC from the entire document or just the current chapter, and set how many outline levels to include with the **Evaluate up to level** field. Under *Create From*, the **Outline** option (default) pulls in styles linked to outline levels via **Tools > Chapter Numbering**, while **Additional styles** lets you fold in extra paragraph styles by clicking **Assign styles** and choosing the level for each one.

The **Entries** tab is where you fine-tune the structure line for each level — chapter number, entry text, tab stop, page number, and hyperlink markers are all represented by icons you can add, remove, or reorder. Pick a level on the left, then click in the white Structure field and use the buttons below to insert or swap elements. Hit **All** to copy the current structure to every level at once.

See `fig02.png`.

On the **Styles** tab you can assign a different paragraph style to each TOC level. Select the level, pick a style from the *Paragraph Styles* list, and click the **<** button to apply it. Use the **Background** tab if you want a colored or bitmap background behind the TOC — select **Color** or **Bitmap** from the row of buttons and configure as needed.
