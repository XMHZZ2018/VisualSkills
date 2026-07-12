# Setting Up a Color-Managed Workflow (GIMP 2.10)

Every device in your pipeline — camera, monitor, printer — sees color differently. ICC profiles act as translators, mapping each device's quirks to a shared reference space so what you edit is what you get.

Open **Edit > Preferences** and head to the **Color Management** section. Set your RGB working space to sRGB (the default and safest bet for most work). If you have an ICC profile for your monitor — from a calibration tool like a Spyder or i1 — assign it here as the Monitor Profile. This is what makes your display show accurate color rather than guessing.

When you open an image that has an embedded profile, GIMP pops up a dialog asking whether to **Convert** it to your working space or **Keep** the original profile. For most editing, hit **Convert** — this translates the pixel values into sRGB so your adjustments behave predictably. If you're handing the file off untouched, **Keep** preserves the original intent.

You can manage profiles on any open image via **Image > Color Management**. From there you can assign a profile (reinterprets colors without changing pixel data), convert to a profile (remaps pixel values to match a new space), or discard and save profiles as needed. Leave **Enable Color Management** checked — always. Unchecking it silently reassigns a built-in sRGB profile, which mangles colors if your image was in a wider gamut.

For print work, activate Soft Proof mode through **View > Display Filters** and load your printer's ICC profile. This simulates on screen how the print will look, flagging out-of-gamut colors before you waste ink. Correct those problem areas while you can still see them.
