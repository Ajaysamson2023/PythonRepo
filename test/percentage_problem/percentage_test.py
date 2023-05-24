import unittest
from src.percentage_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        k = {'A': [35, 56, 35], "b": [34, 43]}
        m = "A"
        actual_output = finding_percent(k, m)
        expected_output = 42.00
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()
