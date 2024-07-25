import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from utils.webdriver_setup import WebDriverSetup
from pages.home_page import HomePage
from pages.procedures_page import ProceduresPage


class TestSearchByAdvancedSearch:
    @pytest.fixture(scope="class")
    def setup(self):
        web_driver_setup = WebDriverSetup()
        driver = web_driver_setup.setup(index=1)
        yield driver
        driver.quit()

    def test_search_functionality(self, setup):
        procedures_page = ProceduresPage(setup)
        procedures_page.click_advanced_search()
        procedures_page.select_implementing_agency(4)
        procedures_page.select_field()
        procedures_page.click_search_button()
        assert procedures_page.is_search_result_displayed()
