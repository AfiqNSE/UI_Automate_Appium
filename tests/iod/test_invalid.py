import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.invalid_page import InvalidIODPage

class TestInvalidIOD(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.invalid_page = InvalidIODPage(self.driver)
        self.errorList = []
        
    def test_invalid(self):
        err = self.invalid_page.nav_invalid()
        if err != None:
            self.errorList.append(err)
        
        err = self.invalid_page.nav_mainFeatures()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)

      
