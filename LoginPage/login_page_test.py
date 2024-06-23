
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from LoginLocatorsPage.login_locator_test import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def open_login_page(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Opened login page: {url}")
        except Exception as e:
            self.logger.error(f"Failed to open login page: {url} - {e}")
            self._take_screenshot("open_login_page")

    def enter_email_address(self, email):
        try:
            enter_email_address = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
            enter_email_address.send_keys(email)
            self.logger.info(f"Email username: {email}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter email address: {email} - {e}")
            self._take_screenshot("enter_email_address")

    def enter_password(self, password):
        try:
            password_field = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))
            password_field.send_keys(password)
            self.logger.info(f"Entered password")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter password - {e}")
            self._take_screenshot("enter_password")

    def click_remember_me_button(self):
        try:
            click_remember_me_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LoginPageLocators.REMEMBER_ME_BUTTON))
            click_remember_me_button.click()
            self.logger.info("Clicked remember me button")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to Clicked remember button - {e}")
            self._take_screenshot("click_remember_me_button")

    def click_login_button(self):
        try:
            login_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LoginPageLocators.CLICK_LOGIN_BUTTON))
            login_button.click()
            self.logger.info("Clicked login button")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click login button - {e}")
            self._take_screenshot("click_login_button")

    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")
