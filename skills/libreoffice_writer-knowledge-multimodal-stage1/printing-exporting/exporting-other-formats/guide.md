# Exporting to EPUB and Other Formats (LibreOffice Writer 7.3.7)

EPUB has become the go-to format for e-readers, tablets, and smartphones. It's essentially an archive of HTML files bundled with images and supporting files. Writer handles EPUB export reasonably well for text-heavy documents, though content like illustrations, tables, and cross-references may not come through perfectly.

**Quick export** is the fastest route: go to **File > Export As > Export Directly as EPUB**. This uses whatever EPUB settings you last configured, prompts you for a filename and location, and you're done — no dialog, no fuss.

If you want more control, use **File > Export As > Export as EPUB** instead. This opens the EPUB Export dialog where you can fine-tune the output.

See `fig01.png`.

Under **General**, pick your EPUB **Version** (2.0 or 3.0 — most modern e-readers handle 3.0 fine). The **Split method** determines how chapters are divided: *Heading* splits on heading styles, while *Page break* splits at each page break. For **Layout method**, choose *Reflowable* to let the ebook adapt to the reader's screen size, or *Fixed* to preserve exact page layout.

The **Customize** section lets you set a **Cover image** path and a **Media directory** for bundled multimedia. If you leave the cover image blank, Writer will automatically use any image named `cover.gif`, `cover.jpg`, `cover.png`, or `cover.svg` it finds. The media directory defaults to a folder with the same name as your document in the current directory.

**Metadata** fields — Identifier, Title, Author, Language, Date — give your EPUB the tags e-readers and libraries use for searching and sorting. These pull from **File > Properties** by default, so setting your document properties ahead of time saves a step here.

For broader format needs beyond EPUB, Writer can also export to XHTML, PDF, and several image formats. Just go to **File > Export**, pick your format from the **File format** dropdown (you'll see options like PNG, XHTML, EPUB, JPEG, and more), give it a name, and click **Export**.

See `fig02.png`.

If you can't find the format you need under **File > Save As** or **File > Export**, consider Calibre — a free, open-source e-book manager available on Windows, macOS, and Linux at [https://calibre-ebook.com](https://calibre-ebook.com). It handles a wide range of conversions from `.odt` files and gives you more control over the final result.
