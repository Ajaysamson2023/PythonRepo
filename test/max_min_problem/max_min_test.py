import unittest
from src.max_min_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input=max_min()
        expected_output=3
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
