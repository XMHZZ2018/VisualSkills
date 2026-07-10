# Creating Tables (LibreOffice Writer 7.3.7)

Tables are a great way to organize data — think financial reports, catalogs, invoices, or even simple lists of names and addresses. They can also double as a page-layout tool when you need precise positioning of text and objects within your document.

All table-related commands live under **Table** on the Menu bar. When your cursor is inside a table, the Table toolbar appears automatically. You can also bring it up manually via **View > Toolbars > Table**. It gives you quick access to things like inserting and deleting rows/columns, merging and splitting cells, borders, alignment, number formats, and more. The Properties deck in the Sidebar also expands with a **Table** panel for adjusting row height, column width, and cell operations.

See `fig01.png`.

The fastest way to drop in a table is to click the **Insert Table** icon on the Standard toolbar. A little grid pops up — just drag to select how many rows and columns you want (up to 15 × 10) and click. Done.

See `fig02.png`.

For more control, open the Insert Table dialog instead: go to **Table > Insert Table**, press **Ctrl+F12**, or click **More Options** at the bottom of that drop-down grid. Here you can give the table a name (handy if you use the Navigator to jump between tables), set exact column and row counts, and configure options like repeating heading rows across pages or preventing the table from splitting over a page break. The *Styles* section at the bottom lets you pick from predefined table styles so you don't have to format everything by hand. When you're happy, hit **Insert** and Writer creates a table spanning the full text area width with equally sized columns.

See `fig03.png`.

You can nest tables too — just click inside a cell of an existing table and insert another one using any of the methods above. This is especially useful for complex page layouts.

There's also an AutoCorrect trick: type a sequence of plus signs and hyphens (like `+-----+-----+-----+`) and press Enter. Writer converts it into a table automatically, using the hyphens to determine column widths. You can toggle this behavior in **Tools > AutoCorrect > AutoCorrect Options** on the *Options* page.

If you already have text that should be a table — say, tab-separated or semicolon-separated data — select it and choose **Table > Convert > Text to Table**. Pick your separator type in the dialog, set any options, and click **OK**. The reverse works too: place your cursor in a table and use **Table > Convert > Table to Text** to flatten it back to plain text, which is great for exporting to other programs.

Finally, you can paste spreadsheet data directly. Open both documents, select the cells in your spreadsheet, copy with **Ctrl+C**, then switch to Writer and paste with **Ctrl+V**. You can also simply drag and drop the selection from the spreadsheet into your Writer document.
