"""TC17: logout prevents returning to protected page."""

def test_tc17_logout_and_browser_back_keep_user_signed_out(driver, login_url, credentials):
    from selenium.webdriver.common.by import By
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login(*credentials)
    page.wait_for_url_change(login_url)
    logout = driver.find_element(By.XPATH, "//a[contains(., '??ng xu?t') or contains(., 'Logout')] | //button[contains(., '??ng xu?t') or contains(., 'Logout')]")
    protected_url = driver.current_url
    logout.click()
    page.wait_for_url_change(protected_url)
    driver.back()
    assert login_url.rstrip("/") in driver.current_url.rstrip("/") or driver.current_url == login_url
