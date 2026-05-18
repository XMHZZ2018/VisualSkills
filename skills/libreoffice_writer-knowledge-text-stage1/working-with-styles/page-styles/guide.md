# Working with Page Styles (LibreOffice Writer 7.3.7)

Page styles in Writer control margins, page size, headers, footers, and columns — everything about the physical layout of your pages. Unlike paragraph or character styles, page styles can't be directly applied to content. Instead, every page inherits its look from an underlying page style, so when you tweak that style, all pages using it update at once. If you need individual pages to look different, you'll create separate page styles.

To get started, open the **Styles** deck and click the **Page Styles** icon. Right-click anywhere in the list and choose **New** to create a fresh style, or select an existing one and hit **Modify**. The Page Style dialog has nine tabs — the most important ones are Page, Header, Footer, Columns, and Borders.

On the **Page** tab, you'll set your paper size and orientation. Pick a predefined format from the **Paper Format** section, or choose **User** and type custom **Width** and **Height** values. Flip between **Portrait** and **Landscape** depending on your needs.

See `fig01.png`.

The **Margins** section on that same tab lets you dial in inner, outer, top, bottom, and gutter spacing. If you choose **Mirrored** in the **Page layout** dropdown under **Layout Settings**, the margin labels switch to Inner and Outer — perfect for book-style printing where left and right pages mirror each other. The **Gutter** margin adds extra binding space on the inner edge.

A common practice for printed layouts is asymmetrical margins: wider outer margins on the right-hand page, with the bottom margin larger than the top. If you're setting up a book, select a mirrored layout so the first chapter page uses the right-page settings, and the rest of the chapter uses a "mirrored" default style for both left and right pages. A mirrored page can carry different headers and footers, which is handy for alternating page numbers or chapter titles.

You can also define entirely separate page styles for left and right pages — say, a full-page photo on the left and two columns of text on the right. Just make sure the **Next Style** field on each style points to the correct following style so Writer cycles through them automatically.

Use the **Page numbers** dropdown to choose a numbering style (1, 2, 3 or i, ii, iii, etc.) that applies wherever you assign this page style. Combined with the **Header** and **Footer** tabs, you can insert fields like page number or chapter name into running headers or footers, giving each section of your document its own look without manual formatting.
