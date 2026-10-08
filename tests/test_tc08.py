"""TC08: wrong password is rejected."""

def test_tc08_wrong_password_is_rejected(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("huongnt", "utc@235")
    assert "t?i kho?n ho?c m?t kh?u kh?ng ch?nh x?c" in page.form.error_text().lower()
