import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.home_page import HomePage
from pages.procedures_page import ProceduresPage
from pages.login_page import LoginPage


class TestLogin:
    @pytest.fixture(scope="class")
    def setup(self):
        web_driver_setup = WebDriverSetup()
        driver = web_driver_setup.setup(index=0)
        yield driver
        driver.quit()

    def test_login(self, setup):
        login_page = LoginPage(setup)
        login_page.click_login_button()

        # Kiểm tra đăng nhập thành công
        assert login_page.is_login_successful(), "Đăng nhập không thành công"
