import unittest
from appium.options.android import UiAutomator2Options
from parameterized import parameterized
from appium import webdriver

from components.main_component import Constant
from config import Config
from pages.login_page import LoginPage

#TODO: Find a way to combine test for driver and staff
class TestStaffLogin(unittest.TestCase):
    def test_login(self, username):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver, username)
        
        self.login_page.enter_staff_username()
        self.login_page.enter_password()
        self.login_page.click_login()
    

class TestDriverLogin(unittest.TestCase):
    def test_login(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver)
        
        self.login_page.enter_driver_username()
        self.login_page.enter_password()
        self.login_page.click_login()
    

             




