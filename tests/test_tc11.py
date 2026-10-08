"""TC11: password is case sensitive."""

def test_tc11_password_case_is_significant(driver, login_url, credentials):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    username, password = credentials
    assert password.lower() != password.upper(), "Test password needs at least one letter"
    page.login(username, password.upper())
    message = page.form.error_text().lower()
    assert message, "Expected an error when password casing is changed"
