"""TC15: SQL injection payload is rejected."""

def test_tc15_sql_injection_does_not_bypass_login(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("' OR '1'='1", "' OR '1'='1")
    assert driver.find_elements(*page.form.USERNAME), "SQL payload unexpectedly left the login page"
    assert page.form.error_text()
