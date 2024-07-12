import unittest
from appium import webdriver
from config import Config
from appium.options.android import UiAutomator2Options
from components.main_component import Components
from pages.iod.longhaul_page import LonghaulPage


class TestStaffLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_staff = LonghaulPage(self.driver)

    def test_longhaul(self):
        self.longhaul_staff.nav_staff_longhaul()
        

class TestDriverLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_driver = LonghaulPage(self.driver)

    def test_longhaul(self):
        self.longhaul_driver.load_longhaulPage()
      
      