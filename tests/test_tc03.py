"""TC03: remember me login."""

def test_tc03_remember_me_login(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    checkbox = driver.find_element(*page.REMEMBER)
    if not checkbox.is_selected():
        checkbox.click()
    assert checkbox.is_selected()
    old_url = driver.current_url
    page.login(*credentials)
    page.wait_for_url_change(old_url)
    assert driver.current_url != login_url
