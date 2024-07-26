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


class SearchHistoryPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.search_logsheetNo = os.getenv("SEARCH_LOGSHEETNO")
        self.staff_photo_docketNo = os.getenv("STAFF_DOCKETNO_PHOTO")
        self.staff_upload_docketNo = os.getenv("STAFF_DOCKETNO_UPLOAD")
        self.staff_signature_docketNo = os.getenv("STAFF_DOCKETNO_SIGNATURE")
        self.driver_photo_docketNo = os.getenv("DRIVER_DOCKETNO_PHOTO")
        self.driver_upload_docketNo = os.getenv("DRIVER_DOCKETNO_UPLOAD")
        self.driver_signature_docketNo = os.getenv("DRIVER_DOCKETNO_SIGNATURE")
        self.driver_completed_logsheet = os.getenv("COMPLETED_LOGSHEET")
        self.view_docketNo = os.getenv("VIEW_DOCKET")
        self.fail_docketNo = os.getenv("FAIL_DOCKETNO")
        self.delay_docketNo = os.getenv("DELAY_DOCKETNO")
        self.driver = driver
        self.component = IODComponents(self.driver)
        
    #Search logsheet
    def staff_docket_estDateTime(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_logsheet()
                if errInsert is not None:
                    
                    self.driver.back()
                    return errInsert

                #Go back to homepage
                self.driver.back()
                StaffHomePage.load_staffHome(self)
                time.sleep(2)
                
            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
        
    #POD camera photo [staff]
    def staff_pod_photoDocket(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.staff_photo_docketNo)
                if errInsert is None:
                    
                    errPod = self.component.pod_photo()
                    if errPod is None:
                        
                        #Go back to homepage
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                        
                    else:
                        self.driver.back()
                        return errPod
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch 
    
    #POD upload photo [staff]
    def staff_pod_uploadDocket(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.staff_upload_docketNo)
                if errInsert is None:
                    
                    errPod = self.component.pod_upload()
                    if errPod is None:
                        
                        #Go back to homepage
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                        
                    else:
                        self.driver.back()
                        return errPod
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
    
    #POD signature [staff]
    def staff_pod_signatureDocket(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.staff_signature_docketNo)
                if errInsert is None:
                    
                    errPod = self.component.pod_signature()
                    if errPod is None:
                        
                        #Go back to homepage
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                        
                    else:
                        self.driver.back()
                        return errPod
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
        
    #Additional details [staff] 
    def staff_additional(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.view_docketNo)
                if errInsert is None:
                    
                    errSign = self.component.nav_viewSignature()
                    if errSign is not None: print(errSign)
                    
                    errPre = self.component.nav_docketPreview()
                    if errPre is None:
                        #Go back to homepage
                        self.driver.back()
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                    
                    else:   
                        self.driver.back()  
                        return(errPre)
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
        
    #Fail docket [staff]
    def staff_fail_docket(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.fail_docketNo)
                if errInsert is None:
                    
                    errFail = self.component.nav_fail()
                    if errFail is None:
                        
                        #Go back to homepage
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                        
                    else:
                        self.driver.back()
                        return errFail
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
    
    #Delay docket [staff] 
    def staff_delay_docket(self):
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.delay_docketNo)
                if errInsert is None:
                    
                    errDelay = self.component.nav_delay()
                    if errDelay is None:
                        
                        #Go back to homepage
                        StaffHomePage.load_staffHome(self)
                        time.sleep(2)
                        
                    else:
                        self.driver.back()
                        return errDelay
                        
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
        
    #POD camera photo [Driver]
    def driver_pod_photoDocket(self) -> str:
        errSide = self.component.nav_sideBar()
        if errSide is None:
            
            errHistory = self.nav_history()
            if errHistory is None:
                
                errOption = self.option_button()
                if errOption is None:
                    
                    errInsert = self.insert_docket(self.driver_photo_docketNo)
                    if errInsert is None:
                        
                        errPod = self.component.pod_photo()
                        if errPod is None:
                            
                            #Go back to homepage
                            DriverHomePage.load_driverHome(self)
                            time.sleep(2)
                            
                        else:
                            self.driver.back()
                            return errPod
                            
                    else:
                        self.driver.back()
                        return errInsert

                else: 
                    self.driver.back()
                    return errOption
                
            else:
                self.driver.back()
                return errHistory
            
        else: 
            return errSide
    
    #POD upload photo [driver]
    def driver_pod_uploadDocket(self) -> str:
        errSide = self.component.nav_sideBar()
        if errSide is None:
            
            errHistory = self.nav_history()
            if errHistory is None:
                
                errOption = self.option_button()
                if errOption is None:
                    
                    errInsert = self.insert_docket(self.driver_upload_docketNo)
                    if errInsert is None:
                        
                        errPod = self.component.pod_upload()
                        if errPod is None:
                            
                            #Go back to homepage
                            DriverHomePage.load_driverHome(self)
                            time.sleep(2)
                            
                        else:
                            self.driver.back()
                            return errPod
                            
                    else:
                        self.driver.back()
                        return errInsert

                else: 
                    self.driver.back()
                    return errOption
                
            else:
                self.driver.back()
                return errHistory
            
        else: 
            return errSide
    
    #POD signature [driver]
    def driver_pod_signatureDocket(self):
        errSide = self.component.nav_sideBar()
        if errSide is None:
            
            errHistory = self.nav_history()
            if errHistory is None:
                
                errOption = self.option_button()
                if errOption is None:
                    
                    errInsert = self.insert_docket(self.driver_signature_docketNo)
                    if errInsert is None:
                        
                        errPod = self.component.pod_signature()
                        if errPod is None:
                            
                            #Go back to homepage
                            DriverHomePage.load_driverHome(self)
                            time.sleep(2)
                            
                        else:
                            self.driver.back()
                            return errPod
                            
                    else:
                        self.driver.back()
                        return errInsert

                else: 
                    self.driver.back()
                    return errOption
                
            else:
                self.driver.back()
                return errHistory
            
        else: 
            return errSide
    
    #View completed jobs [driver] 
    def driver_completed(self) -> str:
        errSearch = self.nav_search()
        if errSearch is None:
            
            errOption = self.option_button()
            if errOption is None:
                
                errInsert = self.insert_docket(self.driver_completed_logsheet)
                if errInsert is None:
                    
                    dockets = self.component.get_dockets()
                    if len(dockets) > 0: 
                        try:
                            
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, dockets[0]))).click()
                            time.sleep(2)
                            
                            errPre = self.component.nav_docketPreview()
                            if errPre is None: 
                                
                                #Go back to homepage
                                for _ in range(3):
                                    self.driver.back()
                                    
                                DriverHomePage.load_driverHome(self)
                                time.sleep(2)
                                
                            else:   
                                for _ in range(3):
                                    self.driver.back()
                                    
                                return(errPre)

                        except TimeoutException:
                            for _ in range(2):
                                    self.driver.back()
                                    
                            return("TimeoutException: Unable to locate selected docket")
                    
                    else: 
                        self.driver.back()
                        return("Error: Empty logsheet")
                            
                else:
                    self.driver.back()
                    return errInsert

            else: 
                self.driver.back()
                return errOption
            
        else: 
            return errSearch
    
    #Fail docket [driver]
    def driver_fail_docket(self):
        errSide = self.component.nav_sideBar()
        if errSide is None:
            
            errHistory = self.nav_history()
            if errHistory is None:
                
                errOption = self.option_button()
                if errOption is None:
                    
                    errInsert = self.insert_docket(self.fail_docketNo)
                    if errInsert is None:
                        
                        errFail = self.component.nav_fail()
                        if errFail is None:
                            
                            #Go back to homepage
                            DriverHomePage.load_driverHome(self)
                            time.sleep(2)
                            
                        else:
                            self.driver.back()
                            return errFail
                            
                    else:
                        self.driver.back()
                        return errInsert

                else: 
                    self.driver.back()
                    return errOption
                
            else:
                self.driver.back()
                return errHistory
            
        else: 
            return errSide
    
    #Delay docket [driver] 
    def driver_delay_docket(self):
        errSide = self.component.nav_sideBar()
        if errSide is None:
            
            errHistory = self.nav_history()
            if errHistory is None:
                
                errOption = self.option_button()
                if errOption is None:
                    
                    errInsert = self.insert_docket(self.delay_docketNo)
                    if errInsert is None:
                        
                        errDelay = self.component.nav_delay()
                        if errDelay is None:
                            
                            #Go back to homepage
                            DriverHomePage.load_driverHome(self)
                            time.sleep(2)
                            
                        else:
                            self.driver.back()
                            return errDelay
                            
                    else:
                        self.driver.back()
                        return errInsert

                else: 
                    self.driver.back()
                    return errOption
                
            else:
                self.driver.back()
                return errHistory
            
        else: 
            return errSide
    
    #Navigate to search page at Staff 
    def nav_search(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Search'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Search button]")
    
    #Navigate to history at Driver
    def nav_history(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'History'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [History button]")
    
    #option button   
    def option_button(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Search logsheet/docket'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Options button]")

    def scan_logsheet(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode').click()
        self.driver.back()
        
    def insert_logsheet(self) -> str:
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))).send_keys(self.search_logsheetNo)
            self.driver.hide_keyboard()
            self.component.submitButton()
                            
            dockets = self.component.get_new_dockets()
            if len(dockets) > 0:
                errEst = self.component.nav_estDateTime(docket=dockets[0])
                if errEst is not None: return errEst
                    
            else:
                self.driver.back()
                return('Error: No new docket in the logsheet')
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate element [Insert logsheet number button]")
    
    #NOTE: KIV for now since we dont have upload barcode feaure  
    def scan_docket(self):
        self.option_buttonStaff()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Docket Barcode').click()
        self.driver.back()

    def insert_docket(self, docketNo) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Docket Number'))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'))).send_keys(docketNo)
            self.driver.hide_keyboard()
            self.component.submitButton()
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate some element [Insert docket number button]") 

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
            
        
