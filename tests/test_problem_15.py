import unittest
from problems.problem_15 import get_taxes_by_amount_and_rate

class GetTaxesByAmountAndRrateTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 2000
        result = get_taxes_by_amount_and_rate(200,0.1)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = 10000
        result = get_taxes_by_amount_and_rate(200,0.5)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = 0
        result = get_taxes_by_amount_and_rate(0,0.1)
        result_1 = get_taxes_by_amount_and_rate(200,0)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_taxes_by_amount_and_rate("Lorem",0.1)
        result_1 = get_taxes_by_amount_and_rate(200,"Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   

    def test_negative_times_case(self):
        excepted = -3000
        result = get_taxes_by_amount_and_rate(-300,0.1)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
