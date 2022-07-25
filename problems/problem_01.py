'''
    Diseñar una función que reciba y retorne una serie de números distintos de cero. 
    La función debe terminar con un valor cero que no se debe retornar, debe el número de valores leídos.
'''


from ast import List
from os import remove
from pickle import APPEND
import string


list = []

def show_any_number_distinc_zero(list):

  
 lista1=[]

 for n in list:
  lista1.append(n)    
      
  if n == 0:
    lista1.remove(0)
    lista1.append(len(lista1))
    break

  
 print(lista1)
    

show_any_number_distinc_zero(list)


    

 

