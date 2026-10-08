"""TC10: wrong credentials are rejected."""

def test_tc10_wrong_credentials_are_rejected(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    page.login("sai_user", "sai_pass")
    assert "t?i kho?n ho?c m?t kh?u kh?ng ch?nh x?c" in page.error_text().lower()
