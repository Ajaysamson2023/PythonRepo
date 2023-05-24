import unittest
from src.no_idea_problem.utils import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_input=disjoint()
        expected_output=1
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()
