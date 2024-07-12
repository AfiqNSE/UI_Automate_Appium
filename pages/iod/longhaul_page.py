import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from components.main_component import Components
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.iod.home_page import DriverHomePage


class LonghaulPage:
    load_dotenv()
    pod_longhaulNo = os.getenv("POD_LONGHAULNO")
    fail_longhaulNo = os.getenv("FAIL_LONGHAULNO")
    
    longhaul_list = []
    
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = Components(self.driver)
    
    #Main process driver longhaul    
    def load_longhaulPage(self):
        self.component.nav_sideBar()
        self.nav_driver_longhaul()
        
        if self.get_displayedLonghaul() is True:
            self.driver_longhaul_pod()
            self.driver_longhaul_fail()
            self.longhaul_viewDetails()
            
            for _ in range(2):
                self.driver.back()   
            
        else:
            self.driver.back()   

    def driver_longhaul_pod(self):
        self.insert_longhaul(self.pod_longhaulNo)
        self.pod_longhaul()
        DriverHomePage.load_driverHome(self)
        time.sleep(2)
              
    def driver_longhaul_fail(self):
        self.component.nav_sideBar()
        self.nav_driver_longhaul()
        self.insert_longhaul(self.fail_longhaulNo)      
        self.component.nav_fail()
        DriverHomePage.load_driverHome(self)
        time.sleep(2)

    def longhaul_viewDetails(self):
        self.component.nav_sideBar()
        self.nav_driver_longhaul()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, self.longhaul_list[0]))).click()
        time.sleep(2)

    #Longhaul navigation for staff
    def nav_staff_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul\nAcceptance').click()
        self.component.cancelButton()
        time.sleep(2)
    
    #Longhaul navigation for driver
    def nav_driver_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul').click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul')))
                      
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [longhaul page]')

    def option_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Loghaul Number'))).click()
        
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [option button]')
        
    def scan_longhaul(self):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Longhaul Barcode').click()
        self.component.cancelButton()

                
    def insert_longhaul(self, longhaulNo):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Longhaul Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(longhaulNo)
        self.driver.hide_keyboard()
        
        if longhaulNo != '':
            self.component.submitButton()
        
        else:
            for _ in range(2):
                self.driver.back()  
                 
            raise ValueError('\nNo longhaul number provided')
    
    def get_displayedLonghaul(self) -> bool:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')
            
            for item in all_items:
                if item.is_displayed():
                    longhaul = item.get_attribute('content-desc')
                    self.longhaul_list.append(longhaul)
                    
            if len(self.longhaul_list) > 0:
                return True
            else:
                return False
            
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [displayed longhaul]')
        
    def pod_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'POD').click()
        
        #Add DO/logsheet photo
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add Photos"])[1]'))).click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Take Photo"]').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Done').click()
                
            except TimeoutException:
                raise ValueError("TimeoutException: Unable to locate [Shutter icon]")
    
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [Add photos]')
        
        time.sleep(1)
        
        #Add attachment
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add Photos"])[2]'))).click()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open Gallery').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, Jun 26"]'))).click()
                
            except TimeoutException:
                raise ValueError("TimeoutException: unable to located [Image from gallery]")
            
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [Add photos]')
        
        time.sleep(1)
        
        self.component.submitButton()
        
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="OK"]'))).click()
