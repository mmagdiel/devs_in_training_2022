import unittest
from problems.problem_16 import get_fizz_buzz

class GetFizzBuzzTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [1,2,"Fizz"]
        result = get_fizz_buzz(3)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz",16,17]
        result = get_fizz_buzz(17)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = []
        result = get_fizz_buzz(0)
        result_1 = get_fizz_buzz(-1)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = []
        result = get_fizz_buzz("Lorem")
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = []
        result = get_fizz_buzz(-3.1416)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
