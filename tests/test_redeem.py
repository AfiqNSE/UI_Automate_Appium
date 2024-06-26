import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver


from config import Config
from pages.staff_page import ApproveRedeemPage

class TestApproveRedeem(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.approve_page = ApproveRedeemPage(self.driver)

    def test_approve(self):
        self.approve_page.nav_redeem()
