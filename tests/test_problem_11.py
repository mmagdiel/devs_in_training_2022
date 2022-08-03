import unittest
from problems.problem_11 import get_employee_salary

class GetEmployeeSalaryTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 2
        result = get_employee_salary(2, [1])
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = 18
        result = get_employee_salary(2, [2,3,4])
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = 0
        result = get_employee_salary(0, [2,3,4])
        result_1 = get_employee_salary(23, [0,0,0])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_employee_salary("Lorem", [2,3,4])
        result_1 = get_employee_salary(23, ["Lorem","ipsum",0])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   

    def test_negative_times_case(self):
        excepted = 0
        excepted_1 = -23
        result = get_employee_salary(0, [-2,-5,8])
        result_1 = get_employee_salary(-23, [1,0])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)  


if __name__ == '__main__':
    unittest.main()
