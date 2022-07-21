import unittest
from problems.problem_07 import calcule_time_and_velocity

class CalculeTimeAndVelocityTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [(233, 6.43)]
        result = calcule_time_and_velocity([(3,53)])
        self.assertEqual(result, excepted)

    def test_complex_case(self):
        excepted = [(233, 6.43), (220, 6.818),(4, 6.25)]
        result = calcule_time_and_velocity([(3,53),(3,40),(4,0)])
        self.assertEqual(result, excepted)   

    def test_zero_time_case(self):
        excepted = []
        result = calcule_time_and_velocity([(0,0)])
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = []
        result = calcule_time_and_velocity([("Lorem","ipsue")])
        self.assertEqual(result, excepted)

    def test_negative_times_case(self):
        excepted = []
        result = calcule_time_and_velocity([(-2,30)])
        self.assertEqual(result, excepted)


if __name__ == '__main__':
    unittest.main()
