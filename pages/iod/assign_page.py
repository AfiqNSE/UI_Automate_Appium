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
    load_dotenv()
    assign_logsheetNo = os.getenv("ASSIGN_LOGSHEETNO")
    dockets_list = []

    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = IODComponents(self.driver)

    def nav_assignPoint(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assign\nPoints').click()

    def scan_logsheet(self):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode'))).click()
            
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Scan Logsheet Barcode]")
        
        self.driver.back()

    def insert_logsheet(self):
        self.nav_assignPoint()
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number'))).click()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(self.assign_logsheetNo)
            self.driver.hide_keyboard()
            
            if self.assign_logsheetNo != '':
                self.component.submitButton()
            else:
                self.driver.back()
                
        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate [Scan Logsheet Barcode]")
 
    #NOTE: Check the filter functionality
    def check_filter(self):
        self.get_displayedDockets()
        time.sleep(2)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not IOD').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'All').click()
    
    #Check select/deselect all button
    def select_mode(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        self.component.nav_selectMode(self.dockets_list)
        self.component.select_all()
        # self.component.deselect_all()
        self.component.exit_selectMode()
        
    def single_assign(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        
        if self.dockets_list != []:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.dockets_list[0]).click()

            # Assign docket
            self.component.submitButton()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('Testing by Appium')
            self.driver.hide_keyboard()
            self.component.submitButton()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
            time.sleep(2)
            
        else:
            raise ValueError("No docket to be assign")
            
    def multiple_assign(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        
        #Get latest element after do single assign
        self.get_displayedDockets()
        time.sleep(2)
                
        if self.dockets_list != []:
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.dockets_list[0])
            self.driver.execute_script('mobile: longClickGesture', {'elementId': element.id})

            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.dockets_list[i+1]).click()

            el = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
            el.click()
            el.send_keys('Multiple Testing by Appium')
            self.driver.hide_keyboard()
            self.component.submitButton()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
            time.sleep(2)

        else:
            raise ValueError("No docket to be assign")
        
        self.driver.back()       
        
    #NOTE: Get latest element that been display at the UI
    def get_displayedDockets(self):
        
        #Wait for the element to shows up & store the latest
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            self.dockets_list = []
            for item in all_items:
                if item.is_displayed():
                    docketNo = item.get_attribute("content-desc")
                    self.dockets_list.append(docketNo)
                   
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [displayed docket]")
        
        


