"""TC12: username whitespace handling."""

def test_tc12_username_surrounding_spaces_are_trimmed(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    old_url = driver.current_url
    page.login(" " + credentials[0] + " ", credentials[1])
    page.wait_for_url_change(old_url)
    assert driver.current_url != login_url
