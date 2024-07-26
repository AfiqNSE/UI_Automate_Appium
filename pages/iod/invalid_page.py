import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.iod_component import IODComponents
from pages.iod.home_page import DriverHomePage

class InvalidIODPage:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        self.component = IODComponents(self.driver)
        
    def nav_invalid(self):
        err = self.component.nav_sideBar()
        if err != None: return(err)
        
        try:
            #Navigate to inavlid page
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Invalid IOD"))).click()
            
        except TimeoutException:
            self.driver.back()
            return("TimeoutException: Unable to locate element [Invalid IOD button]")
    
    def nav_mainFeatures(self) -> str:
        try:
            dockets = self.get_invalidDocket()
            
            if len(dockets) > 0:
                
                try:
                    WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, dockets[0]))).click()

                    err = self.review_pod()
                    if err != None: return(err)
                    
                    err = self.retake_pod()
                    if err != None: return(err)
                    
                except TimeoutException:
                    return("TimeoutException: Unable to locate element [Specific invalid docket]")  
                
            else:
                self.driver.back()
                return("Alert: Empty invalid iod list")
            
            DriverHomePage.load_driverHome(self)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Invalid IOD button]")
            
    def review_pod(self) -> str:
        try: 
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Preview"]').click()
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: unable to located [Review Button]")
        
    def retake_pod(self) -> str: 
        try:
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Retake"]').click()
            
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()
            
            time.sleep(2)

        except TimeoutException:
            return("TimeoutException: Unable to locate some element in [Confirm Upload]")
        
    def get_invalidDocket(self) -> list:
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            invalid_list = []
            for item in all_items:
                if item.is_displayed():
                    docket = item.get_attribute('content-desc')
                    invalid_list.append(docket)
                                
            return invalid_list
        except TimeoutException:
            return []
    
        