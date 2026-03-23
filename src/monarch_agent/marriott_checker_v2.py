from playwright.sync_api import sync_playwright
import hashlib


def is_target_room(name: str, terms: tuple[str, ...]) -> bool:
    name = name.lower()
    return any(term in name for term in terms)


def check_availability(window, config):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(config.property_url)
        page.wait_for_timeout(4000)

        # NOTE: This is intentionally a soft parse until we lock selectors
        text = page.inner_text("body")

        browser.close()

    found_terms = [t for t in config.target_room_terms if t in text.lower()]

    status = "NOT_AVAILABLE"
    if found_terms:
        status = "POSSIBLE_MATCH"

    fingerprint = hashlib.sha256((text[:2000]).encode()).hexdigest()

    return {
        "check_in": window.check_in,
        "check_out": window.check_out,
        "status": status,
        "matches": found_terms,
        "fingerprint": fingerprint,
    }
