'''
    Diseñar una función retorne el sueldo que le corresponde a un trabajador cualquiera de esta empresa.
    Un trabajador de una cierta empresa recibe un sueldo mensual que está determinado por
    el producto entre el número de horas que trabajó durante el mes y el valor de cada hora,
    pero si el trabajador labora más de 40 horas, su valor hora para las horas sobre 40, se
    incrementa en el 60% de su valor.
'''
def get_salary(hours,rate,horax,sueldo_total):
    valor_hora=0
    horas_trabajadas= 40
    if valor_hora < 40:
        print ("Sueldo total")
    elif horax == (sueldo_total * 60 )/100:
        resultado= sueldo_total + hours
