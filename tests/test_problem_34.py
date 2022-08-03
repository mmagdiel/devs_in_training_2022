import unittest
from problems.problem_34 import get_stats

class GetStatsTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [6,14,2,0.816]
        result = get_stats([1,2,3])
        self.assertEqual(result, excepted)

    def test_zero_case(self):
        excepted = [0,0,0,0]
        result = get_stats([])
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = [0,2,0,0.707]
        result = get_stats([1,-1,0,0])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = [0,0,0,0]
        result = get_stats(["Lorem",7000000])
        result_1 = get_stats([1000000,"Lorem"])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = [0,0,0,0]
        result = get_stats({"key":"Lorem"})
        self.assertEqual(result, excepted)



if __name__ == '__main__':
    unittest.main()
