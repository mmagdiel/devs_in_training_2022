import unittest
from problems.problem_0 import is_a

class IsATestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = is_a('a')
        self.assertEqual(result, excepted)

    def test_chars_case(self):
        excepted = False
        result = is_a('e')
        self.assertEqual(result, excepted)   

    def test_array_oversize_case(self):
        excepted = False
        result = is_a(1)
        self.assertEqual(result, excepted)

    def test_simple_error_case(self):
        excepted = False
        result = is_a(True)
        self.assertEqual(result, excepted)        

    def test_empty_list_case(self):
        excepted = False
        result = is_a([])
        self.assertEqual(result, excepted)



if __name__ == '__main__':
    unittest.main()
