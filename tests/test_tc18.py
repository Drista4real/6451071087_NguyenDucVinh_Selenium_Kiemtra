"""TC18: long input does not break login page."""

def test_tc18_long_credentials_do_not_break_page(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("u" * 256, "p" * 256)
    assert driver.find_element("tag name", "body").is_displayed()
    assert "500" not in driver.title
    assert "server error" not in driver.page_source.lower()
