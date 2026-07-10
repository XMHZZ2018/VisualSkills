# Restarting Page Numbering (LibreOffice Writer 7.3.7)

A typical printed book doesn't just number pages straight through from 1 to the end. You'll usually want no numbers on a cover page, lowercase roman numerals (i, ii, iii…) for front matter, and arabic numerals starting fresh at 1 for the body. Master documents can handle all of this — you just need to set up the right paragraph styles.

The trick is to define a paragraph style for the first heading of each chapter (or major section) that forces a page break and resets numbering. Start by picking the style your chapters begin with — usually **Heading 1** — and give it a companion style with the restart behavior baked in.

Open the Paragraph Style dialog for your Heading 1 style and go to the **Text Flow** tab. In the **Breaks** section, check **Insert**, set **Type** to *Page*, **Position** to *Before*, and tick **With page style** (choose **First Page** or whatever page style you want). Leave the **Page number** checkbox unchecked here — this way numbering just continues from the previous page, which is what you want for most chapters.

The Breaks section of the Text Flow tab in the Paragraph Style dialog for Heading 1 shows the **Insert** checkbox checked, **Type** set to *Page*, **Position** set to *Before*, and **With page style** checked with *First Page* selected from its dropdown. Below these options, the **Page number** checkbox is unchecked, with its spinner field showing the value 1.

Now, for the very first chapter — the one where you want numbering to restart at 1 — you need a separate style. Right-click **Heading 1** in the **Paragraph Styles** section of the Styles sidebar and select **New**. On the **Organizer** tab, name it something like *Heading 1 Chapter 1*, set **Inherit from** to *Heading 1*, and pick a category.

The Organizer tab of the Paragraph Style dialog shows the Style section with the **Name** field set to *Heading 1 Chapter 1*, an unchecked **AutoUpdate** checkbox, **Next style** set to *Text Body* with an adjacent Edit Style button, **Inherit from** set to *Heading 1* with its own Edit Style button, and **Category** set to *Custom Styles*.

Switch to the **Text Flow** tab for this new style. Set the same break options — **Insert**, **Type**: *Page*, **Position**: *Before*, **With Page Style**: *First Page* — but this time set **Page number** to **1**. That's what actually restarts the count.

Finally, check the **Outline & List** tab to make sure the **Outline level** is set to *Level 1*. You can assign it to an outline level through **Tools > Chapter Numbering** or directly on the **Outline & List** tab of the Paragraph Style dialog. This ensures the heading still appears in your Table of Contents alongside the other chapter headings.

Apply *Heading 1 Chapter 1* to the first chapter's heading, and use the regular *Heading 1* for every chapter after that. When you rebuild the master document, page numbering will restart exactly where you told it to — no manual page breaks needed.
