import unittest
from problems.problem_21 import get_all_permutation_of_word

class GetPrimesLessOrEqualThanTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = ["cat", "cta", "act", "atc", "tac", "tca"]
        result = get_all_permutation_of_word("cat")
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = ["ana","aan","naa"]
        result = get_all_permutation_of_word("ana")
        self.assertEqual(result, excepted)

    def test_zero_time_case(self):
        excepted = []
        result = get_all_permutation_of_word(15)
        result_1 = get_all_permutation_of_word(3.1416)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_number_case(self):
        excepted = []
        result = get_all_permutation_of_word("L0rem")
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = []
        result = get_all_permutation_of_word(["Lorem", "ipsum"])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
