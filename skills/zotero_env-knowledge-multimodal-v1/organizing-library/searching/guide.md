# Searching Your Library (Zotero 7)

The fastest way to find something is the quick search box in the upper-right corner of the center pane. Click into it (or press **Ctrl/Cmd-F**) and start typing — Zotero filters the item list in real time as you go.

See `fig01.png`.

By default, quick search checks titles, years, and creators. Click the dropdown arrow on the search box to switch modes: **Title, Creator, Year** searches those fields plus publication titles, **All Fields & Tags** adds tags and note text, and **Everything** also searches the full text of indexed PDFs. Pick the mode that fits how much ground you want to cover.

If you have a huge library and search-as-you-type feels sluggish, start your query with a quotation mark (`"`). Zotero will then wait until you press **Enter** or type a closing `"` before running the search.

For more precise filtering, open **Advanced Search** by clicking the magnifying glass icon at the top of the center pane. This opens a dialog where you build criteria row by row — pick a field like **Title**, a condition like **contains**, and enter your value. Add more rows with the **+** button, and choose whether items must match **all** or **any** of them.

See `fig02.png`.

A handy trick: the `%` character works as a wildcard. Searching for `W% Shakespeare` matches "W Shakespeare", "W. Shakespeare", and "William Shakespeare". Searching a field for just `%` finds any item where that field isn't empty.

Once you've built a useful advanced search, hit **Save Search** and give it a name. It appears in your library's left pane like a collection, but it stays live — its contents update automatically as your library changes. For example, a saved search for **Date Added is in the last 7 days** always shows your most recent additions. Right-click a saved search to choose **Edit Saved Search…** or **Delete Saved Search…**.

You can even chain saved searches for complex Boolean logic. To search `(a OR b) AND (c OR d)`, create two saved searches (one for each OR group), then run a third advanced search matching items in both of those saved-search "collections."

Zotero automatically indexes the text inside your PDFs in the background, which is what powers the **Everything** quick search mode and the **Attachment Content** criterion in advanced search. You can adjust indexing limits or rebuild the index from **Settings > Search**. If a PDF isn't showing up in full-text results, select the attachment, check the **Indexed** field in the right pane, and right-click to **Reindex Item** if needed. Note that only PDFs and plain text files are indexed — other formats like .docx or .epub are not.
