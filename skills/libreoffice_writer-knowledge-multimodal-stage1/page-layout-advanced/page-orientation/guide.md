# Changing Page Orientation Within a Document (LibreOffice Writer 7.3.7)

A document can contain pages in more than one orientation — a common scenario is slipping a landscape page into the middle of a portrait document for a wide table or chart. The trick is that orientation lives in a *page style*, so you need a Landscape page style and then tell Writer where to switch to it and back.

## Setting up a Landscape page style

Open the Styles deck in the Sidebar, right-click **Landscape** in the list of page styles, and choose **Modify**. On the *Organizer* tab of the Page Style dialog, make sure **Next Style** is set to **Landscape** — this lets you have several landscape pages in a row without Writer flipping back to portrait after the first one.

See `fig01.png`.

Now switch to the *Page* tab and confirm the **Orientation** is set to **Landscape**. While you're here, adjust the margins so they correspond to the portrait page's margins, just rotated: the portrait top margin becomes the landscape left margin, and so on. Click **OK** to save.

See `fig02.png`.

## Applying the landscape style in your document

Place your cursor in the paragraph or table at the start of the page you want in landscape. Right-click and choose **Paragraph > Paragraph** or **Table Properties** from the context menu. Go to the *Text Flow* tab, select **Insert** (or **Break** for a table) and tick **With Page Style**, then set the page style to **Landscape**. Click **OK** and that page — and everything after it — will be landscape.

To switch back to portrait, position the cursor in the paragraph where portrait should resume. Open the same **Text Flow** settings again, insert a break **With Page Style**, and this time pick the portrait page style that was in use before the landscape section. Click **OK**.

See `fig03.png`.

## Portrait headers and footers on landscape pages

If your landscape pages sit between portrait pages and the document will be printed, you probably want headers and footers aligned with the portrait pages — rotated 90° on the landscape sheet so everything looks consistent when bound. Writer can't do this natively through the page style, but you can fake it with frames: copy the header or footer text from a portrait page, paste it into the landscape page, rotate it via **Format > Character** on the *Position* tab (set **Rotation / Scaling** to **270 degrees**), then wrap it in a frame (**Insert > Frame > Frame**) sized and positioned to match the portrait page's header or footer area.
