'''
    Diseñe un algoritmo al cual se le ingresen n valores y se muestre por pantalla la suma de
los valores, la suma de los cuadrados de ellos, el promedio y la desviación estandar ( sum(x-x_barra) / (N-1) )
'''
import statistics
def get_stats(numbers):
    if type(numbers)==type({"abc":123}):
        return [0,0,0,0]
    for x in numbers:
        if type(x)==type("a"):
            return [0,0,0,0]
    suma = 0
    suma2=0
    promedio=0
    st_dev=0
    redondeo=0
    lista=[]
    for el in numbers:
        suma = el + suma
        suma2 = el**2+suma2
        promedio = suma / len(numbers)
        st_dev = statistics.pstdev(numbers)
        redondeo=round(st_dev,3)
    lista.append(suma)
    lista.append(suma2)
    lista.append(promedio)
    lista.append(redondeo)
    return(lista)