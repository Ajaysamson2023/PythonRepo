import unittest
from src.string_mutation_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_output = mutation()
        expected_output = "abrackdabra"
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
