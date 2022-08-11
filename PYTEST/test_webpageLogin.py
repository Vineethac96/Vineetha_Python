'''
By default, pytest runs tests in sequential order. but this will take longer time in rreal world scenario
But to run tests in parallel: pip intsall pytest-xdist
pytest -n 4 test_webpageLogin.py / pytest test_webpageLogin.py -n 4 -> opens 4 browsers in parallel and tests

if we give pytest -n 4 -> it will run all tests in the package (demo 1,2,3,webpagelogin)
'''

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)
        driver.get('http://www.google.com')
        assert driver.title == "Google"
        driver.quit()

def test_facebook():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()

def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()

def test_gmail():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('http://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()

# def test_rediff():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(10)
#     driver.get('http://www.rediff.com')
#     assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Shopping"
#     driver.quit()


