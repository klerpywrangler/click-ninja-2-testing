# selenium_framework/run_tests.py

import os
import pytest
import datetime
from config.config import Config

def run_tests():
    # Create timestamp for reports
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = os.path.join(Config.REPORT_PATH, timestamp)
    os.makedirs(report_dir, exist_ok=True)
    
    # Run tests with pytest
    html_report = os.path.join(report_dir, "report.html")
    xml_report = os.path.join(report_dir, "report.xml")
    
    args = [
        "-v",
        "--html=" + html_report,
        "--junitxml=" + xml_report,
        "--self-contained-html",
        "tests/"
    ]
    
    pytest.main(args)
    
    print(f"Testing complete. Reports available at: {report_dir}")

if __name__ == "__main__":
    run_tests()