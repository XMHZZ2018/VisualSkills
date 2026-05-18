# Defining a Heading Hierarchy with Styles (LibreOffice Writer 7.3.7)

Paragraph styles are the backbone of heading hierarchy in Writer. They drive the table of contents, outline numbering, and cross-references, so it's worth getting them right from the start.

Writer ships with default heading styles — *Heading 1*, *Heading 2*, and so on — already mapped to outline levels. If those defaults work for you and you just want automatic numbering, you're basically done: apply the styles and let Writer handle the rest. But if you want to swap in your own custom paragraph styles, you'll need to tell Writer which style maps to which level.

Open **Tools > Chapter Numbering** to get to the main dialog. On the **Numbering** tab, you'll see a *Level* list on the left (1 through 10). Click a level, then pick the paragraph style you want assigned to it from the *Paragraph style* drop-down. For instance, you could replace the default *Heading 1* with your own *My Heading 1*, and *Heading 2* with *My Heading 2*. Repeat for each level you need, then click **OK**.

See `fig01.png`.

You can also assign outline levels directly on any paragraph style. Open the style for editing, go to the **Outline & List** tab, and set the desired outline level from the *Outline level* drop-down. This is handy for appendix styles or other headings you want included in the table of contents alongside your main chapter headings.

To add actual numbering (like 1, 1.1, 1.2.1), go back to **Tools > Chapter Numbering**. Select Level 1, set *Number* to "1, 2, 3, …". Then select Level 2, again choose "1, 2, 3, …" and set *Show sublevels* to 2. For Level 3, do the same and set *Show sublevels* to 3. The preview pane on the right updates live so you can see exactly how your nested numbers will look.

See `fig02.png`.

Once numbering is in place, you may want to fine-tune indentation. Switch to the **Position** tab in the same dialog. Select the level you want to adjust and set values for *Aligned at*, *Tab stop at*, and *Indent at*. For example, indenting Level 2 headings from the margin makes the hierarchy visually obvious. If you have long headings that wrap, increase the *Indent at* value so the second line aligns with the heading text rather than the number.

See `fig03.png`.

That's really all there is to it. Define your styles, map them to levels in **Tools > Chapter Numbering**, configure numbering and position, and your document's heading hierarchy is locked in — ready for a table of contents, PDF bookmarks, or Navigator browsing.
