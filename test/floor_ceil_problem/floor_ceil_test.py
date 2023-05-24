import unittest
from src.floor_ceil_problem.utils import *
import numpy


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input = floor()
        expected_output = numpy.array([3.])
        self.assertEqual(actual_input, expected_output)

    def test_something_1(self):
        actual_input = ceil()
        expected_output = numpy.array([5.])
        self.assertEqual(actual_input, expected_output)

    def test_something_2(self):
        actual_input = int()
        expected_output = numpy.array([9])
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
