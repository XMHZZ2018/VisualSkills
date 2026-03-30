# Inspect Network Requests

1. Open Chrome DevTools by pressing `Cmd+Option+I` (Mac) or `Ctrl+Shift+I` (Windows/Linux).
2. Click the **Network** tab in the DevTools panel.
3. Reload the page with `Cmd+R` (Mac) or `Ctrl+R` (Windows/Linux) to capture all requests from page load.
4. Watch the request list populate — each row is an HTTP request.
5. Click any request row to open its detail panel.
6. Click the **Headers** tab to view request/response headers, method, status code, and URL.
7. Click the **Preview** tab to see a formatted view of the response body.
8. Click the **Response** tab to see the raw response body.
9. Click the **Timing** tab to inspect how long each phase (DNS, connection, TTFB, download) took.
10. Use the filter bar at the top to search by URL keyword or filter by type: **XHR**, **JS**, **CSS**, **Img**, **WS**.
11. Click **XHR** in the filter bar to isolate API/AJAX requests only.
12. Right-click any request and select **Copy > Copy as cURL** to replay the request in a terminal.
13. Click the **Preserve log** checkbox to keep requests across page navigations.
14. Click the red **Record** button (circle icon) to stop/start capturing network activity.
15. Click **Clear** (the slash icon) to clear the current request log.
