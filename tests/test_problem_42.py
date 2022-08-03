import unittest
from problems.problem_42 import get_grade_point_average

class GetGradePointAverageTestCase(unittest.TestCase):
    def test_simple_case(self):
        excepted = [3,4,3.4]
        excepted_1 = [1,0,3]
        result = get_grade_point_average([[2,3,4],[3,4,5,4],[3,3,4,4,3]])
        result_1 = get_grade_point_average([[1,1],[0,0,0,0],[2,3,4]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted_1)

    def test_grade_error_case(self):
        excepted = "Error en notas alumno 1"
        result = get_grade_point_average([[3],[3,4,5,4],[3,3,4,4,3]])
        result_1 = get_grade_point_average([[-3,4,20],[3,4,5,4],[3,3,4,4,3]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_dict_format_error_case(self):
        excepted = "Error en el formato de notas"
        result = get_grade_point_average([{"matias":[1,3,5]},{"lucas":[3,2]}])
        result_1 = get_grade_point_average([[True,None],[None,False]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)

    def test_string_format_case(self):
        excepted = "Error en el formato de notas"
        result = get_grade_point_average(["Lorem"])
        result_1 = get_grade_point_average([["Lorem"]])
        self.assertEqual(result, excepted)   
        self.assertEqual(result_1, excepted)   

    def test_string_error_case(self):
        excepted = "Error en el formato de notas"
        result = get_grade_point_average([["2","3","4"],["3","4","5","4"],["3","3","4","4","3"]])
        result_1 = get_grade_point_average([["1","1"],["0","0","0","0"],["2","3","4"]])
        self.assertEqual(result, excepted)
        self.assertEqual(result_1, excepted)  


if __name__ == '__main__':
    unittest.main()
