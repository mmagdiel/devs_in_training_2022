'''
    Diseñar una función que retorne la moda de una lista de datos.
    La moda es el valor más repetido de una muestra dada
'''
from statistics import mode
from typing import Counter


def get_mode(lista):
 res = []  

 
 test_list1 = Counter(lista)
 if lista == str(lista):
    return 'no existe'
 temp = test_list1.most_common(1)[0][1]
 for l in lista:
    if lista.count(l) == temp and l != str(l):
     res = []   
     res.append(l)
     res = list(set(res))
     return(res)
 if l == str(l):  
      return "no existe"  
 
    

