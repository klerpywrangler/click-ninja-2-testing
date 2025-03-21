# selenium_framework/pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    
    def navigate_to(self, url):
        self.driver.get(url)
    
    def find_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            self.logger.error(f"Element not found with locator: {locator}")
            return None
    
    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
            return True
        return False
    
    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
    
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False