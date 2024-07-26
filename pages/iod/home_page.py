import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.iod_component import IODComponents

class StaffHomePage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def load_staffHome(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Management Dashboard')))
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [management dashboard]")
    
    def staff_logout(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button[3]'))).click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate [Logout button]")
                 

class DriverHomePage:
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.present_docket = os.getenv("PRESENT_DOCKET")
        self.past_docket = os.getenv("PAST_DOCKET")
        self.driver = driver
        self.component = IODComponents(self.driver)

    def driver_logout(self):
        self.component.nav_sideBar()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Logout').click()
        time.sleep(2)
    
    def load_driverHome(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Home')))
                    
        except TimeoutException:
            return("TimeoutException: Unable to locate [Home Appbar]")
        
    def logsheet_change(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)'))).click()
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate [Logsheet Change Icon]")
    
    def scan_docket(self) -> str:
        try:
            err = self.option_button()
            if err != None: return(err)
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Docket Barcode'))).click()
            time.sleep(2)
            self.driver.back()
        
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate [Scan Docket Barcode Option]")
    
    def find_presentDocket(self) -> str:
        err = self.option_button()
        if err is None: 
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number'))).click()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(self.present_docket)
                self.driver.hide_keyboard()
                self.component.submitButton()
                time.sleep(2)
                
                #Go back to the main page
                self.driver.back()
                time.sleep(2)
                
            except TimeoutException:
                return("TimeoutException: Unable to locate [Insert Docket Number, present]")
            
        else: return(err)
    
    def find_pastDocket(self) -> str:
        err = self.option_button()
        if err is None: 
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number'))).click()
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(self.past_docket)
                self.driver.hide_keyboard()
                self.component.submitButton()
                time.sleep(2)
                
                #Go back to the main page
                for _ in range(2):
                    self.driver.back()
                time.sleep(2)
                
            except TimeoutException:
                return("TimeoutException: Unable to locate [Insert Docket Number, past]")
            
        else: return(err)

    def scan_logsheet(self) -> str:
        try:
            err = self.option_button()
            if err != None: return(err)
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode'))).click()
            time.sleep(2)
            
            #Go back to the main page
            self.driver.back()
            time.sleep(2)
        
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate [Scan Logsheet Barcode Option]")
    
    def scan_DO(self) -> str:
        try:
            err = self.option_button()
            if err != None: return(err)
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Customer DO Barcode'))).click()
            time.sleep(2)
            
            #Go back to the main page
            self.driver.back()
            time.sleep(2)
        
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate [Scan Customer DO Barcode Option]")
    
    def option_button(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Docket/Logsheet Number'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate [Option Button]")
       
    def driverPage_est(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)').click()

        self.component.get_new_dockets()
        self.component.nav_estDateTime()
        
        time.sleep(2)
        
