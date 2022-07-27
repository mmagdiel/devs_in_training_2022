import unittest
from problems.problem_38 import get_roman_notation

class GetRomanNotationTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = "LVII"
        excepted_1 = "MMM"
        result_1 = get_roman_notation(3000)
        result = get_roman_notation(57)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)   

    def test_complex_case(self):
        excepted = "LVII"
        excepted_1 = "MMM"
        result_1 = get_roman_notation(3000)
        result = get_roman_notation(57)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)   

    def test_with_more_comission_case(self):
        excepted = ""
        result = get_roman_notation(3.1416)
        result_1 = get_roman_notation(None)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_string_case(self):
        excepted = ""
        result = get_roman_notation("Lorem")
        result_1 = get_roman_notation(["Lorem"])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_negative_case(self):
        excepted = ""
        result = get_roman_notation({"abc":100})
        result_1 = get_roman_notation(True)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
