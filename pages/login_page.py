"""Locators documented from the UTC login page shown with the test cases."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    SUBMIT = (By.CSS_SELECTOR, "input.submit__login")
    REMEMBER = (By.ID, "persistent")
    ERROR = (By.CSS_SELECTOR, ".alert, .error, .validation-summary-errors")

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
        return self

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()

    def error_text(self):
        elements = self.driver.find_elements(*self.ERROR)
        return " ".join(element.text for element in elements if element.is_displayed())

    def wait_for_url_change(self, old_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
