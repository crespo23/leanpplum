import pytest
from leanplum.src.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class TestLogin:

    @pytest.mark.tcid12
    def test_00_login_user(self):

        login_p = LoginPage(self.driver)
        login_p.launch_login_page()
        login_p.input_login_username('mihailnc23@gmail.com')
        login_p.input_login_password('Mi!h@LZz')
        login_p.click_on_login_button()
