import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.iod_component import IODComponents
from pages.iod.home_page import DriverHomePage, StaffHomePage


#NOTE: Been used for search & history (Staff & Driver)
class SearchHistoryPage:
    load_dotenv()
    logsheetNo = os.getenv("SEARCH_LOGSHEETNO")
    staff_photo_docketNo = os.getenv("STAFF_DOCKETNO_PHOTO")
    staff_upload_docketNo = os.getenv("STAFF_DOCKETNO_UPLOAD")
    staff_signature_docketNo = os.getenv("STAFF_DOCKETNO_SIGNATURE")
    driver_photo_docketNo = os.getenv("DRIVER_DOCKETNO_PHOTO")
    driver_upload_docketNo = os.getenv("DRIVER_DOCKETNO_UPLOAD")
    driver_signature_docketNo = os.getenv("DRIVER_DOCKETNO_SIGNATURE")
    view_docketNo = os.getenv("VIEW_DOCKET")
    fail_docketNo = os.getenv("FAIL_DOCKETNO")
    delay_docketNo = os.getenv("DELAY_DOCKETNO")
    
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = IODComponents(self.driver)

    #Search logsheet
    def staff_logsheet_search(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_logsheet(self.logsheetNo)
        time.sleep(3)
    
    #POD camera photo [staff]
    def staff_pod_photoDocket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(self.staff_photo_docketNo)
        self.component.pod_photo()
        StaffHomePage.load_staffHome(self)
        time.sleep(3)
    
    #POD upload photo [staff]
    def staff_pod_uploadDocket(self):
        self.nav_search()  
        self.option_buttonStaff()
        self.insert_docket(self.staff_upload_docketNo)
        self.component.pod_upload()
        StaffHomePage.load_staffHome(self)
        time.sleep(3)
    
    #POD signature [staff]
    def staff_pod_signatureDocket(self):
        self.nav_search()        
        self.option_buttonStaff()
        self.insert_docket(self.staff_signature_docketNo)
        self.component.pod_signature()
        StaffHomePage.load_staffHome(self)
        time.sleep(3)
    
    #Fail docket [staff]
    def staff_fail_docket(self):
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(self.fail_docketNo)
        self.component.nav_fail()
        StaffHomePage.load_staffHome(self)
        time.sleep(3)
    
    #Delay docket [staff] 
    def staff_delay_docket(self):   
        self.nav_search()
        self.option_buttonStaff()
        self.insert_docket(self.delay_docketNo)
        self.component.nav_delay()
        StaffHomePage.load_staffHome(self)
        time.sleep(3)
    
    #Additional details [staff] 
    def staff_additional(self):   
        self.nav_search()
        self.option_buttonStaff()
        # self.search_page.check_search_history()
        self.insert_docket(self.view_docketNo)
        self.component.nav_viewSignature()
        self.component.nav_docketPreview()
        time.sleep(3)
        
    #POD camera photo [Driver]
    def driver_pod_photoDocket(self):
        self.component.nav_sideBar()
        self.nav_history()
        self.option_buttonDriver()
        self.insert_docket(self.driver_photo_docketNo)
        self.component.pod_photo()
        DriverHomePage.load_driverHome(self)
        time.sleep(3)
    
    #POD upload photo [driver]
    def driver_pod_uploadDocket(self):
        self.component.nav_sideBar()
        self.nav_history()  
        self.option_buttonDriver()
        self.insert_docket(self.driver_upload_docketNo)
        self.component.pod_upload()
        DriverHomePage.load_driverHome(self)
        time.sleep(3)
    
    #POD signature [driver]
    def driver_pod_signatureDocket(self):
        self.component.nav_sideBar()
        self.nav_history()        
        self.option_buttonDriver()
        self.insert_docket(self.driver_signature_docketNo)
        self.component.pod_signature()
        DriverHomePage.load_driverHome(self)
        time.sleep(3)
    
    #Fail docket [driver]
    def driver_fail_docket(self):
        self.component.nav_sideBar()
        self.nav_history()
        self.option_buttonDriver()
        self.insert_docket(self.fail_docketNo)
        self.component.nav_fail()
        DriverHomePage.load_driverHome(self)
        time.sleep(3)
    
    #Delay docket [driver] 
    def driver_delay_docket(self):   
        self.component.nav_sideBar()
        self.nav_history()
        self.option_buttonDriver()
        self.insert_docket(self.delay_docketNo)
        self.component.nav_delay()
        DriverHomePage.load_driverHome(self)
        time.sleep(3)
    
    #Additional details [driver] 
    def driver_additional(self):   
        self.component.nav_sideBar()
        self.nav_history()
        self.option_buttonDriver()
        # self.search_page.check_search_history()
        self.insert_docket(self.view_docketNo)
        self.component.nav_viewSignature()
        self.component.nav_docketPreview()
        time.sleep(3)
    
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
            self.component.submitButton()
                        
            #Wait & get the elements displayed
            self.component.get_dockets()

            # Do est date time
            self.component.nav_estDateTime()
            
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
            self.component.submitButton()
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
                    history_list.append(history)
                    
            if(len(history_list) != 0):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.signature_docketNo).click()
                time.sleep(2)
                self.driver.back()
                
            else:
                pass
            
        except TimeoutException:
                print('TimeoutException: unable to located [Search History]')
            
        
