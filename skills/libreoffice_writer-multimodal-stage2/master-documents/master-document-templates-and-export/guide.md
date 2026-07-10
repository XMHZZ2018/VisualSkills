# Templates and Final Export (LibreOffice Writer 7.3.7)

A master document template saves you from rebuilding your structure every time you start a similar project. To create one, first set up the master document itself using **File > Send > Create Master Document** as you normally would, with all the subdocuments linked. Then go to **File > Templates > Save as Template** to store it as an `.otm` file. It'll show up in the Templates dialog alongside your regular templates. A quick tip: include something in the name that makes it obvious this is a master document template, not an ordinary one.

When you're ready to share or publish, you'll often want everything collapsed into a single file rather than a web of linked subdocuments. Open the master document, then go to **File > Export** on the Menu bar. In the Export dialog, give the file a name and pick **ODF Text Document (.odt)** as the format, then click **Export**. This produces a self-contained `.odt` with each subdocument written into its own write-protected section.

See `fig01.png`.

Open the newly exported `.odt` and break the protection so you can work with it freely. Head to **Format > Sections**, select the first item in the section list, then Shift+click the last to select them all. Deselect both **Link** in the Link section and **Protect** in the Write Protection section, then click **OK**. If you only need some sections, select the ones you don't want and hit **Remove** — the content stays, but the section markers disappear.

Images need a bit of extra attention in master documents. An image anchored "to page" in a subdocument will lose its anchor entirely once the master document reassembles page numbers and cross-references — it simply vanishes. Images anchored "to character" or "to paragraph," on the other hand, travel with the text and stay put regardless of how subdocuments shift around.

To fix an image's anchoring, right-click it and choose **Properties**. On the **Type** tab of the Image dialog, set the anchor to **To character** or **To paragraph**. Then adjust the horizontal and vertical positioning under *Position* to place it exactly where you want on the page, and click **OK**.

See `fig02.png`.
