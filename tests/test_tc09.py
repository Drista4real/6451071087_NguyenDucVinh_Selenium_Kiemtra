"""TC09: wrong username is rejected."""

def test_tc09_wrong_username_is_rejected(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("huongthunguyen", credentials[1])
    assert page.form.error_text(), "Expected an error for an unknown username"
