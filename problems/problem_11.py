'''
    Diseñar una función que encuentre el salario semanal de un trabajador, dada la tarifa
    horaria y el número de horas trabajadas diariamente.
'''
def get_employee_salary(rate, worked_hours):
    suma=0
    if worked_hours==list(str(worked_hours)) or rate==str(rate) or worked_hours==str(worked_hours):
            return 0
    for x in worked_hours:
        if x=="ipsum":
            return 0
    for i in worked_hours:
        suma = i+suma
        salario = rate * suma
    return(salario)