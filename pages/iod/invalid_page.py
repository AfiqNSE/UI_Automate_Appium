import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.iod.home_page import DriverHomePage

class InvalidIODPage:
    invalid_list = []
    
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def nav_invalid(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Invalid IOD").click()
    
    #NOTE: The main process
    def load_invalidPage(self):
        if  self.get_invalidDocket() is True:
             self.review_pod()
             self.retake_pod()
             
        else:
            self.driver.back()   
            
        DriverHomePage.load_driverHome(self)
            
    def get_invalidDocket(self) -> bool:
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))

            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')
            
            for item in all_items:
                if item.is_displayed():
                    docket = item.get_attribute('content-desc')
                    self.invalid_list.append(docket)
                                
            shows = True
            
        except TimeoutException:
            shows = False
            raise ValueError("TimeoutException: unable to located [Invalid IOD displayed]")

        return shows
    
    def review_pod(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.invalid_list[0]).click()
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Preview"]').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "JD3")]')))
            time.sleep(1)
            self.driver.back()
            
        except TimeoutException:
            raise ValueError("TimeoutException: unable to located [Review Button]")
        
        time.sleep(2)

    def retake_pod(self):
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Retake"]').click()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Shutter'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done'))).click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Confirm Upload'))).click()

        except TimeoutException:
            raise ValueError("TimeoutException: Unable to locate some element in [Confirm Upload]")
        
        time.sleep(2)
    
        