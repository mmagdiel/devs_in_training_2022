import unittest
from problems.problem_10 import get_lenght_and_area_circule

class GetLenghtAndAreaCirculeTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [6.2832, 3.1416]
        result = get_lenght_and_area_circule(1)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [2, 0.3183]
        result = get_lenght_and_area_circule(0.3183)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = [0,0]
        result = get_lenght_and_area_circule(0)
        self.assertEqual(result, excepted)   

    def test_string_case(self):
        excepted = [0,0]
        result = get_lenght_and_area_circule("Lorem")
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = [0,0]
        result = get_lenght_and_area_circule(-3.1416)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
