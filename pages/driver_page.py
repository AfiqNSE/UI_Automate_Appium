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
        
    def nav_history(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "History").click()
        self.driver.back()


#TODO: Create Invalid IOD test module  
class InvalidIODPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def nav_invalid(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Invalid IOD").click()
        self.driver.back()


#TODO: Create Reward test module  
class RewardPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def nav_reward(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Reward").click()
        self.driver.back()
