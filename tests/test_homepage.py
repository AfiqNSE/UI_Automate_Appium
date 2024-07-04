import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.home_page import DriverHomePage, StaffHomePage


class TestStaffHome(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.home_staff = StaffHomePage(self.driver)
    
    def test_staffHome(self):   
        self.home_staff.load_staffHome()



class TestDriverHome(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.home_driver = DriverHomePage(self.driver)  
             
    def test_driverHome(self):
        self.home_driver.load_driverHome()
        self.home_driver.logsheet_change()
        self.home_driver.option_button()
        self.home_driver.insert_docket()
        #K.I.V, already test at search
        # self.home_driver.driverPage_est()
                
        

