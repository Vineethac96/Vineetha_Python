from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.firefox import GeckoDriverManager

#instead of writing diff fixture for diff browsers, we can optimize using params
@pytest.fixture(params=["chrome", "firefox"],scope='class') #this fixture is applied for 1st-chrome and 2nd-firefox
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()