# Exporting to PDF (LibreOffice Writer 7.3.7)

LibreOffice Writer can export any document to PDF, which is handy when you need to share a file that looks the same everywhere. There are two ways to go about it: a quick one-click method, or a more detailed approach with full control over the output.

For a fast export, click the **Export Directly as PDF** icon on the Standard toolbar, or go to **File > Export As > Export Directly as PDF**. This uses whatever PDF settings you last configured and just asks for a filename and location — no fuss.

When you need more control, use **File > Export as > Export as PDF**. This opens the PDF Options dialog, which has six tabs: *General*, *Initial View*, *User Interface*, *Links*, *Security*, and *Digital Signatures*.

See `fig01.png`.

On the **General** tab, you pick which pages to export (all, a range, or just the selection), choose between lossless and JPEG image compression, and set the image resolution. You can also opt into PDF/A for archival, tagged PDF for accessibility, or embed a watermark across every page. Under *Structure*, turning on **Export outlines** gives readers a clickable table of contents in their PDF viewer.

The **Initial View** tab controls how the PDF looks when someone first opens it — whether it starts on a specific page, shows bookmarks or thumbnails in a side pane, and what magnification to use.

Over on the **User Interface** tab, you can hide the menu bar, toolbar, or window controls in the viewer, and even force the PDF to open in full-screen mode. These options are especially useful if you're building a kiosk-style or presentation PDF.

See `fig02.png`.

The **Links** tab determines how hyperlinks behave. You can export Writer outline levels as named destinations, convert references to other document formats (like .odt) into .pdf links, and choose whether cross-document links open in the PDF reader or in a web browser.

For locking things down, the **Security** tab lets you set an *open password* (required to view the PDF) and a *permissions password* (restricts printing, copying, or editing). Once a permissions password is set, you can fine-tune exactly what's allowed — for example, permitting high-resolution printing but blocking content copying.

See `fig03.png`.

Finally, the **Digital Signatures** tab lets you attach a certificate to prove the PDF hasn't been tampered with. Click **Select** to pick a certificate from your key store, enter the certificate password if needed, and optionally fill in location and contact info. The key store path is configured under **Tools > Options > LibreOffice > Security > Certificate Path**.

Once everything looks right, click **Export**, choose your filename, and you're done.
