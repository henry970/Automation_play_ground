from selenium.webdriver.common.by import By


class AddNewCustomerPageLocators:
    CLICK_NEW_CUSTOMER_BUTTON = (By.ID, "new-customer")


class FillNewCustomerFormPageLocators:
    ENTER_EMAIL = (By.ID, "EmailAddress")
    ENTER_FIRSTNAME = (By.ID, "FirstName")
    ENTER_LASTNAME = (By.ID, "LastName")
    ENTER_CITY = (By.ID, "City")
    CLICK_STATE_DROP_DOWN = (By.ID, "StateOrRegion")
    SELECT_STATE = (By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/select/option[7]")
    SELECT_GENDER = (By.XPATH, "/html/body/section/div/div/div/div/form/div[6]/input[1]")
    CLICK_SUBMIT_BUTTON = (By.XPATH, "/html/body/section/div/div/div/div/form/button")

