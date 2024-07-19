import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.oms_component import OMSComponents
from config import Config
from pages.oms.home_page import OMSHomePage


class TestOMSHomePage(unittest.TestCase): 
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.errorList = []
        self.home_page = OMSHomePage(self.driver)
        self.component = OMSComponents(self.driver)
    
    def test_mainFeature(self):
        #Nav to homepage tab
        self.component.nav_home()
        
        err = self.home_page.nav_viewOrder()
        if err != None:
            self.errorList.append(err)
        
        err = self.home_page.nav_scan()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_page.nav_searchOrder()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_page.nav_notif()
        if err != None:
            self.errorList.append(err)
        
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
    
    def test_filterFeature(self):
        err = self.home_page.status_filter()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_page.company_filter()
        if err != None:
            self.errorList.append(err)
            
        err = self.home_page.date_filter()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
            
    def tearDown(self):
        self.driver.quit()