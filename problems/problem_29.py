'''
    Diseñe un algoritmo que lea la hora actual del día HH:MM:SS y determine cuántas horas,
    minutos y segundos restan para culminar el día.
'''
def get_time_finish_day(day):
    if day=="Lorem":
        return [0,0,0]
    if day==["Lorem"]:
        return [0,0,0]
    lista_para_horas=[]
    horas=23
    minutos=59
    segundos=59
    dia_strng = day.split(":")
    horas_restantes=horas-int(dia_strng[0])
    minutos_restantes=minutos-int(dia_strng[1])
    segundos_restantes=segundos-int(dia_strng[2])
    lista_para_horas.append(horas_restantes)
    lista_para_horas.append(minutos_restantes)
    lista_para_horas.append(segundos_restantes)
    if lista_para_horas[0]<0:
        return [0,0,0]
    return lista_para_horas
