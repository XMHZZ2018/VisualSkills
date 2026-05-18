# Fonts, Colors, and Experimental Features (LibreOffice Writer 7.3.7)

## Adding custom fonts

LibreOffice supports PostScript (.pfb), TrueType (.ttf), and OpenType (.otf) font files. Your OS may support other formats too, but selection and quality can vary. If you have admin privileges, just install fonts through your operating system and they'll automatically show up in Writer's font lists.

Looking for free fonts? Sources like Adobe offer hundreds of free-licensed options you can use, share, and edit however you like. The League of Moveable Type and Font Library are also great places to browse. Many Linux distros ship a few free-licensed fonts in their package repositories as well.

## Adding custom colors

Sometimes you need an exact brand color that isn't in the default palette. The trick is to go through a drawing object. Drop any shape — a simple square works — into your document, then right-click it and choose **Area** from the context menu.

Head over to the **Color** tab. Under **Colors > Palette**, pick which palette you want to add your new color to. In the **New** section, define the color using RGB values or a Hex code, or click the **Pick** button to select it visually from the color chart.

See `fig01.png`.

Once you've got the color right, click **Add** in the lower-left corner, give it a name in the pop-up, and hit **OK** to save. After that, feel free to delete the drawing object — your custom color now lives in the palette and is available everywhere in Writer.

## Enabling experimental features

Writer has a handful of features tucked away behind an experimental flag. To turn them on, go to **Tools > Options > LibreOffice > Advanced** and check **Enable experimental features (may be unstable)** near the bottom of the *Optional Features* section. Fair warning: these features may be incomplete or buggy, and they can change between releases.

See `fig02.png`.

A couple of experimental goodies worth knowing about: the Sidebar gains two extra decks — *Manage Changes* and *Design* — and you get access to **Outline Folding** via **Tools > Options > LibreOffice Writer > View** (look for **Show outline-folding buttons**). With that enabled, a small arrow appears next to headings, letting you collapse all the text under a heading with a single click. If *Include sub levels* is also selected, clicking a heading folds everything down to the next same-level heading, subheadings and all.
