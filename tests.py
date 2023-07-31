import unittest
from management_tests import WebAppManagementTests
from state_tests import WebServerStateTests
from addition_tests import WebCalculatorAdditionTests
from multiplication_tests import WebCalculatorMultiplicationTests
from division_tests import WebCalculatorDivisionTests
from remainder_tests import WebCalculatorRemainderTests


def create_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebAppManagementTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebServerStateTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebCalculatorAdditionTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebCalculatorMultiplicationTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebCalculatorDivisionTests))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(WebCalculatorRemainderTests))
    return test_suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_test_suite()
    result = runner.run(test_suite)

    print("\n===== Результаты тестов =====")
    print(f"Всего тестов: {result.testsRun}")
    print(f"Успешных: {result.testsRun - len(result.errors) - len(result.failures)}")
    print(f"Неудачных: {len(result.errors) + len(result.failures)}")

    if result.wasSuccessful():
        print("Все тесты прошли успешно.")
    else:
        print("Тесты не были пройдены. Проверьте ошибки и неудачные тесты.")
