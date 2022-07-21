import unittest
from problems.problem_14 import get_count_by_char

class GetCountByCharTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [(2,"m"),(1,"o"),(2,"r"),(1,"i"),(1,"t"),(1,"e")]
        result = get_count_by_char("Mortimer")
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = []
        result = get_count_by_char(12345)
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = []
        result = get_count_by_char("M0rtimer")
        result_1 = get_count_by_char("Mort&imer")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_list_case(self):
        excepted = []
        result = get_count_by_char(["Lorem", "ipsum"])
        self.assertEqual(result, excepted)

    def test_boolean_case(self):
        excepted = []
        result = get_count_by_char(True)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
