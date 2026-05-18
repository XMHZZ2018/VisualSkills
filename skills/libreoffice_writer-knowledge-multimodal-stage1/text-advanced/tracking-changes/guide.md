# Tracking Changes (LibreOffice Writer 7.3.7)

Writer's change tracking feature — sometimes called "redlines" or "revision marks" — lets you record every addition, deletion, and formatting tweak so that you or a colleague can review them later. Not everything gets tracked (tab stops, formulas, and linked graphics are notable exceptions), but for day-to-day text editing it covers what you need.

**Turning it on** is simple: go to **Edit > Track Changes > Record**. The menu item appears highlighted when recording is active. To toggle the visual markup on or off without stopping the recording, use **Edit > Track Changes > Show**. Hover over any marked change to see a tooltip with the author, date, time, and type of edit.

You can also add a comment to a specific change by placing your cursor in the changed area and choosing **Edit > Track Changes > Comment**, or clicking the **Insert Track Change Comment** button on the Track Changes toolbar. Use the arrow buttons inside the comment dialog to step through changes one by one.

When you're done editing, stop recording with another click on **Edit > Track Changes > Record**.

See `fig01.png`.

**Preparing a document for review** is worth a moment of setup. First, check whether the file already contains multiple versions (**File > Versions**); if so, save the current state as a separate document and use that as your review copy. Make sure recording is on, then lock it down with **Edit > Track Changes > Protect** — enter a password (twice) and click **OK**. Now reviewers must supply the password before they can turn off tracking or accept/reject changes. A shortcut: you can do the same thing from **File > Properties > Security** by selecting **Record changes**, clicking **Protect**, and entering the password.

**Accepting or rejecting changes** can happen several ways. For quick, inline decisions, right-click a tracked change and choose **Accept Change** or **Reject Change** from the context menu. Accepting a change makes it permanent; rejecting it reverts the text to its original state.

For a broader view, open **Edit > Track Changes > Manage**. The Manage Changes dialog lists every pending change with its action type, author, date, and any comment. Select a change and the corresponding text highlights in the document so you can see exactly what's affected. Click **Accept** or **Reject** for individual changes, or use **Accept All** / **Reject All** to handle everything at once.

See `fig02.png`.

Need to narrow things down? Switch to the **Filter** tab in the Manage Changes dialog to filter by date range, author, action type, or comment text. Once your filter is set, flip back to the **List** tab to see only the changes that match.

If a reviewer forgot to turn on tracking altogether, you can still recover the differences. Open the edited document, then go to **Edit > Track Changes > Compare Document**, pick the original file, and click **Open**. Writer marks all the differences as tracked changes, and from there you accept or reject them in the usual way.
