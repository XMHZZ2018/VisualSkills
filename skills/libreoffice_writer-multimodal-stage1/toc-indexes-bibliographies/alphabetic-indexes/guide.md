# Alphabetic Indexes (LibreOffice Writer 7.3.7)

An alphabetic index is a list of keywords or phrases used throughout your document, paired with page numbers so readers can find things fast. Writer lets you mark entries manually, optionally use a concordance file, and then generate the index in a few clicks.

To add an index entry, place your cursor in the word you want indexed — or select an entire phrase — and go to **Insert > Table of Contents and Index > Index Entry**. The selected text appears in the **Entry** field; tweak it if you like, then hit **Insert**. You don't have to close the dialog between entries — just click somewhere else in your document, click the dialog again, adjust the entry, and press **Insert** to keep going.

See `fig01.png`.

You can organize entries into groups using the **1st key** field. For example, if your index should list "Calc," "Impress," and "Writer" as subentries under "LibreOffice," type "LibreOffice" in the **1st key** box for each of those entries. A **2nd key** adds another nesting level, though that degree of complexity is rarely needed. Check **Main entry** if one page is the primary reference for a term — you can later style that page number in bold to make it stand out.

If you have a lot of terms to index, a concordance file saves time. It's a plain text file where each line follows the format: `Search_term;Alternative_entry;1st_key;2nd_key;Match_case;Word_only`. Writer scans the document for each search term and creates the entries automatically. The trade-off is less precision — you may get unwanted hits for common words.

When you're ready to generate the index, click where you want it to appear and open **Insert > Table of Contents and Index > Table of Contents, Index or Bibliography**. On the **Type** tab, set the type to **Alphabetical Index**. Consider enabling **Combine identical entries with p or pp** for cleaner page ranges, and tick **Case sensitive** if capitalization matters. If you prepared a concordance file, select **Concordance file** and browse to it. Click **OK** and the index drops in.

See `fig02.png`.

To customize the look, right-click anywhere in the generated index and choose **Edit Index**. The **Entries** tab controls the structure of each line — the **E** icon is the entry text, **T** is a tab stop, and **#** is the page number. You can apply character styles to any element (handy for making page numbers a different size). Under the **Format** section, enable **Alphabetical delimiter** to get letter headings (A, B, C…) separating groups, or choose **Key separated by commas** to put subentries on one line.

The **Columns** tab lets you lay the index out in multiple columns — just set the number and optionally add a separator line between them. The **Styles** and **Background** tabs work the same way as for a table of contents.

Writer won't update the index automatically when you add or remove entries. Right-click the index and select **Update Index** whenever your content changes, or use the Navigator to find and update it. To remove the index entirely, right-click it and choose **Delete Index**.
