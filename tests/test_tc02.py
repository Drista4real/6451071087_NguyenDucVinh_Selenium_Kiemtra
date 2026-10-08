"""TC02: valid login with Enter."""

def test_tc02_valid_login_with_enter(driver, login_url, credentials):
    from selenium.webdriver.common.keys import Keys
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    user, password = credentials
    driver.find_element(*page.USERNAME).send_keys(user)
    field = driver.find_element(*page.PASSWORD)
    field.send_keys(password)
    old_url = driver.current_url
    field.send_keys(Keys.ENTER)
    page.wait_for_url_change(old_url)
    assert driver.current_url != login_url
