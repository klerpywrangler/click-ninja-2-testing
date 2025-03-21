# selenium_framework/config/config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Browser settings
    BROWSER = os.getenv("BROWSER", "chrome")
    HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"
    
    # URL settings
    BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
    
    # Timeouts
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "10"))
    PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
    
    # Credentials
    USERNAME = os.getenv("USERNAME", "test_user")
    PASSWORD = os.getenv("PASSWORD", "test_password")
    
    # Report settings
    REPORT_PATH = os.getenv("REPORT_PATH", "./reports")