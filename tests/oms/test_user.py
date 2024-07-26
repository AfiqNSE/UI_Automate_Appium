import unittest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from components.oms_component import OMSComponents
from config import Config
from pages.oms.user_page import OMSUserPage

class TestOMSUser(unittest.TestCase):
    def setUp(self):
        options = UiAutomator2Options().load_capabilities(Config.oms_capabilities)
        self.driver = webdriver.Remote(Config.appium_server_url, options=options)
        self.errorList = []
        self.user_page = OMSUserPage(self.driver)
        self.component = OMSComponents(self.driver)
    
    #Create users
    def test_createUser(self):
        #Nav to user tab
        self.component.nav_users()
        
        #Add users
        err = self.user_page.create_superAdmin() #create SuperAdmin
        if err != None:
            self.errorList.append(err)
            
        err = self.user_page.create_accAdmin() #create accAdmin
        if err != None:
            self.errorList.append(err)
            
        err = self.user_page.create_userAdmin() #create userAdmin
        if err != None:
            self.errorList.append(err)
            
        err = self.user_page.create_accUser() #create accUser
        if err != None:
            self.errorList.append(err)
            
        err = self.user_page.create_user() #create user
        if err != None:
            self.errorList.append(err)
        
        if len(self.errorList) > 0:
            print("\n [", len(self.errorList), "] Error/Alert Detected:")
            for error in self.errorList:
                print(error)
    
    #Search created users
    def test_searchUser(self):
        err = self.user_page.nav_search()
        if err != None: print("\nError/Alert Detected:", err)
    
    #Test create existing user            
    def test_existingUser(self):
        err = self.user_page.create_existingUser()
        if err != None: print("\nError/Alert Detected:", err)

    #Edit created user
    def test_editUser(self):
        err = self.user_page.nav_editUser()
        if err != None: print("\nError/Alert Detected:", err)
    
    #Delete created user       
    def test_deleteUser(self):
        err = self.user_page.nav_deleteUser()
        if err != None: print("\nError/Alert Detected:", err)
    
    def tearDown(self):
        self.driver.quit()   