from playwright.sync_api import sync_playwright
import hashlib


def check_availability():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # TODO: replace with full Marriott booking flow navigation
        page.goto("https://www.marriott.com")

        content = page.content()

        browser.close()

    fingerprint = hashlib.sha256(content.encode()).hexdigest()

    return {
        "status": "UNKNOWN",
        "fingerprint": fingerprint,
        "notes": "Stub run, no parsing yet"
    }
