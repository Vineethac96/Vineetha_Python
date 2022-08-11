import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = None

def setup_module(module):    #setup_module -name should be as is
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

def teardown_module(module):   #teardown_module -name should be as is
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"



'''to run test cases with/in html and generate html report-QA
pip install pytest-html

command to run: pytest test_google_test.py -v --html = report.html

Right-click on the report.html and select the option Copy Path.

'''