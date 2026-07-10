# Tracking Changes (LibreOffice Writer 7.3.7)

Writer's change tracking feature — sometimes called "redlines" or "revision marks" — lets you record every addition, deletion, and formatting tweak so that you or a colleague can review them later. Not everything gets tracked (tab stops, formulas, and linked graphics are notable exceptions), but for day-to-day text editing it covers what you need.

**Turning it on** is simple: go to **Edit > Track Changes > Record**. The menu item appears highlighted when recording is active. To toggle the visual markup on or off without stopping the recording, use **Edit > Track Changes > Show**. Hover over any marked change to see a tooltip with the author, date, time, and type of edit.

You can also add a comment to a specific change by placing your cursor in the changed area and choosing **Edit > Track Changes > Comment**, or clicking the **Insert Track Change Comment** button on the Track Changes toolbar. Use the arrow buttons inside the comment dialog to step through changes one by one.

When you're done editing, stop recording with another click on **Edit > Track Changes > Record**.

The Edit menu is shown with the **Track Changes** submenu expanded. The left side lists the Edit menu items, with "Track Changes" highlighted in blue. The right side shows the Track Changes submenu, which contains — from top to bottom — **Record** (checked, with the shortcut Cmd+Shift+C) and **Show** (also checked), followed by **Manage…**, **Previous**, **Next**, **Accept**, **Accept and Move to Next**, **Accept All**, **Reject**, **Reject and Move to Next**, **Reject All**, then **Comment…** and **Protect…**, and finally **Compare Document…** and **Merge Document…** at the bottom.

**Preparing a document for review** is worth a moment of setup. First, check whether the file already contains multiple versions (**File > Versions**); if so, save the current state as a separate document and use that as your review copy. Make sure recording is on, then lock it down with **Edit > Track Changes > Protect** — enter a password (twice) and click **OK**. Now reviewers must supply the password before they can turn off tracking or accept/reject changes. A shortcut: you can do the same thing from **File > Properties > Security** by selecting **Record changes**, clicking **Protect**, and entering the password.

**Accepting or rejecting changes** can happen several ways. For quick, inline decisions, right-click a tracked change and choose **Accept Change** or **Reject Change** from the context menu. Accepting a change makes it permanent; rejecting it reverts the text to its original state.

For a broader view, open **Edit > Track Changes > Manage**. The Manage Changes dialog lists every pending change with its action type, author, date, and any comment. Select a change and the corresponding text highlights in the document so you can see exactly what's affected. Click **Accept** or **Reject** for individual changes, or use **Accept All** / **Reject All** to handle everything at once.

The **Manage Changes** dialog is displayed with two tabs at the top: **List** (currently selected) and **Filter**. The List tab contains a table with four columns: Action, Author, Date, and Comment. The table shows multiple tracked changes — deletions marked with a red X icon, insertions marked with a green plus icon, table-related changes, and formatting changes — all attributed to the author "Jean Hollis Weber" with timestamps from 13/03/2022. One row is highlighted in green, showing an insertion with the comment "New feature." Another row has the comment "This no longer exists." At the bottom of the dialog are four buttons: **Accept**, **Reject**, **Accept All**, and **Reject All**, along with a **Close** button on the far right.

Need to narrow things down? Switch to the **Filter** tab in the Manage Changes dialog to filter by date range, author, action type, or comment text. Once your filter is set, flip back to the **List** tab to see only the changes that match.

If a reviewer forgot to turn on tracking altogether, you can still recover the differences. Open the edited document, then go to **Edit > Track Changes > Compare Document**, pick the original file, and click **Open**. Writer marks all the differences as tracked changes, and from there you accept or reject them in the usual way.

---

## UI Reference  —  Right Sidebar

_Scope: Manage Changes panel (Alt+7): Accept/Reject buttons, filter tab_

The collapsed right sidebar is a vertical strip of 8 icon buttons along the right edge of the window. Each opens a full docked panel. Toggle the sidebar with Ctrl+F5 or View > Sidebar.

The screenshot shows the LibreOffice Writer window with an empty document open. Along the far-right edge of the window is a narrow vertical strip containing eight small icon buttons stacked top to bottom — this is the collapsed sidebar. The topmost button is highlighted with a red rectangle and displays a tooltip reading "Properties (Alt+1)." The main document area with its toolbar, formatting bar, and ruler occupies the rest of the window.

## Panel Buttons (top to bottom)

- **Properties** (Alt+1) — Formatting panel with three collapsible sections:
  - *Style:* Paragraph style dropdown, Clone Formatting, Update/New Style buttons.
  - *Character:* Font family, size, Bold/Italic/Underline/Strikethrough, Font Color, Highlighting, Change Case, Super/Subscript.
  - *Paragraph:* Alignment, lists/indent toolbar, line spacing, above/below spacing fields, left/right/first-line indent.

- **Styles** (Alt+2 / F11) — Full style manager: category toolbar (Paragraph/Character/Frame/Page/List/Table Styles), hierarchical style list, Fill Format Mode, filter dropdown. See [Styles](styles.md).

- **Gallery** (Alt+3) — Clip-art browser: categories (Arrows, BPMN, Bullets, Diagrams, Flow chart, Icons), thumbnail grid, Icon/Detailed view, New… button.

- **Navigator** (Alt+4 / F5) — Document structure tree: Headings, Tables, Frames, Images, OLE objects, Bookmarks, Sections, Hyperlinks, References, Indexes, Comments, Drawing objects, Fields, Footnotes, Endnotes. Includes page navigation controls and drag-mode options.

- **Page** (Alt+5) — Page layout panel:
  - *Format:* Size (A4), Width/Height, Orientation (Portrait/Landscape), Margins.
  - *Styles:* Page number format, Background, Layout, Columns.
  - *Header/Footer:* Enable toggles, margins, spacing, same-content options.

- **Style Inspector** (Alt+6) — Two-column Properties/Value tree showing all applied styles: Paragraph Styles, Paragraph Direct Formatting, Character Styles, Character Direct Formatting (50+ properties per node).

- **Manage Changes** (Alt+7) — Two tabs:
  - *List:* Action/Author/Date/Comment table with Accept/Reject/Accept All/Reject All buttons.
  - *Filter:* Date range, Author, Action, Comment filters.

- **Accessibility Check** (Alt+8) — Runs an accessibility audit and lists issues by category, each with a Fix… button.
