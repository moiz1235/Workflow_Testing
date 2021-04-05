
'''
Test Setup/Teardown are executed before/after each test case respectively

Test Setup: Initialise all Objects, Connections with other components like Databases etc. and remove any files that may affect
            your test cases

Test Teardown: Delete all Objects used in test cases, close connections and remove any files created by the test cases

'''
import unittest
from src import application2 as tasks
import os

class TestSuite(unittest.TestCase):
    def setUp(self):
        self.student1 = tasks.Student('John','21', 3.4)
        if os.path.exists(os.getcwd()+r'\hello.txt'):
            os.remove(os.getcwd()+r'\hello.txt')

    def test_graduation(self):

        with self.subTest(key="Graduation Test"):
            expectedValue = "Congrats on your graduation"
            actualValue = self.student1.graduate()
            self.assertEqual(expectedValue, actualValue, "Not matching strings")

    def test_textFile(self):
        self.student1.writeSomething()
        with open('hello.txt', 'r') as f:
            actualValue = f.readline().strip('\n')
        expectedValue = 'Hello World'
        self.assertEqual(expectedValue, actualValue, "Not matching strings")

    def tearDown(self):
        del self.student1
        if os.path.exists(os.getcwd() + r'\hello.txt'):
            os.remove(os.getcwd() + r'\hello.txt')

if __name__ == '__main__':
    with open('log.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)


