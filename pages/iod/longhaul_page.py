import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from components.iod_component import IODComponents
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.iod.home_page import DriverHomePage


class LonghaulPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.pod_longhaulNo = os.getenv("POD_LONGHAULNO")
        self.fail_longhaulNo = os.getenv("FAIL_LONGHAULNO")
        self.driver = driver
        self.component = IODComponents(self.driver)
        self.longhaul_list = []
        
    #Main process for longhaul acceptance
    def nav_staff_longhaul(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul\nAcceptance'))).click()
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Loghaul Acceptance button]")
      
    def nav_driver_longhaul(self) -> str:
        err = self.component.nav_sideBar()
        if err != None: return err
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul'))).click()
            
            #Longhaul page
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul')))
                    
        except TimeoutException:
            return('TimeoutException: Unable to locate [longhaul page]')
        
    def scan_longhaul(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Loghaul Number'))).click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Longhaul Barcode'))).click()
                
                self.driver.back()
                
            except TimeoutException:
                self.driver.back()
                return("TimeoutException: Unable to locate element [Scan Longhaul Barcode]")
        
        except TimeoutException:
            return('TimeoutException: Unable to locate [option button]')
    
    #View longhaul
    def longhaul_viewDetails(self) -> str:
        try:
            longhaul = self.get_displayedLonghaul()
            
            if len(longhaul) > 0:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, longhaul[0]))).click()
                time.sleep(2)
                
                for _ in range(2):
                    self.driver.back()
            
            else:
                self.driver.back()
                return("Error: Empty longhaul")
                
        except TimeoutException:
            return("TimeoutException: Unable to open selected longhaul")
        
    #POD longhaul   
    def driver_longhaul_pod(self) -> str:
        errNo = self.insert_longhaulNo(self.pod_longhaulNo)
        if errNo is None:
            
            errPOD = self.nav_process()
            if errPOD is not None: return errPOD
            
            DriverHomePage.load_driverHome(self)
            time.sleep(2)
            
        else: return errNo
    
    #FAIL longhaul          
    def driver_longhaul_fail(self) -> str:
        errNav = self.nav_driver_longhaul()
        if errNav is not None: return errNav
        
        errNo = self.insert_longhaulNo(self.fail_longhaulNo)
        if errNo is None:
            
            errFail = self.component.nav_fail()
            if errFail is not None: 
                self.driver.back()
                return errFail
            
            DriverHomePage.load_driverHome(self)
            time.sleep(2)
            
        else: return errNo
    
    def insert_longhaulNo(self, longhaulNo) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Loghaul Number'))).click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Longhaul Number'))).click()
                
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(longhaulNo)
                self.driver.hide_keyboard()
                self.component.submitButton()
                
            except TimeoutException:
                return('TimeoutException: Unable to locate [Insert longhaul button]')
        
        except TimeoutException:
            return('TimeoutException: Unable to locate [option button]')
           
    def nav_process(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'POD'))).click()
            
            err = self.pod_process()
            if err is None:
                self.component.submitButton()
                
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@content-desc="OK"]'))).click()
                
            else:
                for _ in range(2):
                    self.driver.back()
                    
                return err
            
        except TimeoutException:
            self.driver.back()
            return('TimeoutException: Unable to locate [POD button]')
        
    def pod_process(self) -> str:
        try:
            #Add DO/logsheet photo
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add Photos"])[1]'))).click()
            self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Take Photo"]').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Done').click()
                
            except TimeoutException:
                return("TimeoutException: Unable to locate [Shutter icon]")
            
            time.sleep(2)
            
            #Add attachment
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Add Photos"])[2]'))).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Open Gallery').click()
                
                try:
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, '1721381865966.jpg, 53.40 kB, Jul 19'))).click()
                    
                except TimeoutException:
                    
                    for _ in range(2):
                        self.driver.back()
                        
                    return("TimeoutException: unable to located [Image from gallery]")
                
            except TimeoutException:
                return('TimeoutException: Unable to locate [Add photos]')
    
        except TimeoutException:
            return('TimeoutException: Unable to locate [Add photos]')
        
    def get_displayedLonghaul(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')
            
            longhaul_list = []
            for item in all_items:
                if item.is_displayed():
                    longhaul_list.append(item.get_attribute('content-desc'))
            
            return longhaul_list
        
        except TimeoutException:
            return []
