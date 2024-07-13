import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from components.iod_component import IODComponents


class LanguagePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def nav_staff_language(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

    def nav_driver_english(self):
        IODComponents.nav_sideBar(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Language').click()
        time.sleep(2)
        
    def nav_driver_bahasa(self):
        IODComponents.nav_sideBar(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bahasa').click()
        time.sleep(2)
    
    #Change to Malay
    def malay_language(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Bahasa Melayu'))).click()
        except TimeoutException:
            print("TimeoutException: Unable to locate [Malay Language]")

    #change to English
    def english_language(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'English'))).click()
        except TimeoutException:
            print("TimeoutException: Unable to locate [English Language]")
