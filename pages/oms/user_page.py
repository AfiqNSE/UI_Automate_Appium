import os
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from components.oms_component import OMSComponents


class OMSUserPage:
    def __init__(self, driver: webdriver.Remote):
        load_dotenv()
        self.displayName_superAdmin = os.getenv("DISPLAYNAME_SUPERADMIN")
        self.userName_superAdmin = os.getenv("USERNAME_SUPERADMIN")
        self.displayName_accAdmin = os.getenv("DISPLAYNAME_ACCADMIN")
        self.userName_accAdmin = os.getenv("USERNAME_ACCADMIN")
        self.displayName_userAdmin = os.getenv("DISPLAYNAME_USERADMIN")
        self.userName_userAdmin = os.getenv("USERNAME_USERADMIN")
        self.displayName_accUser = os.getenv("DISPLAYNAME_ACCUSER")
        self.userName_accUser = os.getenv("USERNAME_ACCUSER")
        self.displayName_user = os.getenv("DISPLAYNAME_USER")
        self.userName_user = os.getenv("USERNAME_USER")
        self.password = os.getenv("OMS_PASSWORD")
        self.searchDisplayName = os.getenv("SEARCH_DISPLAYNAME")
        self.driver = driver
        self.component = OMSComponents(self.driver)
        self.user_list = []

    def create_superAdmin(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            err = self.nav_addUser(_displayName=self.displayName_superAdmin, _userName=self.userName_superAdmin)
            if err is not None: return(err)
            
            err = self.nav_userRole(role='(//android.view.View[@content-desc="SuperAdmin"])[1]')
            if err is not None: return(err)
          
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)
            self.driver.back()
            
        except TimeoutException:
            return('TimeoutException: Cannot find [add user button]')
            
        except Exception as e:
            self.driver.back()
            return("Error: Creating super admin failed: ", e)
        
    def create_accAdmin(self) -> str:
        try:  
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            err = self.nav_addUser(_displayName=self.displayName_accAdmin, _userName=self.userName_accAdmin)
            if err is not None: return(err)
            
            err = self.nav_userRole(role='(//android.view.View[@content-desc="AccAdmin"])[1]')
            if err is not None: return(err)
            
            err = self.nav_userCompany()
            if err is not None: return(err)
            
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)
            self.driver.back()
            
        except TimeoutException:
            return('TimeoutException: Cannot find [add user button]')
            
        except Exception as e:
            self.driver.back()
            return("Error: Creating acc admin failed: ", e)
    
    def create_userAdmin(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            err = self.nav_addUser(_displayName=self.displayName_userAdmin, _userName=self.userName_userAdmin)
            if err is not None: return(err)
            
            err = self.nav_userRole(role='(//android.view.View[@content-desc="UserAdmin"])[1]')
            if err is not None: return(err)
            
            err = self.nav_userCompany()
            if err is not None: return(err)
            
            err = self.nav_userDealer()
            if err is not None: return(err)
    
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)
            self.driver.back()
            
        except TimeoutException:
            return('TimeoutException: Cannot find [add user button]')
            
        except Exception as e:
            self.driver.back()
            return("Error: Creating user admin failed: ", e)
    
    def create_accUser(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            err = self.nav_addUser(_displayName=self.displayName_accUser, _userName=self.userName_accUser)
            if err is not None: return(err)
            
            err = self.nav_userRole(role='(//android.view.View[@content-desc="AccUser"])[1]')
            if err is not None: return(err)
            
            err = self.nav_userCompany()
            if err is not None: return(err)
            
            err = self.nav_userBranch()
            if err is not None: return(err)
            
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)
            self.driver.back()
            
        except TimeoutException:
            return('TimeoutException: Cannot find [add user button]')
            
        except Exception as e:
            self.driver.back()
            return("Error: Creating acc user failed: ", e)
    
    def create_user(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            err = self.nav_addUser(_displayName=self.displayName_user, _userName=self.userName_user)
            if err is not None: return(err)
            
            err = self.nav_userRole(role='(//android.view.View[@content-desc="User"])[1]')
            if err is not None: return(err)
            
            err = self.nav_userCompany()
            if err is not None: return(err)
            
            err = self.nav_userDealer()
            if err is not None: return(err)
            
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)
            
            #Go back to user page and refresh
            self.driver.back()
            self.component.refresh_page()
            time.sleep(2)
            
        except TimeoutException:
            return('TimeoutException [User]: Cannot find [add user button]')
            
        except Exception as e:
            self.driver.back()
            return("Error [User]: Creating user failed: ", e)
    
    #Test to create existing [appium superadmin]
    def create_existingUser(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[2]'))).click()     
            time.sleep(2)
            
            if self.nav_addUser(_displayName=self.displayName_superAdmin, _userName=self.userName_superAdmin) != None: return('Error: Cannot add displayName & userName [Existing superadmin]')
            if self.nav_userRole(role='(//android.view.View[@content-desc="SuperAdmin"])[1]') != None: return('Error: Cannot pick role [Existing superadmin]')
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            time.sleep(2)

            #NOTE: Check error message
            try: 
                el = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.view.View[@content-desc="Username has already been used, please enter a new username"])[1]')))  
                
                if el.is_displayed():
                    self.driver.back()
                
            except TimeoutException:
                self.driver.back()
                return('TimeoutException [User]: Cannot find error message')
            
        except TimeoutException:
            return('TimeoutException [User]: Cannot find add user button')
            
        except Exception as e:
            self.driver.back()
            return("Error [User]: Creating user failed: ", e)
     
    def nav_editUser(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[1]'))).click()     
            
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))

            element.clear()
            element.send_keys('Appium SuperAdmin')
            self.driver.press_keycode(66)
            time.sleep(2)
            
            try:
                #Wait for the element to shows up
                WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')))
                
                #Get the elements
                all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')
                
                self.users = []
                for item in all_items:
                    if item.is_displayed():
                        self.users.append(item.get_attribute('content-desc'))
                    
            except TimeoutException:
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                return("TimeoutException [Edit User]: Unable to locate element [User]" )
            
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.users[0]).click()
            
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Edit"]').click()
            time.sleep(1)
            
            #Edit User Name
            userName = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[2]')))
            time.sleep(2)
            userName.click()
            userName.clear()
            userName.send_keys('AppTest1(Edit)')
            self.driver.hide_keyboard()
            time.sleep(1)
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Submit"]').click()
            
            self.driver.back()
            self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
            self.component.refresh_page()
            time.sleep(2)
            
        except TimeoutException:
            return('TimeoutException [Edit User]: Unable to locate element [Search button]')
           
    def nav_deleteUser(self) -> str:
        user_list = ["Appium SuperAdmin", "Appium AccAdmin", "Appium UserAdmin", "Appium AccUser", "Appium User"]
        try:
            for i in user_list:
                WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[1]'))).click()     
            
                element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
                element.click()
                element.clear()
                element.send_keys(i)
                self.driver.press_keycode(66)
                time.sleep(2)
                
                try:
                    #Wait for the element to shows up
                    WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')))
                    
                    #Get the elements
                    all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')
                    
                    self.users = []
                    for item in all_items:
                        if item.is_displayed():
                            self.users.append(item.get_attribute('content-desc'))
                        
                except TimeoutException:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return("TimeoutException [Delete User]: Unable to locate element [User]" )
                
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.users[0]).click()
                
                #delete method
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Delete"]').click()
                time.sleep(1)
                
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Yes"]').click()
                time.sleep(2)
            
                #Go Back and refresh page
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                self.component.refresh_page()
                time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException [Delete User]: Unable to locate element [Search button]")
               
    def nav_search(self) -> str:
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.widget.Button[1]'))).click()     
            
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))

            element.clear()
            element.send_keys('Appium')
            self.driver.press_keycode(66)
            
            try:
                #Wait for the element to shows up
                WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')))
                
                #Get the elements
                all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View[starts-with(@content-desc, "A")]')
                
                self.user_list = []
                for item in all_items:
                    if item.is_displayed():
                        self.user_list.append(item)
  
                time.sleep(2)
                
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                
                if len(self.user_list) < 5:
                    self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                    return("Error [Search]: Only [" + len(self.user_list) + "] users detected" )
                       
            except TimeoutException:
                self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Cancel"]').click()
                return("TimeoutException [Search]: Unable to locate element [User list]" )
            
        except TimeoutException:
            return("TimeoutException [Search]: Unable to locate element [Search button]")
    
    def nav_addUser(self, _displayName, _userName:str) -> str:
        try:
            #Display Name
            displayName = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[1]')))
            displayName.click()
            displayName.send_keys(_displayName)
            self.driver.hide_keyboard()
            
            #User Name
            userName = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[2]')))
            userName.click()
            userName.send_keys(_userName)
            self.driver.hide_keyboard()
            
            #Password
            password = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[3]')))
            password.click()
            password.send_keys(self.password)
            self.driver.hide_keyboard()
            
            #Confirm Passowrd
            cPassword = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[4]')))
            cPassword.click()
            cPassword.send_keys(self.password)
            self.driver.hide_keyboard()
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Add user button]")
        
    def nav_userRole(self, role) -> str:
        try:
            #Role
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[5]/android.widget.Button[2]'))).click()
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, role))).click()
            time.sleep(1)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [User role button]")
        
    def nav_userCompany(self) -> str:
        try:
            #Company
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[6]/android.widget.Button[2]'))).click()
            
            #Get company list
            companies = self.component.get_company(page='users')
            if len(companies) == 0: return('Error: Unable to get the list of company')
            
            baseTxt = '(//android.view.View[@content-desc="company"])[2]'
            xpath = baseTxt.replace("company", companies[0])
        
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, xpath))).click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Company role button]")
        
    def nav_userDealer(self) -> str:
        try:
            #Dealer
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Select"]/android.widget.Button'))).click()
            
            #Get dealer list
            dealers = self.component.get_dealer(page='users') 
            if len(dealers) == 0: return('Error: Unable to get the list of dealer')
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, dealers[0]))).click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Dealer role button]")
    
    def nav_userBranch(self):
        try:
            #Branch
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.widget.EditText[7]/android.widget.Button[2]'))).click()
            
            #Get branch list
            branches = self.component.get_branch(page='users')
            if len(branches) == 0: return('Error: Unable to get the list of branch')
            
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, branches[0]))).click()
            time.sleep(2)
            
        except TimeoutException:
            return("TimeoutException: Unable to locate element [Dealer role button]")
        
    #NOTE: For future reference
    def get_users(self):
        try:
            #Wait for the element to shows up
            WebDriverWait(self.driver,20).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View')))
            
            #Get the elements
            all_items = self.driver.find_elements(AppiumBy.XPATH, '//android.view.View')
            
            self.list_user = []
            for item in all_items:
                if item.is_displayed():
                    self.list_user.append(item.get_attribute('content-desc'))
                                
        except TimeoutException:
            return("TimeoutException: Unable to locate element [User list]")
    