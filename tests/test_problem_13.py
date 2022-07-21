import unittest
from problems.problem_13 import is_even

class IsEvenTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = is_even(2)
        result_1 = is_even(0)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted) 

    def test_fail_case(self):
        excepted = False
        result = is_even(15)
        result_1 = is_even(-5)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted) 

    def test_zero_time_case(self):
        excepted = False
        result = is_even(2.34)
        result_1 = is_even(3.1416)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = False
        result = is_even("Lorem")
        self.assertEqual(result, excepted)

    def test_negative_case(self):
        excepted = True
        result = is_even(-4)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
