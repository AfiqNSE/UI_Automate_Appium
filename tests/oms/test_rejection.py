import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.oms_component import OMSComponents
from config import Config
from pages.oms.rejection_page import OMSRejectionPage

class TestOMSRejection(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.rejection_page = OMSRejectionPage(self.driver)
        self.component = OMSComponents(self.driver)
        self.errorList = []
        
    def test_viewReject(self):
        #Navigate to rejections page
        self.component.nav_rejection()
        self.component.refresh_page()
            
        err = self.rejection_page.status_filter()
        if err != None: 
            self.errorList.append(err)
            
        err = self.rejection_page.date_filter()
        if err != None: 
            self.errorList.append(err)
            
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
    
    def test_closeReject(self):
        err = self.rejection_page.nav_closeReject()
        if err != None: 
            self.errorList.append(err)
            
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
    
    def tearDown(self):
        self.driver.quit()