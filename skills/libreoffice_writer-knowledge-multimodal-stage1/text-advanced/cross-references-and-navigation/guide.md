# Cross-References and Navigator (LibreOffice Writer 7.3.7)

Typed cross-references to other parts of a document go stale fast — rename a heading or shuffle sections and suddenly your "see page 12" points nowhere. Writer gives you two tools to keep internal links honest: *hyperlinks* and *automatic cross-references*. Both let you Ctrl+click to jump to the target, but they behave differently after that.

A hyperlink does **not** auto-update if you change the text of the linked item (though you can fix it by hand). You also can't choose what the link displays — it's just the link. Cross-references, on the other hand, update automatically and let you pick what appears in the text: the heading name, the page number, or other variations. If you need to reference a heading, caption, or other linked item and want the text to stay current, use automatic cross-references via **Insert > Cross-reference** (see Chapter 17, Fields, for details).

**Bookmarks** are listed in the Navigator and give you single-click jumps to any spot in a document. In HTML output, they become anchors you can link to by hyperlink. Set one with **Insert > Bookmark**, then cross-reference it through the Fields dialog.

## Using Hyperlinks

Type or paste a URL (or a web address) and press **Space** or **Enter** — Writer auto-detects it, applies hyperlink formatting (color and underline), and makes it clickable. If that doesn't happen, turn on **Tools > AutoCorrect > AutoCorrect Options**, then check the **URL Recognition** option on the *Options* tab. To undo an unwanted hyperlink, hit **Ctrl+Z** immediately, or right-click it later and choose **Remove Hyperlink**.

To edit an existing hyperlink, click inside it and choose **Edit Hyperlink** from the context menu, or click the **Hyperlink** icon on the Standard Toolbar, or go to **Edit > Hyperlink**. Make your changes, click **Apply**, then **Close**. You can change link colors globally via **Tools > Options > LibreOffice > Application Colors** — scroll to the *Unvisited links* and *Visited links* entries under the *General* section.

By default, Ctrl+click opens hyperlinks. To switch to single-click, go to **Tools > Options > LibreOffice > Security**, click **Options**, and deselect **Ctrl-click required to open hyperlinks**.

## Rearranging Content with the Navigator

The Navigator lets you drag entire headings — along with all their subheadings and body text — to a new position in your document. Open it with **F5** or **View > Navigator**.

If necessary, click the expansion symbol next to a heading to reveal its subheadings. When you have deeply nested sections, narrow the view by changing the **Heading Levels Shown** selector to show only the top one or two levels. Then just drag the heading block to its new location in the Navigator list. Alternatively, click a heading and use the **Promote Chapter** or **Demote Chapter** icons to move it (and its subsections) up or down. To move *only* the heading without its child content, hold **Ctrl** while clicking **Promote Chapter** or **Demote Chapter**.
