# Creating an Image Map (LibreOffice Writer 7.3.7)

An image map lets you define clickable regions — called hotspots — on top of an image. Each hotspot acts like a graphical hyperlink: clicking it can open a web address, jump to another part of the same document, or open a file on your computer. You can place several hotspots of different shapes on a single image, which is handy for things like interactive diagrams or navigation graphics.

To get started, select the image you want to work with in your Writer document, then go to **Tools > ImageMap** on the menu bar. This opens the ImageMap Editor, which shows your image in the main area along with a toolbar across the top.

See `fig01.png`.

Draw your hotspot regions using the shape tools in the toolbar — **Rectangle**, **Ellipse**, **Polygon**, and **Freeform Polygon**. They work just like the shapes in the Drawing toolbar: click and drag on the image to define the area. A hotspot is outlined so you can see its shape. If you need to fine-tune a polygon, select it and use **Edit Points** to adjust individual vertices. **Move**, **Insert**, and **Delete Points** are also available for reshaping.

Once you've drawn a hotspot, fill in the fields below the toolbar. The **Address** field takes the URL or target the hotspot should link to — for an anchor within the same document, use the format `file:///path/document_name#anchor_name`. The **Text** field sets the tooltip that appears when the cursor hovers over the hotspot. **Frame** controls where the link opens: `_self` keeps it in the current window, `_blank` opens a new one, and `_top` or `_parent` work with framed pages. In most cases, `_self` is the right choice.

A few more toolbar buttons worth knowing: **Active** toggles whether a selected hotspot is enabled or disabled, **Macro** lets you attach a macro instead of a simple link, and **Properties** opens the hyperlink properties for the hotspot and adds a Name attribute.

Use **Undo** and **Redo** if you make a mistake. When everything looks right, click **Apply** to write the image map into your document. If you want to save the map to a separate file for reuse, click **Save**. You're done — close the dialog and test your hotspots by Ctrl-clicking them in the document.
