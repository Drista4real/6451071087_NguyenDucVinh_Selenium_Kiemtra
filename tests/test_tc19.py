"""TC19: tab order follows login form."""

def test_tc19_tab_order_username_password_submit(driver, login_url):
    from selenium.webdriver.common.keys import Keys
    from pages.login_page import LoginPage
    page = LoginPage(driver).open(login_url)
    username = driver.find_element(*page.form.USERNAME)
    password = driver.find_element(*page.form.PASSWORD)
    submit = driver.find_element(*page.form.SUBMIT)
    username.click()
    username.send_keys(Keys.TAB)
    assert driver.switch_to.active_element == password
    password.send_keys(Keys.TAB)
    assert driver.switch_to.active_element == submit
