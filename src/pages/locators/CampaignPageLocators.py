from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures('init_driver')
class CampaignPageLocators:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    HOVER_CAMPAIGN_HEADER = (By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/div[1]')
    CAMPAIGN_HEADER_BUTTON = (By.XPATH, '/html/body/main/div/div[1]/div[1]/div[2]/div[1]/div[2]/a[1]/div/div/div')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//span[text()="Create Campaign"]')
    MULTI_MASSAGE_SELECTOR = (By.XPATH, '/html/body/main/div/div[3]/div/div/div/div[2]/div[1]/div/div[2]/div')
    CAMPAIGN_NAME_SEL = (By.XPATH, '/html/body/main/div/div[3]/div/div/div/div[2]/div[3]/div[1]/div[2]/input')
    CAMPAIGN_GOAL_DROPDOWN = (By.XPATH, '/html/body/main/div/div[3]/div[1]/div/div/div[2]/div[3]/div[2]/div/div[2]/div')
    CAMPAIGN_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, '#lp-anchored-popup-popper-200 li:nth-child(6) div')

    # def select_campaign_goal_dropdown(self, driver):
    #     dropdown = (self.driver.find_element(*CampaignPageLocators.CAMPAIGN_GOAL_DROPDOWN))
    #     dropdown.click()
    #     elem = self.find_element(*CampaignPageLocators.CAMPAIGN_DROPDOWN_OPTIONS)
    #     self.driver.execute_script("arguments[0].click();", elem)