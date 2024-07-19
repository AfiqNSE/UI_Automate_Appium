import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.oms_component import OMSComponents
from config import Config
from pages.oms.delivered_page import OMSDeliveredPage

class TestOMSDelivered(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.errorList = []
        self.delivered_page = OMSDeliveredPage(self.driver)
        self.component = OMSComponents(self.driver)
        
    def test_viewDelivered(self):
        #Nav to delivered tab
        self.component.nav_delivered()
        
        err = self.delivered_page.nav_viewOrder()
        if err != None:
            self.errorList.append(err)
            
        err = self.delivered_page.nav_filter()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
            
    def test_rejectOrder(self):
        err = self.delivered_page.nav_rejectAll()
        if err != None:
            self.errorList.append(err)
            
        err = self.delivered_page.nav_rejectPartial()
        if err != None:
            self.errorList.append(err)
            
        #Check error list
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)

    def tearDown(self):
        self.driver.quit()    