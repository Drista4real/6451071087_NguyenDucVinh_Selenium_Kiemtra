"""TC06: missing username validation."""

def test_tc06_missing_username(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    driver.find_element(*page.form.PASSWORD).send_keys("1256")
    driver.find_element(*page.form.SUBMIT).click()
    message = page.form.error_text().lower()
    assert "tên đăng nhập" in message or "username" in message
