import unittest
from problems.problem_24 import get_salary

class GetSalaryTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1000000
        result = get_salary(1000000,3000000)
        self.assertEqual(result, excepted)

    def test_with_comission_case(self):
        excepted = 1210000
        result = get_salary(1000000,7000000)
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = 1190000
        result = get_salary(1000000,17000000)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = get_salary("Lorem",7000000)
        result_1 = get_salary(1000000,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = 0
        result = get_salary(1000000,-3000000)
        result_1 = get_salary(-1000000,3000000)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
