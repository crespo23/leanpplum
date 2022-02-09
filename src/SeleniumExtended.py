from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10


    @staticmethod
    def wait_and_input_text_(driver, locator, text, timeout=10):

        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    @staticmethod
    def wait_and_click(driver, locator, timeout=10):

        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    @staticmethod
    def choose_option_from_dropdown(driver, selector, selector2, timeout=10):
        dropdown_menu = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(selector))
        dropdown_menu.click()

        dropdown_menu_options = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector2))
        dropdown_menu_options.click()

    @staticmethod
    def hover(driver, selector, selector2, timeout=10):
        header_campaign_menu = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(selector))

        action = ActionChains(driver)

        hover = action.move_to_element(header_campaign_menu)
        hover.perform()
        campaign_link = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(selector2))
        campaign_link.click()

