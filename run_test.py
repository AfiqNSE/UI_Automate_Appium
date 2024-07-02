import unittest
from config import Config
from tests.test_analytics import TestDriverAnalytics, TestStaffAnalytics
from tests.test_approve import TestStaffApprove
from tests.test_assign import TestStaffAssign
from tests.test_invalid import TestDriverInvalid
from tests.test_language import TestStaffLanguage, TestDriverLanguage
from tests.test_login_logout import  TestDriverLogout, TestStaffLogin, TestDriverLogin, TestStaffLogout
from tests.test_longhaul import TestStaffLonghaul, TestDriverLonghaul
from tests.test_report import TestStaffReport
from tests.test_reward import TestDriverReward
from tests.test_search import TestDriverHistory, TestStaffSearch
from tests.test_notification import TestNotification
from tests.test_homepage import TestStaffHome, TestDriverHome


if __name__ == '__main__':
    loader = unittest.TestLoader()
    staff_suite = unittest.TestSuite()
    driver_suite = unittest.TestSuite()

    #Staff Test
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLogin))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffHome))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLanguage))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLonghaul))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffApprove))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffSearch))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffAssign))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffAnalytics))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffReport))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLogout))

    
    #Driver Test
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverLogin))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverHome))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestNotification))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverLonghaul))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverHistory))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverAnalytics))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverInvalid))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverReward))
    driver_suite.addTests(loader.loadTestsFromTestCase(TestDriverLogout))

 
    unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(staff_suite)
    unittest.TextTestRunner(verbosity=Config.VERBOSITY).run(driver_suite)

    print("Test Done")

