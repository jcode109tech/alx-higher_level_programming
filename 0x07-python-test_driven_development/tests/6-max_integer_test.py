# test_max_integer.py

import unittest
max_integer = __import__('6-max_integer').max_integer

""" 
   Test by unitest 
"""

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_mixed(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_max_integer_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_strings(self):
        self.assertEqual(max_integer(["1", "2", "3"]), "3")

    def test_max_integer_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_integer_duplicate_elements(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_max_integer_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

