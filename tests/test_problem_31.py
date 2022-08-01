import unittest
from problems.problem_31 import add_time

class AddTimeTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = "22:45:55"
        result = add_time("21:15:45","01:30:10")
        self.assertEqual(result, excepted)

    def test_with_comission_case(self):
        excepted = "1:01:00:00"
        result = add_time("21:15:45","03:45:15")
        self.assertEqual(result, excepted)

    def test_with_more_comission_case(self):
        excepted = "00:00:00"
        result = add_time("Lorem","03:45:15")
        result_1 = add_time("03:45:15","Lorem")
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   

    def test_string_case(self):
        excepted = "00:00:00"
        result = add_time("55:90:75","03:45:15")
        result_1 = add_time("03:45:15","55:90:75")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = "20:15:30"
        result = add_time("21:30:45","-01:15:15")
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
