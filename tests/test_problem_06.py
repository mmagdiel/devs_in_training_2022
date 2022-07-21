import unittest
from problems.problem_06 import is_divide_product_of_the_other

class IsDivideProductOfTheOtherTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = is_divide_product_of_the_other(6,2,3)
        self.assertEqual(result, excepted)

    def test_fail_case(self):
        excepted = False
        result = is_divide_product_of_the_other(2,3,5)
        self.assertEqual(result, excepted)   

    def test_negative_number_case(self):
        excepted = True
        result = is_divide_product_of_the_other(-2,-3,-6)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = False
        result = is_divide_product_of_the_other(2,"Lorem","ipsue")
        self.assertEqual(result, excepted)

    def test_negative_multiples_case(self):
        excepted = False
        result = is_divide_product_of_the_other(-1,3.1416,2.7182)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
