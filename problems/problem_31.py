'''
    Diseñe un algoritmo para sumar dos tiempos dados en horas, minutos y segundos.
'''
def add_time(time_1, time_2):
    if time_1==str("Lorem") or time_2==str("Lorem"):
        return "00:00:00"
    lista_de_horas=[]
    lista_de_horas2=[]
    lista_de_horas3=[]
    listafinal=[]
    hora_nueva1= time_1.split(":")
    hora_nueva2= time_2.split(":")
    horas_restantes1=int(hora_nueva1[0])
    minutos_restantes1=int(hora_nueva1[1])
    segundos_restantes1=int(hora_nueva1[2])
    horas_restantes2=int(hora_nueva2[0])
    minutos_restantes2=int(hora_nueva2[1])
    segundos_restantes2=int(hora_nueva2[2])
    if horas_restantes1>24 or horas_restantes2>24:
        return "00:00:00"
    lista_de_horas.append(horas_restantes1)
    lista_de_horas.append(minutos_restantes1)
    lista_de_horas.append(segundos_restantes1)
    lista_de_horas2.append(horas_restantes2)
    lista_de_horas2.append(minutos_restantes2)
    lista_de_horas2.append(segundos_restantes2)
    mayor, menor = (lista_de_horas, lista_de_horas2) if len(lista_de_horas) > len(lista_de_horas2) else (lista_de_horas2, lista_de_horas)
    for i, _ in enumerate(mayor):
        if i + 1 > len(menor):
            lista_de_horas3.append(mayor[i])
        else:
            lista_de_horas3.append(mayor[i] + menor[i])
    lista_de_horas3.insert(1,":")    
    lista_de_horas3.insert(3,":") 
    for i in lista_de_horas3:
        i=str(i)
        listafinal.append(i)
    String = "".join(listafinal)    
    return(String)