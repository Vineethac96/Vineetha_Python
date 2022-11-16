import pytest

from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Config.config import TestData

class Test_Login(BaseTest):

    def test_signuplink_visible(self):
        self.loginPage = LoginPage(self.driver)  #create an object of login page class
        flag = self.loginPage.is_signup_link_exists()
        assert flag
'''or assert self.loginPage.is_signup_link_exists() directly'''


    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
