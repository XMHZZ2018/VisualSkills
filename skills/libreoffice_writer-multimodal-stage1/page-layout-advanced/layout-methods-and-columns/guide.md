# Layout Methods and Columns (LibreOffice Writer 7.3.7)

Writer gives you several ways to control page layout: columns, frames, tables, sections, page orientation changes, and borders/backgrounds. Every page in a Writer document is based on a page style, and all the other layout methods build on top of that underlying style.

A quick tip before you start: turn on layout helpers by going to **Tools > Options > LibreOffice > Application Colors** to show text, object, table, and section boundaries. You can also tweak paragraph marks, tabs, and breaks under **Tools > Options > LibreOffice Writer > Formatting Aids**. These visual cues make complex layouts much easier to wrangle.

## Choosing a layout method

Which technique you pick depends on what your final document needs to be. For a book-style layout with one column of text and the occasional figure, page styles alone will carry you. If you need two or more columns — like an index where text flows left-to-right then down — use sections with columns. For a newsletter with two or three columns per page and articles that jump across pages, combine page styles with linked frames and anchored graphics.

Keep in mind that if you're targeting HTML, EPUB, or another reflowable format, stick to minimal layout techniques. Columns, frames, and wide tables often don't export cleanly to those formats.

## Defining columns on a page

Start by setting up your base page style (typically *Default Page Style*) with the column count you'll use most. Open it via **Format > Page Style** on the menu bar, or right-click the page and choose **Page Style** from the context menu. Head over to the **Columns** tab.

In the **Settings** section, pick the number of columns and set the spacing between them. You can choose one of Writer's predefined column layouts or create a custom one. The live preview on the right side of the dialog shows exactly how your layout will look. Hit **OK** when you're happy.

See `fig01.png`.

If you want different column counts on the same page — say a full-width title above a two-column body — you'll need sections instead of page-level columns. That's covered under "Using sections for page layout."

## Column width and spacing

By default, **AutoWidth** is selected, which divides space equally among all columns. To set custom widths, deselect **AutoWidth** in the *Width and Spacing* section, then type a width for each column individually. Use the **Spacing** line to control the gap between each pair of columns. If you have more than three columns, use the arrow buttons on the *Column* line to scroll through them.
