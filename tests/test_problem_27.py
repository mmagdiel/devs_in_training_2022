import unittest
from problems.problem_27 import convert_foot

class ConvertFootTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 3048
        result = convert_foot(100)
        self.assertEqual(result, excepted)

    def test_with_comission_case(self):
        excepted = 95.7559
        result = convert_foot(3.1416)
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = 0
        result = convert_foot([1000000])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = convert_foot("Lorem")
        self.assertEqual(result, excepted)   

    def test_negative_case(self):
        excepted = 0
        result = convert_foot(-3000000)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
