import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config
from pages.staff_page import IODReportPage, GeneralReportPage 

class TestStaffReport(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.iod_page = IODReportPage(self.driver)
        self.general_page = GeneralReportPage(self.driver)

    def test_01_iod_report(self):
        self.iod_page.nav_report()
        self.iod_page.check_form()
        self.iod_page.iod_form_data()
        self.iod_page.iod_filter_truckNo()
        self.iod_page.iod_filter_supplierName()
        self.iod_page.iod_filter_lateDeliveryFor()
        self.iod_page.iod_filter_zone()
        self.iod_page.iod_lateDays_orderBy()

    def test_02_general_report(self):
        self.general_page.change_report()
        self.iod_page.check_form()
        self.general_page.general_form_data()
        self.general_page.general_filter_truckNo()
        self.iod_page.iod_filter_supplierName()
        self.general_page.general_filter_jobNo()
