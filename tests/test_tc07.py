"""TC07: missing password validation."""

def test_tc07_missing_password(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    driver.find_element(*page.form.USERNAME).send_keys(credentials[0])
    driver.find_element(*page.form.SUBMIT).click()
    message = page.form.error_text().lower()
    assert "mật khẩu" in message or "password" in message
