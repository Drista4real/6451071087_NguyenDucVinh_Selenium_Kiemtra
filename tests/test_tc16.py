"""TC16: protected home redirects to login."""

def test_tc16_direct_home_access_redirects_to_login(driver, login_url):
    import os
    home_url = os.getenv("HOME_URL")
    if not home_url:
        import pytest
        pytest.skip("Set HOME_URL to the protected internal page")
    driver.get(home_url)
    assert driver.current_url.rstrip("/") == login_url.rstrip("/")
