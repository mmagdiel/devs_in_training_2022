import unittest
from problems.problem_35 import get_salary

class GetSalaryTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 5600
        result = get_salary(1000,1,1)
        self.assertEqual(result, excepted)

    def test_no_hour_extra_case(self):
        excepted = 1000
        result = get_salary(1000,0,0)
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = 0
        result = get_salary([],{},5)
        result_1 = get_salary(5,{},[])
        result_2 = get_salary(20,[],{})
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)  
        
    def test_string_case(self):
        excepted = 0
        result = get_salary("Lorem",7,2)
        result_1 = get_salary(1000,"Lorem",7)
        result_2 = get_salary(1000,2,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   

    def test_negative_case(self):
        excepted = 0
        result = get_salary(1000,-30,80)
        result_1 = get_salary(-1000,30,80)
        result_2 = get_salary(1000,2,-80)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  
        self.assertEqual(result_2, excepted)   

if __name__ == '__main__':
    unittest.main()
