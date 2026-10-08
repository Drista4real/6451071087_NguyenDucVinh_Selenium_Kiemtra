"""Shared browser fixtures for the UTC login acceptance suite."""
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()

@pytest.fixture
def login_url():
    url = os.getenv("LOGIN_URL")
    if not url:
        pytest.skip("Set LOGIN_URL to the UTC login page before running browser tests")
    return url
