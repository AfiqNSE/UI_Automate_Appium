import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.iod_component import IODComponents


class AssignPointPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.assign_logsheetNo = os.getenv("ASSIGN_LOGSHEETNO")
        self.driver = driver
        self.component = IODComponents(self.driver)
    
    #Main feature: assign by scan
    def scan_assignPoint(self) -> str:
        try:
            err = self.nav_assignPoint()
            if err == None: 
                
                try:
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode'))).click()
                    self.driver.back()
                
                except TimeoutException:
                    self.driver.back()
                    return("TimeoutException: Unable to locate [Scan Logsheet Barcode]")

            else: return(err)
            
        except Exception as e:
            return("Error: Unable to perform scan assign point due to ", e)

    #Main feature: assign by insert
    def insert_assignPoint(self) -> str:
        self.errorList = []
        
        try:
            err = self.nav_assignPoint()
            if err is None:
                try:
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number'))).click()
                    
                    el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
                    el.send_keys(self.assign_logsheetNo)
                    self.driver.hide_keyboard()
                    self.component.submitButton()
                    
                    dockets = self.get_displayedDocket()
                    
                    if len(dockets) > 0:
                        errFilter = self.check_filter()
                        if errFilter is not None: return errFilter
                        
                        errSelect = self.select_mode(docket= dockets[0])
                        if errSelect is not None: return errSelect
                        
                        errSingle = self.single_assign(docket= dockets[0])
                        if errSingle is not None: return errSingle
                        
                        errMultiple = self.multiple_assign()
                        if errMultiple is not None: return errMultiple
                                                
                    else:
                        self.driver.back()
                        return("Alert: Logsheet is empty")
                        
                except TimeoutException:
                    self.driver.back()
                    return("TimeoutException: Unable to locate [Insert logsheet number button]")
                
            else: return err
            
        except Exception as e:
            return("Error: Unable to perform insert assign point due to", e)

    def nav_assignPoint(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Assign\nPoints'))).click()
        
        except TimeoutException:
            return("TimeoutException: Unable to locate [Assign Points button]")
 
    #NOTE: Check the filter functionality
    def check_filter(self) -> str:
        try:

            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Not Assign'))).click()
            time.sleep(2)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Assigned'))).click()
            time.sleep(2)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Not IOD'))).click()
            time.sleep(2)
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'All'))).click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate some element for filter")
        
    #Check select/deselect all button
    def select_mode(self, docket) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Not Assign'))).click()
            
            errActive = self.component.active_selectMode(docket)
            if errActive is None:
                
                errSelect = self.component.select_all()
                if errSelect is not None: return errSelect
                
                errDeselect = self.component.deselect_all()
                if errDeselect is not None: return errDeselect
                
                errDeactive = self.component.deactive_selectMode()
                if errDeactive != None: return errDeactive
            
            else: 
                return errActive
                
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Not Assign filter]")

    #Asign one docket
    def single_assign(self, docket) -> str: 
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Not Assign'))).click()
            
            try:
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, docket))).click()
                self.component.submitButton()
                time.sleep(2)
                
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('Testing by Appium')
                self.driver.hide_keyboard()
                self.component.submitButton()            
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
                time.sleep(2)
                
            except TimeoutException:
                return("TimeoutException: Unable to select docket to be assign")
            
        except TimeoutException:
            return("TimeoutException: Unable to locate [Not Assign filter]")
    
    #Assign multiple docte       
    def multiple_assign(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Not Assign'))).click()
            
            #Get update list of dockets after do single assign
            updatedDockets = self.get_displayedDocket()
                
            if len(updatedDockets) > 0:
                try:
                    errActive = self.component.active_selectMode(docket=updatedDockets[0])
                    if errActive is None:
                        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, updatedDockets[1]))).click()
                        time.sleep(2)
                        
                        el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
                        el.click()
                        el.send_keys('Multiple Testing by Appium')
                        self.driver.hide_keyboard()
                        self.component.submitButton()                    
                        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
                        time.sleep(2)
                        
                        #Go back to homepage
                        self.driver.back()
                        time.sleep(2)
                        
                    else: return errActive
                
                except TimeoutException:
                    return("TimeoutException: Unable to select docket to be assign")
               
            else:
                self.driver.back()
                return("Alert: Unable to get updated dockets list")

        except TimeoutException:
            return("TimeoutException: Unable to locate [Not Assign filter]")
    
    #NOTE: Get latest element that been display at the UI
    def get_displayedDocket(self):
        
        #Wait for the element to shows up & store the latest
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            dockets_list = []
            for item in all_items:
                if item.is_displayed():
                    dockets_list.append(item.get_attribute("content-desc"))
                    
            return dockets_list
        except TimeoutException:
            return []
        
    
        
        


