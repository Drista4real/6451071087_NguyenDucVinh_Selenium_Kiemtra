"""Locators documented from the UTC login page shown with the test cases."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    SUBMIT = (By.CSS_SELECTOR, "form[action='/Login'] input.submit_login[type='submit']")
    REMEMBER = (By.ID, "persistent")
    REMEMBER_LABEL = (By.CSS_SELECTOR, "label.check[for='persistent']")
    GOOGLE_LOGIN = (By.CSS_SELECTOR, "a[href^='https://accounts.google.com/o/oauth2/auth']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/Login/GetPass']")
    ERROR = (By.CSS_SELECTOR, ".alert, .error, .validation-summary-errors")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        return self

    def set_remember_me(self, selected):
        checkbox = self.driver.find_element(*self.REMEMBER)
        if checkbox.is_selected() != selected:
            self.driver.find_element(*self.REMEMBER_LABEL).click()

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def error_text(self):
        elements = self.driver.find_elements(*self.ERROR)
        return " ".join(element.text for element in elements if element.is_displayed())

    def wait_for_url_change(self, old_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
