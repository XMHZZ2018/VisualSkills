# Using the Particles Effect (OpenToonz 1.7)

The Particles effect generates a new level of particles in your chosen column/layer — think rain, snow, sparkles, smoke, or a field of stars grown from a single animated element. Parameters are spread across five tabs in the FX Settings pane: **Source**, **Birth Params**, **Environment**, **Animation**, and **Colors**. A set of built-in presets is a great starting point if you want to reverse-engineer how things work.

See `fig01.png`.

To feed the effect an image, connect any column/layer node to the **Texture** port on the Particles effect node in the schematic. Each time you connect one, a new Texture port appears, so you can stack multiple particle sources. The particle inherits whatever animation or transforms are on that column — if your drawing spins, your particles spin too.

Control images let you steer parameters spatially. Connect a column/layer to a **Control** port on the effect node, then type that port's number into the relevant **Control Image** field in FX Settings (type **0** for none). Brightness in the control image maps to intensity — brighter pixels mean faster speed, larger size, longer lifetime, etc. Transparent areas read as black.

On the **Source** tab, set the spawn area with **Center**, **Width**, and **Height**, or skip those entirely and use a control image whose opaque regions define where particles appear. The **Birth Rate** controls how many particles spawn per frame (decimals work — 0.2 means one particle every five frames). Set **Starting Frame** to a negative number if you need the effect already "running" at frame 1, like a snowfall that shouldn't visibly ramp up.

See `fig02.png`.

Under **Birth Params**, each particle gets a randomly assigned speed, size, orientation, mass, and lifetime at the moment it's born. Min/max sliders give you the randomization range. Check **Linked to Scale** if you want bigger particles to move faster (a cheap depth-of-field cheat). The **Trail** setting stamps previous positions behind a moving particle, and **Top Layer** controls z-ordering — set it to **Smaller** for a convincing perspective stack.

The **Environment** tab is where external forces live. **Gravity** accelerates particles in a direction (0° = down, values rotate clockwise). Point a smoothly-gradated control image at the Gravity field and particles will drift toward bright areas like iron filings to a magnet. **Friction** opposes motion to slow or stop particles; **Wind** adds constant velocity without acceleration. **Scattering** injects random per-frame displacement — switch its mode to **Smooth** and set a **Swing** value for a gentle swaying motion instead of jitter.

See `fig03.png`.

On the **Animation** tab, **Rotation Speed** spins all particles uniformly (it's not a birth attribute, so animating it turns them all together). Add **Extra Speed** with **Smooth** swing mode for organic tumbling. Enable **Follow Particles Movement** to orient particles along their travel path — essential for arrows, rain streaks, or anything directional. **Opacity** fade-in/fade-out frames let particles materialize and dissolve gracefully, and **Size Increase** grows or shrinks them over their lifetime.

Finally, the **Colors** tab lets particles tint at birth, mid-life (fade-in), and death (fade-out) using color spectrums or a control image sampled at the particle's position. Crank the **Spread** value to randomize the RGB channels around your chosen hue for natural variation.
