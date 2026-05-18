# Adding Captions to Images (LibreOffice Writer 7.3.7)

There are three ways to caption images in Writer: automatic captions, the Caption dialog, or doing it manually. Each has its place depending on how much control you need.

## Automatic captions

If you want every image you insert to get a caption automatically, head to **Tools > Options > LibreOffice Writer > AutoCaption**. On the right side of the dialog, pick which object types get captions and configure the sequence name, numbering style, and separator. From then on, whenever you insert an image, Writer wraps it in a frame with a caption area ready for your text.

To fine-tune what gets auto-captioned — say you only want it for images, not tables — check or uncheck the relevant entries under **Add captions automatically when inserting**. Make sure **LibreOffice Writer Image** is selected if images are what you're after. You can even type a custom category name (like *Photo*) into the Category box; Writer will create a new numbering sequence for it.

## Using the Caption dialog

For one-off captions, select your image, then right-click and choose **Insert Caption** from the context menu (or use **Insert > Caption** from the menu bar). In the dialog, set the **Category**, **Numbering**, and **Separator** fields to your liking — for example, *Figure*, *Arabic (1 2 3)*, and a colon. Type your caption text in the **Caption** box at the top; the preview at the bottom shows the full assembled label. Hit **OK** and the image plus caption land in a frame together.

See `fig01.png`.

## Numbering by chapter

Click the **Options** button inside the Caption dialog to access chapter-based numbering. Use the **Level** field to tie caption numbers to your outline headings — so figures restart at each chapter (e.g., Figure 1.1, Figure 2.1). The **Separator** field here controls what sits between the chapter number and the figure number. You can also set a **Character style** for the caption and toggle **Apply border and shadow** for framed captions.

See `fig02.png`.

## Adding captions manually

If you export to other formats, auto-generated captions sometimes get lost. A manual approach avoids that. The simplest way: place the image and its caption in separate paragraphs. Anchor the image to its paragraph, press **Enter** to create a new line below, and type something like "Figure " followed by an auto-number. To insert that number, click **Insert > Field > More Fields** (or press **Ctrl+F2**), go to the **Variables** tab, select **Number range** as the type, pick **Figure** in the Select list, choose your format, and click **Insert**. The running number appears inline, and you just type your caption text after it.

Alternatively, you can place the image and caption inside a table for tighter layout control — but for most documents, the paragraph method works great.
