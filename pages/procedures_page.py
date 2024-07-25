import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ProceduresPage:
    def __init__(self, driver):
        self.driver = driver

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

    def click_advanced_search(self):
        try:
            click_advanced_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@class = 'mat-focus-indicator mat-stroked-button mat-button-base']"))
            )
            click_advanced_search.click()
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")

    def select_implementing_agency(self, value):
        try:
            select_implementing_agency = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, f"mat-radio-{value}"))
            )
            select_implementing_agency.click()
            if value == 3:
                select_1 = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable(
                        (By.XPATH, '//body/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[2]/div[2]/mat-form-field[1]/div[1]/div[1]'))
                )
                select_1.click()
                select_2 = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
                select_2.click()
                print(select_2.text)
                time.sleep(1)
                select_3 = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         '/html[1]/body[1]/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[3]/div[2]/mat-form-field[1]/div[1]/div[1]'))
                )
                select_3.click()
                select_4 = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
                select_4.click()
                print(select_4.text)
            elif value == 4:
                select_5 = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH,
                         '/html[1]/body[1]/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[2]/div[2]/mat-form-field[1]/div[1]/div[1]'))
                )
                select_5.click()
                time.sleep(0.5)
                select_6 = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
                select_6.click()
                print(select_6.text)
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")

    def select_field(self):
        try:
            select_field = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '/html[1]/body[1]/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[4]/div[2]/mat-form-field[1]/div[1]/div[1]'))
            )
            select_field.click()
            time.sleep(0.5)
            select_field_id = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
            select_field_id.click()
            print(select_field_id.text)
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")

    def select_level(self):
        try:
            select_level = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '/html[1]/body[1]/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[6]/div[2]/mat-form-field[1]/div[1]/div[1]'))
            )
            select_level.click()
            time.sleep(1)
            select_level_id = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
            select_level_id.click()
            print(select_level_id.text)
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")

    def select_object(self):
        try:
            select_object = WebDriverWait(self.driver,10).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     '/html[1]/body[1]/app-root[1]/app-default-layout[1]/app-default-layout-nav[1]/div[2]/app-search[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/div[7]/div[2]/mat-form-field[1]/div[1]/div[1]'))
            )
            select_object.click()
            time.sleep(1)
            select_object_id = self.driver.find_element(By.CSS_SELECTOR, "[id*='mat-option-']:last-of-type")
            select_object_id.click()
            print(select_object_id.text)
        except NoSuchElementException:
            print("Không tìm thấy bất kỳ danh mục nào")

    def click_search_button(self):
        try:
            enter_search = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class = 'mat-focus-indicator mat-stroked-button mat-button-base']"))
            )
            enter_search.click()
        except NoSuchElementException:
            print("Không tìm thấy nút tìm kiếm")