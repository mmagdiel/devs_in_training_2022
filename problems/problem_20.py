'''
    Diseñar una función que retorne la moda de una lista de datos.
    La moda es el valor más repetido de una muestra dada
'''
from statistics import mode
from typing import Counter


from typing import Counter

def get_mode(lista):
 res = "No Existe" 
 test_list1 = Counter(lista)
 

 if len(test_list1) == 0:
    print('No existe')
 else:   
  temp = test_list1.most_common(1)[0][1]
  for l in lista:
    if lista.count(l) == temp and l != str(l):
     res = []
     res.append(l)
     res = list(set(res))
  print(res)
  if len(res) == 1:   
   res = 2 
   print(res)
 
  
  
    
get_mode([2,2,3,3])     
