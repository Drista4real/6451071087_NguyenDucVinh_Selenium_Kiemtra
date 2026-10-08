"""TC05: empty username and password."""

def test_tc05_empty_credentials_show_validation(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    driver.find_element(*page.form.SUBMIT).click()
    message = page.form.error_text()
    assert message, "Expected a validation message for empty credentials"
    assert "??ng nh?p" in message.lower() or "m?t kh?u" in message.lower() or "username" in message.lower()
