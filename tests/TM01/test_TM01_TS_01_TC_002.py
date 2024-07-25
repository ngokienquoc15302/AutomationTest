import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.home_page import HomePage


class TestSearchByKeyWord:
    @pytest.fixture(scope="class")
    def setup(self):
        web_driver_setup = WebDriverSetup()
        driver = web_driver_setup.setup(index=0)
        yield driver
        driver.quit()

    def test_search_functionality(self, setup):
        home_page = HomePage(setup)
        home_page.enter_search_keyword("abcxyz")
        home_page.click_search_button()
        assert home_page.is_search_result_displayed()
