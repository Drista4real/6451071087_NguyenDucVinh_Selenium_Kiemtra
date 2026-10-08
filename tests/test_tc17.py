"""TC17: logout prevents returning to protected page."""

def test_tc17_logout_and_browser_back_keep_user_signed_out(driver, login_url, credentials):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login(*credentials)
    page.wait_for_url_change(login_url)
    logout_locator = (By.XPATH, "//*[self::a or self::button or @role='button'][contains(., 'Đăng xuất') or contains(., 'Logout') or contains(., 'Log out') or contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'logout') or contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'logout') or contains(translate(@href, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'logout') or contains(translate(@id, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'logout') or contains(translate(@class, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'logout')]")
    logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(logout_locator))
    protected_url = driver.current_url
    logout.click()
    page.wait_for_url_change(protected_url)
    driver.back()
    assert "/login" in driver.current_url.lower(), "Browser Back returned to a protected page"
