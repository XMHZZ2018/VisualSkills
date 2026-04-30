# Interactive Navigation & Hyperlinks (LibreOffice Impress 7.3.7)

Impress lets you turn any shape, image, or text object into a clickable button that jumps to another slide, opens a document, or runs a macro — perfect for kiosk-style presentations where the audience navigates on their own.

**Adding a hyperlink to text.** Select the text you want to make clickable, then go to **Insert > Hyperlinks** on the Menu bar (or press **Ctrl+K**). The Hyperlink dialog has four types on the left: **Internet**, **Mail**, **Document**, and **New Document**. For slide-to-slide navigation, pick **Document**, leave the **Path** field empty (since you're linking within the same file), and click the target icon next to **Target** to browse and select a specific slide. Hit **Apply**, then **Close**.

Read the screenshot `fig01.png` in this directory — you will see the Hyperlink dialog with the Document page selected, showing Path and Target fields for linking to a specific slide.

**Tip:** If Impress is auto-converting typed URLs into hyperlinks and you don't want that, go to **Tools > AutoCorrect Options > Options** and deselect **URL Recognition**.

**Using interactions for shape-based navigation.** Interactions are the real workhorse for kiosk presentations — they let you assign a click action to any object, not just text. Select a shape, then either right-click and choose **Interaction**, click **Interaction** on the Line and Filling toolbar, or go to **Format > Interaction** on the Menu bar.

In the Interaction dialog, the **Action at mouse click** dropdown gives you options like **Go to first slide**, **Go to last slide**, **Go to next slide**, **Go to previous slide**, and **Go to page or object** (which lets you pick a specific slide from a target list). You can also choose **Go to document** to link to an external file, **Play audio** to trigger a sound, or even **Run macro**. Click **OK** to save.

Read the screenshot `fig02.png` in this directory — you will see the Interaction dialog with the Action at mouse click dropdown expanded, listing options like Go to first slide, Go to page or object, Play audio, and Run macro.

**Building a navigation bar.** A common pattern is to place a row of shapes on the master slide — "Home," "Next," "Back" buttons — each with a different interaction assigned. Since they live on the master slide, they appear on every slide automatically. Combine this with a custom slide show (**Slide Show > Custom Slide Show**) to control exactly which slides appear and in what order, giving you a fully non-linear, menu-driven presentation.

**Running the presentation.** Press **F5** to start from the first slide, or **Shift+F5** to start from the current one. You can also go to **Slide Show > Start from First Slide**. When slide transitions are set to **On mouse click**, the audience clicks your interactive shapes to navigate rather than advancing linearly.
