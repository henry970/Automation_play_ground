import logging
import time
import self
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from LogoutPageLocators.logout_page_locators import LogoutPageLocators


class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def click_logout_button(self):
        try:
            # Wait until the button is clickable and then click it
            click_logout_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(LogoutPageLocators.LOGOUT_BUTTON))
            click_logout_button.click()
            self.logger.info("Clicked logout button")
            time.sleep(5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click login button - {e}")
            self._take_screenshot("click_logout_button")

    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")
