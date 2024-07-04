import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.main_component import Components
from config import Config
from pages.home_page import DriverHomePage, StaffHomePage
from pages.login_page import LoginPage

class TestStaffLogin(unittest.TestCase):
    def test_Login(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.login_page = LoginPage(self.driver)
        self.home_page = StaffHomePage(self.driver)
        
        self.login_page.enter_staff_username()
        self.login_page.enter_password()
        self.login_page.click_login()
        self.home_page.load_staffHome()


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
        self.home_page = DriverHomePage(self.driver)
        
        self.login_page.enter_driver_username()
        self.login_page.enter_password()
        self.login_page.click_login()
        self.home_page.load_driverHome()
    

class TestDriverLogout(unittest.TestCase):
    def test_driverLogout(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.logout_driver = Components(self.driver)
    
        self.logout_driver.driver_logout()          




