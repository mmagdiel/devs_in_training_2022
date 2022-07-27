import unittest
from problems.problem_32 import get_salary

class GetSalaryTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1072000
        result = get_salary([100000,200000,300000])
        self.assertEqual(result, excepted)

    def test_with_comission_case(self):
        excepted = 1000000
        result = get_salary([])
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = 1000000
        result = get_salary("12")
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 1000000
        result = get_salary(["Lorem",7000000])
        result_1 = get_salary([1000000,"Lorem"])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = 1000000
        result = get_salary([1000000,-3000000])
        result_1 = get_salary([-1000000,3000000])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
