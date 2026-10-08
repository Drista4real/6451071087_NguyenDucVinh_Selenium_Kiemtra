"""TC08: wrong password is rejected."""

def test_tc08_wrong_password_is_rejected(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("huongnt", "utc@235")
    assert page.form.error_text(), "Expected an error for an incorrect password"
