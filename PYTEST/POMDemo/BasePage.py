from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''This class is the parent of all classes
It contains all the generic methods and utilities for all the pages'''

class BasePage:

    '''constructor of the base page class'''
    def __init__(self,driver):   #constructo, it is the Python equivalent of the C++ constructor in an object-oriented approach. The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes
        self.driver = driver

    '''this is used to click on a button'''
    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).click()

    '''this is used to send keys/values'''
    def do_sendkeys(self, by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    '''this is used to get an element's text'''
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    '''this is used to check visibility of an element'''
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    '''this is used to get title of a page'''
    def get_title(self, title):
        WebDriverWait(self.driver,10).until(EC.title_is(title)) #wait until that tile is dispalyed and get it
        return self.driver.title