"""TC07: missing password validation."""

def test_tc07_missing_password(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    driver.find_element(*page.USERNAME).send_keys("huongnt")
    driver.find_element(*page.SUBMIT).click()
    message = page.error_text().lower()
    assert "m?t kh?u" in message or "password" in message
