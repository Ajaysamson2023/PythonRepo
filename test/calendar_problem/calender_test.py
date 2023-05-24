import unittest
from src.calendar_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = calender_mod()
        expected_output = "MONDAY"
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
