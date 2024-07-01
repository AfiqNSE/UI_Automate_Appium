import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from config import Config

class TestDriverAnalytics(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
