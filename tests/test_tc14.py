"""TC14: repeated failures trigger protection."""

def test_tc14_repeated_failures_trigger_account_protection(driver, login_url):
    import os
    import pytest
    if os.getenv("RUN_TC14") != "1":
        pytest.skip("Set RUN_TC14=1 only for an approved test account and environment")
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    for _ in range(5):
        user = driver.find_element(*page.form.USERNAME)
        password = driver.find_element(*page.form.PASSWORD)
        user.clear(); user.send_keys(os.getenv("TEST_USERNAME", "huongnt"))
        password.clear(); password.send_keys("incorrect-password")
        driver.find_element(*page.form.SUBMIT).click()
    page_text = driver.find_element("tag name", "body").text.lower()
    assert any(term in page_text for term in ("captcha", "thử lại", "khóa", "locked", "too many")), \
        "Expected CAPTCHA, lockout, or retry protection after five failures"
