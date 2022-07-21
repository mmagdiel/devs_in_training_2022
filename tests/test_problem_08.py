import unittest
from problems.problem_08 import get_primes_less_or_equal_than

class GetPrimesLessOrEqualThanTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [2]
        result = get_primes_less_or_equal_than(2)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [2,3,5,7,11,13]
        result = get_primes_less_or_equal_than(15)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = []
        result = get_primes_less_or_equal_than(0)
        result_1 = get_primes_less_or_equal_than(1)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = []
        result = get_primes_less_or_equal_than("Lorem")
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = [2,3]
        result = get_primes_less_or_equal_than(-3.1416)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
