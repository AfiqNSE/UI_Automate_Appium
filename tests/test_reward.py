import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver

from components.main_component import Components
from config import Config
from pages.driver_page import RewardPage

class TestDriverReward(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.reward = RewardPage(self.driver)
        self.component = Components(self.driver)
        
    def test_reward(self):
        self.component.nav_sideBar()
        self.reward.nav_reward()
