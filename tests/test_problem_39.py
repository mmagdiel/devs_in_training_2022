import unittest
from problems.problem_39 import get_integer_exponent

class GetIntegerExponentTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 2
        excepted_1 = 9,8696
        excepted_2 = -8
        result = get_integer_exponent(2,1)
        result_1 = get_integer_exponent(3.1416,2)
        result_2 = get_integer_exponent(-2,3)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)
        self.assertEqual(result_2, excepted_2)

    def test_non_exponent_case(self):
        excepted = 0
        result = get_integer_exponent(2, 3.1416)
        result_1 = get_integer_exponent(2,{"abc":3})
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_list__case(self):
        excepted = 0
        result = get_integer_exponent(2,[2,3])
        result_1 = get_integer_exponent([2,3],5)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_string_case(self):
        excepted = 0
        result = get_integer_exponent("Lorem",7000000)
        result_1 = get_integer_exponent(1000000,"Lorem")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_rare_case(self):
        excepted = 0
        result = get_integer_exponent(23,False)
        result_1 = get_integer_exponent(10,None)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
