# Using Sections for Page Layout (LibreOffice Writer 7.3.7)

Sections in Writer let you treat a block of text differently from the rest of your document. Think of them as containers — you can use them to write-protect text, hide content, pull in content from another file, add columns to just part of a page, or give a region its own background and footnote style.

To create a section, place your cursor where you want it (or select existing text), then go to **Insert > Section**. The dialog that opens has five tabs: *Section*, *Columns*, *Indents*, *Area*, and *Footnotes/Endnotes*. Give the section a meaningful name in the **New Section** box — it shows up in the Navigator, so something descriptive helps. When you're happy with the settings, hit **Insert**.

See `fig01.png`.

If you want the section to pull in content from a separate file, check the **Link** option on the *Section* tab, click **Browse**, and pick the source document. You can even link to a specific section within that file using the *Section* drop-down. Writer can update linked sections automatically — configure that under **Tools > Options > LibreOffice Writer > General** in the *Update links when loading* area.

To keep people from editing a section's content, tick **Protect** in the *Write Protection* area. You can optionally add a password by also selecting **With password** — just be aware that a forgotten password can't easily be recovered. Protection only locks the content, not the section's formatting or attributes.

You can hide a section entirely by checking **Hide** in the *Hide* area. You can even make it conditional — enter a condition in the **With Condition** field using the same syntax as Writer's fields and formulas. This is great for producing different versions from a single source document (say, a student copy vs. a teacher copy of a test).

Need columns in just part of your page? The *Columns* tab lets you split the section into multiple columns. Check **Evenly distribute contents to all columns** if you want the text to balance out; leave it unchecked for newspaper-style flow where each column fills completely before the next one starts.

See `fig02.png`.

The *Indents* tab controls left and right margins for the section via the **Before section** and **After section** fields, with a handy preview on the right. The *Area* tab adds color or image backgrounds, and the *Footnotes/Endnotes* tab lets you restart numbering, change the format, or collect endnotes at the section's end instead of the document's end.

To edit or remove sections later, go to **Format > Sections**. Select a section from the list, change its name, link, protection, or hide settings, and click **OK**. To tweak column or formatting options, select the section and click **Options**. Clicking **Remove** doesn't delete the content — it just dissolves the section wrapper, merging the text back into the main document flow.

See `fig03.png`.
