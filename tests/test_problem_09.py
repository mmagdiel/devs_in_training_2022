import unittest
from problems.problem_09 import get_triangle_area

class GetTriangleAreaTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1
        result = get_triangle_area(1,2)
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = 3.1416
        result = get_triangle_area(3.1416, 2)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = 0
        result = get_triangle_area(0,2)
        result_1 = get_triangle_area(3,0)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = 0
        result = get_triangle_area("Lorem", 2)
        self.assertEqual(result, excepted)

    def test_negative_case(self):
        excepted = 0
        result = get_triangle_area(-3.1416, 2)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
