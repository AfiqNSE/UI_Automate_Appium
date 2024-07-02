import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from components.constant_component import Constant
from components.main_component import Components
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LonghaulPage:
    longhaul_list = []
    
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    #Longhaul navigation for staff
    def nav_staff_longhaul(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul\nAcceptance').click()
        Components.cancelButton()
        
    #Longhaul navigation for driver
    def nav_driver_longhaul(self) -> bool:
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Longhaul').click()
        
        try:
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Longhaul')))
            
            self.get_displayedLonghaul()
            time.sleep(1)
            shows = True
                      
        except TimeoutException:
            shows = False
            raise ValueError('TimeoutException: Unable to locate [longhaul page]')
        
        return shows
    
    def option_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Loghaul Number'))).click()
        
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [option button]')
        
    def scan_longhaul(self):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Longhaul Barcode').click()
        Components.cancelButton()
                
    def insert_longhaul(self):
        self.option_button()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Longhaul Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(Constant.SEARCH_LONGHAULNO)
        self.driver.hide_keyboard()
        
        if Constant.SEARCH_LOGSHEETNO != '':
            Components.submitButton()
        
        else:
            raise ValueError('\nNo longhaul number provided')
        
        self.driver.back()
        
    def get_displayedLonghaul(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "LH3")]')
            
            for item in all_items:
                if item.is_displayed():
                    longhaul = item.get_attribute('content-desc')
                    self.longhaul_list.append(longhaul)
            
            print(len(self.longhaul_list))
                    
        except TimeoutException:
            raise ValueError('TimeoutException: Unable to locate [displayed longhaul]')
        
    #TODO: Longhaul POD
    def longhaul_pod(self):
        pass
    
    #TODO: Longhaul_fail
    def longhaul_fail(self):
        pass
    
    
        