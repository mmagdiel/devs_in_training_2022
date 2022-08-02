'''
    Diseñar una función que encuentre el salario semanal de un trabajador, dada la tarifa
    horaria y el número de horas trabajadas diariamente.
'''
def get_employee_salary(rate, worked_hours):
    
    if rate == int (rate) and worked_hours == int (worked_hours):

        salario_semanal = rate * worked_hours

        return salario_semanal
