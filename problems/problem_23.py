'''
    Diseñar una función retorne el sueldo que le corresponde a un trabajador cualquiera de esta empresa.
    Un trabajador de una cierta empresa recibe un sueldo mensual que está determinado por
    el producto entre el número de horas que trabajó durante el mes y el valor de cada hora,
    pero si el trabajador labora más de 40 horas, su valor hora para las horas sobre 40, se
    incrementa en el 60% de su valor.
'''
sueldo = 0

def get_salary(hours,rate):
    
    if (hours < 40):
        
        sueldo = hours * rate
    
        return sueldo

    else:
        (hours > 40)

        valor_hora_trabajada = ((rate * 60) / 100)

        valor_hora_extra = (valor_hora_trabajada + rate)

        salario_mensual_total = (valor_hora_extra * hours)

    return salario_mensual_total

