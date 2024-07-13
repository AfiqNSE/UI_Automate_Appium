import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.oms.home_page import OMSHomePage


class TestOMSHomePage(unittest.TestCase):
    def test_homepage(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.home_page = OMSHomePage(self.driver)
        
        self.home_page.check_scan()
        
    def tearDown(self):
        self.driver.quit()