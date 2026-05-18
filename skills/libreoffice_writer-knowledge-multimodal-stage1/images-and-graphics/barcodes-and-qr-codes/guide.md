# Generating Barcodes and QR Codes (LibreOffice Writer 7.3.7)

Writer, Calc, Impress, and Draw can all generate barcodes and QR codes directly — no extensions needed. Barcodes are used for all sorts of purposes, and a QR code (Quick Response code) is simply a type of barcode. QR codes often contain data that points to a website or application.

To get started, go to **Insert > Object > QR and Barcode** on the menu bar. This opens the **QR and Barcode** dialog where you configure everything in one place.

See `fig01.png`.

In the **URL/Text** field, type whatever data you want encoded — a URL like `www.libreoffice.org`, an ISBN number, a product code, or any plain text. Next, pick an **Error correction** level (Low, Medium, Quartile, or High). Higher correction makes the code more resilient to damage or smudging but also more complex visually.

Set the **Margin** value to control the whitespace border around the generated graphic. Finally, use the **Type** dropdown to choose between **QR Code** and **Barcode**. Hit **OK** and Writer drops the generated graphic right into your document.

See `fig02.png` for the barcode example.

Once the code is in your document, it behaves like any other embedded object. You can click it to select it, drag the handles to resize it, or reposition it on the page. If you need to change the encoded data or settings after the fact, just right-click the code and select **Edit Barcode** — the same dialog reopens so you can tweak anything.
