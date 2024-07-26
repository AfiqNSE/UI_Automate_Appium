import unittest
from config import Config
from tests.oms.test_delivered import TestOMSDelivered
from tests.oms.test_homepage import TestOMSHomePage
from tests.oms.test_login_logout import TestOMSLoginLogout
from tests.oms.test_rejection import TestOMSRejection
from tests.oms.test_user import TestOMSUser

if __name__ == '__main__':
    oms_suite = unittest.TestSuite()


    ##OMS App Test
    print("\n*OMS Appium Test:*")
    #OMS -> Login Test
    oms_suite.addTest(TestOMSLoginLogout("test_login"))
    
    # OMS -> HomePage Tests
    oms_suite.addTest(TestOMSHomePage("test_mainFeature"))
    oms_suite.addTest(TestOMSHomePage("test_filterFeature"))
    
    #OMS -> Delivered Test
    oms_suite.addTest(TestOMSDelivered("test_viewDelivered"))
    oms_suite.addTest(TestOMSDelivered("test_rejectOrder"))
    
    #OMS -> Reject Test
    oms_suite.addTest(TestOMSRejection("test_viewReject"))
    oms_suite.addTest(TestOMSRejection("test_closeReject"))
    
    #OMS -> User Test
    oms_suite.addTest(TestOMSUser("test_createUser"))
    oms_suite.addTest(TestOMSUser("test_searchUser"))
    oms_suite.addTest(TestOMSUser("test_existingUser"))
    oms_suite.addTest(TestOMSUser("test_editUser"))
    oms_suite.addTest(TestOMSUser("test_deleteUser"))
    
    #OMS -> Logout Test
    oms_suite.addTest(TestOMSLoginLogout("test_logout"))
    
    unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(oms_suite)