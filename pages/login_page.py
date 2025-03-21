# selenium_framework/pages/login_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..config.config import Config

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.ID, "username")  # Update these based on your app
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{Config.BASE_URL}/login"  # Update based on your app
    
    def load(self):
        self.navigate_to(self.url)
        return self
    
    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
    
    def login_with_default_credentials(self):
        self.login(Config.USERNAME, Config.PASSWORD)
    
    def is_error_message_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)