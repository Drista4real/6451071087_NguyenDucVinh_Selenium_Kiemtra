"""TC20: CAPTCHA image and input are shown on password recovery page."""


def test_tc20_password_recovery_displays_captcha(driver, login_url):
    from urllib.parse import urlsplit

    from pages.recover_password_page import RecoverPasswordPage

    parsed_url = urlsplit(login_url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    page = RecoverPasswordPage(driver).open(base_url)

    captcha_image = driver.find_element(*page.CAPTCHA_IMAGE)
    captcha_input = driver.find_element(*page.CAPTCHA_INPUT)
    email_input = driver.find_element(*page.EMAIL_INPUT)

    assert captcha_image.is_displayed(), "CAPTCHA image is not visible"
    assert captcha_input.is_displayed(), "CAPTCHA input is not visible"
    assert email_input.is_displayed(), "Email input is not visible on recovery form"
