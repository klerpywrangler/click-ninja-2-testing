# selenium_framework/tests/flows/test_login_flow.py

import pytest
from ...pages.login_page import LoginPage
from ..base_test import BaseTest
from ...config.config import Config

class TestLoginFlow(BaseTest):
    def test_successful_login(self):
        """Test that a user can successfully log in with valid credentials."""
        login_page = LoginPage(self.driver).load()
        login_page.login_with_default_credentials()
        
        # Add assertions based on what happens after successful login
        # For example, check if redirected to dashboard
        assert "dashboard" in self.driver.current_url.lower(), "User was not redirected to dashboard after login"
    
    def test_invalid_login(self):
        """Test that a user cannot log in with invalid credentials."""
        login_page = LoginPage(self.driver).load()
        login_page.login("wrong_user", "wrong_password")
        
        assert login_page.is_error_message_displayed(), "Error message not displayed for invalid credentials"