'''
    Diseñar una función para calcular la velocidad (en m/s) de los corredores de la carrera de
    1.500 metros. La entrada consistirá en parejas de números (minutos, segundos) que dan el
    tiempo del corredor; por cada corredor. Se debe retornar el tiempo en segundos, así como la velocidad media. 
    Ejemplo de entrada de datos: [(3,53) (3,40) (3,46) (3,52) (4,0)]
'''
def calcule_time_and_velocity(lista):
    lista=[]
    i=0
    tupla=(3,53)
    velocidad=0
    tiempo=0
    distancia = 1500
    minutos=3
    segundos=53
    tiempo = minutos * 60 + segundos
    velocidad = distancia / tiempo
    while i<len(tupla):
        lista.append(tupla)
        i+=0
    print(lista)
