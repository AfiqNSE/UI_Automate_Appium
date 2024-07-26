import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.search_history_page import SearchHistoryPage

#Fix the code
class TestStaffSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchHistoryPage(self.driver)
        self.errorList = []

    def test_staff_estDateTime(self):
        err = self.search_page.staff_docket_estDateTime()
        if err != None: print("\nError/Alert Detected:", err)
        
    def test_staff_pod(self):
        err = self.search_page.staff_pod_photoDocket()
        if err != None:
            self.errorList.append(err)
        
        err = self.search_page.staff_pod_uploadDocket()
        if err != None:
            self.errorList.append(err)
            
        err = self.search_page.staff_pod_signatureDocket()
        if err != None:
            self.errorList.append(err)
            
        err = self.search_page.staff_additional()
        if err != None:
            self.errorList.append(err)
        
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
    
    def test_staff_fail(self):
        err = self.search_page.staff_fail_docket()
        if err != None: print("\nError/Alert Detected:", err)
    
    def test_staff_delay(self):
        err = self.search_page.staff_delay_docket()
        if err != None: print("\nError/Alert Detected:", err)
        
    def tearDown(self):
        self.driver.quit()


class TestDriverSearch(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.search_page = SearchHistoryPage(self.driver)
        self.errorList = []
        
    def test_driver_completed(self):
        err = self.search_page.driver_completed()
        if err != None: print("\nError/Alert Detected:", err)  
              
    def test_driver_pod(self):
        err = self.search_page.driver_pod_photoDocket()
        if err != None:
            self.errorList.append(err)
        
        err = self.search_page.driver_pod_uploadDocket()
        if err != None:
            self.errorList.append(err)
            
        err = self.search_page.driver_pod_signatureDocket()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
        
    def test_driver_fail(self):
        err = self.search_page.driver_fail_docket()
        if err != None: print("\nError/Alert Detected:", err)
        
    def test_driver_delay(self):
        err = self.search_page.driver_delay_docket()
        if err != None: print("\nError/Alert Detected:", err)
        
    def tearDown(self):
        self.driver.quit()
    

