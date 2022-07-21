import unittest
from problems.problem_23 import get_salary


class GetSalaryTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 450
        result = get_salary(15,30)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = 680
        result = get_salary(60,10)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = 0
        result = get_salary(0, 500)
        result_1 = get_salary(50,0)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_salary("Lorem",50)
        result_1 = get_salary(50,"Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  

    def test_negative_times_case(self):
        excepted = 0
        result = get_salary(-3.1416, 30)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
