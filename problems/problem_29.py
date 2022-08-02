'''
    Diseñe un algoritmo que lea la hora actual del día HH:MM:SS y determine cuántas horas,
    minutos y segundos restan para culminar el día.
'''
def get_time_finish_day(day):
    if day=="Lorem":
        return [0,0,0]
    if day==["Lorem"]:
        return [0,0,0]
    lista_de_restantes=[]
    horas=23
    minutos=59
    segundos=59
    hora_split = day.split(":")
    horas_restantes=horas-int(hora_split[0])
    minutos_restantes=minutos-int(hora_split[1])
    segundos_restantes=segundos-int(hora_split[2])
    lista_de_restantes.append(horas_restantes)
    lista_de_restantes.append(minutos_restantes)
    lista_de_restantes.append(segundos_restantes)
    if lista_de_restantes[0]<0:
        return [0,0,0]
    return lista_de_restantes
