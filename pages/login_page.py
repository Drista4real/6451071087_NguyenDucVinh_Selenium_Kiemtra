"""Page object that composes the main sections of the login page DOM."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.components.login_form import LoginForm
from pages.components.login_help import LoginHelp


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.form = LoginForm(driver)
        self.help = LoginHelp(driver)

    def open(self, url):
        self.driver.get(url)
        return self

    def login(self, username, password):
        self.form.login(username, password)

    def wait_for_url_change(self, old_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))
