import unittest
from problems.problem_02 import MCD

class MCDTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1
        result = MCD(2,3)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = MCD(15,"Lorem")
        self.assertEqual(result, excepted)   

    def test_complex_case(self):
        excepted = 12
        result = MCD(48,60)
        self.assertEqual(result, excepted)

    def test_doble_string_case(self):
        excepted = 0
        result = MCD("Lorem","ipsum")
        self.assertEqual(result, excepted)        

    def test_doble_float_case(self):
        excepted = 8
        result = MCD(8.32, 64.85)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
