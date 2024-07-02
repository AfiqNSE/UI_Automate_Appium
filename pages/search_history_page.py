import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.constant_component import Constant
from components.main_component import Components


#NOTE: Been used for search & history (Staff & Driver)
class SearchHistoryPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_search(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search').click()
        
    def nav_history(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'History').click()

    def option_buttonDriver(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan/Insert Docket Number').click()
        
    def option_buttonStaff(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search logsheet/docket').click()

    def scan_logsheet(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode').click()
        self.driver.back()
        
    def insert_logsheet(self, logsheetNo):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(logsheetNo)
        self.driver.hide_keyboard()
        
        if logsheetNo != '':
            Components.submitButton()
                        
            #Wait & get the elements displayed
            Components(self.driver).get_dockets()

            # Do sst date time
            Components(self.driver).nav_estDateTime()
            
        else:
            raise ValueError('\nNo logsheet number provided')
        
        #Go back to homepage
        for _ in range(2):
            self.driver.back()
    
    #NOTE: KIV for now since we dont have upload barcode feaure  
    def scan_docket(self):
        self.option_buttonStaff()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Docket Barcode').click()
        self.driver.back()

    def insert_docket(self, docketNo):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(docketNo)
        self.driver.hide_keyboard()
        
        if docketNo != "":
            Components.submitButton()
        else:
            raise ValueError('\nNo docket number provided')    

    #TODO: Fix search history not detecting the "content-desc" attr
    def check_search_history(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View')
            
            history_list = []
            for item in all_items:
                if item.is_displayed():
                    history = item.get_attribute("content-desc")
                    print(history)
                    history_list.append(history)
            
            print(history_list)
                    
            if(len(history_list) != 0):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, Constant.POD_DOCKETNO_SIGNATURE).click()
                time.sleep(1)
                self.driver.back()
            
        except TimeoutException:
                print('Timeout: Elements did not appear within the expected time.')
            
        
