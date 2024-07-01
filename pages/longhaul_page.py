import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from components.main_component import Components, Constant
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LonghaulPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    #Longhaul navigation for staff
    def nav_staff_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul\nAcceptance').click()
        Components.cancelButton(self)
        
    #Longhaul navigation for driver
    def nav_driver_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul')))
            
            self.get_displayedLonghaul()
            time.sleep(1)  
                      
        except TimeoutException:
            raise ValueError('Timeout: Elements (Longhaul) did not appear within the expected time.')
        
    def option_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Loghaul Number'))).click()
        
        except TimeoutException:
            raise ValueError('Timeout: Elements (Option button) did not appear within the expected time.')
        
    def scan_longhaul(self):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Longhaul Barcode').click()
        Components.cancelButton(self)
                
    def insert_longhaul(self):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Longhaul Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(Constant.SEARCH_LONGHAULNO)
        self.driver.hide_keyboard()
        
        if Constant.SEARCH_LOGSHEETNO != '':
            Components.submitButton(self)
        
        else:
            raise ValueError('\nNo longhaul number provided')
        
        self.driver.back()
        
    def get_displayedLonghaul(self):
        try:
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')
            
            longhaul_list = []
            
            for item in all_items:
                if item.is_displayed():
                    longhaul = item.get_attribute('content-desc')
                    longhaul_list.append(longhaul)
            
            print(len(longhaul_list))
                    
        except TimeoutException:
            raise ValueError('Timeout: Elements (Longhaul) did not appear within the expected time.')
        
    #TODO: Longhaul POD
    def longhaul_pod(self):
        pass
    
    #TODO: Longhaul_fail
    def longhaul_fail(self):
        pass
    
    
        