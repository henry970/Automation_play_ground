import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from LoginPage.login_page_test import LoginPage
from AddNewCustomerPage.Add_new_customer_page import NewCustomer, FillNewCustomerFormPage
from LogoutPage.Logout_Page_test import LogoutPage


#
@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


# @pytest.fixture(scope="module")
# def driver_setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(20)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page("https://automationplayground.com/crm/login.html")
    return login_page


# login page
def test_login_page_on_automation_play_ground_website(login):
    login.enter_email_address("Henryokolie@gmail.com")
    login.enter_password("test123@")
    login.click_remember_me_button()
    login.click_login_button()


def test_new_customer_button_on_automation_play_ground_website(login):
    test_new_customer_page = NewCustomer(login.driver)
    test_new_customer_page.click_new_customer()


# Add new customer
def test_fill_new_customer_form_on_automation_play_ground_website(login):
    test_fill_new_customer_form_page = FillNewCustomerFormPage(login.driver)
    test_fill_new_customer_form_page.enter_email_address("test@gmail.com")
    test_fill_new_customer_form_page.enter_firstName("Henry")
    test_fill_new_customer_form_page.enter_LastName("Okolie")
    test_fill_new_customer_form_page.enter_city("Arizona")
    test_fill_new_customer_form_page.click_state_drop_down_button()
    test_fill_new_customer_form_page.Select_state()
    test_fill_new_customer_form_page.select_gender()
    test_fill_new_customer_form_page.click_submit_button()


# logout button
def test_logot_button_on_automation_play_ground_website(login):
    test_new_customer_page = LogoutPage(login.driver)
    test_new_customer_page.click_logout_button()
