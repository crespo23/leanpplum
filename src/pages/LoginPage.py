from leanplum.src.pages.locators.LoginPageLocators import LoginPageLocator

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from leanplum.src.helpers.config_helpers import get_base_url
from leanplum.src.SeleniumExtended import SeleniumExtended


class LoginPage(LoginPageLocator):

    endpoint = '/dashboard/login'

    def __init__(self, driver):
        self.driver = driver

    def launch_login_page(self):
        base_url = get_base_url()
        login_page_url = base_url + self.endpoint
        self.driver.get(login_page_url)

    def input_login_username(self, username):
        SeleniumExtended.wait_and_input_text_(self.driver, self.LOGIN_USER_NAME, username)
        #self.sl.wait_and_input_text_(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        SeleniumExtended.wait_and_input_text_(self.driver, self.LOGIN_PASSWORD, password)

    def click_on_login_button(self,):
        SeleniumExtended.wait_and_click(self.driver, self.LOGIN_BUTTON)
