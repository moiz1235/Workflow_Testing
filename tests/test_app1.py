"""
Announcements:

    1. This week's lab (Lab 10) on Flask
    2. Project Phase 1 demo - 14th April
    3. Next week - Last week of code reviews
"""

import unittest
from src import application1 as tasks


class TestSuite(unittest.TestCase):

    def test_exponential(self):
        expectedValue = 125
        actualValue = tasks.getExponential(5,3)
        self.assertEqual(expectedValue, actualValue)

    def test_greaterThan(self):

        with self.subTest(key="Greater Than Ten"):
            actualValue = tasks.testGreaterThan10(12)
            self.assertTrue(actualValue)

        with self.subTest(key="Less Than Ten"):
            actualValue = tasks.testGreaterThan10(5)
            self.assertFalse( actualValue)

        with self.subTest(key="Equal to Ten"):
            actualValue = tasks.testGreaterThan10(10)
            self.assertIsNone(actualValue)

    def test_squared(self):
        list = [1,2,3,4]
        expectedValue = [1,4,9,16]
        actualValue = tasks.getSquared(list)
        self.assertListEqual(actualValue, expectedValue)

if __name__ == '__main__':
    unittest.main()


