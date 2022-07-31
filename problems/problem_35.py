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
    if type(base)==type(list()) or type(hour_extraordinary_daytime)==type(list()) or type(hour_extraordinary_nighttime)==type(list()):
        return 0
    if base==str(base) or hour_extraordinary_daytime==str(hour_extraordinary_daytime) or hour_extraordinary_nighttime==str(hour_extraordinary_nighttime):
        return 0
    if base<0 or hour_extraordinary_daytime<0 or hour_extraordinary_nighttime<0:
        return 0
    sueldo=base
    horaextradia=hour_extraordinary_daytime*2000
    horaextranoc=hour_extraordinary_nighttime*(2000*1.3)
    semanasueldo=sueldo+horaextradia+horaextranoc
    return(semanasueldo)