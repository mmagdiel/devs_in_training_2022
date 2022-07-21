import unittest
from problems.problem_05 import max_of_four_number

class MaxOfFourNumberTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 4
        result = max_of_four_number(1,2,3,4)
        self.assertEqual(result, excepted)

    def test_several_max_case(self):
        excepted = 3
        result = max_of_four_number(2,3,3,2)
        self.assertEqual(result, excepted)   

    def test_negative_number_case(self):
        excepted = -2
        result = max_of_four_number(-2,-3,-5,-6)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = max_of_four_number("Lorem","ipsue","2",3)
        self.assertEqual(result, excepted)

    def test_negative_multiples_case(self):
        excepted = 3.1416
        result = max_of_four_number(0,-1,3.1416,2.7182)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
