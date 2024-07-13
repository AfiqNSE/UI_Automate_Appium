import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.iod_component import IODComponents
from config import Config
from pages.iod.reward_page import RewardPage

class TestDriverReward(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.iod_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.reward = RewardPage(self.driver)
        self.component = IODComponents(self.driver)
        
    def test_reward(self):
        self.component.nav_sideBar()
        self.reward.nav_reward()
        self.reward.load_rewardPage()
