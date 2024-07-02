import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.constant_component import Constant
from selenium.webdriver.common.action_chains import ActionChains


# Testing part for IOD Report
class IODReportPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    def nav_report(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Report'))).click()
            
        except TimeoutException:
            raise ValueError("Timeout: Element (Report) did not appear within the expected time.")

    #NOTE:Check if search form visible or not
    def check_form(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Submit')))
            
        except TimeoutException:
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(3)').click()

    def iod_form_data(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()

        time.sleep(5)

    #NOTE:Filter based on Truck No
    def iod_filter_truckNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]').click()

        try:
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            truck_numbers = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        truck_number = item.get_attribute('content-desc')
                        truck_numbers.append(truck_number)

        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear.")
            
        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()
    
    #NOTE:Filter based on Supplier Name
    def iod_filter_supplierName(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Supplier Name').click()

        try:
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            supplier_Names =[]
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        supplier_Name = item.get_attribute('content-desc')
                        supplier_Names.append(supplier_Name)

        except:
            raise ValueError("Timeout: Elements did not appear.")

        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, supplier_Names[i]).click()

        self.driver.back()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

    #NOTE:Filter based on Later Delivery For
    def iod_filter_lateDeliveryFor(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Late Delivery').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
        #NOTE: Reset filter
        #TODO: Fix reset filter at FE for late delivery
        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Less than 14 Days').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show All').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()

    #NOTE:Filter based on Zone
    def iod_filter_zone(self):
        el = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Late Delivery"]')
        
        actions = ActionChains(self.driver)
        x = -400
        y = 0
        
        #Tap the late delivery filter and swipe to left
        actions.move_to_element(el)
        actions.click_and_hold().move_by_offset(xoffset=x, yoffset=y).release().perform()
        
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Zone'))).click()
            
        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear within the expected time.")
        
        try:
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            zone_list = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        zone = item.get_attribute('content-desc')
                        zone_list.append(zone)

        except:
            raise ValueError("Timeout: Elements did not appear.")
        
        for i in range(2):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, zone_list[i]).click()
            
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
        #TODO: Fix Reset filter at FE at FE for zone
        
    def iod_lateDays_orderBy(self):
        #NOTE: Multiple taps to show desc & asc order
        for _ in range(3):
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Late Days').click()

        time.sleep(2)




# Testing part for General Report
class GeneralReportPage:
    #defining constructor  
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def change_report(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'General Report').click()
        self.driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="General Report"])[1]').click()

    def general_form_data(self):
        # Insert Customer name
        try:
            customerName = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText").instance(1)')))
            customerName.click()
            customerName.send_keys('DAIKIN')
            self.driver.hide_keyboard()

        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear.")
  
        # Pick Date From
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]'))).click()
            for _ in range(5):
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, Constant.REPORT_DATEFROM).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()
        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear.")
        
        # Pick Date To
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'))).click()
            for _ in range(2):
                self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)').click()

                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, Constant.REPORT_DATETO).click()
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'OK').click()

        except TimeoutException:
            raise ValueError("Timeout: Elements did not appear.")

        # Click show truck no
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Show Truck No').click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Submit').click()

        time.sleep(5)

    def general_filter_truckNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Truck No"])[1]').click()

        try:
            # Locate the ScrollView container
            scroll_view = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView')

            # Find all direct child views within the ScrollView
            all_items = scroll_view.find_elements(AppiumBy.XPATH, './/android.view.View')

            truck_numbers = []
            for item in all_items:
                if item.is_displayed():
                    if item.get_attribute('content-desc') != "Show All":
                        truck_number = item.get_attribute('content-desc')
                        truck_numbers.append(truck_number)

        except:
            raise ValueError("Timeout: Elements did not appear.")
            
        for i in range(2):
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, truck_numbers[i]).click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)
        
        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()

    def general_filter_jobNo(self):
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Job %"])[1]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, '60% to 90%').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(5)').click()
        time.sleep(2)

        #NOTE: Reset filter
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(5)').click()


