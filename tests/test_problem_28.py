import unittest
from problems.problem_28 import get_pesos_donations

class GetPesosDonationsTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [3.5475, 2.2575]
        result = get_pesos_donations(3.52,1,2.08)
        self.assertEqual(result, excepted)

    def test_list_case(self):
        excepted = [0,0]
        result = get_pesos_donations([10,70,50],10,70)
        result_1 = get_pesos_donations(10,[10,70,50],70)
        result_2 = get_pesos_donations(70,50,[10,70,50])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted) 

    def test_zero_case(self):
        excepted = [0,0]
        result = get_pesos_donations(0,0,0)
        self.assertEqual(result, excepted)

    def test_string_case(self):
        excepted = [0,0]
        result = get_pesos_donations("Lorem",7,1)
        result_1 = get_pesos_donations(1,"Lorem",7)
        result_2 = get_pesos_donations(1,"Lorem",7)
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   
        self.assertEqual(result_2, excepted)   

    def test_negative_case(self):
        excepted = [0,0]
        result = get_pesos_donations(-100,300,100)
        result_1 = get_pesos_donations(1000,-300,100)
        result_2 = get_pesos_donations(1000,300,-100)
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  
        self.assertEqual(result_2, excepted)  

if __name__ == '__main__':
    unittest.main()
