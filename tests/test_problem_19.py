import unittest
from problems.problem_19 import get_compound_interest

class GetCompoundInterestTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1432,69
        result = get_compound_interest(1000, 0.25, 12)
        self.assertEqual(result, excepted)

    def test_zero_case(self):
        excepted = 1000
        result = get_compound_interest(1000, 0, 10)
        result_1 = get_compound_interest(1000, 0.25, 0)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  

    def test_no_capital_case(self):
        excepted = 0
        result = get_compound_interest(0,0.25,16)
        self.assertEqual(result, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_compound_interest("Lorem",0.25,52)
        result_1 = get_compound_interest(0,"Lorem",16)
        result_2 = get_compound_interest(0,0.25,"Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  
        self.assertEqual(result_2, excepted)  

    def test_negative_times_case(self):
        excepted = 0
        result = get_compound_interest([1000], 0.25, 16)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
