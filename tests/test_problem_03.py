import unittest
from problems.problem_03 import mcm

class mcmTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 6
        result = mcm(2,3)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = mcm(15,"Lorem")
        self.assertEqual(result, excepted)   

    def test_complex_case(self):
        excepted = 240
        result = mcm(48,60)
        self.assertEqual(result, excepted)

    def test_doble_string_case(self):
        excepted = 0
        result = mcm("Lorem", "ipsum")
        self.assertEqual(result, excepted)        

    def test_doble_float_case(self):
        excepted = 64
        result = mcm(8.32, 64.85)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
