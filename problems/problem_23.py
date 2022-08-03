'''
    Diseñar una función retorne el sueldo que le corresponde a un trabajador cualquiera de esta empresa.
    Un trabajador de una cierta empresa recibe un sueldo mensual que está determinado por
    el producto entre el número de horas que trabajó durante el mes y el valor de cada hora,
    pero si el trabajador labora más de 40 horas, su valor hora para las horas sobre 40, se
    incrementa en el 60% de su valor.
'''
def get_salary(hours, rate): 
    if hours > 40: 
        return 40 * rate + (hours - 40) * rate * 1.5
    else: 
        return hours * rate 
hours = 50
rate = 100
pay = get_salary(hours, rate) 
return(f"Total sueldo bruto:{pay:.2f} ")  pass
