"""Page object for the password recovery form and its CAPTCHA DOM elements."""
from selenium.webdriver.common.by import By


class RecoverPasswordPage:
    CAPTCHA_IMAGE = (By.CSS_SELECTOR, ".form form img[src*='/login/index/captcha']")
    CAPTCHA_INPUT = (By.NAME, "captcha")
    EMAIL_INPUT = (By.NAME, "email")

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url.rstrip("/") + "/Login/GetPass")
        return self
