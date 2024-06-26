from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# Testing class for Language
class StaffLanguagePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def change_staff_language(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
        
        #Change to Malay
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bahasa Melayu').click()

        #change to English
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'English').click()