import unittest
from problems.problem_22 import are_primes_relatives

class ArePrimesRelativesTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = are_primes_relatives(2,3)
        self.assertEqual(result, excepted)

    def test_fail_case(self):
        excepted = False
        result = are_primes_relatives(15, 3)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = False
        result = are_primes_relatives("Lorem", 1)
        result_1 = are_primes_relatives(1, "Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_complex_case(self):
        excepted = True
        result = are_primes_relatives(64,125)
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = False
        result = are_primes_relatives(-3.1416, 2)
        result_1 = are_primes_relatives(1, -3.1416)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   


if __name__ == '__main__':
    unittest.main()
