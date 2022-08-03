'''
    Diseñar una función que encuentre el salario semanal de un trabajador, dada la tarifa
    horaria y el número de horas trabajadas diariamente.
'''
def get_employee_salary(rate, worked_hours):
 s = []
 total = []
 for x in worked_hours:
   if isinstance(x, int):
       s.append(x)

 if rate == str(rate):
        return(0)
 else:    
     totalH = sum(s)
     pago = rate * totalH
     return(pago)
 
    