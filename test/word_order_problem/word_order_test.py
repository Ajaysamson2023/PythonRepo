import unittest
from src.word_order_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = word_problem()
        expected_output = {'bcdef': 2, 'abcdefg': 1, 'bcde': 1}
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
