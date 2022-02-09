from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from leanplum.src.helpers.config_helpers import get_base_url
from leanplum.src.SeleniumExtended import SeleniumExtended
from leanplum.src.pages.locators.CampaignPageLocators import CampaignPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class CampaignPage(CampaignPageLocators):


    def __init__(self, driver):
        self.driver = driver

    def launch_campaign(self):
        SeleniumExtended.hover(self.driver, self.HOVER_CAMPAIGN_HEADER, self.CAMPAIGN_HEADER_BUTTON)
        SeleniumExtended.wait_and_click(self.driver, self.CREATE_CAMPAIGN_BUTTON)

    def create_campaign(self):
        SeleniumExtended.wait_and_click(self.driver, self.MULTI_MASSAGE_SELECTOR)
        SeleniumExtended.wait_and_input_text_(self.driver, self.CAMPAIGN_NAME_SEL, 'blbalbabal')
        SeleniumExtended.choose_option_from_dropdown(self.driver, self.CAMPAIGN_GOAL_DROPDOWN, self.CAMPAIGN_DROPDOWN_OPTIONS)

        #SeleniumExtended.wait_and_click(self.driver, self.CAMPAIGN_GOAL_DROPDOWN)
        print('baabbaba')
    def hover_and_click(self):
        Hover = ActionChains(self.driver).move_to_element()


