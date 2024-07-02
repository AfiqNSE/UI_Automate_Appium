from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

#TODO: Create Invalid IOD test module  
class InvalidIODPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def nav_invalid(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Invalid IOD").click()
        self.driver.back()
