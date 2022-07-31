'''
    Diseñe un algoritmo al cual se le ingresen n valores y se muestre por pantalla la suma de
los valores, la suma de los cuadrados de ellos, el promedio y la desviación estandar ( sum(x-x_barra) / (N-1) )
'''
import statistics
def get_stats(numbers):
     list =[]
     i=0
     for i in list:
      i=i+1
     st_dev = statistics.pstdev(list)
     return(round(st_dev,6))