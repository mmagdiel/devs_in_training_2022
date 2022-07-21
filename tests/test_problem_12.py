import unittest
from problems.problem_12 import is_palindrome

class IsPalindromeTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = True
        result = is_palindrome("radar")
        self.assertEqual(result, excepted)

    def test_fail_case(self):
        excepted = False
        result = is_palindrome("Lorem")
        self.assertEqual(result, excepted)

    def test_numbers_case(self):
        excepted = False
        result = is_palindrome(121)
        result_1 = is_palindrome("12321")
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_complex_case(self):
        excepted = False
        result = is_palindrome("r-a.d.a-r")
        self.assertEqual(result, excepted)

    def test_two_words_case(self):
        excepted = False
        result = is_palindrome("ana radar ana")
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
