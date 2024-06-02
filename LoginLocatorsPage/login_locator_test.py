from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "email-id")
    PASSWORD_FIELD = (By.ID, "password")
    REMEMBER_ME_BUTTON = (By.ID, "remember")
    CLICK_LOGIN_BUTTON = (By.ID, "submit-id")
