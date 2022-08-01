import unittest
from problems.problem_30 import get_center_number

class GetCenterNumberTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 2
        result = get_center_number(1,2,3)
        self.assertEqual(result, excepted)

    def test_negative_case(self):
        excepted = -30
        result = get_center_number(-10,-30,-50)
        self.assertEqual(result, excepted)

    def test_duplicates_case(self):
        excepted = 2
        result = get_center_number(2,2,2)
        result_1 = get_center_number(1,2,2)
        result_2 = get_center_number(2,2,3)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted) 
        self.assertEqual(result_2, excepted)   

    def test_with_more_comission_case(self):
        excepted = 0
        result = get_center_number([10,17,20],11,22)
        result_1 = get_center_number(17,[11,22,33],29)
        result_2 = get_center_number(20,11,[29,31,43])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted) 
        self.assertEqual(result_2, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_center_number("Lorem",700,200)
        result_1 = get_center_number(100,"Lorem",200)
        result_2 = get_center_number(100,700,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   


if __name__ == '__main__':
    unittest.main()
