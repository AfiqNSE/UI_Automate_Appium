import unittest
from config import Config
from tests.iod.test_leaderboard import TestIODLeaderboard
from tests.iod.test_approve import TestIODApprove
from tests.iod.test_assign import TestIODAssign
from tests.iod.test_invalid import TestInvalidIOD
from tests.iod.test_language import TestDriverLanguage, TestStaffLanguage
from tests.iod.test_login_logout import TestIODLoginLogout
from tests.iod.test_longhaul import TestDriverLonghaul, TestLonghaulAcceptance
from tests.iod.test_report import TestIODReport
from tests.iod.test_reward import TestIODReward
from tests.iod.test_search import TestDriverSearch, TestStaffSearch
from tests.iod.test_notification import TestIODNotification
from tests.iod.test_homepage import TestDriverHome

if __name__ == '__main__':
    loader = unittest.TestLoader()
    iod_suite = unittest.TestSuite()

    print("\n*IOD Appium Test:*")
    #IOD App Staff Test [Done]
    iod_suite.addTest(TestIODLoginLogout("test_Login", user_type='staff'))
    
    #IOD -> Staff Language Test [Done]
    iod_suite.addTest(TestStaffLanguage("test_ChangeToMalay"))
    iod_suite.addTest(TestStaffLanguage("test_ChangeToEnglish"))
    
    #IOD -> Staff Longhaul Test [Done]
    iod_suite.addTests(loader.loadTestsFromTestCase(TestLonghaulAcceptance)) 
    
    #IOD -> Staff Approve Test [Done]
    iod_suite.addTests(loader.loadTestsFromTestCase(TestIODApprove)) 
    
    #IOD -> Staff Search Test [Done]
    iod_suite.addTest(TestStaffSearch("test_staff_estDateTime"))
    iod_suite.addTest(TestStaffSearch("test_staff_pod"))
    iod_suite.addTest(TestStaffSearch("test_staff_fail"))
    iod_suite.addTest(TestStaffSearch("test_staff_delay"))
    
    #IOD -> Staff Assign test [Done]
    iod_suite.addTest(TestIODAssign("test_scanAssign"))
    iod_suite.addTest(TestIODAssign("test_insertAssign"))
    
    #IOD -> Staff Leaderboard Test [Done]
    iod_suite.addTests(loader.loadTestsFromTestCase(TestIODLeaderboard))
    
    #IOD -> Report Test [Done]
    iod_suite.addTest(TestIODReport("test_iodReport"))
    iod_suite.addTest(TestIODReport("test_generalReport"))
    
    #IOD -> Logout Test [Done]
    iod_suite.addTest(TestIODLoginLogout("test_Logout", user_type='staff'))


    #IOD App Driver Test
    #IOD -> Login Test [Done]
    iod_suite.addTest(TestIODLoginLogout("test_Login", user_type='driver'))
    
    #IOD -> Driver Home Test
    iod_suite.addTests(loader.loadTestsFromTestCase(TestDriverHome))
    
    #IOD -> Driver Notification Test [Done]
    iod_suite.addTests(loader.loadTestsFromTestCase(TestIODNotification))
    
    #IOD -> Driver Longhaul Test [Done]
    iod_suite.addTest(TestDriverLonghaul("test_longhaul"))
    iod_suite.addTest(TestDriverLonghaul("test_longhaulPOD"))
    iod_suite.addTest(TestDriverLonghaul("test_longhaulFail"))
    
    #IOD -> Driver Search Test [DONE]
    iod_suite.addTest(TestDriverSearch("driver_completed"))
    iod_suite.addTest(TestDriverSearch("test_driver_pod"))
    iod_suite.addTest(TestDriverSearch("test_driver_fail"))
    iod_suite.addTest(TestDriverSearch("test_driver_delay"))
    
    #IOD -> Driver Invalid Test [DONE]
    iod_suite.addTests(loader.loadTestsFromTestCase(TestInvalidIOD))
    
    #IOD -> Driver Redeem Test [Done]
    iod_suite.addTest(TestIODReward("test_viewPoints"))
    iod_suite.addTest(TestIODReward("test_redeemPoints"))
    
    #IOD -> Driver Logout Test [Done]
    iod_suite.addTest(TestIODLoginLogout("test_Logout", user_type='driver'))
    
    #Run Test
    unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(iod_suite)


