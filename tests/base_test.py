# selenium_framework/tests/base_test.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from ..config.config import Config

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup for Railway environment
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Initialize the WebDriver
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(Config.IMPLICIT_WAIT)
        self.driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)
        
        # Return the WebDriver instance for the test
        yield
        
        # Teardown
        self.driver.quit()