import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.longhaul_page import LonghaulPage


class TestStaffLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_page = LonghaulPage(self.driver)

    def test_longhaul(self):
        self.longhaul_page.nav_staff_longhaul()
        

class TestDriverLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul = LonghaulPage(self.driver)

    def test_longhaul(self):
        self.longhaul.nav_driver_longhaul()