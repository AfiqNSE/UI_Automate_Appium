import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.home_page import DriverHomePage

class TestDriverHome(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.home_driver = DriverHomePage(self.driver)
        self.errorList = []
             
    def test_driverHome(self):
        err = self.home_driver.logsheet_change()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_driver.find_presentDocket()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_driver.find_pastDocket()
        if err != None:
            self.errorList.append(err)
        
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
                
        

