import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.assign_page import AssignPointPage

class TestIODAssign(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.assign_page = AssignPointPage(self.driver)

    def test_scanAssign(self):
        err = self.assign_page.scan_assignPoint()
        if err != None: print("\nError/Alert Detected:", err)
    
    def test_insertAssign(self):
        err = self.assign_page.insert_assignPoint()
        if err != None: print("\nError/Alert Detected:", err)
        
    def tearDown(self):
        self.driver.quit()

