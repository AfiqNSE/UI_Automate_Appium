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
        
    def nav_changeMalay(self):
        try:
            err = self.nav_optionButton()
            if err != None: return(err)
            
            err = self.malay_language()
            if err != None: return(err)
            
            time.sleep(2)
               
        except Exception as e:
            return("Error: Unable to perform langauge changes", e)
        
    def nav_changeEnglish(self):
        try:
            err = self.nav_optionButton()
            if err != None: return(err)
            
            err = self.english_language()
            if err != None: return(err)
            
            time.sleep(2)
            
        except Exception as e:
            return("Error: Unable to perform langauge changes", e)
        
    def nav_optionButton(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to find element [Language button]")
    
    def malay_language(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Bahasa Melayu'))).click()
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate [Malay Language]")

    def english_language(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'English'))).click()
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate [English Language]")
        
    def nav_driver_english(self):
        IODComponents.nav_sideBar(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Language').click()
        time.sleep(2)
        
    def nav_driver_bahasa(self):
        IODComponents.nav_sideBar(self)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Bahasa').click()
        time.sleep(2)
