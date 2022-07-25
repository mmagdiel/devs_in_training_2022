import unittest
from problems.problem_01 import show_any_number_distinc_zero

class ShowAnyNumberZeroTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [1,2,3,3]
        result = show_any_number_distinc_zero([1,2,3,0])
        self.assertEqual(result, excepted)

    def test_chars_case(self):
        excepted = ['3','7',2]
        result = show_any_number_distinc_zero(['3','7',0])
        self.assertEqual(result, excepted)   

    def test_array_oversize_case(self):
        excepted = ['1','2',2]
        result = show_any_number_distinc_zero(["1","2",0,"3","4","5"])
        self.assertEqual(result, excepted)

    def test_simple_error_case(self):
        excepted = [0]
        result = show_any_number_distinc_zero("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        self.assertEqual(result, excepted)        

    def test_empty_list_case(self):
        excepted = [0]
        result = show_any_number_distinc_zero([])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
