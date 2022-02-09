import pytest
import time
from leanplum.src.pages.LoginPage import LoginPage
from leanplum.src.pages.CampaignPage import CampaignPage


@pytest.mark.usefixtures('init_driver')
class Test_e2e():

    def test_01_create_ccamapigns(self):
        #log = self.getLogger()
        login_p = LoginPage(self.driver)
        login_p.launch_login_page()
        login_p.input_login_username('mihailnc23@gmail.com')
        login_p.input_login_password('Mi!h@LZz')
        login_p.click_on_login_button()
        #   log.info('Login successful')
        campaign_p = CampaignPage(self.driver)
        campaign_p.launch_campaign()
        campaign_p.create_campaign()

