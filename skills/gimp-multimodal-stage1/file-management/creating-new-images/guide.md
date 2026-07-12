# Creating New Images (GIMP 2.10)

To start a blank canvas, go to **File > New…** or hit **Ctrl+N**. This opens the "Create a New Image" dialog where you set the dimensions, color mode, and other properties before GIMP hands you an empty image window.

See `fig01.png`.

At the top of the dialog you'll find a **Template** dropdown — a quick way to pick common presets (letter size, web banners, etc.) without typing values manually. If you have a size you reuse constantly, you can save your own template later via **File > Create Template…** from any open image that already has the dimensions you want.

Below the template selector, set your **Width** and **Height**. The default unit is pixels, but you can switch to inches, millimeters, or other units from the adjacent menu. Two small portrait/landscape buttons let you swap width and height with one click. Keep in mind that very large pixel dimensions eat memory fast — every filter and operation scales with total pixel count.

Click the triangle labeled **Advanced Options** to reveal resolution, color space, precision, and fill settings. **X and Y resolution** mainly affect print output; they won't change your pixel dimensions but determine how those pixels map to physical units. **Colorspace** lets you choose between RGB (the default for most work) and Grayscale. You can't create an indexed image directly here, but you can convert afterward with **Image > Mode > Indexed**.

See `fig02.png`.

**Precision** is where GIMP 2.10 shines — you can work in 8-bit, 16-bit, or 32-bit per channel (integer or floating point). Higher precision means smoother gradients and more editing headroom, especially useful if you plan heavy color grading. For the **Fill with** option, pick from Foreground, Background, White, Transparency, or Pattern to set what your fresh canvas starts with. Choosing Transparency adds an alpha channel automatically.

Finally, you can attach a **Comment** to the image metadata — some formats like PNG and JPEG will preserve it on export. Once everything looks right, hit **OK** and your new image appears ready for work.
