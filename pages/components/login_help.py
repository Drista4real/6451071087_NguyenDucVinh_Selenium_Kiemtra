"""Locators for the help links beside the login form."""
from selenium.webdriver.common.by import By


class LoginHelp:
    GOOGLE_LOGIN = (By.CSS_SELECTOR, "a[href^='https://accounts.google.com/o/oauth2/auth']")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "a[href='/Login/GetPass']")

    def __init__(self, driver):
        self.driver = driver

    def google_login_link(self):
        return self.driver.find_element(*self.GOOGLE_LOGIN)

    def forgot_password_link(self):
        return self.driver.find_element(*self.FORGOT_PASSWORD)
