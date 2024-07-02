import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.main_component import Components
from config import Config
from pages.login_page import LoginPage

#TODO: Find a way to combine test for driver and staff
class TestStaffLogin(unittest.TestCase):
    def test_Login(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver)
        
        self.login_page.enter_staff_username()
        self.login_page.enter_password()
        self.login_page.click_login()


class TestStaffLogout(unittest.TestCase):
    def test_staffLogout(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.logout_staff = Components(self.driver)
    
        self.logout_staff.staff_logout()

        
class TestDriverLogin(unittest.TestCase):
    def test_Login(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver)
        
        self.login_page.enter_driver_username()
        self.login_page.enter_password()
        self.login_page.click_login()
    

class TestDriverLogout(unittest.TestCase):
    def test_driverLogout(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.logout_driver = Components(self.driver)
    
        self.logout_driver.driver_logout()          




