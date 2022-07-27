import unittest
from problems.problem_37 import get_fibonacci

class GetFibonacciTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597]
        excepted_1 = [1,1,2,3,5,8,13]
        result = get_fibonacci(17)
        result_1 = get_fibonacci(7)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)

    def test_with_comission_case(self):
        excepted = []
        result = get_fibonacci(3.1416)
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = []
        result = get_fibonacci({"abc":35})
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = []
        result = get_fibonacci("Lorem")
        self.assertEqual(result, excepted)   

    def test_negative_case(self):
        excepted = []
        result = get_fibonacci(-3)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
