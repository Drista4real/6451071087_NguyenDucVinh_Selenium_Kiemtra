"""TC13: password input is masked."""

def test_tc13_password_input_is_masked(driver, login_url):
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    field = driver.find_element(*page.form.PASSWORD)
    field.send_keys("secret")
    assert field.get_attribute("type") == "password"
