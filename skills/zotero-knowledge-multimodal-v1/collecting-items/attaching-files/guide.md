# Attaching Files and Web Pages (Zotero 7)

Zotero doesn't just track metadata — it can also store and organize the actual files (PDFs, snapshots, documents) alongside your references. Files can live as **child attachments** under a regular item or as **standalone items**. You almost always want child attachments, since standalone files can't be cited, searched properly, or used with My Publications.

If you drop a bare PDF into your library, Zotero will try to retrieve its metadata and create a parent item automatically. If that fails, right-click the PDF, choose **Create Parent Item**, and paste in a DOI or ISBN. As a last resort, pick **Manual Entry** to fill in the metadata yourself.

**Stored files** (the default) are copied into Zotero's data directory, synced across devices, and deleted when you remove the attachment. **Linked files** just point to a file on disk — they won't sync, can't be used in group libraries or the mobile apps, and stick around even if you delete the Zotero item. Stick with stored files unless you have a specific reason not to. If you do use linked files across machines, set a **linked attachment base directory** under **Settings > Advanced** so Zotero can resolve paths on each computer.

The easiest way to attach files is through the browser. When you save an item with the **Zotero Connector**, any associated PDFs or snapshots are grabbed automatically. You can control this behavior in Zotero's **Settings > General** preferences.

Inside the Zotero app, just drag a file from Finder or Explorer onto an existing item in the center pane to add it as a child attachment. Dropping it onto a collection or into empty space creates a standalone item instead. To create a *linked* file rather than a copy, hold `Cmd+Option` (Mac) or `Ctrl+Shift` (Windows/Linux) while dropping.

You can also select an item and click the **Add Attachment** paperclip button in the toolbar. From the dropdown, choose **Attach Stored Copy of File…** or **Attach Link to File…**. There's also **Attach Link to URI…** for linking to a web page or an app like OneNote or Evernote. These same options appear when you right-click an item and choose **Add Attachment**.

See `fig01.png`.

To open an attached file, double-click it in the center pane, or right-click and select **View PDF** / **View File**. To find the actual file on disk, right-click and choose **Show File**.

Zotero can also save **web snapshots** — offline copies of a page frozen at the moment you captured it. If the Connector doesn't recognize structured data on a page, clicking the save button will store it as a Web Page item with a snapshot. You can also right-click the Connector button and choose **Save to Zotero (Web Page with Snapshot)** to snapshot any page on demand.

See `fig02.png`.
