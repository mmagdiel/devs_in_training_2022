import unittest
from problems.problem_41 import maximum_list

class MaximumListTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 4
        excepted_1 = 30
        result = maximum_list([1,2,3,4])
        result_1 = maximum_list([10,20,30,15])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)

    def test_another_type_case(self):
        excepted = 0
        result = maximum_list([])
        result_1 = maximum_list({"abc":[1,2,3,4]})
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_rare_case(self):
        excepted = 0
        result = maximum_list([True, False, True])
        result_1 = maximum_list([1, None, 2])
        self.assertEqual(result, excepted)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = maximum_list([{"Lorem":70}])
        result_1 = maximum_list([10,"Lorem"])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = 3.1416
        result = maximum_list([3.1416,0,-3])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
