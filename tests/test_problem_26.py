import unittest
from problems.problem_26 import sum_distinc_numbers

class SumDistincNumbersTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 400
        result = sum_distinc_numbers(100,300)
        self.assertEqual(result, excepted)

    def test_negative_case(self):
        excepted = 200
        result = sum_distinc_numbers(-100,300)
        self.assertEqual(result, excepted)

    def test_none_case(self):
        excepted = 0
        result = sum_distinc_numbers(100,100)
        self.assertEqual(result, excepted)

    def test_list_case(self):
        excepted = 0
        result = sum_distinc_numbers([100,170],[200,100])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = sum_distinc_numbers("Lorem",7000000)
        result_1 = sum_distinc_numbers(1000000,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   


if __name__ == '__main__':
    unittest.main()
