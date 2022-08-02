'''
    Diseñar una función que encuentre el salario semanal de un trabajador, dada la tarifa
    horaria y el número de horas trabajadas diariamente.
'''
def get_employee_salary(rate, worked_hours):
    if rate==str(rate) or worked_hours==str(worked_hours):
            return 0
    if worked_hours==list(str(worked_hours)):
            return 0
    suma=0
    for ele in worked_hours:
        if ele=="ipsum":
            return 0
    for i in worked_hours:
        suma = i+suma
        salario = rate * suma
    return(salario)
