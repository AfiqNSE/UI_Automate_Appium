import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.main_component import Components

class StaffHomePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def load_staffHome(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Management Dashboard')))
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [management dashboard]")
        

class DriverHomePage:
    load_dotenv()
    view_docketNo = os.getenv("VIEW_DOCKET")
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = Components(self.driver)
    
    def load_driverHome(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Home')))
                    
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Home Appbar]")
        
    def logsheet_change(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)'))).click()
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()
            time.sleep(2)
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Logsheet Change Icon]")
    
    def option_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Docket/Logsheet Number'))).click()
        
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Option Button]")
        
    def scan_docket(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Docket Barcode'))).click()
            self.component.cancelButton()
        
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Scan Docket Barcode Option]")
    
    def insert_docket(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number'))).click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(self.view_docketNo)
            
            if self.view_docketNo != '':
                self.component.submitButton()
            else:
                raise ValueError('\nNo logsheet number provided')
            
            self.driver.back()
            time.sleep(2)
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Insert Docket Number Option]")
    
    def scan_logsheet(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode'))).click()
            self.component.cancelButton()
        
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Scan Logsheet Barcode Option]")
    
    def scan_DO(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Customer DO Barcode'))).click()
            self.component.cancelButton()
        
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Scan Customer DO Barcode Option]")
        
    def driverPage_est(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()

        self.component.get_dockets()
        self.component.nav_estDateTime()
        
        time.sleep(2)
        
