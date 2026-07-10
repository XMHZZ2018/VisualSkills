# Numbering Pages (LibreOffice Writer 7.3.7)

Page numbers in Writer are fields you insert into a header or footer — they update automatically on every page. To get started, place your cursor in a header or footer and go to **Insert > Page Number**, or use **Insert > Field > Page Number**. The number appears with a gray background on screen (that's just the field marker; it won't print).

See `fig01.png`.

To align the page number, click in the footer paragraph and use the alignment icons on the Formatting toolbar, or right-click and choose **Paragraph > Paragraph**, then pick an alignment on the **Alignment** tab.

By default, page numbers display as Arabic numerals (1, 2, 3…). If you want a different format — say, lowercase Roman numerals for a preface — right-click the text area, select **Page Style**, and on the **Page** tab find the **Page numbers** drop-down under *Layout Settings*. Pick the format you need and click **OK**. Keep in mind this changes every page that shares the same page style.

See `fig02.png`.

When you need to restart numbering — common after a title page or table of contents — you'll work with paragraph breaks. Place the cursor in the first paragraph of the page where numbering should restart. Open **Format > Paragraph** (or right-click and choose **Paragraph > Paragraph**), then go to the **Text Flow** tab. In the *Breaks* area, check **Insert**, set *Type* to **Page**, *Position* to **Before**, and tick **With page style** choosing the appropriate style (e.g., Default Page Style). Then check **Page number** and type the number you want to start from — typically 1. Click **OK**.

See `fig03.png`.

If you want the first page of your document to start at a number other than 1, the process is the same: insert a page number field in the header or footer, then apply the paragraph break settings above to the first paragraph, entering whatever starting number you like. Note that setting an even starting number will produce a blank page before it, since Writer follows the convention of odd numbers on right-hand pages.

You can also combine page numbers with other text in the header. For instance, type "Page " before the field, or add a Page Count field via **Insert > Field > Page Count** to get something like "Page 2 of 12." For chapter-based numbering (1-1, 1-2, 2-1…), first set up chapter numbering with **Tools > Chapter Numbering**, then insert a Chapter field from **Insert > Field > More Fields** on the **Document** tab, choosing **Chapter number** in the *Format* list, alongside your page number.
