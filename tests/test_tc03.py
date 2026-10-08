"""TC03: remember me login."""

def test_tc03_remember_me_login(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.form.set_remember_me(True)
    assert driver.find_element(*page.form.REMEMBER).is_selected()
    old_url = driver.current_url
    page.login(*credentials)
    page.wait_for_url_change(old_url)
    assert driver.current_url != login_url
