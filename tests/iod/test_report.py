import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from config import Config
from pages.iod.report_page import ReportsPage


class TestIODReport(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.report_page = ReportsPage(self.driver)

    def test_iodReport(self):
        errrorList = self.report_page.iod_report()
        if errrorList != []:
            print("\n [", len(errrorList), "] Error/Alert Detected:")
            for error in errrorList:
                print(error)
    
    def test_generalReport(self):
        errrorList = self.report_page.general_report()
        if errrorList != []:
            print("\n [", len(errrorList), "] Error/Alert Detected:")
            for error in errrorList:
                print(error)

    def tearDown(self):
        self.driver.quit()
