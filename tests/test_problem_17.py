import unittest
from problems.problem_17 import get_volumen_on_liters

class GetVolumenOnLitersTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1
        result = get_volumen_on_liters(10,10,10)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = 2.25
        result = get_volumen_on_liters(15,15,10)
        self.assertEqual(result, excepted)

    def test_zero_case(self):
        excepted = 0
        result = get_volumen_on_liters(0,10,3)
        result_1 = get_volumen_on_liters(10,0,30)
        result_2 = get_volumen_on_liters(40,53,0)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_volumen_on_liters("Lorem",10,23)
        result_1 = get_volumen_on_liters(10,"Lorem",30)
        result_2 = get_volumen_on_liters(40,53,"Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   

    def test_negative_times_case(self):
        excepted = 0
        result = get_volumen_on_liters(-3.1416,-15,40)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
