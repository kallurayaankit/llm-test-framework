import os
import pytest
from playwright.sync_api import sync_playwright


def _headless() -> bool:
    """Headless by default; set HEADLESS=false locally to watch the browser."""
    return os.getenv("HEADLESS", "true").lower() != "false"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=_headless())
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()