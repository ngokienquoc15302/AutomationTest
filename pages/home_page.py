from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_keyword(self, keyword):
        try:
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'inputSearchControl2'))
            )
            search_input.clear()
            search_input.send_keys(keyword)
        except NoSuchElementException:
            print("Không tìm thấy phần tử tìm kiếm")

    def click_search_button(self):
        try:
            enter_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "mat-focus-indicator.btn-search.mat-flat-button.mat-button-base"))
            )
            enter_search.click()
        except NoSuchElementException:
            print("Không tìm thấy nút tìm kiếm")

    def is_search_result_displayed(self):
        try:
            search_results = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mat-row.cdk-row.ng-star-inserted'))
            )
            print(len(search_results))
            return len(search_results) > 0
        except TimeoutException:
            print("Không tìm thấy phần tử tìm kiếm trên trang")
            return AssertionError
        except NoSuchElementException:
            print("Không tìm thấy phần tử tìm kiếm trên trang")
            return AssertionError

    def click_category(self):
        try:
            click_category = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='citizenItem ng-star-inserted']"))
            )
            click_category.click()
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")
