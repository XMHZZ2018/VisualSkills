# Adding Images to a Document (LibreOffice Writer 7.3.7)

Writer supports photos, drawings, scanned images, clip art, and charts — basically any graphic or image file you can throw at it. The most common raster formats (GIF, JPG, PNG, BMP) all work fine, and vector formats are supported too. Before you insert anything, think about whether the document will be printed in color or grayscale, and whether your images are at an appropriate resolution (72–96 dpi is plenty for screen-only documents).

**Drag and drop** is the quickest way to get an image in. Open a file browser, find your image, and drag it straight into the Writer document — a faint vertical line shows where it will land. This embeds a copy by default; hold **Ctrl+Shift** while dragging to link the file instead.

If you prefer a dialog, click where you want the image, then go to **Insert > Image** on the Menu bar (or click the **Insert Image** icon on the Standard toolbar). The Insert Image dialog lets you browse to the file and select it. Check **Preview** to see a thumbnail before committing, then click **Open**.

See `fig01.png`.

At the bottom of that dialog you'll notice a **Link** checkbox. When checked, Writer stores a reference to the file on disk rather than embedding a copy. This keeps your document small and means any external edits to the image show up automatically next time you open the file. The downside: if you move the document to another machine without the image files, they won't display.

To **copy and paste** an image, just copy it in any application (or another LibreOffice document), switch to your Writer document, click where you want it, and press **Ctrl+V** or use **Paste** from the context menu. Be aware that if the source application closes before you paste, the clipboard contents may be lost.

If you linked images but later decide you want them embedded, go to **Edit > Links to External Files**. The Edit Links dialog lists every linked file — select the ones you want, click **Break Link**, and confirm with **Yes**.

See `fig02.png`.

To go the other direction — converting an embedded image to a linked one — right-click the image, choose **Properties**, switch to the **Image** tab, and click the **Browse** button next to the **Link File name** field. Point it to the file on disk and click **Open**, then **OK**.

For **scanning directly into Writer**, make sure your scanner is connected, then choose **Insert > Media > Select Source** to pick the scanner device. Position your cursor where the image should go and run **Insert > Media > Scan > Request** to open the scanning software and pull the image straight in. You'll generally get better results scanning into a dedicated graphics app first and cleaning the image up before inserting it into Writer.

The **Gallery** sidebar (**View > Gallery** or the Gallery icon on the Sidebar) gives you quick access to reusable clip art, graphics, and sounds bundled with LibreOffice. You can drag objects from the Gallery directly into your document, or copy and link them as needed.
