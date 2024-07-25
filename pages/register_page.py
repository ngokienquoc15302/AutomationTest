from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        initial_windows = self.driver.window_handles
        try:
            register_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/app-default-layout["
                                                      "1]/app-default-layout-header[1]/header[1]/div[1]/mat-toolbar["
                                                      "1]/button[3]"))
            )
            register_button.click()
            return initial_windows
        except NoSuchElementException:
            print("Không tìm thấy nút đăng nhập")
            return None

    def is_register_successful(self, initial_windows):

        try:
            WebDriverWait(self.driver, 10).until(
                lambda driver: len(driver.window_handles) > len(initial_windows)
            )
            current_windows = self.driver.window_handles

            if len(current_windows) > len(initial_windows):
                print("Đã xuất hiện cửa sổ đăng ký mới")
                return True
            else:
                return False
        except TimeoutException:
            return False
        except Exception as e:
            print("Đã xảy ra lỗi:", str(e))
            return False
