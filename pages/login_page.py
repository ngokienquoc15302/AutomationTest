from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_button(self):
        try:
            login_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/app-root[1]/app-default-layout["
                                                      "1]/app-default-layout-header[1]/header[1]/div[1]/mat-toolbar["
                                                      "1]/button[2]"))
            )
            login_button.click()
        except NoSuchElementException:
            print("Không tìm thấy nút đăng nhập")

    def is_login_successful(self):
        try:
            # Thay đổi title_expected với tiêu đề mong đợi sau khi đăng nhập thành công
            title_expected = "Cổng Dịch vụ công Quốc gia"  # Cập nhật tiêu đề mong đợi
            WebDriverWait(self.driver, 10).until(
                EC.title_is(title_expected)
            )
            print("Chuyển đến trang đăng nhập của Dịch vụ công Quốc gia")
            return True
        except TimeoutException:
            return False
        except Exception as e:
            print("Đã xảy ra lỗi:", str(e))
            return False
