import unittest
from problems.problem_20 import get_mode


class GetModeTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 2
        result = get_mode([2,2,3,4,5,6,5,6,2])
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [2,5,6]
        result = get_mode([2,2,3,4,5,6,5,6])
        self.assertEqual(result, excepted)

    def test_zero_case(self):
        excepted = "No existe"
        excepted_1 = [1,2,3,4,5]
        result = get_mode([])
        result_1 = get_mode([1,2,3,4,5])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted_1)

    def test_string_case(self):
        excepted = "No existe"
        result = get_mode(["Lorem", "ipsue"])
        self.assertEqual(result, excepted)

    def test_negative_case(self):
        excepted = -2
        result = get_mode([-2, 2, 1,-2, 2, 1, -2])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
