import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.constant_component import Constant
from components.main_component import Components
from pages.home_page import DriverHomePage, StaffHomePage


#NOTE: Been used for search & history (Staff & Driver)
class SearchHistoryPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    #Search logsheet
    def staff_logsheet_search(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_logsheet(Constant.SEARCH_LOGSHEETNO)
    
    #POD camera photo [staff]
    def staff_pod_photoDocket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_PHOTO)
        Components.pod_photo(self)
        StaffHomePage.load_staffHome(self)
    
    #POD upload photo [staff]
    def staff_pod_uploadDocket(self):
        self.nav_search()  
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_UPLOAD)
        Components.pod_upload(self)
        StaffHomePage.load_staffHome(self)
    
    #POD signature [staff]
    def staff_pod_signatureDocket(self):
        self.nav_search()        
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        Components.pod_signature(self)
        StaffHomePage.load_staffHome(self)
    
    #Fail docket [staff]
    def staff_fail_docket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.FAIL_DOCKETNO)
        Components.nav_fail(self)
        StaffHomePage.load_staffHome(self)
    
    #Delay docket [staff] 
    def staff_delay_docket(self):   
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.DELAY_DOCKETNO)
        Components.nav_delay(self)
        StaffHomePage.load_staffHome(self)
    
    #Additional details [staff] 
    def staff_additional(self):   
        self.nav_search()
        # self.search_page.check_search_history()
        self.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        Components.nav_viewSignature(self)
        Components.nav_docketPreview(self)
        
    #POD camera photo [Driver]
    def driver_pod_photoDocket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_PHOTO)
        Components.pod_photo(self)
        DriverHomePage.load_driverHome(self)
    
    #POD upload photo [driver]
    def driver_pod_uploadDocket(self):
        self.nav_search()  
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_UPLOAD)
        Components.pod_upload(self)
        DriverHomePage.load_driverHome(self)
    
    #POD signature [driver]
    def driver_pod_signatureDocket(self):
        self.nav_search()        
        self.option_buttonStaff()
        self.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        Components.pod_signature(self)
        DriverHomePage.load_driverHome(self)
    
    #Fail docket [driver]
    def driver_fail_docket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.FAIL_DOCKETNO)
        Components.nav_fail(self)
        DriverHomePage.load_driverHome(self)
    
    #Delay docket [driver] 
    def driver_delay_docket(self):   
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(Constant.DELAY_DOCKETNO)
        Components.nav_delay(self)
        DriverHomePage.load_driverHome(self)
    
    #Additional details [driver] 
    def driver_additional(self):   
        self.nav_search()
        # self.search_page.check_search_history()
        self.insert_docket(Constant.POD_DOCKETNO_SIGNATURE)
        Components.nav_viewSignature(self)
        Components.nav_docketPreview(self)
    
    #Navigate to search page at Staff 
    def nav_search(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Search').click()
    
    #Navigate to history at Driver
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
            Components.submitButton(self)
                        
            #Wait & get the elements displayed
            Components(self.driver).get_dockets()

            # Do est date time
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
            Components.submitButton(self)
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
                print('TimeoutException: Elements did not appear within the expected time.')
            
        
