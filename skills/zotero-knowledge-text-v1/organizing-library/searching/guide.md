# Searching Your Library (Zotero 7)

The search box lives at the top-right of the center pane. Click into it (or press **Ctrl/Cmd-F**) and start typing — Zotero filters your items in real time as you go. By default it searches "All Fields & Tags," but click the dropdown to switch between **Title, Creator, Year**, **All Fields & Tags**, or **Everything** (which includes full-text content of indexed PDFs).

If you have a huge library and search-as-you-type feels sluggish, type a `"` before your query. Zotero will wait until you press **Enter** or close the quote before running the search.

For more control, open **Advanced Search** by clicking the magnifying glass icon next to the search box. This opens a dedicated window where you pick a field (like **Title**, **Date**, **Collection**, etc.), a condition (like "contains" or "is before"), and a value. Hit the **+** button to stack multiple filters — by default an item must match **all** of them, but you can switch the **Match** dropdown to **any**.

The `%` character works as a wildcard in advanced searches. For instance, `W% Shakespeare` matches "W. Shakespeare," "William Shakespeare," and so on. Searching a field for just `%` finds any item where that field isn't empty.

Once you've built a useful advanced search, click **Save Search** and give it a name. It appears in the left pane like a collection but updates itself automatically — great for things like "items added in the last 7 days." Right-click a saved search to choose **Edit Saved Search…** or **Delete Saved Search…**. You can also create one directly by right-clicking a library name and choosing **New Saved Search…**.

For complex Boolean logic like `(a OR b) AND (c OR d)`, create two saved searches (one for each OR group), then run a third advanced search filtering by **Collection is Condition1 AND Collection is Condition2**.

Zotero automatically indexes PDF text in the background, making it searchable via **Everything** quick search or the **Attachment Content** field in advanced search. You can tune indexing limits and rebuild the index under **Edit > Settings > Search**.
