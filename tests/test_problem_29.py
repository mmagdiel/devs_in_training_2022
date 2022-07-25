import unittest
from problems.problem_29 import get_time_finish_day

class GetTimeFinishDayTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [0,0,0]
        result = get_time_finish_day("23:59:59")
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [1,10,20]
        result = get_time_finish_day("22:49:39")
        self.assertEqual(result, excepted)

    def test_noday_case(self):
        excepted = [0,0,0]
        result = get_time_finish_day("52:81:82")
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = [0,0,0]
        result = get_time_finish_day("Lorem")
        self.assertEqual(result, excepted)   

    def test_list_case(self):
        excepted = [0,0,0]
        result = get_time_finish_day(["Lorem"])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
