"""TC14: repeated failures trigger protection."""

def test_tc14_repeated_failures_trigger_account_protection(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    for _ in range(5):
        user = driver.find_element(*page.USERNAME)
        password = driver.find_element(*page.PASSWORD)
        user.clear(); user.send_keys("huongnt")
        password.clear(); password.send_keys("incorrect-password")
        driver.find_element(*page.SUBMIT).click()
    page_text = driver.find_element("tag name", "body").text.lower()
    assert any(term in page_text for term in ("captcha", "th? l?i", "kh?a", "locked", "too many")), \
        "Expected CAPTCHA, lockout, or retry protection after five failures"
