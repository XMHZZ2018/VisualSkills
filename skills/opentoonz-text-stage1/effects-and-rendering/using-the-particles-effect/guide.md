# Using the Particles Effect (OpenToonz 1.7)

The Particles effect generates rain, snow, smoke, sparkles, or any repeated element from a source image. Parameters are organized across five tabs in the **Fx Settings** pane: **Source**, **Birth Params**, **Environment**, **Animation**, and **Colors**. Built-in presets are a great starting point — tweak from there.

**Setting up particle images:** Link any column/layer node to the **Texture** port on the Particles effect node in the schematic. Each connection opens a new Texture port, so you can feed in multiple source drawings. The particle inherits the column's animation and transformations — if your source spins, the particles spin too.

**Control images** let external artwork drive parameters like source area, speed, or gravity. Connect a column/layer to a **Control** port on the Particles node, then in **Fx Settings**, type that port's number into the relevant Control Image field (type **0** for none). Brightness in the control image maps to parameter intensity; transparent areas count as black.

**Source tab** defines where particles spawn. Set **Center** (X/Y), **Width**, and **Height** for a geometric region, or use a control image to confine birth to its opaque areas. Under Particle Generation, **Birth Rate** controls how many particles appear per frame (decimals work — 0.2 means one every five frames). Use a negative **Starting Frame** to let an effect "pre-roll" before frame 1, so a snowfall already looks full on the first visible frame.

**Birth Params** assigns each particle its lifetime traits. **Speed** and **Speed Angle** (0° = up, clockwise from there) set initial motion. **Size** is a percentage of original (randomized between min/max). **Orientation** rotates the texture, **Mass** matters when gravity is active, and **Lifetime** (in frames) determines when particles vanish. The **Trail** setting duplicates previous positions for a comet-tail look — adjust **Step** to thin it out. **Top Layer** controls z-order: Younger, Older, Smaller, Bigger, or Random.

**Environment tab** adds external forces. **Gravity** accelerates particles (angle 0° = down); point a control image at it and particles gravitate toward bright regions instead. **Friction** opposes motion — crank it high to stop particles dead in a bright area. **Wind** adds constant velocity (no acceleration) at a given angle. **Scattering** introduces random jitter per frame; switch **Swing Mode** to **Smooth** for gentler oscillation over the frame count you set.

**Animation tab** transforms particles over their lifespan. **Rotation Speed** spins all particles uniformly (not a birth attribute), while **Extra Speed** adds per-particle randomness. Enable **Follow Particles Movement** to orient textures along their trajectory. **Opacity** fade-in/fade-out ramps transparency at birth and death over a set frame count. **Size Increase** scales particles each frame — positive grows, negative shrinks.

**Colors tab** tints particles at three life stages. Define a color spectrum (or use a control image) for **Birth Color**, **Fade-in Color**, and **Fade-out Color**, each with its own intensity, spread, and frame range. Enabling **Pick Control Image's Color for Every Frame** re-samples color at the particle's current position rather than locking it at birth.
