"""TC04: login without remember me."""

def test_tc04_login_without_remember_me(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.form.set_remember_me(False)
    assert not driver.find_element(*page.form.REMEMBER).is_selected()
    old_url = driver.current_url
    page.login(*credentials)
    page.wait_for_url_change(old_url)
    assert driver.current_url != login_url
