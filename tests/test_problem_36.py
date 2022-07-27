import unittest
from problems.problem_36 import swap_vars

class SwapVvarsTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [100,300]
        result = swap_vars(100,300)
        self.assertEqual(result, excepted)

    def test_with_comission_case(self):
        excepted = ["xyz","abc"]
        result = swap_vars("abc","xyz")
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = [["a","b","c"],[1,2,3]]
        result = swap_vars([1,2,3],["a","b","c"])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = [False,None]
        result = swap_vars(None,False)
        self.assertEqual(result, excepted)   

    def test_negative_case(self):
        excepted = [-300, {"a":100}]
        result = swap_vars({"a":100},-300)
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
