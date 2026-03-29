---
name: chrome-knowledge
description: Comprehensive guide for Chrome browser tasks — settings, bookmarks, extensions, privacy, downloads, and more
---

# Chrome Knowledge

Reference guide for performing common Chrome browser tasks.

## Settings & Preferences

### Change Chrome Interface Language

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings** (third option from the bottom of the menu).
3. In the left sidebar, click **Languages** (or scroll to the bottom of the Settings page and click **Advanced**, then find the **Languages** section).
4. Under the **Language** subsection, click **Add languages**.
5. In the dialog, search for and check the desired language (e.g., "English (United States)"), then click **Add**.
6. Back in the language list, click the three-dot menu next to the newly added language.
7. Select **Display Google Chrome in this language** (the first option in the menu).
8. A **Relaunch** button appears at the top of the language section. Click it to restart Chrome.

#### Verification
After relaunch, the entire Chrome interface (menus, settings labels, sidebar) displays in the selected language.

---

### Change Chrome Profile Name

#### Steps
1. Open Chrome and click the **profile icon** in the top-right corner (next to the three-dot menu).
2. In the profile dropdown, click **Customize profile**.
3. The **Customize profile** page opens at `chrome://settings/manageProfile`.
4. In the **Name your Chrome profile** text field, clear the existing name and type the new name.
5. The change saves automatically — no confirmation button is needed.

#### Verification
The profile icon area and profile dropdown now display the updated name.

---

### Change Default Font Size

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Appearance** (or navigate to `chrome://settings/appearance`).
4. Locate the **Font size** dropdown (default is "Medium (Recommended)").
5. Click the dropdown and select the desired size: Very small, Small, Medium (Recommended), Large, or Very large.

#### Verification
Open any webpage — text renders at the newly selected font size.

---

### Change Number of Google Search Results Per Page

#### Steps
1. Perform any Google search in Chrome.
2. Click the address bar to edit the URL.
3. Press the **End** key (Windows) or **Fn + Right Arrow** (Mac) to jump to the end of the URL.
4. Append `&num=50` (or any number between 1 and 100) to the end of the URL.
5. Press **Enter** to reload the page.

#### Verification
The search results page now displays the specified number of results (e.g., 50) instead of the default 10. This parameter persists for subsequent pages of results.

---

### Make Bing the Default Search Engine

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Search engine** (or navigate to `chrome://settings/searchEngines`).
4. In the **Search engine used in the address bar** dropdown, select **Bing**.

#### Verification
Type a search query in the address bar and press Enter. Results now appear on bing.com instead of google.com.

---

### Remove or Change Startup Page

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **On startup** (or navigate to `chrome://settings/onStartup`).
4. Three options are available:
   - **Open the New Tab page** — Chrome opens a blank new tab.
   - **Continue where you left off** — Chrome reopens all tabs from the previous session.
   - **Open a specific page or set of pages** — Click **Add a new page**, enter the URL, and click **Add**. To remove an existing startup page, click the three-dot menu next to it and select **Remove**.

#### Verification
Close and reopen Chrome. The browser starts with the configured page(s).

---

### Disable Dark Mode (via Extension)

#### Steps
1. Open Chrome and navigate to the **Chrome Web Store** (search "chrome store" in Google or go to `https://chromewebstore.google.com`).
2. Search for **"Dark Mode"** in the Web Store search bar.
3. Select the **Dark Mode** extension (described as "A global dark theme for the web") from the results.
4. Click **Add to Chrome**, then click **Add extension** in the confirmation dialog.
5. Click the **Extensions** (puzzle piece) icon in the toolbar and click the **pin** icon next to Dark Mode to pin it to the toolbar.
6. Click the pinned **Dark Mode** icon to toggle dark mode on or off for any webpage.

#### Verification
Clicking the Dark Mode icon toggles the page theme between dark and light modes.

---

### Disable Chrome Refresh 2023 UI (Command Line Flag)

#### Steps
1. Copy the command line flag: `--disable-features=CustomizeChromeSidePanel`
2. Close all Chrome windows completely.
3. Right-click any Chrome shortcut (desktop, Start menu, or taskbar) and select **Properties**.
4. In the **Shortcut** tab, locate the **Target** field.
5. Place the cursor after the closing quotation mark of the chrome.exe path, add a space, and paste the flag.
   - Example: `"C:\Program Files\Google\Chrome\Application\chrome.exe" --disable-features=CustomizeChromeSidePanel`
6. Click **Apply**, then **OK**.
7. Launch Chrome using this modified shortcut.

#### Verification
Chrome opens with the older pre-Refresh 2023 UI style (classic toolbar buttons, side panel button reverted). To reverse, repeat the steps and delete the flag from the Target field.

---

## Bookmarks & Tabs

### Bookmark a Page to the Bookmarks Bar

#### Steps
1. Navigate to the page you want to bookmark.
2. Click the **star icon** on the right side of the address bar.
3. In the **Bookmark added** dialog:
   - Edit the **Name** field if desired.
   - Set the **Folder** dropdown to **Bookmarks Bar**.
4. Click **Done**.
5. If the bookmarks bar is not visible, enable it: click the three-dot menu > **Bookmarks and lists** > **Show Bookmarks Bar** (keyboard shortcut: **Ctrl+Shift+B** on Windows/Linux, **Cmd+Shift+B** on Mac).

#### Verification
The bookmark appears on the bookmarks bar below the address bar and is accessible from any tab.

---

### Create a Bookmark Folder on the Bookmarks Bar

#### Steps
1. Ensure the bookmarks bar is visible (Ctrl+Shift+B to toggle).
2. Right-click on the bookmarks bar.
3. Select **Add folder** from the context menu.
4. In the **New Folder** dialog, type a name for the folder (e.g., "Quick Tips").
5. Confirm the location is set to **Bookmarks Bar**.
6. Click **Save**.
7. To add bookmarks to the folder, drag existing bookmarks from the bookmarks bar into the folder, or when bookmarking a new page, select the folder from the Folder dropdown in the bookmark dialog.

#### Verification
The folder icon appears on the bookmarks bar. Clicking it shows a dropdown with the contained bookmarks.

---

### Restore Last Closed Tab

#### Steps

**Method 1 — Keyboard shortcut:**
1. Press **Ctrl+Shift+T** (Windows/Linux) or **Cmd+Shift+T** (Mac).
2. The most recently closed tab reopens. Repeat to restore additional closed tabs in reverse order.

**Method 2 — Three-dot menu:**
1. Click the three-dot menu (top-right corner).
2. Hover over **History**.
3. Under **Recently closed**, click the tab you want to restore.
4. To restore an entire closed window, click **Restore window** (listed with a count of tabs).

**Method 3 — Auto-restore all tabs on startup:**
1. Go to **Settings** > **On startup** (or `chrome://settings/onStartup`).
2. Select **Continue where you left off**.

#### Verification
The previously closed tab(s) reappear with their full content and history intact.

---

## Privacy & Security

### Auto-Delete Browsing Data When Closing Chrome

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Privacy and security**.
4. Click **Site settings**.
5. Scroll down and click **On-device site data** (near the bottom of the list).
6. Under **Default behavior**, select **Delete data sites have saved to your device when you close all windows**.

#### Verification
The radio button for auto-delete is selected (blue). After closing all Chrome windows and reopening, cookies and site data from the previous session are cleared (you will be logged out of websites).

---

### Clear Specific Website Cookies

#### Steps
1. Open Chrome and press **Ctrl+Shift+Delete** (keyboard shortcut), or click the three-dot menu > **More tools** > **Clear browsing data**.
2. The **Clear browsing data** dialog opens on the **Basic** tab.
3. Set the **Time range** dropdown (options: Last hour, Last 24 hours, Last 7 days, Last 4 weeks, All time).
4. Check or uncheck the desired categories:
   - **Browsing history**
   - **Cookies and other site data**
   - **Cached images and files**
5. Click **Clear data**.

#### Verification
After clearing, previously stored cookies for the selected time range are removed. You may need to re-login to websites.

---

### Enable Do Not Track

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Privacy and security**.
4. Click **Third-party cookies** (or navigate to `chrome://settings/cookies`).
5. Scroll down to the **Advanced** section.
6. Toggle on **Send a "Do Not Track" request with your browsing traffic**.
7. A confirmation dialog appears explaining that websites may or may not honor the request. Click **Confirm**.

#### Verification
The toggle is switched on (blue). Note: this sends a request header to websites but compliance is voluntary.

---

### Enable Safe Browsing (Enhanced Protection)

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Privacy and security**.
4. Click **Security**.
5. Under **Safe Browsing**, three options are displayed:
   - **Enhanced protection** — proactive protection, password breach warnings, sends URLs to Google for checking.
   - **Standard protection** — default level, warns about known dangerous sites.
   - **No protection (not recommended)** — disables Safe Browsing entirely.
6. Select **Enhanced protection**.

#### Verification
The Enhanced protection radio button is selected (blue) and its feature list is expanded below it.

---

## Extensions

### Install an Unpacked Extension

#### Steps
1. Obtain the extension source files (e.g., download a zip file and extract it to a folder).
2. Open Chrome and navigate to `chrome://extensions` (or click the three-dot menu > **Extensions** > **Manage Extensions**).
3. Toggle on **Developer mode** (switch in the top-right corner of the extensions page).
4. Three new buttons appear: **Load unpacked**, **Pack extension**, and **Update**.
5. Click **Load unpacked**.
6. In the file picker dialog, navigate to and select the extracted extension folder, then click **Select Folder**.
7. The extension card appears on the extensions page with its name, version, and ID.

#### Verification
The extension is listed on `chrome://extensions` with its toggle enabled. Open a new tab to confirm the extension functions as expected. Click **Errors** on the extension card to check for any issues.

---

## Downloads & Shortcuts

### Save a Webpage as PDF (Using GoFullPage Extension)

#### Steps
1. Open Chrome and navigate to the **Chrome Web Store** (`https://chromewebstore.google.com`).
2. Search for **"GoFullPage"** (or "Full Page Screen Capture").
3. Click on **GoFullPage - Full Page Screen Capture** in the results.
4. Click **Add to Chrome**, then **Add extension**.
5. Navigate to the webpage you want to save as PDF.
6. Click the **GoFullPage** extension icon (camera icon) in the toolbar.
7. The extension captures the entire page and displays a preview.
8. Click the **Download PDF** button in the top-right area of the capture preview.
9. Accept any permission dialogs. The PDF downloads to your default downloads folder.

#### Verification
Open the downloaded PDF file — it contains the full webpage content rendered as a PDF document.

---

### Create a Desktop Shortcut for a Website

#### Steps
1. Open Chrome and navigate to the desired website.
2. Resize the Chrome window so the desktop is visible behind it (click the Restore Down button or drag the window edges).
3. In the address bar, locate the small **site icon** (favicon) to the left of the URL.
4. Click and drag the site icon from the address bar onto the desktop.
5. Release the mouse button to drop the shortcut.

#### Verification
A new shortcut icon appears on the desktop. Double-clicking it opens Chrome and navigates to the website.

---

## Passwords

### View Saved Passwords

#### Steps
1. Open Chrome and click the three-dot menu (top-right corner).
2. Click **Settings**.
3. In the left sidebar, click **Autofill and passwords** (or **Autofill** in older versions).
4. Click **Password Manager** (or navigate to `chrome://settings/passwords`).
5. Under **Saved Passwords**, a list of sites with stored credentials is displayed.
6. Click on any entry to view its details.
7. Click the **eye icon** (show password) next to the password field to reveal the password. You may be prompted to enter your computer's login password or use biometric authentication.
8. Click the **copy icon** next to the username or password to copy it to the clipboard.

#### Verification
The password is displayed in plain text. The detail view also shows options to **Edit** or **Delete** the saved credential.

---

## Google Services in Chrome

### Use Google Flights to Find Flights

#### Steps
1. Navigate to `https://www.google.com/travel/flights` in Chrome.
2. **Set departure:** Type a city name (e.g., "New York") to include all nearby airports, or type a specific airport code. Use the **+** icon to add multiple departure airports.
3. **Set destination:** Type a city, country, region, or continent. Leave it blank to explore all destinations on the map.
4. **Set dates:** Click the date fields to open the calendar. Browse month by month to see price overlays on each date. Set trip length for round trips.
5. **Apply filters:** Click **Filters** to set:
   - **Stops** — select Nonstop, 1 stop, etc.
   - **Duration** — set maximum flight duration.
   - **Airlines** — exclude or include specific airlines.
   - **Bags** — filter by carry-on or checked bag inclusion.
6. **Review results:** Check the **Cheapest** tab for lowest prices. Look for crossed-out bag icons indicating fares without carry-on bag access.
7. **Use the Price Graph:** Click the **Price graph** tab to see price trends for the route over time.
8. **Set price alerts:** Toggle the price tracking option for your route to receive email notifications when prices change.

#### Tips
- Search for one person at a time — group searches may show higher prices if not all seats are available at the cheapest fare class.
- Book directly with the airline rather than through third-party travel agents for better support during delays or cancellations.
- Check credit card travel portals for potentially better prices or points earning.
- Recommended booking windows: 1-3 months ahead for domestic, 2-8 months ahead for international flights.

#### Verification
Flight results display with prices, durations, stops, and CO2 emissions. Clicking a result shows booking options from multiple providers.
