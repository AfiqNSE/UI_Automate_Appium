import unittest
from components.main_component import Constant
from config import Config
from tests.staff_test.test_staff_login import TestStaffLogin
from tests.staff_test.test_staff_language import TestStaffLanguage
from tests.staff_test.test_staff_longhaul import TestStaffLonghaul
from tests.staff_test.test_staff_approve import TestStaffApprove
from tests.staff_test.test_staff_search import TestStaffSearch
from tests.staff_test.test_staff_assign import TestStaffAssign
from tests.staff_test.test_staff_analytics import TestStaffAnalytics
from tests.staff_test.test_staff_report import TestStaffReport

if __name__ == '__main__':
    loader = unittest.TestLoader()

    #Staff Test
    staff_suite = unittest.TestSuite()
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLogin))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLanguage))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffLonghaul))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffApprove))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffSearch))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffAssign))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffAnalytics))
    staff_suite.addTests(loader.loadTestsFromTestCase(TestStaffReport))
    
    #Driver Test
    driver_suite = unittest.TestSuite()
    # driver_suite.addTests(loader.loadTestsFromTestCase(TestLogin))
 
    # unittest.TextTestRunner(Config.VERBOSITY).run(staff_suite)
    unittest.TextTestRunner(Config.VERBOSITY).run(driver_suite)

    print("Test Done")

