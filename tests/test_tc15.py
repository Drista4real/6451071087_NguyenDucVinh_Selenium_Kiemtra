"""TC15: SQL injection payload is rejected."""

def test_tc15_sql_injection_does_not_bypass_login(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("' OR '1'='1", "' OR '1'='1")
    assert driver.current_url == login_url
    assert page.error_text()
