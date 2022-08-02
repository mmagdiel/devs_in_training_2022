'''
    Diseñar una función retorne el sueldo que le corresponde a un trabajador cualquiera de esta empresa.
    Un trabajador de una cierta empresa recibe un sueldo mensual que está determinado por
    el producto entre el número de horas que trabajó durante el mes y el valor de cada hora,
    pero si el trabajador labora más de 40 horas, su valor hora para las horas sobre 40, se
    incrementa en el 60% de su valor.
'''
def get_salary(hours,rate):
    if hours==str(hours) or rate==str(rate) or hours<0 or rate<0:
        return 0
    salario_total=hours*rate
    if hours < 40:
        return salario_total
    else:
        hora_extra=hours-40
        porciento=(rate*60)/100
        valor_extra=(porciento*hora_extra)+salario_total
        return valor_extra
