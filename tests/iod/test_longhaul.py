import unittest
from appium import webdriver
from config import Config
from appium.options.android import UiAutomator2Options
from pages.iod.longhaul_page import LonghaulPage


class TestLonghaulAcceptance(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_staff = LonghaulPage(self.driver)

    def test_longhaul(self):
        err = self.longhaul_staff.nav_staff_longhaul()
        if err != None: print("\nError/Alert Detected:", err)
        
    def tearDown(self):
        self.driver.quit()
        
#Fix the code
class TestDriverLonghaul(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.longhaul_driver = LonghaulPage(self.driver)
        self.errorList = []
        
    def test_longhaul(self):
        err = self.longhaul_driver.nav_driver_longhaul()
        if err != None:
            self.errorList.append(err)
        
        err = self.longhaul_driver.scan_longhaul()
        if err != None:
            self.errorList.append(err)
            
        err = self.longhaul_driver.longhaul_viewDetails()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
        
    def test_longhaulPOD(self):
        err = self.longhaul_driver.driver_longhaul_pod()
        if err != None: print("\nError/Alert Detected:", err)
    
    def test_longhaulFail(self):
        err = self.longhaul_driver.driver_longhaul_fail()
        if err != None: print("\nError/Alert Detected:", err)
    
        
    def tearDown(self):
        self.driver.quit()
      
      