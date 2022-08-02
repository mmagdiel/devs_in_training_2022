'''
    El sueldo semanal de los trabajadores de una cierta fábrica está compuesto por un sueldo
    base, más la valorización de las horas extraordinarias que acumulen dentro de la semana
    de trabajo. Para calcular la valorización de las horas extraordinarias se utiliza la siguiente
    tabla:
    • Cada hora extraordinaria en horario normal (entre las 7 A.M. y las 12 P.M.) tienen un valor
    de $2.000
    • Cada hora extraordinaria en horario nocturno (entre las 12 P.M. y las 7 A.M.) tienen un
    valor de 1,3 veces la del horario normal.
    Diseñe una funció que calcule el sueldo semanal de un trabajador cualquiera de esta
    fábrica
'''
def get_salary(base, hour_extraordinary_daytime, hour_extraordinary_nighttime):
    
    