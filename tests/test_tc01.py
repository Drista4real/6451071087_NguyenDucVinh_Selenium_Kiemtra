"""TC01: valid click login."""

def test_tc01_valid_login_by_click(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    old_url = driver.current_url
    page.login(*credentials)
    page.wait_for_url_change(old_url)
    assert not driver.find_elements(*page.form.USERNAME), "Login form is still visible after sign-in"
