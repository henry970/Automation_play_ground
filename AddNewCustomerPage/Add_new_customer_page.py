import logging
import time
import self
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from AddNewCustomerPageLocators.Add_new_customer_page_locators import AddNewCustomerPageLocators, \
    FillNewCustomerFormPageLocators


class NewCustomer:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def click_new_customer(self):
        try:
            click_new_customer = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(AddNewCustomerPageLocators.CLICK_NEW_CUSTOMER_BUTTON))
            click_new_customer.click()
            self.logger.info("Clicked new customer")
            time.sleep(5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click new customer - {e}")
            self._take_screenshot("click_new_customer")

    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")


class FillNewCustomerFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def enter_email_address(self, email):
        try:
            enter_email_address = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.ENTER_EMAIL))
            enter_email_address.send_keys(email)
            self.logger.info(f"Email username: {email}")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter email address: {email} - {e}")
            self._take_screenshot("enter_email_address")

    def enter_firstName(self, first):
        try:
            enter_firstName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.ENTER_FIRSTNAME))
            enter_firstName.send_keys(first)
            self.logger.info(f"Entered enter firstName")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter firstName - {e}")
            self._take_screenshot("enter_firstName")

    def enter_LastName(self, last):
        try:
            enter_LastName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.ENTER_LASTNAME))
            enter_LastName.send_keys(last)
            self.logger.info(f"Entered enter lastName")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter LastName - {e}")
            self._take_screenshot("enter_LastName")

    def enter_city(self, city):
        try:
            enter_city = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.ENTER_CITY))
            enter_city.send_keys(city)
            self.logger.info(f"Entered enter city")
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to enter city - {e}")
            self._take_screenshot("enter_city")

    def click_state_drop_down_button(self):
        try:
            click_state_drop_down_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FillNewCustomerFormPageLocators.CLICK_STATE_DROP_DOWN))
            click_state_drop_down_button.click()
            self.logger.info("Clicked state drop down button")
            time.sleep(5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to Clicked state button - {e}")
            self._take_screenshot("click_state_drop_down_button")

    def Select_state(self):
        try:
            Select_state = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FillNewCustomerFormPageLocators.SELECT_STATE))
            Select_state.click()
            self.logger.info("Select state")
            time.sleep(10)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to Select state - {e}")
            self._take_screenshot("Select_state")

    def select_gender(self):
        try:
            gender_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.SELECT_GENDER))
            # Scroll to the element
            self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_element)
            # Wait for the element to be clickable and then click
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FillNewCustomerFormPageLocators.SELECT_GENDER)).click()
            self.logger.info("Selected gender")
            time.sleep(5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to select gender - {e}")
            self._take_screenshot("select_gender")

    def click_submit_button(self):
        try:
            # Scroll down to the submit button
            submit_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FillNewCustomerFormPageLocators.CLICK_SUBMIT_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

            # Wait until the button is clickable and then click it
            submit_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(FillNewCustomerFormPageLocators.CLICK_SUBMIT_BUTTON))
            submit_button.click()
            self.logger.info("Clicked submit button")
            time.sleep(5)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"Failed to click submit button - {e}")
            self._take_screenshot("click_submit_button")

    def _take_screenshot(self, action_name):
        screenshot_path = f"screenshots/{action_name}_{int(time.time())}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Screenshot saved to {screenshot_path}")
