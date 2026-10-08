"""TC16: protected home redirects to login."""

def test_tc16_direct_home_access_redirects_to_login(driver, login_url):
    import os
    home_url = os.getenv("HOME_URL", "https://vanphongdientu.utc.edu.vn/trang-chu")
    driver.get(home_url)
    assert "/login" in driver.current_url.lower(), "Unauthenticated visit was not redirected to login"
