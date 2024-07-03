import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.main_component import Components


# Testing part for Assign Point
class AssignPointPage:
    load_dotenv()
    assign_logsheetNo = os.getenv("ASSIGN_LOGSHEETNO")
    assign_dockets = []

    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def nav_assignPoint(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assign\nPoints').click()

    def scan_logsheet(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Scan Logsheet Barcode').click()
        self.driver.back()

    def insert_logsheet(self):
        self.nav_assignPoint()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Insert Logsheet Number').click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys(self.assign_logsheetNo)
        self.driver.hide_keyboard()
        Components.submitButton(self)

    #NOTE: Check the filter functionality
    def check_filter(self):
        self.get_AssignDockets()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not IOD').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'All').click()
        
    def select_mode(self):
        #Check select/deselect all button
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        Components(self.driver).nav_selectMode(self.assign_dockets)
        Components(self.driver).select_all()
        Components(self.driver).deselect_all()
        Components(self.driver).exit_selectMode()
        
    def single_assign(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        
        if self.assign_dockets != []:
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.assign_dockets[0]).click()

            # Assign docket
            Components.submitButton()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('Testing by Appium')
            self.driver.hide_keyboard()
            Components.submitButton()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()
        else:
            raise ValueError("No docket to be assign")
            
    def multiple_assign(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Not Assign').click()
        
        #Get latest element after do single assign
        self.get_AssignDockets()
        
        if self.assign_dockets != []: 
            element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.assign_dockets[0])
            self.driver.execute_script('mobile: longClickGesture', {'elementId': element.id})

            for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.assign_dockets[i+1]).click()

            el = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
            el.click()
            el.send_keys('Multiple Testing by Appium')
            time.sleep(1)
            self.driver.hide_keyboard()
            Components.submitButton()
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Assigned').click()

        else:
            raise ValueError("No docket to be assign")
            
        
    #NOTE: Get latest element that been display at the UI
    def get_AssignDockets(self):
        #Wait for the element to shows up & store the latest
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            for item in all_items:
                if item.is_displayed():
                    docketNo = item.get_attribute("content-desc")
                    if "Haven't Assign Points" in docketNo:
                        self.assign_dockets.append(docketNo)
                    else:
                        pass
                   
        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear within the expected time.")


