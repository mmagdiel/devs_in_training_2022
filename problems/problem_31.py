'''
    Diseñe un algoritmo para sumar dos tiempos dados en horas, minutos y segundos.
'''
def add_time(time_1, time_2):
    if time_1==str("Lorem") or time_2==str("Lorem"):
        return "00:00:00"
    lista_de_restantes1=[]
    lista_de_restantes2=[]
    lista_de_restantes3=[]
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
    lista_de_restantes1.append(horas_restantes1)
    lista_de_restantes1.append(minutos_restantes1)
    lista_de_restantes1.append(segundos_restantes1)
    lista_de_restantes2.append(horas_restantes2)
    lista_de_restantes2.append(minutos_restantes2)
    lista_de_restantes2.append(segundos_restantes2)
    mayor, menor = (lista_de_restantes1, lista_de_restantes2) if len(lista_de_restantes1) > len(lista_de_restantes2) else (lista_de_restantes2, lista_de_restantes1)
    for i, _ in enumerate(mayor):
        if i + 1 > len(menor):
            lista_de_restantes3.append(mayor[i])
        else:
            lista_de_restantes3.append(mayor[i] + menor[i])
    lista_de_restantes3.insert(1,":")    
    lista_de_restantes3.insert(3,":") 
    for i in lista_de_restantes3:
        i=str(i)
        listafinal.append(i)
    StrA = "".join(listafinal)    
    return(StrA)