import os
import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from dotenv import load_dotenv
from config import Config
from pages.iod.home_page import DriverHomePage, StaffHomePage
from pages.iod.login_page import IODLoginPage

class BaseTest(unittest.TestCase):
    #Base class for Appium tests. Provides shared setup/teardown and page objects.
    driver = None
    login_page = None
    staff_home = None
    driver_home = None
    logout_staff = None
    logout_driver = None

    @classmethod
    def setUpClass(cls):
        #Sets up the Appium driver and page objects for all tests in the class.
        load_dotenv()
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        cls.driver = webdriver.Remote(Config.appium_server_url, options=options)
        cls.login_page = IODLoginPage(cls.driver)
        cls.staff_home = StaffHomePage(cls.driver)
        cls.driver_home = DriverHomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

class TestIODLoginLogout(BaseTest):
    def __init__(self, methodName='runTest', user_type=None):
        super().__init__(methodName)
        load_dotenv()
        self.staff_username = os.getenv("STAFF_USERNAME")
        self.driver_username = os.getenv('DRIVER_USERNAME')
        self.password = os.getenv("IOD_PASSWORD")
        self.user_type = user_type
        
    def test_Login(self):
        if self.user_type == 'staff':
            self.login_page.enter_username(self.staff_username)
        elif self.user_type == 'driver':
            self.login_page.enter_username(self.driver_username)
        
        self.login_page.enter_password(self.password)
        self.login_page.click_login()
        
        if self.user_type == 'staff':
            err = self.staff_home.load_staffHome()
            if err != None: print("\nError/Alert Detected:", err)
            
        elif self.user_type == 'driver':
            err = self.driver_home.load_driverHome()
            if err != None: print("\nError/Alert Detected:", err)
            
    def test_Logout(self):
        if self.user_type == 'staff':
            self.staff_home.staff_logout()
        elif self.user_type == 'driver':
            self.driver_home.driver_logout()