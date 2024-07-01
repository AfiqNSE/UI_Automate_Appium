from appium import webdriver

from appium.webdriver.common.appiumby import AppiumBy

#TODO: Create Notification test module  
class NotificationPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver


#TODO: Create History test module  
class HistoryPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver


#TODO: Create Analytics test module  
class AnalyticsPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver


#TODO: Create Invalid IOD test module  
class InvalidIODPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver


#TODO: Create Reward test module  
class RewardPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
