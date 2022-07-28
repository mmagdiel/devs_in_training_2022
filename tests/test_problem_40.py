import unittest
from problems.problem_40 import get_trace

class GetTraceTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = 1
        excepted_1 = 2
        result = get_trace([1])
        result_1 = get_trace([[1,2],[2,1]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)

    def test_with_comission_case(self):
        excepted = 3
        excepted_1 = 4
        result = get_trace([[1,2,3],[3,1,2],[3,2,1]])
        result_1 = get_trace([[1,2,3,4],[2,1,3,4],[3,2,1,4],[4,3,2,1]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)

    def test_with_more_comission_case(self):
        excepted = 0
        result = get_trace([[100,False],[True,170]])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = 0
        result = get_trace([["Lorem"],[7000000]])
        result_1 = get_trace([[1000000],["Lorem"]])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = 0
        result = get_trace([{"abc":100},{"xyz":-300}])
        result_1 = get_trace([{"abc":-100},{"xyz":300}])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
