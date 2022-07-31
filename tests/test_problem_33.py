import unittest
from problems.problem_33 import get_gender_percentage

class GetGenderPercentageTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [50,50]
        excepted_1 = [66.67, 33.33]
        result = get_gender_percentage(1,1)
        self.assertEqual(result, excepted)
        result_1 = get_gender_percentage(2,1)
        self.assertEqual(result_1, excepted_1)

    def test_desbalance_case(self):
        excepted_1 = [100, 0]
        excepted_2 = [0, 100]
        result_1 = get_gender_percentage(5,0)
        self.assertEqual(result_1, excepted_1)  
        result_2 = get_gender_percentage(0,5)
        self.assertEqual(result_2, excepted_2)  

    def test_with_more_comission_case(self):
        excepted = [0,0]
        result = get_gender_percentage([5],0)
        result_1 = get_gender_percentage(5,[0])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_string_case(self):
        excepted = [0,0]
        result = get_gender_percentage("Lorem",7000000)
        result_1 = get_gender_percentage(1000000,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = [0,0]
        result = get_gender_percentage(1000000,-3000000)
        result_1 = get_gender_percentage(-1000000,3000000)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
