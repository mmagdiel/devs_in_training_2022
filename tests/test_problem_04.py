import unittest
from problems.problem_04 import sum_multiples_of_three

class SumMultiplesOfThreeTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 3
        result = sum_multiples_of_three(3)
        self.assertEqual(result, excepted)

    def test_not_multiple_case(self):
        excepted = 0
        result = sum_multiples_of_three(2)
        self.assertEqual(result, excepted)   

    def test_complex_case(self):
        excepted = 30
        result = sum_multiples_of_three(13)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = sum_multiples_of_three("Lorem")
        self.assertEqual(result, excepted)

    def test_negative_multiples_case(self):
        excepted = -30
        result = sum_multiples_of_three(-13)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
