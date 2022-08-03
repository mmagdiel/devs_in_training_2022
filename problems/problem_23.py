'''
    Diseñar una función retorne el sueldo que le corresponde a un trabajador cualquiera de esta empresa.
    Un trabajador de una cierta empresa recibe un sueldo mensual que está determinado por
    el producto entre el número de horas que trabajó durante el mes y el valor de cada hora,
    pero si el trabajador labora más de 40 horas, su valor hora para las horas sobre 40, se
    incrementa en el 60% de su valor.
'''




def get_salary(hours,rate):
    if hours == str(hours) or rate == str(rate):
        return(0)
    elif hours > 40:
        result = hours * rate 
        porcentaje = result / 100 * 60 
        op1 = result + porcentaje
        return(op1)

    elif hours < 0 or rate < 0:
        return(0)   
    else:
        op2 = hours * rate
        return(op2)    

