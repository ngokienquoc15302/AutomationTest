import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.register_page import RegisterPage


class TestRegister:
    @pytest.fixture(scope="class")
    def setup(self):
        web_driver_setup = WebDriverSetup()
        driver = web_driver_setup.setup(index=0)
        yield driver
        driver.quit()

    def test_login(self, setup):
        register_page = RegisterPage(setup)
        initial_windows = register_page.click_register_button()
        assert register_page.is_register_successful(initial_windows), "Đăng ký không thành công"
