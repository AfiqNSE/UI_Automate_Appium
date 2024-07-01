from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from components.main_component import Components


# Testing class for Language
class LanguagePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def nav_staff_language(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

    def nav_driver_language(self):
        Components.nav_sideBar(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Language').click()
    
    def malay_language(self):
        #Change to Malay
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Bahasa Melayu'))).click()
        except TimeoutException:
            print("Timeout Exception")

    def english_language(self):
        #change to English
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'English'))).click()
        except TimeoutException:
            print("Timeout Exception")
