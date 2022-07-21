import unittest
from problems.problem_18 import get_three_multiple_inverse_list

class GetThreeMultipleInverseListTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = []
        result = get_three_multiple_inverse_list(2)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [9,6,3]
        result = get_three_multiple_inverse_list(9)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = []
        result = get_three_multiple_inverse_list(-6)
        result_1 = get_three_multiple_inverse_list(0)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = []
        result = get_three_multiple_inverse_list("Lorem")
        self.assertEqual(result, excepted)

    def test_list_case(self):
        excepted = []
        result = get_three_multiple_inverse_list([0,2])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
