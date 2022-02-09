from selenium.webdriver.common.by import By


class LoginPageLocator:

    LOGIN_USER_NAME = (By.CSS_SELECTOR, 'input[ng-model="loginModel.email"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, 'input[ng-model="loginModel.password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[ng-disabled="loginModel.isLoading"]')
