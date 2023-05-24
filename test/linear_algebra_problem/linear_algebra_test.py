import unittest
from src.linear_algebra_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = linear_algebra()
        expected_output = 50.0
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
