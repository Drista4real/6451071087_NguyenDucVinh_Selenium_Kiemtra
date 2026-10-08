"""Locators and actions for the login form DOM section."""
from selenium.webdriver.common.by import By


class LoginForm:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "userpwd")
    SUBMIT = (By.CSS_SELECTOR, "form[action='/Login'] input.submit_login[type='submit']")
    REMEMBER = (By.ID, "persistent")
    REMEMBER_LABEL = (By.CSS_SELECTOR, "label.check[for='persistent']")
    ERROR = (By.CSS_SELECTOR, ".alert, .error, .validation-summary-errors")

    def __init__(self, driver):
        self.driver = driver

    def username_field(self):
        return self.driver.find_element(*self.USERNAME)

    def password_field(self):
        return self.driver.find_element(*self.PASSWORD)

    def submit(self):
        self.driver.find_element(*self.SUBMIT).click()

    def login(self, username, password):
        self.username_field().send_keys(username)
        self.password_field().send_keys(password)
        self.submit()

    def set_remember_me(self, selected):
        checkbox = self.driver.find_element(*self.REMEMBER)
        if checkbox.is_selected() != selected:
            self.driver.find_element(*self.REMEMBER_LABEL).click()

    def error_text(self):
        elements = self.driver.find_elements(*self.ERROR)
        return " ".join(element.text for element in elements if element.is_displayed())
