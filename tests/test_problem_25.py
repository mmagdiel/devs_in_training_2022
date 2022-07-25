from pickle import FALSE
import unittest
from problems.problem_25 import is_pythagorean_triple

class IsPythagoreanTripleTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = is_pythagorean_triple(4,3,5)
        result_1 = is_pythagorean_triple(65,72,97)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        
    def test_negative_case(self):
        excepted = True
        result_1 = is_pythagorean_triple(0,0,0)
        result = is_pythagorean_triple(-5,12,-13)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   

    def test_list_case(self):
        excepted = False
        result = is_pythagorean_triple([4,3,5],4,5)
        result_1 = is_pythagorean_triple(4,[5,12,13],5)
        result_2 = is_pythagorean_triple(5,4,[7,24,25])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   

    def test_zero_time_case(self):
        excepted = False
        result = is_pythagorean_triple(0,3,5)
        self.assertEqual(result, excepted)   

    def test_string_case(self):
        excepted = False
        result = is_pythagorean_triple("Lorem",3,5)
        result_1 = is_pythagorean_triple(4,"Lorem",5)
        result_2 = is_pythagorean_triple(5,4,"Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   


if __name__ == '__main__':
    unittest.main()
