import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.main_utils import Utils


# Testing class for Search
class SearchPage():
    new_dockets = []
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_search(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search').click()

    def button_option(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search logsheet/docket').click()

    def scan_logsheet(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode').click()
        self.driver.back()
        
    def insert_logsheet(self, logsheetNO):
        self.button_option()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(logsheetNO)
        self.driver.hide_keyboard()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()

        #Wait & get the elements displayed
        self.get_elements()
         
        self.driver.back()
        
    def scan_docket(self):
        self.button_option()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Docket Barcode').click()
        self.driver.back()

    def insert_docket(self, docketNo):
        # self.button_option()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(docketNo)
        self.driver.hide_keyboard()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()
    
    #TODO: estDateTime docket
    def nav_estDateTime(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.new_dockets[0]).click()
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "Estimation")]'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            pass 
        
    
    #TODO: POD docket
    def nav_pod(self):
        if self.new_dockets != []:
            pass
        else:
            print("No new docket found")
    
    def nav_fail(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Fail').click()
        
        #Choose fail reason
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Fail Reason').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Store Closed'))).click()
        
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
        self.fail_attachment()
        self.remove_attachment()
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Management Dashboard')))
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
         
    def nav_delay(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Delay').click()
        
        #Choose delay reason
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select Delay Reason:').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Truck breakdown'))).click()
        
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
        self.delay_attachment()
        self.remove_attachment()
        
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'SUBMIT').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Management Dashboard')))
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
    
    def fail_attachment(self):
        #Take photo directly
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        self.driver.back()
    
        #Upload Do/Logsheet photo
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'IMG_20240626_034459.jpg, 146 kB, 3:44 AM'))).click()
                
        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
        
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Take Photo"])[2]'))).click()
                
            except TimeoutException:
                 print("Timeout: Elements did not appear within the expected time.")
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'IMG_20240626_034459.jpg, 146 kB, 3:44 AM'))).click()
                
            except TimeoutException:
                print("Timeout: Elements did not appear within the expected time.")
    
    def delay_attachment(self):
        #Take photo directly
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photo').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Take Photos').click()
        self.driver.back()
    
        #Upload attachment
        for _ in range(2):
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Take Photo'))).click()

            except TimeoutException:
                 print("Timeout: Elements did not appear within the expected time.")
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Upload Photo').click()
            
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="IMG_20240626_034459.jpg, 146 kB, 3:44 AM"]/android.widget.RelativeLayout/android.view.View'))).click()
                
            except TimeoutException:
                print("Timeout: Elements did not appear within the expected time.")
    
    def remove_logsheetPhoto(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
    
    def remove_attachment(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'))).click()

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
            
    #NOTE: Get latest element that been display at the UI
    def get_elements(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            for item in all_items:
                if item.is_displayed():
                    docket = item.get_attribute("content-desc")
                    if "NEW" in docket:
                        self.new_dockets.append(docket)

        except TimeoutException:
            print("Timeout: Elements did not appear within the expected time.")
                     