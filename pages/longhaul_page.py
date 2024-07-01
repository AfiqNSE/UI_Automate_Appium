from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from components.main_component import Components

# Testing class for Longhaul Acceptance
class LonghaulPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    #Longhaul navigation for staff
    def nav_staff_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul\nAcceptance').click()
        Components.cancelButton()
        
    #Longhaul navigation for driver
    def nav_driver_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul').click()
        self.driver.back()