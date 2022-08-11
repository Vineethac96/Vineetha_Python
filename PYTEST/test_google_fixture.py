import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('----------setup------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print('----------teardown------')
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

@pytest.mark.usefixtures('init_driver')
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"

'''can use fixture declared function as the parameter or can write with markers'''
