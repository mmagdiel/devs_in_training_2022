'''
    Diseñar una función que retorne, en orden inverso, cada múltiplo de 3 entre 1 y un número dado.
'''
from operator import mod


number = 9
def get_three_multiple_inverse_list(number):
  
  for numero in range(1, number+1):
    if(number % numero  == 0):

     print(numero)   
       

get_three_multiple_inverse_list(number)


    
