import unittest
from config import Config
from tests.iod.test_analytics import TestDriverAnalytics, TestStaffAnalytics
from tests.iod.test_approve import TestStaffApprove
from tests.iod.test_assign import TestStaffAssign
from tests.iod.test_invalid import TestDriverInvalid
from tests.iod.test_language import TestStaffLanguage, TestDriverLanguage
from tests.iod.test_login_logout import TestIODLoginLogout
from tests.iod.test_longhaul import TestStaffLonghaul, TestDriverLonghaul
from tests.iod.test_report import TestStaffReport
from tests.iod.test_reward import TestDriverReward
from tests.iod.test_search import TestDriverSearch, TestStaffSearch
from tests.iod.test_notification import TestNotification
from tests.iod.test_homepage import TestStaffHome, TestDriverHome
from tests.oms.test_delivered import TestOMSDelivered
from tests.oms.test_homepage import TestOMSHomePage
from tests.oms.test_login_logout import TestOMSLogin
from tests.oms.test_user import TestOMSUser


if __name__ == '__main__':
    loader = unittest.TestLoader()
    iod_suite = unittest.TestSuite()
    oms_suite = unittest.TestSuite()

    ##IOD App Staff Test
    #print("\nIOD Staff Appium Test:")
    iod_suite.addTest(TestIODLoginLogout("test_Login", user_type='staff'))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffHome)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffLanguage)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffLonghaul)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffApprove)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffSearch)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffAssign)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffAnalytics)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestStaffReport)) 
    iod_suite.addTest(TestIODLoginLogout("test_Logout", user_type='staff'))

    ##IOD App Driver Test
    #print("\nIOD Driver Appium Test:")
    iod_suite.addTest(TestIODLoginLogout("test_Login", user_type='driver'))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverHome))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestNotification)) 
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverLonghaul))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverSearch))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverAnalytics))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverInvalid))
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverReward))
    iod_suite.addTest(TestIODLoginLogout("test_Logout", user_type='driver'))

    ##OMS App Test
    print("\n*OMS Appium Test*")
    #OMS -> Login Test
    oms_suite.addTests(loader.loadTestsFromTestCase(TestOMSLogin))
    
    #OMS -> HomePage Test
    oms_suite.addTests(loader.loadTestsFromTestCase(TestOMSHomePage))
    
    #OMS -> Delivered Test
    oms_suite.addTests(loader.loadTestsFromTestCase(TestOMSDelivered))
    
    #OMS -> User Test
    oms_suite.addTest(TestOMSUser("test_createUser"))
    oms_suite.addTest(TestOMSUser("test_searchUser"))
    oms_suite.addTest(TestOMSUser("test_existingUser"))
    oms_suite.addTest(TestOMSUser("test_editUser"))
    oms_suite.addTest(TestOMSUser("test_deleteUser"))
    
    #Run Test
    # unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(iod_suite)
    unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(oms_suite)



