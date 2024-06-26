import unittest
from tests.test_login import TestLogin
from tests.test_language import TestStaffLanguage
from tests.test_longhaul import TestLonghaul
from tests.test_redeem import TestApproveRedeem
from tests.test_search import TestSearch
from tests.test_assign import TestAssignPoint
from tests.test_analytics import TestAnalytics
from tests.test_report import TestReport

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    # suite.addTests(loader.loadTestsFromTestCase(TestLanguage))
    # suite.addTests(loader.loadTestsFromTestCase(TestLonghaul))
    # suite.addTests(loader.loadTestsFromTestCase(TestApproveRedeem))
    suite.addTests(loader.loadTestsFromTestCase(TestSearch))
    # suite.addTests(loader.loadTestsFromTestCase(TestAssignPoint))
    # suite.addTests(loader.loadTestsFromTestCase(TestAnalytics))
    # suite.addTests(loader.loadTestsFromTestCase(TestReport))
 
    unittest.TextTestRunner(verbosity=2).run(suite)

    print("Test Done")

