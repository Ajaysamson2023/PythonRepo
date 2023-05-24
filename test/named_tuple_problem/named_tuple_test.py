import unittest
from src.named_tuple_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = col_tuple()
        expected_output = 76.33333333333333
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
