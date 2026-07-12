# Configuring Global Options (QGIS 3.44)

Everything application-wide lives in one place: **Settings > Options**. The dialog is tabbed along the left side — General, System, CRS and Transforms, Data Sources, Rendering, and so on. Changes are saved to your active user profile and apply to every new project you open under that profile. Some changes (like UI theme or widget style) require a restart before they take effect.

See `fig01.png`.

In the **General** tab, the *Override System Locale* group lets you force a specific language and number/date format regardless of your OS settings. Below that, the *Application* section controls cosmetics: widget style, UI theme ("default", "Night Mapping", or "Blend of Gray"), icon size, and font. You can also hide the splash screen, toggle the news feed on the welcome page, and set how long timed messages linger.

The *Project Files* section is where you decide what happens at launch — show the Welcome Page, open the most recent project, or always start fresh. You can designate a default project template, choose between QGZ (archive with auxiliary data embedded) and QGS (plain text) as your default format, and control whether paths are stored as absolute or relative. The "Enable macros" dropdown is worth setting to "Ask" so you don't accidentally run untrusted embedded Python.

Over on the **System** tab, you can register additional SVG paths, plugin directories, and documentation URLs. The *Environment* section is especially handy on macOS where GUI apps don't inherit shell variables — enable "Use custom variables," then add entries with an Apply method like Overwrite, Prepend, Append, or If Undefined. A read-only table below shows all current environment variables for verification.

See `fig02.png`.

The **CRS and Transforms** tab governs how new projects get their coordinate reference system — either from the first layer added or from a fixed default you choose. For layers loaded without CRS metadata, you can tell QGIS to leave them as unknown, prompt you, or silently assign the project or default CRS. The *Coordinate Transforms* sub-tab lets you predefine datum transformations so you're not prompted every time two systems interact.

Under **Rendering**, you control map refresh intervals, maximum CPU cores for rendering, and whether new layers auto-display on the canvas. The vector sub-tab offers feature simplification (faster draws at the cost of geometric precision), while the raster sub-tab configures resampling methods and contrast enhancement algorithms.

The **Network** tab is critical behind corporate firewalls. Set your proxy type (HTTP, SOCKS5, or system default), host, port, and exclusion list. You can also tune request timeouts, WMS cache expiration, and the on-disk cache size. For authentication, the dedicated **Authentication** tab manages PKI certificates and stored credentials used across connections.

Other tabs worth knowing: **Canvas & Legend** sets map background color and double-click behavior in the layer tree; **Map Tools** configures measurement units, identify-tool highlight appearance, and predefined scales; **Colors** and **Fonts** let you manage global palettes and font replacements across operating systems; **Variables** exposes global-level expression variables you can add or remove at will.
