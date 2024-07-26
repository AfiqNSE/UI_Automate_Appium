import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.iod.approve_page import ApprovePage

class TestIODApprove(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.approve_page = ApprovePage(self.driver)

    def test_approve(self):
        err = self.approve_page.nav_redeem()
        if err != None: print("\nError/Alert Detected:", err)
    
    def tearDown(self):
        self.driver.quit() 
