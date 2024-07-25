from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import json


class WebDriverSetup:
    def __init__(self, config_file='resources/config.json'):
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        with open(self.config_file) as config_file:
            self.config = json.load(config_file)

    def setup(self, index=0):
        config = self.config[index]
        url = config.get("url", "https://defaultwebsite.com")
        browser = config.get("browser", "chrome")
        chrome_options = Options()
        chrome_options.add_argument("user-data-dir=C:/Users/ngoki/AppData/Local/Google/Chrome/User Data/")
        chrome_options.add_argument("--profile-directory=Default")
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise Exception("Browser not supported")

        driver.maximize_window()
        driver.get(url)
        return driver
