# Using Tables for Page Layout (LibreOffice Writer 7.3.7)

Tables in Writer aren't just for data — they're a handy way to build structured page layouts like sideheads, multi-column arrangements, and neatly aligned header or footer content. Think of a table as an invisible grid you can drop text and graphics into, giving you far more control than tabs or spaces ever could.

## Positioning info in headers and footers

Instead of fussing with frames or manual spacing, drop a borderless table into a header or footer. This lets you cleanly position elements like page numbers on the left, the document title in the center, and the author on the right — all in a single row. For even simpler cases, fields (**Insert > Header and Footer > Fields**) might be enough.

## Creating sideheads with tables

Sideheads — those marginal labels you see in resumes and user guides — are easy to pull off with a two-column table. The narrow left column holds your sidehead text, while the wider right column carries the main body content. The first paragraph in each cell aligns beside the sidehead, giving that classic offset look.

To set one up, place your cursor where you want it and go to **Table > Insert Table** (or press **Ctrl+F12**). Create a two-column, one-row table with no heading, and pick **None** under Styles so the table is borderless. Hit **Insert**.

See `fig01.png`.

Now right-click the table and choose **Table Properties**. On the **Columns** tab, set your column widths — for example, 3.30 cm for the sidehead and 13.70 cm for the body text, matching your page's left margin offset.

See `fig02.png`.

Then switch to the **Table** tab in the same dialog. Under Spacing, set **Above** and **Below** to match the top and bottom spacing of your regular body paragraphs so the table blends seamlessly into the page flow. Give the table a meaningful name in the Properties section and click **OK**.

If you'd rather have each paragraph break onto its own row (handy when content grows), put each chunk in a separate table row and let the table break between pages. Alternatively, keep everything in one row if you want text and graphics to reflow together when you edit.

**Tip:** You can quickly check a paragraph's spacing by clicking into it and opening the Properties deck in the Sidebar — look under *Paragraph > Spacing* for the values.
