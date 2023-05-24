import unittest
from src.merge_tools_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_output = merge_the_tools(string, k)
        expected_output = "AB"
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

