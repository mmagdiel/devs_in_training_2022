'''
    Diseñar una función que encuentre el salario semanal de un trabajador, dada la tarifa
    horaria y el número de horas trabajadas diariamente.
'''
def get_employee_salary(rate, worked_hours):
    
antiguedad_en_anos = float (input ('Ingresa el valor de antiguedad en anos: '))
horas_trabajadas = float (input ('Ingresa el valor de horas trabajadas: '))
pago_por_hora=15000
salario_bruto=horas_trabajadas*pago_por_hora
if horas_trabajadas>38:
    salario_bruto=salario_bruto+(horas_trabajadas-38)*pago_por_hora*0.5
if salario_bruto>570000:
    impuesto=salario_bruto*0.1
else:
    impuesto=salario_bruto*0.05
if antiguedad_en_anos>=10:
    bonificacion=200000
else:
    bonificacion=0
salario_neto=salario_bruto-impuesto+bonificacion
return ('Valor de bonificacion: ' + repr (bonificacion))
return ('Valor de impuesto: ' + repr (impuesto))
return ('Valor de pago por hora: ' + repr (pago_por_hora))
return ('Valor de salario bruto: ' + repr (salario_bruto))
return ('Valor de salario neto: ' + repr (salario_neto))
return ()