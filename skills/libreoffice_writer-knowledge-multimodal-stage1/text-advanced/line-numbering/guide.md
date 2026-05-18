# Line Numbering (LibreOffice Writer 7.3.7)

Line numbers in the margin are handy for legal documents, poetry, or code listings. Writer can number an entire document or just selected paragraphs, and the numbers show up when you print.

To turn on line numbering for the whole document, go to **Tools > Line Numbering** and check **Show numbering** in the top-left corner of the dialog. Hit **OK** and you're done — every line gets a number.

See `fig01.png`.

From that same dialog you can tweak quite a bit. The **Interval** field controls how often numbers appear (every line, every 5th, every 10th — whatever you like). **Position** sets which margin the numbers sit in, and **Spacing** adjusts the gap between the number and the text. You can pick a **Character style** to change how the numbers look, and choose a **Format** (1, 2, 3 or i, ii, iii, etc.). Under **Count**, you'll find options to skip blank lines, lines in text frames, or header/footer lines, and you can choose whether numbering restarts on each new page.

If you want a visual separator between groups of lines, fill in the **Separator** section — pick some text (a short dash, say) and set how often it appears.

To disable line numbering for the whole document, edit the *Default Paragraph Style*. Open the **Styles** pane in the Sidebar, right-click **Default Paragraph Style**, choose **Modify**, go to the **Outline & List** tab, and deselect **Include this paragraph in line numbering**. Click **OK**.

See `fig02.png`.

To enable numbering for only specific paragraphs, first disable it document-wide as described above, then select the paragraphs you want numbered. Open **Format > Paragraph** (or right-click and choose **Paragraph > Paragraph**), go to the **Outline & List** tab, and check **Include this paragraph in line numbering**. You can also disable numbering for individual paragraphs the same way — just deselect that checkbox.

If you need numbering to start at a specific value, click in the target paragraph, open the **Outline & List** tab again, make sure **Include this paragraph in line numbering** is selected, then check **Restart at this paragraph** and type the starting number in the **Start with** box.
