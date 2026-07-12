# Navigating the 2D Map View (QGIS 3.44)

The map canvas is your central workspace — it renders all visible layers and responds to panning, zooming, and interaction from the **Navigation Toolbar** or the **View** menu.

To pan, grab the **Pan Map** tool and hold the left mouse button while dragging. You can also hold `Space` and move the mouse, or press the arrow keys. A single left-click re-centers the map on that point.

Zooming is flexible: roll the mouse wheel (add `Ctrl` for finer increments), or use **Zoom In** / **Zoom Out** to click-center at double/half scale. Drag a rectangle with either zoom tool to jump straight to that extent. Hold `Alt` while using one to temporarily swap to the other.

For quick resets, **Zoom Full** (`Ctrl+Shift+F`) fits all layers into view, while **Zoom to Layer(s)** and **Zoom to Selection** target what you've highlighted in the Layers panel. **Zoom Last** and **Zoom Next** let you step back and forward through your extent history like a browser.

If you're working with an active raster, **Zoom to Native Resolution** aligns one raster pixel to one screen pixel — handy for inspecting detail.

Right-click anywhere on the canvas to copy the clicked coordinate in the map CRS, WGS84, or a custom CRS — paste it into expressions, scripts, or a spreadsheet.

When things get heavy, press `Esc` to interrupt a long render mid-draw. For bulk layer setup, uncheck the **Render** checkbox in the bottom-right status bar to suspend all redraws until you're ready, then re-enable it for an immediate refresh.

You can also open additional synchronized views via **View → New Map View** — great for an overview-and-detail layout or comparing themes side by side.
